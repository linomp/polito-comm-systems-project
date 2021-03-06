from dependencies import db

from schemas.costumer import Costumer


def add_costumer(new_costumer: Costumer):
    values = (None,
              new_costumer.name,
              new_costumer.category)

    query = "INSERT INTO costumers(id, name, category) VALUES (%s, %s, %s)"
    db.execute(query, values)

    return

def get_list_all_cst():
    values=()
    query = "SELECT * FROM costumers"
    data = db.fetch_all(query, values)

    return data


def get_costumer_from_id(costumer_id: int):
    values = (costumer_id,)
    query = "SELECT id, name, category FROM costumers WHERE id=%s"
    data = db.fetch_one(query, values)

    if not (data is None):
        new_cst = Costumer(id=data[0], name=data[1], category=data[2])

        return new_cst
    else:
        return None


def get_costumer_from_name(name: str):
    values = (name,)
    query = "SELECT id, name, category FROM costumers WHERE name=%s"
    data = db.fetch_one(query, values)

    if not (data is None):
        new_cst = Costumer(id=data[0], name=data[1], category=data[2])

        return new_cst
    else:
        return None


def add_user2costumer(user_id: int, cst_id: int, role: str):
    if (check_user2costumer(user_id, cst_id) != 0):
        return

    values = (None,
              user_id,
              cst_id,
              role)
    query = "INSERT INTO users2costumers (id, user_id, cst_id, role) VALUES (%s, %s, %s, %s)"
    db.execute(query, values)

    return


def check_user2costumer(user_id: int, cst_id: int):
    values = (user_id, cst_id)

    query = "SELECT * FROM users2costumers WHERE user_id=%s AND cst_id=%s"
    data = db.fetch_all(query, values)

    return len(data)


def remove_user2costumer(user_id: int, cst_id: int):
    values = (user_id, cst_id)
    query = "DELETE FROM users2costumers WHERE user_id=%s AND cst_id=%s"
    db.execute(query, values)

    return


def get_all_users_from_cst(cst_id: int):
    values = (cst_id,)
    query = "SELECT * FROM users2costumers WHERE cst_id=%s"
    data = db.fetch_all(query, values)

    return data


def update_name(cst_id: int, name: str):
    values = (name, cst_id)
    query = "UPDATE costumers SET name=%s WHERE id=%s"
    db.execute(query, values)

    return


def update_category(cst_id: int, new_categ: str):
    values = (new_categ, cst_id)
    query = "UPDATE costumers SET category=%s WHERE id=%s"
    db.execute(query, values)

    return


def remove_costumer(costumer_id: int):
    values = (costumer_id,)
    query = "DELETE FROM costumers WHERE id=%s"
    db.execute(query, values)

    return
