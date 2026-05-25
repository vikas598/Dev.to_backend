from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, utils
from ..database import get_db
from sqlalchemy.orm import Session

router= APIRouter( prefix = '/users', tags=['users'])

@router.post('/', status_code= status.HTTP_201_CREATED, response_model= schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    print(user.password)
    print(type(user.password))
    print(len(user.password))
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user 