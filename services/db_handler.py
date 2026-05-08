from .config import db
from .models.models import Profile,Friend

def db_init(path):
    db.init(path)
    db.connect()
    db.create_tables([Profile, Friend])
    return db