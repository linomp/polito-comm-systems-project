from core import db_functions
from schemas.costumer import Costumer


async def add_user(new_costumer: Costumer):
    values = {"id": new_costumer.id,    #É PRECISO METER ID TABELA?
              "cst_id": new_costumer.cst_id,
              "name": new_costumer.name,
              "category": new_costumer.category}
              
    query = "INSERT INTO costumers(id, cst_id, name, category) VALUES (:id, :cst_id, :name, :category)"
    insert_id = await db_functions.execute(query=query, values=values)

    return 


