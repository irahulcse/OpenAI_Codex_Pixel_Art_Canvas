# Pixel Art Canvas Session Summary

Date: 2026-06-17

## Project Goal

Build a Flask pixel art canvas app where users can:

- Draw on a 32x32 grid
- Pick colors from a palette
- Name and save their artwork
- Browse saved canvases in a gallery
- Download any saved canvas as a PNG file

Stack:

- Flask
- SQLite
- Flask-SQLAlchemy
- HTML5 Canvas
- Vanilla JavaScript
- Pillow
- Pytest

## Project Conventions From AGENTS.md

- Use Flask-SQLAlchemy for all database access.
- Use Pillow for PNG export.
- Use pytest for tests.
- Keep route handlers thin; business logic belongs in service functions.
- Do not use print statements for logging.
- Do not write raw SQL; use the SQLAlchemy ORM.
- Do not add new dependencies without updating `requirements.txt`.
- Single-file tests and lint can be run without asking.
- Ask before deleting files, installing new packages, or running the full test suite.
- Review routes that modify data for input validation.
- Review database queries for unbounded result sets.

Notes found in `AGENTS.md`:

- "Flask-SQLAlachemy" appears to be a typo for "Flask-SQLAlchemy".
- The single-file test example says `pytest test/test-routes.py -v`, but the expected test directory is `tests/`.

## Files Created Or Updated

### `app.py`

- Created the Flask app.
- Configured SQLite through Flask-SQLAlchemy.
- Initializes the database on startup with `db.create_all()`.
- Added app factory support with `create_app(test_config=None)`.
- Added routes:
  - `GET /`
  - `GET /gallery`
  - `POST /canvases`
  - `GET /canvases/<canvas_id>/download`
- Runs locally on `127.0.0.1:5050` by default to avoid macOS port `5000` conflicts.

### `models.py`

- Added SQLAlchemy `db` object.
- Added `Canvas` model with:
  - `id`
  - `name`
  - `pixel_data`
  - `created_at`

### `services.py`

- Added business logic outside route handlers.
- Added validation for canvas name and 32x32 pixel data.
- Added save logic for canvases.
- Added bounded gallery query with a limit of 100 canvases.
- Added single-canvas lookup.
- Added Pillow PNG export logic.
- PNG export scales 32x32 artwork to 512x512 using nearest-neighbor scaling.

### `templates/index.html`

- Added drawing page.
- Includes:
  - 32x32 HTML5 canvas drawing grid
  - Color palette
  - Canvas name input
  - Save button
  - On-screen success/error message
  - Link to gallery

### `templates/gallery.html`

- Added gallery page.
- Shows:
  - Canvas preview
  - Canvas name
  - Saved date
  - Download button
  - Link back to drawing page

### `tests/test_app.py`

- Added focused pytest coverage for:
  - index page loading
  - canvas save success
  - invalid save input rejection
  - gallery rendering saved canvases
  - PNG download generation

## Local App URLs

Drawing page:

```text
http://127.0.0.1:5050/
```

Gallery page:

```text
http://127.0.0.1:5050/gallery
```

## Run The App

```bash
python3 app.py
```

The app defaults to:

```text
http://127.0.0.1:5050/
```

You can override the port:

```bash
PORT=5051 python3 app.py
```

## Test Command Used

Single-file test command:

```bash
PYTHONPYCACHEPREFIX=/private/tmp/pixel_pycache python3 -m pytest tests/test_app.py -v
```

Result:

```text
5 passed in 0.41s
```

The full test suite was not run because `AGENTS.md` says to ask first before running it.

## Manual Verification Performed

- Confirmed app starts with `python3 app.py`.
- Confirmed `GET /` returns `200 OK`.
- Confirmed `POST /canvases` saves valid 32x32 pixel data.
- Confirmed invalid save input returns `400`.
- Confirmed `GET /gallery` returns `200 OK`.
- Confirmed gallery includes saved canvas previews and download links.
- Confirmed PNG download route returns:
  - `200 OK`
  - `Content-Type: image/png`
  - attachment filename such as `smoke-test.png`
- Confirmed downloaded PNG opens as:

```text
PNG (512, 512) RGB
```

## Important Notes

- Port `5000` conflicted with a macOS AirTunes/AirPlay service and returned `403 Forbidden`.
- The app was updated to use port `5050` by default.
- A local SQLite database was created at `instance/pixel_art_canvas.db`.
- Manual smoke testing created sample records such as `Smoke Test` and `Rahul`.

## Current Status

The app currently supports:

- Drawing
- Saving
- Gallery browsing
- PNG downloading
- Focused automated tests

The Flask development server was running successfully at:

```text
http://127.0.0.1:5050/
```
