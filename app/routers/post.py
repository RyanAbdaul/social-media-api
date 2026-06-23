from typing import List, Optional
from fastapi import Response, status, HTTPException, Depends, APIRouter
from .. import schemas, models, oauth2
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)


@router.get('/', response_model=List[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db),  current_user: int = Depends(oauth2.get_current_user),
            limit : int = 10, skip : int = 0, search : Optional[str] = ''):
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts



@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_posts(post : schemas.PostCreate, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    
    new_post = models.Post(user_id=current_user.id, **post.model_dump())
    db.add(new_post)
    db.commit() 
    db.refresh(new_post)
    return new_post
    


@router.get('/{id}', response_model=schemas.PostResponse)
def get_post(id: int, response: Response, db: Session = Depends(get_db)):
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with {id} is not found')
        
    return post


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id {id} was not found')
    
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Unauthorized to perform the requested action')
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put('/{id}', response_model=schemas.PostResponse)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Post with id {id} was not found')
    
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Unauthorized to perform the requested action')
    post_query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()
    return post_query.first()