from models.recipe import Recipe
from serializers.recipe_serializer import recipe_schema, recipes_schema
from serializers.ingridient_serializer import ingredient_schema
from config import Session
from sqlalchemy import select

class RecipeService:
    @staticmethod
    def get_recipes():
        with Session() as session:
            recipes = session.scalars(select(Recipe)).all()
            return recipes_schema.dumps(recipes)
    
    @staticmethod
    def get_recipe(id):
        with Session() as session:
            recipe = session.scalars(select(Recipe).where(Recipe.id == id)).first()
            return recipe_schema.dumps(recipe)
