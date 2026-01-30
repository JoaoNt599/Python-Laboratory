from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from apirestful.models import Base, engine 


DATABASE_URI = "sqlite:///db.sqlite3" 

# Docker
# DATABASE_URI = "postgresql://postgres:postgres@db:5432/loja"


def setup_database():
    engine = create_engine(DATABASE_URI)
    Base.metadata.create_all(engine)  

    # Docker
    # engine = create_engine(DATABASE_URI)
    # Session = sessionmaker(bind=engine)
    # session = Session()

if __name__ == "__main__":
    setup_database()
    print("Tabelas criadas")
