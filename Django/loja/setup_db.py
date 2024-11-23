from sqlalchemy import create_engine
from apirestful.models import Base  


DATABASE_URI = "sqlite:///db.sqlite3" 

def setup_database():
    engine = create_engine(DATABASE_URI)
    Base.metadata.create_all(engine)  

if __name__ == "__main__":
    setup_database()
    print("Tabelas criadas")
