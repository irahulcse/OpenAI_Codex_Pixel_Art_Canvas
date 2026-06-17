import os

from flask import Flask, jsonify, render_template, request, send_file

from models import db
from services import (
    ValidationError,
    export_canvas_png,
    get_canvas_by_id,
    get_gallery_canvases,
    save_canvas,
)


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/gallery")
    def gallery():
        canvases = get_gallery_canvases()
        return render_template("gallery.html", canvases=canvases)

    @app.route("/canvases", methods=["POST"])
    def create_canvas():
        data = request.get_json(silent=True) or {}

        try:
            canvas = save_canvas(data.get("name"), data.get("pixel_data"))
        except ValidationError as error:
            return jsonify({"message": str(error)}), 400

        return jsonify({"id": canvas.id, "message": "Canvas saved successfully."}), 201

    @app.route("/canvases/<int:canvas_id>/download")
    def download_canvas(canvas_id):
        canvas = get_canvas_by_id(canvas_id)
        png_file, filename = export_canvas_png(canvas)

        return send_file(
            png_file,
            mimetype="image/png",
            as_attachment=True,
            download_name=filename,
        )

    with app.app_context():
        db.create_all()

    return app


app = create_app()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host="127.0.0.1", port=port, debug=True)
