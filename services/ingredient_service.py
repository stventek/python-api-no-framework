from models import Ingredient
from serializers.ingridient_serializer import ingredient_schema, ingredients_schema
from config import Session
from sqlalchemy import select

class IngredientService:
    @staticmethod
    def get_ingredients():
        with Session() as session:
            ingredients = session.scalars(select(Ingredient)).all()
            return ingredients_schema.dumps(ingredients)
    
    @staticmethod
    def get_ingredient(id):
        with Session() as session:
            ingredient = session.scalars(select(Ingredient).where(Ingredient.id == id)).first()
            return ingredient_schema.dumps(ingredient)
