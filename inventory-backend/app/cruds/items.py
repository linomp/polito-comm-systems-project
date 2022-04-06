from app.core.db import database


async def get_all_items():
    query = "SELECT * FROM items"
    data = await database.fetch_all(query)

    return [{**i} for i in data]
