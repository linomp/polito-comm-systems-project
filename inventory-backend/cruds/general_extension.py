from pymysql import NULL
from dependencies import db



#def delete_from_extension_table(categ:str, item_id:int):


#NOT TESTED
def get_details(categ: str, item_id: int):
    values = (categ, item_id)
    query = "SELECT * FROM %s WHERE item_id = %s"
    data = db.fetch_one(query, values)

    return data