#!/usr/bin/env python

"""
Script to run FastAPI server with Uvicorn.
"""

import uvicorn  # type: ignore


def run():
    from bcn_rainfall_api.config import Config

    uvicorn.run(
        "bcn_rainfall_api.app:fastapi_app",
        **Config(path="config.yml").get_api_settings.server.model_dump(),
    )


if __name__ == "__main__":
    run()
