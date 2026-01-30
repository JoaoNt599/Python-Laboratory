from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import IntegrityError


# Database configuration
DATABASE_URL = "sqlite:///users.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


# Model
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<User(id={self.user_id}, name={self.name}, email={self.email})>"


# $ Base.metadata.create_all(bind=engine)


# CRUD functions
def create_user(name: str, email: str, is_active: bool = True):
    """Create a new user"""
    with SessionLocal() as session:
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
            raise ValueError("Email already registered")

        except Exception:
            session.rollback()
            raise


def get_users():
    """Return all users"""
    with SessionLocal() as session:
        return session.query(User).all()


def get_user_by_id(user_id: int):
    """Return a user by ID"""
    with SessionLocal() as session:
        return session.query(User).filter(User.user_id == user_id).first()


def get_user_by_email(email: str):
    """Return a user by email"""
    with SessionLocal() as session:
        return session.query(User).filter(User.email == email).first()


def update_user(user_id: int, name: str, email: str, is_active: bool):
    """Update a user"""
    with SessionLocal() as session:
        try:
            user = session.query(User).filter(User.user_id == user_id).first()
            if not user:
                return None

            user.name = name
            user.email = email
            user.is_active = is_active

            session.commit()
            return user

        except IntegrityError:
            session.rollback()
            raise ValueError("Email already registered")

        except Exception:
            session.rollback()
            raise


def delete_user(user_id: int):
    """Delete a user"""
    with SessionLocal() as session:
        try:
            user = session.query(User).filter(User.user_id == user_id).first()
            if not user:
                return False

            session.delete(user)
            session.commit()
            return True

        except Exception:
            session.rollback()
            raise



# Simple manual test
if __name__ == "__main__":
    # CREATE
    user = create_user("João", "joao@email.com")
    print(user)

    # READ
    print(get_users())

    # READ BY EMAIL
    print(get_user_by_email("joao@email.com"))

    # UPDATE
    updated = update_user(user.user_id, "João Neto", "joao@email.com", True)
    print(updated)

    # DELETE
    deleted = delete_user(user.user_id)
    print("Deleted:", deleted)
