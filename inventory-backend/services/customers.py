def add_new_customer(customer_data: Costumer):
    new_customer = Costumer(id=customer_data.id, name=customer_data.name, category=customer_data.category)

    customer_funcs.create_customer(new_customer)

    created_user = user_funcs.get_user_from_email(customer_data.mail_adr)

    return created_user
