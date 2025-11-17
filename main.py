from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    """
    Return a simple greeting payload for the API root endpoint.

    Returns
    -------
    dict[str, str]
        A dictionary containing a single greeting entry: {"Hello": "World"}.
    """
    return {"Hello": "World"}
