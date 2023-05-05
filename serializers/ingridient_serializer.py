from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.ingredient import Ingredient
from marshmallow import  fields

class IngredientSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Ingredient

ingredient_schema = IngredientSchema()
ingredients_schema = IngredientSchema(many=True)
