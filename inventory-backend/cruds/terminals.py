from dependencies import db
from schemas.terminal import Terminal


def add_terminal(new_terminal: Terminal):
    if (check_terminal(new_terminal.mac_adr, new_terminal.cst_id) != 0):
        return

    values = (None,
              new_terminal.mac_adr,
              new_terminal.cst_id,
              new_terminal.pin)

    query = "INSERT INTO terminal_table (id, mac_adr, cst_id, pin) VALUES (%s, %s, %s, %s)"
    db.execute(query, values)

    return


def check_terminal(mac_adr: str, cst_id: int):
    values = (mac_adr, cst_id)

    query = "SELECT * FROM terminal_table WHERE mac_adr=%s AND cst_id=%s"
    data = db.fetch_all(query, values)

    return len(data)


def remove_terminal(mac_adr: int, cst_id: int):
    values = (mac_adr, cst_id)
    query = "DELETE FROM terminal_table WHERE mac_adr=%s AND cst_id=%s"
    db.execute(query, values)

    return
