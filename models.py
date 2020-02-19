from app import db

class Post(db.Document):
    content = db.StringField(required=True)
    date = db.StringField(required=True)
    like = db.IntField(default=0)
    unlike = db.IntField(default=0)

    def __str__(self):
        return self.content