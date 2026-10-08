


class physick:
    def __init__(self,name,density):
        self.name = name
        self.density=density
list_of_matirials=["water","gold","steel"]

density=0


materials_db = {
    "water": 1.0,
    "gold": 19.3,
    "steel": 7.8
}

# Запрашиваем ввод и приводим к нижнему регистру для точного совпадения со словарем
user_input = input("Enter the material: ").strip().lower()

if user_input not in materials_db:
    print("Error: Material not found.")
else:
    # Получаем правильное имя (с заглавной буквы) и плотность из базы данных
    name = user_input.title()
    density = materials_db[user_input]

    matirial=physick(name,density)
    print(f"your matirial  is {matirial.name}")
    print(f" your matirial density is {matirial.density} gr/sm3")



