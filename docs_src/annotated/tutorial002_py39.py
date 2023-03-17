from typing import Annotated, Optional

from fastapi import Depends, FastAPI

app = FastAPI()


class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


CommonQueryParamsDepends = Annotated[CommonQueryParams, Depends()]


@app.get("/items/")
async def read_items(commons: CommonQueryParamsDepends):
    return commons
