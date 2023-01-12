""" broken_access_control """

from fastapi import APIRouter

router = APIRouter()


@router.get("/broker_access_control/{user_id}", tags=["broker_access_control"])
async def read_user(user_id: str):
    """ broker_access_control user_id """
    return {"user_id": user_id}
