print("Meal Planner developed by Monty")
diet = input("Enter diet type (veg/nonveg): ").lower()
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in cm: "))
age = int(input("Enter age: "))
gender = input("Enter gender (male/female): ").lower()
goal = input("Enter goal (lose/gain): ").lower()

print("\n--- Your Healthy Meal Suggestions ---\n")

if goal == "lose":
    if diet == "veg":
        breakfast = ["Oats with fruits", "Poha with vegetables", "Fruit bowl with nuts"]
        lunch = ["Brown rice with dal", "Chapati with vegetable curry", "Curd rice with salad"]
        dinner = ["Vegetable soup", "Salad with sprouts", "Steamed vegetables"]
    else:
        breakfast = ["Boiled eggs and fruit", "Egg omelette with toast", "Greek yogurt and fruit"]
        lunch = ["Grilled chicken with vegetables", "Fish curry with rice", "Chicken salad"]
        dinner = ["Fish soup", "Grilled chicken salad", "Boiled eggs with vegetables"]

elif goal == "gain":
    if diet == "veg":
        breakfast = ["Milk banana smoothie", "Peanut butter sandwich", "Paneer paratha"]
        lunch = ["Paneer curry with rice", "Dal makhani with chapati", "Vegetable pulao with curd"]
        dinner = ["Curd rice", "Vegetable khichdi", "Paneer bhurji with chapati"]
    else:
        breakfast = ["Egg omelette with milk", "Chicken sandwich", "Protein smoothie"]
        lunch = ["Chicken curry with rice", "Egg curry with chapati", "Fish curry with rice"]
        dinner = ["Chicken tikka with vegetables", "Fish fry with salad", "Egg bhurji with chapati"]

else:
    print("Invalid goal entered")
    exit()

print("Breakfast options:")
for item in breakfast:
    print("-", item)

print("\nLunch options:")
for item in lunch:
    print("-", item)

print("\nDinner options:")
for item in dinner:
    print("-", item)
