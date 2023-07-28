from peewee import Model, IntegerField, TextField
from database import db

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    dept_id = IntegerField(primary_key=True)
    dept_name = TextField(null=True)

    class Meta:
        table_name = 'department'