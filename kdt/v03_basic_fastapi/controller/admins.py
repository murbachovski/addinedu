from model import t_pgsql
from fastapi import APIRouter

router = APIRouter(
    prefix="/admins",
    tags=["admins"],
    responses={404: {"description": "Not found"}}
)

@router.get("/list")
def list_admin():
    results = t_pgsql.list_admin()
    return results