from components import constants
from cruds.costumers import add_user2costumer
from schemas.costumer import Costumer, NewCostumerDAO
from cruds import costumers as customer_funcs
from schemas.user import NewUserDAO
from components.custom_exceptions import DefaultUserCreationException, CustomerCreationException, DatabaseException
from services.users import add_new_user


def create_new_customer(customer_data: Costumer) -> NewCostumerDAO:
    try:
        new_customer = Costumer(name=customer_data.name, category=customer_data.category)

        customer_funcs.add_costumer(new_customer)

        created_customer = customer_funcs.get_costumer_from_name(customer_data.name)

        # Create by default an admin user and return its credentials as well
        default_user_data = NewUserDAO(name=constants.DEFAULT_USER_NAME,
                                       mail_adr=customer_data.name + constants.DEFAULT_ADMIN_USER_SUFFIX,
                                       password=constants.DEFAULT_USER_PASSWORD)
        new_user = add_new_user(default_user_data)

        # Associate new default user with new customer
        add_user2costumer(user_id=new_user.id, cst_id=created_customer.id, role=constants.USER_ROLE_ADMIN)
        new_customer = NewCostumerDAO(id=created_customer.id, name=created_customer.name,
                                      category=created_customer.category,
                                      default_user=default_user_data)

        return new_customer

    except DatabaseException:
        raise DefaultUserCreationException(f"Could not create user for customer {customer_data.name}")

    except CustomerCreationException:
        raise CustomerCreationException(f"Creation of customer {customer_data.name} failed")
