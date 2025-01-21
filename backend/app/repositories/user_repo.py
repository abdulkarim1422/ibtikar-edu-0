from app.initializers import db
from app import models
from sqlmodel import select

def get_all_users():
    with db.get_session() as session:
        users = session.exec(select(models.User)).all()
        return users
    
def get_user_by_id(user_id):
    with db.get_session() as session:
        user = session.get(models.User, user_id)
        return user
    
def create_user(user):
    with db.get_session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
def update_user(user_id, user):
    with db.get_session() as session:
        user_obj = session.get(models.User, user_id)
        user_obj.email = user.email
        user_obj.password = user.password
        session.add(user_obj)
        session.commit()
        session.refresh(user_obj)
        return user_obj
    
def delete_user(user_id):
    with db.get_session() as session:
        user = session.get(models.User, user_id)
        session.delete(user)
        session.commit()
        return user
    
def get_user_by_email(email):
    with db.get_session() as session:
        user = session.exec(select(models.User).where(models.User.email == email)).first()
        return user
    
