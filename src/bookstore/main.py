from typing import Any
from typing import List
from typing import Optional

from fastapi import FastAPI
from fastapi import HTTPException
from starlette.responses import JSONResponse

from .models import Book
from .models import BookResponse

app = FastAPI()


@app.get("/books/{book_id}")
async def book_details(book_id: int) -> dict[str, Any]:
    return {"book_id": book_id, "Title": "Wool", "Author": "Hugh Howley"}


@app.get("/author/{author_id}")
async def author_details(author_id: int) -> dict[str, Any]:
    return {"Author_id": author_id, "Author Name": "Hugh Howley"}


@app.get("/books/")
async def read_books(year: Optional[int] = None) -> dict[str, Any]:
    if year:
        return {"Year": year, "Books": ["Book 1", "Book 2"]}
    return {"book": ["All Book"]}


@app.post("/book")
async def add_book(book: Book) -> Book:
    return book


@app.get("/allbooks")
async def read_all_books() -> List[BookResponse]:
    return [
        {"id": 1, "title": "Wool", "author": "Hugh Howley"},
        {"id": 2, "title": "Game of Thrones", "author": "George R. R. Martin"},
    ]


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": "Oops something went wrong!!"},
    )


@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=400)
