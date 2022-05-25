from dependencies import db
from schemas.item import Item


def add_item(new_item: Item):
    values = (None,
              new_item.name,
              new_item.description,
              new_item.category,
              new_item.costumer_id,
              new_item.rfid
              )

    query = "INSERT INTO items (id, name, description, category, costumer_id, rfid) VALUES (%s, %s, %s, %s, %s, %s)"
    db.execute(query, values)

    return


def get_item_from_id(item_id: int):
    values = (item_id,)
    query = "SELECT id, name, description, category, costumer_id, rfid FROM items WHERE id=%s"
    data = db.fetch_one(query, values)

    if not (data is None):
        new_item = Item(id=data[0], name=data[1], description=data[2], category=data[3],
                        costumer_id=data[4], rfid=data[5])

        return new_item


def get_item_from_rfid(item_rfid: int):
    values = (item_rfid,)
    query = "SELECT id, name, description, category, costumer_id, rfid FROM items WHERE rfid=%s"
    data = db.fetch_one(query, values)

    if not (data is None):
        new_item = Item(id=data[0], name=data[1], description=data[2], category=data[3],
                        costumer_id=data[4], rfid=data[5])

        return new_item


def get_all_items_with_name(name: str):
    values = (name,)
    query = "SELECT * FROM items WHERE name=%s"
    data = db.fetch_all(query, values)

    return data


def get_all_items_from_category(categ: str):
    values = (categ,)
    query = "SELECT * FROM items WHERE category=%s"
    data = db.fetch_all(query, values)

    return data


def get_all_items_from_cst(cst_id: int):
    values = (cst_id,)
    query = "SELECT * FROM items WHERE costumer_id=%s"
    data = db.fetch_all(query, values)

    return data


def update_category(item_id: int, new_categ: str):
    values = (new_categ, item_id)
    query = "UPDATE items SET category=%s WHERE id=%s"
    db.execute(query, values)

    return


def update_name(item_id: int, new_name: str):
    values = (new_name, item_id)
    query = "UPDATE items SET name=%s WHERE id=%s"
    db.execute(query, values)

    return


def update_description(item_id: int, description: str):
    values = (description, item_id)
    query = "UPDATE items SET description=%s WHERE id=%s"
    db.execute(query, values)

    return


def remove_item(item_id: int):
    values = (item_id,)
    query = "DELETE FROM items WHERE id=%s"
    db.execute(query, values)

    return
