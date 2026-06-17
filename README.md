# Pixel Art Canvas

A Flask pixel art app for drawing on a 32x32 grid, saving canvases, browsing a gallery, and downloading artwork as PNG files. Built as a learning-by-doing Codex project.


## Screenshots

![Pixel Art Canvas](images/Screenshot%202026-06-17%20at%2010.17.26.png)
![Pixel Art Canvas](images/Screenshot%202026-06-17%20at%2010.17.18.png)
![Pixel Art Canvas](images/Screenshot%202026-06-17%20at%2009.14.13.png)
![Pixel Art Canvas](images/Screenshot%202026-06-17%20at%2009.16.03.png)


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
