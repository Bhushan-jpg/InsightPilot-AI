from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas import UserCreate, UserLogin
from auth import (
    hash_password,
    verify_password,
    create_access_token,
    verify_token
)

from database import get_db
from models import User


router = APIRouter()



# ==========================
# Signup
# ==========================

@router.post("/signup")
def signup(
    user: UserCreate,
    db: Session = Depends(get_db)
):


    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()



    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )




    hashed_password = hash_password(
        user.password
    )



    new_user = User(

        name=user.name,

        email=user.email,

        password=hashed_password

    )



    db.add(new_user)

    db.commit()

    db.refresh(new_user)



    return {

        "message":
        "User Registered Successfully"

    }







# ==========================
# Login
# ==========================


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):


    db_user = db.query(User).filter(
        User.email == user.email
    ).first()



    if not db_user:


        raise HTTPException(

            status_code=401,

            detail="Invalid Email or Password"

        )





    password_match = verify_password(

        user.password,

        db_user.password

    )




    if not password_match:


        raise HTTPException(

            status_code=401,

            detail="Invalid Email or Password"

        )






    token = create_access_token(

        {

            "sub":
            db_user.email

        }

    )






    return {


        "access_token":
        token,


        "token_type":
        "bearer",



        "user":

        {

            "name":
            db_user.name,


            "email":
            db_user.email

        }


    }







# ==========================
# Protected Dashboard Test
# ==========================


@router.get("/dashboard")
def dashboard(

    current_user: str = Depends(verify_token)

):


    return {


        "message":
        f"Welcome {current_user}"

    }