import json
import os

# File to store recipes
DATA_FILE = "data/recipes.json"

# Ensure the data directory exists
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)


def load_recipes():
    try:
        if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:  # Check if the file is non-empty
            with open(DATA_FILE, "r") as file:
                return json.load(file)  # Load JSON data
        else:
            return []  # Return an empty list if the file doesn't exist or is empty
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file. Initializing with an empty recipe list.")
        return []  # Return an empty list if JSON decoding fails


# Save recipes to the file
def save_recipes(recipes):
    with open(DATA_FILE, "w") as file:
        json.dump(recipes, file, indent=4)


# Add a new recipe
def add_recipe(recipes):
    title = input("Enter the recipe title: ").strip()
    ingredients = input("Enter ingredients (comma-separated): ").split(",")
    instructions = input("Enter the instructions: ").strip()

    recipe = {
        "title": title,
        "ingredients": [ingredient.strip() for ingredient in ingredients],
        "instructions": instructions
    }
    recipes.append(recipe)
    save_recipes(recipes)
    print("Recipe added successfully!")


# View all recipes
def view_recipes(recipes):
    if not recipes:
        print("No recipes found.")
    else:
        for index, recipe in enumerate(recipes, start=1):
            print(f"\nRecipe {index}:")
            print(f"Title: {recipe['title']}")
            print(f"Ingredients: {', '.join(recipe['ingredients'])}")
            print(f"Instructions: {recipe['instructions']}")


# Search for recipes
def search_recipes(recipes):
    keyword = input("Enter a keyword to search (title or ingredient): ").lower()
    results = [
        recipe for recipe in recipes
        if
        keyword in recipe['title'].lower() or any(keyword in ingredient.lower() for ingredient in recipe['ingredients'])
    ]
    if not results:
        print("No recipes found.")
    else:
        print(f"Found {len(results)} recipe(s):")
        for recipe in results:
            print(f"Title: {recipe['title']}")
            print(f"Ingredients: {', '.join(recipe['ingredients'])}")
            print(f"Instructions: {recipe['instructions']}\n")


# Edit a recipe
def edit_recipe(recipes):
    title = input("Enter the title of the recipe to edit: ").strip()
    for recipe in recipes:
        if recipe['title'].lower() == title.lower():
            print("Editing Recipe...")
            recipe['title'] = input(f"New title (or press Enter to keep '{recipe['title']}'): ") or recipe['title']
            ingredients = input("New ingredients (comma-separated, or press Enter to keep current): ")
            if ingredients:
                recipe['ingredients'] = [ingredient.strip() for ingredient in ingredients.split(",")]
            recipe['instructions'] = input(f"New instructions (or press Enter to keep current): ") or recipe[
                'instructions']
            save_recipes(recipes)
            print("Recipe updated successfully!")
            return
    print("Recipe not found.")


# Delete a recipe
def delete_recipe(recipes):
    title = input("Enter the title of the recipe to delete: ").strip()
    for recipe in recipes:
        if recipe['title'].lower() == title.lower():
            recipes.remove(recipe)
            save_recipes(recipes)
            print("Recipe deleted successfully!")
            return
    print("Recipe not found.")


# Main menu
def main():
    print("Welcome to the Recipe Manager!")
    recipes = load_recipes()

    while True:
        print("\nOptions:")
        print("1. Add a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_recipe(recipes)
        elif choice == "2":
            view_recipes(recipes)
        elif choice == "3":
            search_recipes(recipes)
        elif choice == "4":
            edit_recipe(recipes)
        elif choice == "5":
            delete_recipe(recipes)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
