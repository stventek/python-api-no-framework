from werkzeug.routing import Rule
from controllers.recipe_controller import RecipeController
from routes.utils import create_route
from services.recipe_service import RecipeService

recipeController = RecipeController(RecipeService())

routes = []
routes.append(create_route('/recipes', recipeController.get_recipes, "GET"))
routes.append(create_route('/recipe/<int:id>', recipeController.get_recipe, "GET"))

def setup_routes():
    return routes
