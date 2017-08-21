"""
Onbill models

"""
from mongoengine import Document, EmbeddedDocument, fields, connect

connect('mongodb')


class FrontUser(Document):
    id = fields.StringField(required=True)
    password = fields.StringField(required=True)
    email = fields.StringField(required=True)
    emailVerified = fields.BooleanField(default=False)
    termsVersion = fields.IntField()
