from typing import List


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        # DFS: O(r + n + s) time, O(r) space, where r is the size of recipes, n is
        # total number of unique ingredients, and s is the size of supplies

        can_cook_recipe = {}
        for ingredient in supplies:
            can_cook_recipe[ingredient] = True
        recipe_index = {}
        for i, recipe in enumerate(recipes):
            recipe_index[recipe] = i

        def dfs(recipe: str) -> bool:
            if recipe in can_cook_recipe:
                return can_cook_recipe[recipe]
            elif recipe not in recipe_index:
                return False
            can_cook_recipe[recipe] = False
            for ingredient in ingredients[recipe_index[recipe]]:
                if not dfs(ingredient):
                    return False
            can_cook_recipe[recipe] = True
            return can_cook_recipe[recipe]

        cookable_recipes = []
        for recipe in recipes:
            if dfs(recipe):
                cookable_recipes.append(recipe)
        return cookable_recipes
