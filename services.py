from io import BytesIO
import re

from PIL import Image, ImageColor

from models import Canvas, db


GRID_SIZE = 32
GALLERY_LIMIT = 100
EXPORT_SCALE = 16
HEX_COLOR_PATTERN = re.compile(r"^#[0-9a-fA-F]{6}$")
FILENAME_PATTERN = re.compile(r"[^a-zA-Z0-9_-]+")


class ValidationError(ValueError):
    pass


def save_canvas(name, pixel_data):
    cleaned_name = _validate_name(name)
    _validate_pixel_data(pixel_data)

    canvas = Canvas(name=cleaned_name, pixel_data=pixel_data)
    db.session.add(canvas)
    db.session.commit()

    return canvas


def get_gallery_canvases(limit=GALLERY_LIMIT):
    return (
        Canvas.query.order_by(Canvas.created_at.desc())
        .limit(limit)
        .all()
    )


def get_canvas_by_id(canvas_id):
    return db.get_or_404(Canvas, canvas_id)


def export_canvas_png(canvas):
    image = Image.new("RGB", (GRID_SIZE, GRID_SIZE), "white")
    pixels = image.load()

    for row_index, row in enumerate(canvas.pixel_data):
        for column_index, color in enumerate(row):
            pixels[column_index, row_index] = ImageColor.getrgb(color)

    image = image.resize(
        (GRID_SIZE * EXPORT_SCALE, GRID_SIZE * EXPORT_SCALE),
        Image.Resampling.NEAREST,
    )

    output = BytesIO()
    image.save(output, format="PNG")
    output.seek(0)

    return output, _png_filename(canvas.name)


def _validate_name(name):
    if not isinstance(name, str):
        raise ValidationError("Canvas name is required.")

    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValidationError("Canvas name is required.")

    if len(cleaned_name) > 120:
        raise ValidationError("Canvas name must be 120 characters or fewer.")

    return cleaned_name


def _validate_pixel_data(pixel_data):
    if not isinstance(pixel_data, list) or len(pixel_data) != GRID_SIZE:
        raise ValidationError("Pixel data must be a 32x32 grid.")

    for row in pixel_data:
        if not isinstance(row, list) or len(row) != GRID_SIZE:
            raise ValidationError("Pixel data must be a 32x32 grid.")

        for color in row:
            if not isinstance(color, str) or not HEX_COLOR_PATTERN.fullmatch(color):
                raise ValidationError("Each pixel must be a hex colour string.")


def _png_filename(name):
    filename = FILENAME_PATTERN.sub("-", name.strip().lower()).strip("-")
    return f"{filename or 'canvas'}.png"
