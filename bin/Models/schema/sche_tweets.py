from sqlalchemy import Table,Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, String
from bin.Config.db_setting import meta,engine


Tweet = Table("Tweet",meta,
        Column("id",String(length=60),primary_key=True),
        Column("content",String(length=256)),
        Column("create_at",DateTime()),
        Column("update_at",DateTime()),
        Column("create_by",String(length=60),ForeignKey('users.id'))
        )

meta.create_all(engine)