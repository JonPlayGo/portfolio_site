

user = 'JonPlayGo'
password = 'jpgo2008'
host = 'JonPlayGo.mysql.pythonanywhere-services.com'
database = 'JonPlayGo$works_portfolio'

connection_string = f'mysql://{user}:{password}@{host}/{database}'

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Work(Base):
    __tablename__ = 'works'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    text = Column(String(255))
    logo = Column(String(255))
    data = Column(String(255))

def save_work_to_database(work_name, work_text, work_logo,work_data):
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    work = Work(name=work_name, text=work_text, logo=work_logo ,data=work_data)
    session.add(work)
    session.commit()

def get_works_from_database():
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()
    works = session.query(Work).all()
    return [(work.name, work.text, work.logo, eval(work.data)) for work in works]

def delete_all_data_from_database():
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Work).delete()
    session.commit()

if __name__ == "__main__":
    delete_all_data_from_database()