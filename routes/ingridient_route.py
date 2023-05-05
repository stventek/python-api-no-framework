from werkzeug.routing import Rule
from controllers.ingredient_controller import IngredientController
from routes.utils import create_route
from services.ingredient_service import IngredientService

ingredientController = IngredientController(IngredientService())

routes = []
routes.append(create_route('/ingredients', ingredientController.get_ingredients, "GET"))
routes.append(create_route('/ingredient/<int:id>', ingredientController.get_ingredient, "GET"))

def setup_routes():
    return routes
