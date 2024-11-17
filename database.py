from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///database.db"

engine = create_engine('mysql+pymysql://GangaJoshi:Prabha9milan@GangaJoshi.mysql.pythonanywhere-services.com/GangaJoshi$fynd')
# engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
