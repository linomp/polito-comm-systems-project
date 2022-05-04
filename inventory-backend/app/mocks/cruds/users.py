from app.mocks.schemas.user import UserInDB

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$i1UKz6kbp15O4dssJJ5se.dnmyVDdm1x3.jI6ZUAgyAUUAPlb0Pei",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "$2b$12$A7AYHxnpgEzWr6AHPJhYP.D7lz/KA/vC2xcKrhwAsQ7taA.sPV1L2",
        "disabled": True,
    },
}


def get_user(username: str):
    if username in fake_users_db:
        user_dict = fake_users_db[username]
        return UserInDB(**user_dict)
