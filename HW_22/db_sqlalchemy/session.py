from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

__engine = create_engine('postgresql://postgres:322@localhost/store')

session: Session = sessionmaker(__engine)()
