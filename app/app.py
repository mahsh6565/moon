"""Reflex entry point that hosts Moon's existing FastAPI application.

Reflex expects a module-level app object in app.app. Moon already
contains the complete dashboard, subscription endpoints, WebSocket handlers,
and persistence layer in main.py. The API transformer lets Reflex serve
that FastAPI application without rewriting the dashboard in Reflex components.
"""

from __future__ import annotations

import reflex as rx

from main import app as moon_fastapi_app


def index():
    """Minimal root page required by the Reflex production compiler.

    The real Moon pages (/login, /dashboard, /sub/...) continue to be served
    by the mounted FastAPI application.
    """

    return rx.text("Moon Gateway")


app = rx.App(api_transformer=moon_fastapi_app)
app.add_page(index, route="/", title="Moon Gateway")
