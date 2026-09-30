"""Reflex configuration for the Moon FastAPI compatibility adapter.

The dashboard itself remains the existing FastAPI application. Reflex is used
as the hosting/build entry point and mounts that application through the API
transformer defined in ``app/app.py``.
"""

import reflex as rx


config = rx.Config(
    app_name="app",
    app_module_import="app.app",
)
