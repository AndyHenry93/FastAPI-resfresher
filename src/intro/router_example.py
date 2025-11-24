from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("/items/{item_id}")
async def read_item(item_id: int) -> dict[str, Any]:
    return {"item_id": item_id}
