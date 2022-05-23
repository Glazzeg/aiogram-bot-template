from gino import Gino
from data.config import POSTGRESSURI
from gino.schema import GinoSchemaVisitor
db = Gino()


async def create_db():
    await db.set_bind(POSTGRESSURI)
    db.gino: GinoSchemaVisitor
    await db.gino.create_all()