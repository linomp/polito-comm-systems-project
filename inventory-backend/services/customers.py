from schemas.costumer import Costumer
from cruds import costumers as customer_funcs


def create_new_customer(customer_data: Costumer):
    new_customer = Costumer(id=customer_data.id, name=customer_data.name, category=customer_data.category)

    customer_funcs.add_costumer(new_customer)

    created_user = customer_funcs.get_costumer_from_name(customer_data.name)

    # TODO: create by default an admin user and return its credentials as well

    return created_user
