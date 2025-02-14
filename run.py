#!/usr/bin/env python

"""
CLI to run FastAPI or Flask servers.
"""

import uvicorn  # type: ignore


def run():
    """
    Run FastAPI with Uvicorn.
    """

    from bcn_rainfall_api.config import Config

    uvicorn.run(
        "bcn_rainfall_api.app:fastapi_app",
        **Config(path="config.yml").get_api_settings.server.model_dump(),
    )


if __name__ == "__main__":
    run()
