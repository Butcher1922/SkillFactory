import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)

def connect_db():
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def request_data():
    print("Введите свои данные (на английском языке)")
    first_name = input("Введите имя: ")
    last_name = input("Введдите фамилию: ")
    gender = input("Введите пол: ")
    email = input("Введите email: ")    
    birthdate = input("Введите дату рождения (в формате ГГГГ-ММ-ДД. Например, 1999-01-01): ")
    height = input("Введите рост в метрах (в формате 1.82): ")
    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )
    return user

def main():
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Данные сохранены, спасибо!")


if __name__ == "__main__":
    main()
