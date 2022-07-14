from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from schemas.Token import Token
from schemas.user import UserDAO
from services.users import *
from cruds import users as user_funcs
from cruds import costumers as cst_funcs
from components.custom_exceptions import *

from env import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()


@router.post("/token", tags=["auth"], response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.mail_adr}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", tags=["users"], response_model=UserDAO)
async def get_current_user(current_user: User = Depends(get_current_active_user)):
    return UserDAO(id=current_user.id,
                   name=current_user.name,
                   mail_adr=current_user.mail_adr,
                   rfid=current_user.rfid,
                   pin=current_user.pin)


@router.get("/users/protected/", tags=["users"])
async def protected_route_example(current_user: User = Depends(get_current_active_user)):
    msg = await get_protected_route_example(current_user)
    return msg


@router.post("/users", tags=["users"])
async def create_user(user_data: NewUserDAO):
    try:
        if user_funcs.get_user_from_email(user_data.mail_adr):
            raise InvalidEmailException
        if user_funcs.get_user_from_rfid(user_data.rfid):
            raise InvalidRFIDException

        created_user = add_new_user(user_data)

        return created_user
    except InvalidEmailException:
        raise HTTPException(status_code=403, detail="Email already in use")
    except InvalidRFIDException:
        raise HTTPException(status_code=403, detail="RFID already in use")


@router.post("/users/card/update_card", tags=["users"])
async def update_user_rfid_card(card_data: NewCardDAO, current_user: User = Depends(get_current_active_user)):
    try:
        if user_funcs.get_user_from_rfid(current_user.rfid):
            raise InvalidRFIDException

        user = updt_users_card(current_user.id, card_data)

        return user
    except InvalidRFIDException:
        raise HTTPException(status_code=403, detail="RFID already in use")


@router.post("/users/card/login", tags=["users"])
async def login_from_rfid_card(card_data: NewCardDAO):
    try:
        user = login_from_card(card_data)

        return user

    except WrongPinException:
        raise HTTPException(status_code=401, detail="Wrong pin")
    except InvalidCardIDException:
        raise HTTPException(status_code=404, detail="Card is Invalid")


@router.post("/users/employees/add_client", tags=["users"])
async def add_client_to_cst(new_client_id: int, costumer_id: int,
                            current_user: User = Depends(get_current_active_user)):
    try:
        if not user_funcs.get_user_from_id(new_client_id):
            raise InvalidUserIDException

        if not cst_funcs.get_costumer_from_id(costumer_id):
            raise InvalidCostumerIDException

        check_if_employee(current_user.id, costumer_id)
        add_client(new_client_id, costumer_id)

        return
    except InvalidCostumerIDException:
        raise HTTPException(status_code=404, detail="Invalid costumer ID")
    except InvalidUserIDException:
        raise HTTPException(status_code=404, detail="Invalid user ID")
    except NotAssociatedException:
        raise HTTPException(status_code=403, detail="You are not associated to costumer")
    except NoPermissionException:
        raise HTTPException(status_code=403, detail="You don't have permission")
    except AlreadyClientException:
        raise HTTPException(status_code=400, detail="User is already a client")
    except AlreadyEmployeeException:
        raise HTTPException(status_code=400, detail="User is already an employee")


@router.post("/users/admin/add_employee", tags=["users"])
async def add_client_to_cst(new_employee_id: int, costumer_id: int,
                            current_user: User = Depends(get_current_active_user)):
    try:
        if not user_funcs.get_user_from_id(new_employee_id):
            raise InvalidUserIDException

        if not cst_funcs.get_costumer_from_id(costumer_id):
            raise InvalidCostumerIDException

        check_if_admin(current_user.id, costumer_id)
        add_employee(new_employee_id, costumer_id)

        return
    except InvalidCostumerIDException:
        raise HTTPException(status_code=404, detail="Invalid costumer ID")
    except InvalidUserIDException:
        raise HTTPException(status_code=404, detail="Invalid user ID")
    except NotAssociatedException:
        raise HTTPException(status_code=403, detail="You are not associated to costumer")
    except NoPermissionException:
        raise HTTPException(status_code=403, detail="You don't have permission")
    except AlreadyClientException:
        raise HTTPException(status_code=400, detail="User is already a client")
    except AlreadyEmployeeException:
        raise HTTPException(status_code=400, detail="User is already an employee")


@router.get("/users/view_my_cst", tags=["users"])
async def get_user_associated_cst(current_user: User = Depends(get_current_active_user)):
    data = user_funcs.get_all_csts_from_user(current_user.id)

    cst_list = []
    idx = len(data)
    for i in range(idx):
        aux = cst_funcs.get_costumer_from_id(data[i][2])
        cst_list.append({"id": aux.id,
                         "name": aux.name,
                         "category": aux.category,
                         "role": data[i][3]})

    return cst_list
