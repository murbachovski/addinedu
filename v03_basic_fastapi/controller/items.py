from typing import Union
from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["imtes"],
    responses={404: {"description": "Not found"}}
)

@router.get("/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}