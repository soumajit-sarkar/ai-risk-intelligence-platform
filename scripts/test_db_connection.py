from sqlalchemy import text

from app.db.database import engine


def main():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT DATABASE()"))
            database_name = result.scalar()

            print("Database connection successful!")
            print(f"Connected database: {database_name}")

    except Exception as exc:
        print("Database connection failed!")
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()