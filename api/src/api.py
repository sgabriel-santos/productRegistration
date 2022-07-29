from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config.ConfigDB import origins
from .routes.Routes import routes

""""
    Main file. Instance the FastAPI and include the main endpoints of application         
"""

description = """
## Introduction
This application has as main objective to Perform basic operations on a database
containing products
"""

tags_metadata = [
    {
        "name": "product",
        "description": "Products operations"
    }
]

app = FastAPI(
    title="IHR-SE Application",
    description=description,
    version="0.0.1",
    openapi_tags=tags_metadata
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for route in routes:
    app.include_router(route.router) 