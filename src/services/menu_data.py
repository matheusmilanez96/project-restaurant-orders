import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        with open(source_path, encoding="utf-8") as file:
            menu_reader = csv.reader(file)
            header, *data = menu_reader

            for row in data:
                dish = row[0]
                price = float(row[1])
                ingredient = row[2]
                amount = int(row[3])

                new_dish = Dish(dish, price)
                if new_dish not in self.dishes:
                    self.dishes.add(new_dish)

                for current_dish in self.dishes:
                    if current_dish == new_dish:
                        current_dish.add_ingredient_dependency(
                            Ingredient(ingredient), amount)
