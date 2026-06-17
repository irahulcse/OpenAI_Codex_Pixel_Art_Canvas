# Pixel Art Canvas

A Flask pixel art app for drawing on a 32x32 grid, saving canvases, browsing a gallery, and downloading artwork as PNG files.

## Features

- Draw on a 32x32 HTML5 canvas grid
- Choose colors from a palette
- Save artwork with a name
- Browse saved canvases in a gallery
- Download saved artwork as PNG files generated with Pillow

## Tech Stack

- Flask
- SQLite
- Flask-SQLAlchemy
- HTML5 Canvas
- Vanilla JavaScript
- Pillow
- Pytest

## Local Setup

```bash
python3 -m pip install -r requirements.txt
python3 app.py
```

Open:

```text
http://127.0.0.1:5050/
```

## Tests

```bash
python3 -m pytest tests/test_app.py -v
```

## Routes

- `GET /` - drawing page
- `GET /gallery` - saved canvas gallery
- `POST /canvases` - save a canvas
- `GET /canvases/<canvas_id>/download` - download a canvas PNG

## Deployment Notes

The app includes a `Procfile` for platforms that support Gunicorn:

```text
web: gunicorn --bind 0.0.0.0:$PORT app:app
```

For a simple demo deployment, SQLite will work, but saved canvases may not persist across deploys or restarts on platforms with ephemeral filesystems. For production, move to a managed database such as PostgreSQL.
