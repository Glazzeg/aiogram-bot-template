from sqlalchemy import sql, Column

from utils.db_api.database import db


class Item(db.Model):
    __tablename__ = "items"
    query: sql.Select

    id = Column(db.Integer, Sequence=("user_is_seq"), primary_key=True)
    category_code = Column(db.string(20))
    category_name = Column(db.string(50))

    subcategory_code = Column(db.string(20))
    subcategory_name = Column(db.string(50))

    name = Column(db.string(50))
    photo = Column(db.string(250))
    description = Column(db.string(700))

    def __repr__(self):
        return f"{self.name}"