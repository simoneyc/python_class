# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:19:22 2024

@author: simone
"""

recipes = [
    {"name": "普羅旺斯雜燴", "ingredients": {"櫛瓜", "茄子", "牛蕃茄", "洋蔥", "甜椒", "大蒜"}},
    {"name": "洋蔥炒蛋", "ingredients": {"洋蔥", "蛋"}},
    {"name": "櫛瓜蝦仁煎蛋", "ingredients": {"櫛瓜", "雞蛋", "蝦仁", "米酒"}},
    {"name": "洋蔥燴蛋豆腐", "ingredients": {"蝦仁", "蛋豆腐", "洋蔥", "雞蛋"}},
    {"name": "茄子煲豆腐", "ingredients": {"茄子", "豆腐", "蔥"}},
    {"name": "豚汁味噌湯", "ingredients": {"牛蒡", "蘿蔔", "豬五花", "豆腐", "味噌"}}
]

def fun_1(ingredient):
    global recipes
    match_recipe = []
    for recipe in recipes:
        if recipe["ingredients"].issubset(ingredient):
            match_recipe.append(recipe["name"])
    # print
    for item in match_recipe:
        print(item,end=" ")
    print()
    
def fun_2(num):
    global recipes
    print(recipes[num-1]["ingredients"])
    print()
def fun_3(name,ingredient):
    global recipes
    recipes.append({"name":name,"ingredients":set(ingredient)})
    
while True:
    choice = input("1.xxx 2.xxx 3.xxx 4.xxx: ")
    if choice == '1':
        user_input = input("食材:")
        user_input = user_input.replace("+", ",").replace(" ", ",")
        ingredients = set(filter(None,user_input.split(",")))
        fun_1(ingredients)
    elif choice == "2":
        print("查詢食譜: ")
        i = 1
        for item in recipes:
            print(str(i) + " " + item["name"],end =" ")
            i += 1
        print()
        num = input("輸入食譜編號:")
        num = int(num)         
        fun_2(num)
    elif choice == "3":
        name = input("食譜名稱:")
        ingre = input("食材:")
        ingre = ingre.replace("+", ",").replace(" ", ",")
        ingre = set(filter(None, ingre.split(",")))
        fun_3(name, ingre)
    else:
        break