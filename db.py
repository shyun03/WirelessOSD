from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import pymysql
pymysql.install_as_MySQLdb()

user_name = "root"
user_pwd = "0313"
db_host = "52.79.111.158"
db_name = "OSD_DB"

DATABASE = 'mysql+pymysql://%s:%s@%s:3306/%s?charset=utf8mb4' % (
    user_name,
    user_pwd,
    db_host,
    db_name
)

ENGINE = create_engine(
    DATABASE, 
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base= declarative_base()
Base.query = session.query_property()
