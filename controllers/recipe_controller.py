from werkzeug.wrappers import Response

class RecipeController:

    def __init__(self, service):
        self.service = service

    def get_recipes(self, request):
        recipes = self.service.get_recipes()
        return Response(recipes, content_type="application/json")

    def get_recipe(self, request, id):
        recipe = self.service.get_recipe(id)
        return Response(recipe, content_type="application/json")
