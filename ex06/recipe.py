cookbook ={ 
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    }, 
    "Cake": { 
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    },
} 
def print_all_recipe_names():
    if len(cookbook) == 0:
        print("No recipes found in the cookbook.")
    else:
        print("Recipe names:")
        for recipe_name in cookbook.keys():
            print(recipe_name)

def print_recipe_details(recipe_name):
    if recipe_name in cookbook:
        recipe = cookbook[recipe_name]
        print("Recipe details for:", recipe_name)
        print("Ingredients:"," ".join(recipe['ingredients']))
        print("Meal Type:", recipe['meal_type'])
        print("Preparation Time:", recipe['preparation_time'], "minutes")
    else:
        print("Recipe not found in the cookbook.")

def delete_recipe(recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
        print("Recipe", recipe_name, "deleted successfully.")
    else:
        print("Recipe not found in the cookbook.")

def add_recipe():
    recipe_name = input("Enter recipe name: ")
    ingredients = input("Enter ingredient")
    meal_type = input("Enter meal type: ")
    preparation_time = int(input("Enter preparation time (in minutes): "))

    cookbook[recipe_name] = {
        'ingredients': ingredients,
        'meal_type': meal_type,
        'preparation_time': preparation_time
    }
    print("Recipe", recipe_name, "added successfully.")

option = input()
print(option)
if option == "1":
   print("option 1 selectionner")