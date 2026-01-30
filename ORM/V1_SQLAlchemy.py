from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "sqlite:///users.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


# Model
from sqlalchmey import Column, Integer, String, Boolean

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True) 
    is_active =  Column(Boolean, default=False)

# $ Base.metadata.create_all(bind=engine)


# CREATE
def create_user(name: str, email: str, is_active: bool = True):
    # with SessionLocal() as session():
    #    existng_user = session.query(User).filter(User.email == email).first()
    #    if existng_user:
    #        raise ValueError("Email already registerd")
    try:
        user = User(
            name=name,
            email=email,
            is_active=is_active
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    except IntegrityError:
        session.rollback()
        raise ValueError("Email already regiterd")

    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

# READ
def get_users():
    session = SessionLocal()
    try:
        return session.query(User).all()
    finally:
        session.close()

# READ - ID
def get_user_by_id(user_id: int):
    session = SessionLocal()
    try:
        return session.query(User).filter(User.id == user_id).first()
    finally:
        session.close()

# READ - email
def get_user_by_email(email: str):
    with SessionLocal() as session:
        return session.query(User).filter(User.email == email).first()

# UPDATE
def update_user(user_id: int, name: str, email: str, is_active: bool):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        
        user.name = name 
        user.email = email
        user.is_active = is_active

        session.commit()
        return user
    except:
        session.rollback()
        raise
    finally:
        session.close()

# DELETE
def delete_user(user_id: int):
    session = SessionLocal()
    try:
     user = session.query(User).filter(User.id == user_id).first()
     if not user:
         return False
     
     session.delete(user)
     session.commit()
     return True
    except:
        session.rollback()
        raise
    finally:
        session.close()