recipes_list = []

ingredients_list = []

def take_recipe():
    name = input("Recipe name: ")
    cooking_time = int(input("Cooking time in minutes: "))
    ingredients = input("Ingredients for the recipe: "). split(", ")

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }
    return recipe


n = int(input("How many recipes would you like to enter? "))

for i in range(n):
    recipe = take_recipe()

    for ingredient in recipe["ingredients"]:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

for recipe in recipes_list:
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
        recipe["difficulty"] = "Easy"
    elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
        recipe["difficulty"] = "Medium"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
        recipe["difficulty"] = "Intermediate"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) >= 4:
        recipe["difficulty"] = "Hard"

for recipe in recipes_list:
    print("Recipe:", recipe["name"])
    print("Cooking time (min):", recipe["cooking_time"])
    print("Ingredients")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty:", recipe["difficulty"])
    print()

print("Ingredients Available Across All Recipes")
print("========================================")

ingredients_list.sort()

for ingredient in ingredients_list:
    print(ingredient)
