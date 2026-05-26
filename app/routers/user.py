from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, utils, oauth2
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

@router.get('/{id}', response_model= schemas.UserResponse)
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"user with id {id} not found")
    return user

@router.get('/me', response_model= schemas.UserProfile)
def view_profile(current_user= Depends(oauth2.get_current_user)):
    return current_user