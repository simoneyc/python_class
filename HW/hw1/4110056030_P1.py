class RecipeApp:
    def __init__(self):
        self.recipes = [
            {"name": "普羅旺斯雜燴", "ingredients": {"櫛瓜", "茄子", "牛蕃茄", "洋蔥", "甜椒", "大蒜"}},
            {"name": "洋蔥炒蛋", "ingredients": {"洋蔥", "蛋"}},
            {"name": "櫛瓜蝦仁煎蛋", "ingredients": {"櫛瓜", "雞蛋", "蝦仁", "米酒"}},
            {"name": "洋蔥燴蛋豆腐", "ingredients": {"蝦仁", "蛋豆腐", "洋蔥", "雞蛋"}},
            {"name": "茄子煲豆腐", "ingredients": {"茄子", "豆腐", "蔥"}},
            {"name": "豚汁味噌湯", "ingredients": {"牛蒡", "蘿蔔", "豬五花", "豆腐", "味噌"}}
        ]

    def search_recipes_by_ingredients(self, ingredients):
        matching_recipes = []
        for recipe in self.recipes:
            if recipe["ingredients"].issubset(ingredients):
                matching_recipes.append(recipe["name"])
        return matching_recipes

    def search_recipes_by_name(self, name):
        matching_recipes = [recipe for recipe in self.recipes if recipe["name"].lower() == name.lower()]
        return matching_recipes

    def display_recipes(self, recipes):
        if recipes:
            # print("以下是您可以製作的食譜：")
            for recipe in recipes:
                print(recipe, end=' ')
            print()
        else:
            print("找不到符合的食譜")

    def add_recipe(self, name, ingredients):
        self.recipes.append({"name": name, "ingredients": set(ingredients)})
        # print(f"食譜 '{name}' 已成功添加！")

    def run_app(self):
        while True:
        
            choice = input("1.快速料理製作,2.食譜材料確認,3.新增食譜,4.關閉:")

            if choice == "1":
                user_input = input("食材:")
                user_input = user_input.replace(' ', ',').replace('+', ',')
                ingredients = set(filter(None, user_input.split(',')))
                matching_recipes = self.search_recipes_by_ingredients(ingredients)
                self.display_recipes(matching_recipes)

            elif choice == "2":
                i = 1
                for recipe in self.recipes:
                    print( str(i) + " " + recipe['name'], end=" ")
                    i += 1
                print()
                recipe_num = input("輸入食譜編號:")
                if recipe_num.isdigit():  # 判斷是否為數字
                    index = int(recipe_num) - 1  # 由於索引是從0開始，所以需要減1
                    if 0 <= index < len(self.recipes):
                        ingredients = self.recipes[index]['ingredients']
                        print(self.recipes[index]['ingredients'])
                    else:
                        print("無效的編號，請輸入有效的編號")
                else:
                    matching_recipes = self.search_recipes_by_name(recipe_num)
                    self.display_recipes(matching_recipes)

            elif choice == "3":
                recipe_name = input("食譜名稱:")
                ingredients = input("食材:").replace(' ', ',').replace('+', ',')
                ingredients = set(filter(None, ingredients.split(',')))
                self.add_recipe(recipe_name, ingredients)
    
            elif choice == "4":
                break

            else:
                print("請輸入有效的選擇(1-4)")

if __name__ == "__main__":
    app = RecipeApp()
    app.run_app()
