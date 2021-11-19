
from marshmallow import Schema, fields,validate

class CreatePostInputSchema(Schema):
    name =  fields.String(required=True,validate=validate.Length(min=1))
    description = fields.String(required=True)