from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import base


def session_maker():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    base.Base.metadata.create_all(engine)
    return Session()
