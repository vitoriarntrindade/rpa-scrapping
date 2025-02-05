from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import declarative_base, sessionmaker
from config import MYSQL_CONFIG


DB_URL = f"mysql+pymysql://{MYSQL_CONFIG['user']}:{MYSQL_CONFIG['password']}@{MYSQL_CONFIG['host']}/{MYSQL_CONFIG['database']}"
engine = create_engine(DB_URL, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class News(Base):
    """Modelo para a tabela de notícias."""
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


def create_table():
    Base.metadata.create_all(bind=engine)


def insert_news(title: str):
    """Insere uma notícia no banco de dados usando SQLAlchemy."""
    with SessionLocal() as session:
        news_entry = News(title=title)
        session.add(news_entry)
        session.commit()
        print("Notícia armazenada no banco de dados.")

