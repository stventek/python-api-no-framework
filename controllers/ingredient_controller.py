from werkzeug.wrappers import Response

class IngredientController:

    def __init__(self, service):
        self.service = service

    def get_ingredients(self, request):
        ingredients = self.service.get_ingredients()
        return Response(ingredients, content_type="application/json")

    def get_ingredient(self, request, id):
        ingredient = self.service.get_ingredient(id)
        return Response(ingredient, content_type="application/json")
