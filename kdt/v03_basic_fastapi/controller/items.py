from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}}
)

@router.get("/{items_id}")
def read_items(items_id : int):
    return {"items_id": items_id}