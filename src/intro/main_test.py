import intro.router_example as router_example
from fastapi import FastAPI

app = FastAPI()

app.include_router(router_example.router)


@app.get("/")
async def read_root() -> dict[str, str]:
    """
    Return a simple greeting JSON response for the root endpoint.
    This function is intended to be used as a FastAPI root ("/") handler.

    Returns
    -------
    dict[str, str]
        A mapping with a single key "Hello" and value "World".
    """
    return {"Hello": "World"}
