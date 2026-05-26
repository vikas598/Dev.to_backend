from fastapi import APIRouter, Depends, status, HTTPException, File, UploadFile
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

@router.get('/me', response_model= schemas.UserProfile)
def get_me(current_user= Depends(oauth2.get_current_user)):
    return current_user

@router.put('/me', response_model= schemas.UserProfile)
def update_me(user_update: schemas.UserUpdate, db: Session = Depends(get_db), current_user= Depends(oauth2.get_current_user)):
    user_data = user_update.model_dump(exclude_unset=True)
    for key, value in user_data.items():
        setattr(current_user, key, value)
    
    db.add(current_user)
    db.commit()
    db.refresh(current_user)

    return current_user

@router.put('/me/avatar', response_model= schemas.UserProfile)

@router.get('/{id:int}', response_model= schemas.UserResponse)
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"user with id {id} not found")
    return user