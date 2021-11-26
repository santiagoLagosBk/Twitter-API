
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,Date
from bin.Config.db_setting import meta,engine


user_query = Table("users",meta,
    Column("id",String(length=60),primary_key=True),
    Column("email",String(length=30)),
    Column("nickname",String(length=20)),
    Column("fist_name",String(length=50)),
    Column("last_name",String(length=45)),
    Column("birth_date",Date),
    Column("password",String(length=60))
    )

meta.create_all(engine)