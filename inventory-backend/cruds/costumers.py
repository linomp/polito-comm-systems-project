from core import db_functions
from schemas.costumer import Costumer


async def add_costumer(new_costumer: Costumer):
    values = {"cst_id": new_costumer.cst_id,
              "name": new_costumer.name,
              "category": new_costumer.category}
              
    query = "INSERT INTO costumers(cst_id, name, category) VALUES (:cst_id, :name, :category)"
    insert_id = await db_functions.execute(query=query, values=values)

    return 

async def get_costumer_from_id(costumer_id: int):
    query = f"SELECT id, costumer_id, name, category FROM costumers WHERE costumer_id={costumer_id}"
    data = await db_functions.fetch_one(query)

    return data
