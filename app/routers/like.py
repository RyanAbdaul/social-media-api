from fastapi import status, HTTPException, Depends, APIRouter
from .. import schemas, models, utils, oauth2
from sqlalchemy.orm import Session
from ..database import get_db
import time
router = APIRouter(
    prefix='/likes',
    tags=['Interactions']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_likes(like: schemas.Like, db : Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == like.post_id)
    post = post_query.first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {like.post_id} does not exist')
    
    like_query = db.query(models.Like).filter(models.Like.post_id == like.post_id, models.Like.user_id == current_user.id)
    found_like = like_query.first()
    
    if like.dir == 1:
        
        if found_like:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Post with id {found_like.post_id} already liked by user with id {current_user.id}')
        
        new_like = models.Like(user_id=current_user.id, post_id=post.id)
        db.add(new_like)
        db.commit()
        return {'message': 'successfully added like'}
    else:
        if not found_like:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='like does not exist')
        
        like_query.delete(synchronize_session=False)
        db.commit()
        return {'message': 'successfully deleted like'}