from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:@localhost:3306/FAST_API_CLOUD")
meta = MetaData()
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()