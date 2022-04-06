from fastapi import APIRouter

from app.cruds.items import get_all_items

router = APIRouter()


@router.get("/items/", tags=["items"])
async def read_items():
    tweet_list = await get_all_items()

    return tweet_list
