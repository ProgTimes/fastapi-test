from typing import List, Set

from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel
from pydantic.types import UrlStr
from starlette.status import HTTP_201_CREATED

app = FastAPI()


@app.get("/items/", include_in_schema=False)
async def read_items():
    return [{"item_id": "Foo"}]
