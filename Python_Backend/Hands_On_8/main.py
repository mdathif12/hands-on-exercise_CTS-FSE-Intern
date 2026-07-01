from fastapi import FastAPI

from database import Base
from database import engine

from routers.courses import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="RESTful Course API",
    version="1.0"
)

"""
Versioning Strategies

1. URL Versioning
   /api/v1/courses

2. Header Versioning
   Accept:
   application/vnd.api+json;version=1

URL versioning is easy to use.
Header versioning keeps URLs clean.
"""

app.include_router(router)