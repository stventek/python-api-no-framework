from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.recipe import Recipe
from marshmallow import fields

class RecipeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Recipe
        load_instance = True
    ingredients = fields.Nested("IngredientSchema", many=True)    

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)
