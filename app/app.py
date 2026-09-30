"""Reflex entry point that hosts Moon's existing FastAPI application.

Reflex expects a module-level `app` object in `app.app`. Moon already
contains the complete dashboard, subscription endpoints, WebSocket handlers,
and persistence layer in `main.py`. The API transformer lets Reflex serve
that FastAPI application without rewriting the dashboard in Reflex components.
"""

from __future__ import annotations

import reflex as rx

from main import app as moon_fastapi_app


@rx.page(route="/__reflex_check", title="Moon Gateway")
def reflex_check_page():
    """Small compile-time page required by the Reflex toolchain.

    The real Moon pages (`/login`, `/dashboard`, `/sub/...`) continue to
    be served by the mounted FastAPI application.
    """

    return rx.text("Moon Gateway")


app = rx.App(api_transformer=moon_fastapi_app)
