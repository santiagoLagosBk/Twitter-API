from sqlalchemy import create_engine,MetaData

engine = create_engine("mysql+pymysql://root:root123@localhost:3306/twitter",
encoding='utf-8')

meta = MetaData()
conn = engine.execute()
