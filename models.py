from sqlmodel import Field, SQLModel, create_engine


class Chat(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    race: str
    age: int | None = None


# Configuration base SQLite
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

# Création des tables
SQLModel.metadata.create_all(engine)