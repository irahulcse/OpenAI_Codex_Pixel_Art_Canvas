from io import BytesIO

from PIL import Image

from app import create_app
from models import Canvas, db


def make_pixels(fill="#ffffff"):
    return [[fill for _ in range(32)] for _ in range(32)]


def create_test_app(tmp_path):
    database_path = tmp_path / "test_pixel_art_canvas.db"
    return create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{database_path}",
        }
    )


def test_index_page_loads(tmp_path):
    app = create_test_app(tmp_path)

    response = app.test_client().get("/")

    assert response.status_code == 200
    assert b"Pixel Art Canvas" in response.data
    assert b"View gallery" in response.data


def test_canvas_can_be_saved(tmp_path):
    app = create_test_app(tmp_path)
    pixels = make_pixels()
    pixels[0][0] = "#000000"

    response = app.test_client().post(
        "/canvases",
        json={"name": "Test Canvas", "pixel_data": pixels},
    )

    assert response.status_code == 201
    assert response.get_json()["message"] == "Canvas saved successfully."

    with app.app_context():
        canvas = Canvas.query.one()
        assert canvas.name == "Test Canvas"
        assert canvas.pixel_data[0][0] == "#000000"


def test_canvas_save_validates_input(tmp_path):
    app = create_test_app(tmp_path)

    response = app.test_client().post(
        "/canvases",
        json={"name": "", "pixel_data": []},
    )

    assert response.status_code == 400
    assert response.get_json()["message"] == "Canvas name is required."


def test_gallery_shows_saved_canvas(tmp_path):
    app = create_test_app(tmp_path)
    pixels = make_pixels("#2a9d8f")
    with app.app_context():
        db.session.add(Canvas(name="Gallery Item", pixel_data=pixels))
        db.session.commit()

    response = app.test_client().get("/gallery")

    assert response.status_code == 200
    assert b"Gallery Item" in response.data
    assert b"Download" in response.data
    assert b"Back to drawing" in response.data


def test_canvas_download_returns_png(tmp_path):
    app = create_test_app(tmp_path)
    pixels = make_pixels()
    pixels[0][0] = "#e63946"
    with app.app_context():
        canvas = Canvas(name="Download Me", pixel_data=pixels)
        db.session.add(canvas)
        db.session.commit()
        canvas_id = canvas.id

    response = app.test_client().get(f"/canvases/{canvas_id}/download")

    assert response.status_code == 200
    assert response.content_type == "image/png"
    assert "attachment; filename=download-me.png" in response.headers["Content-Disposition"]

    image = Image.open(BytesIO(response.data))
    assert image.format == "PNG"
    assert image.size == (512, 512)
    assert image.getpixel((0, 0)) == (230, 57, 70)
