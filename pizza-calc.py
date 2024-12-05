from typing import List

class Ingredient: # ингредиент
    def __init__(self, name: str, weight : float, cost : float) -> None:
        self.name = name  # название
        self.weight = weight  # вес в граммах
        self.cost = cost  # стоимость в рублях
        
    def get_name(self) -> str: # название
        return self.name
    
    def get_weight(self) -> float: # вес в граммах
        return self.weight
        
    def get_cost(self) -> float: # стоимость в рублях
        return self.cost

class Pizza: # пицца
    def __init__(self, name: str) -> None:
        self.name = name # название
        self.ingredient_list: List[Ingredient] = [] # лист ингредиентов
        
    def get_name(self) -> str: # название
        return self.name
    
    def add_ingredient(self, ingredient: Ingredient) -> None: # добавить ингредиент в пиццу
        self.ingredient_list.append(ingredient)
    
    def get_cost(self) -> float: # стоимость в рублях
        return sum(ingredient.get_cost() for ingredient in self.ingredient_list)
    
    def get_weight(self) -> float: # вес в килограммах
        return sum(ingredient.get_weight() for ingredient in self.ingredient_list) / 1000

class Order: # заказ
    def __init__(self) -> None:
        self.pizza_list: List[Pizza] = []
    
    def add_pizza(self, pizza: Pizza) -> None: # добвить пиццу в заказ
        self.pizza_list.append(pizza)
    
    def get_cost(self) -> float: # стоимость в рублях
        return sum(pizza.get_cost() for pizza in self.pizza_list)
    
    def print_receipt(self) -> None: # вывести рецепт
        for pizza in self.pizza_list:
            print(f'{pizza.get_name()} ({pizza.get_weight():.3f}кг) - {pizza.get_cost():.2f}руб')
    
#тест 
cheddar = Ingredient("Чеддер", 220, 100.0)
mozzarella = Ingredient("Моцарелла", 200, 150.0)
pepperoni = Ingredient("Пепперони", 100, 120.0)
mushrooms = Ingredient("Грибы", 150, 80.0)
olives = Ingredient("Оливки", 80, 90.0)
tomatoes = Ingredient("Помидоры", 120, 70.0)
basil = Ingredient("Базилик", 30, 50.0)
chicken = Ingredient("Курица", 200, 200.0)
onion = Ingredient("Лук", 50, 30.0)
pepper = Ingredient("Перец", 100, 60.0)
garlic = Ingredient("Чеснок", 20, 40.0)
cherry_tomatoes = Ingredient("Помидоры черри", 200, 55.0)
raddish = Ingredient("Редис", 100, 73.0)

order = Order()

pizza = Pizza('Чиполлино')
pizza.add_ingredient(onion)
pizza.add_ingredient(tomatoes)
pizza.add_ingredient(cherry_tomatoes)
pizza.add_ingredient(raddish)
pizza.add_ingredient(mozzarella)
order.add_pizza(pizza)

pizza = Pizza('Без ананасов')
pizza.add_ingredient(pepperoni)
pizza.add_ingredient(chicken)
pizza.add_ingredient(olives)
pizza.add_ingredient(basil)
pizza.add_ingredient(mushrooms)
pizza.add_ingredient(cheddar)
order.add_pizza(pizza)

pizza = Pizza('Радость тестировщика')
order.add_pizza(pizza)

order.print_receipt()

'''
Калькулятор пиццы

Хомячок Хома любит плотно покушать. Одно из его любимых блюд это пицца. Помогите Хоме скомпилировать пиццу из ингредиентов и посчитать стоимость заказа.

Необходимо создать класс Ingredient, конструктор класса принимает три обязательных аргумента:

    name - название ингредиента
    weight - вес в граммах
    cost - стоимость в рублях

В класс Ingredient необходимо добавить следующие getter-методы:

    get_name() - возвращает название ингредиента
    get_weight() - возвращает вес в граммах
    get_cost() - возвращает стоимость в рублях

Необхоидмо создать класс Pizza, конструктор класса принимает один обязательный аргумент name - название пиццы.

Необходимо добавить в класс следующие методы:

    get_name() - возвращает название пиццы
    add_ingredient(ingredient) - принимает объект типа Ingredient и добавляет ингредиент в пиццу
    get_cost() - возвращает стоимость пиццы в рублях
    get_weight() - возвращает вес пиццы в килограммах (1кг=1000г)

Необходимо создать класс Order и добавить в него следующие методы:

    add_pizza(pizza) - принимает объект типа Pizza и добавляет пиццу в заказ
    get_cost() - возвращает стоимость заказа в рублях

    print_receipt() - печатает чек на экран, пример вывода чека на экран:

    Четыре сыра (0.450кг) - 450.00руб
    Ветчина и сыр (1.000кг) - 600.00руб
    Мясная (0.550кг) - 445.00руб

    Обратите внимание, что вес выводится с 3 знаками после запятой, а стоимость с 2 знаками после запятой, количество знаков перед запятой может быть любым. Воспользуйтесь форматированием строк в вашем ЯП.

Пример использования

Ниже приведен пример использования классов. Пример не является частью реализации и не должен присутствовать в конечном решении:

cream_sauce=Ingredient('Сливочный соус', 50, 50)
blue_cheese=Ingredient('Сыр блю чиз', 100, 100)
mozzarella=Ingredient('Моцарелла', 100, 100)
cheddar=Ingredient('Чеддер', 100, 100)
parmesan=Ingredient('Пармезан', 100, 100)

pizza=Pizza('Четыре сыра')
pizza.add_ingredient(cream_sauce)
pizza.add_ingredient(blue_cheese)
pizza.add_ingredient(mozzarella)
pizza.add_ingredient(cheddar)
pizza.add_ingredient(parmesan)

order=Order()
order.add_pizza(pizza)
order.add_pizza(pizza)
order.add_pizza(pizza)

pizza.get_cost()
450
pizza.get_weight()
0.45
order.get_cost()
1350
order.print_receipt()
Четыре сыра (0.450кг) - 450.00руб
Четыре сыра (0.450кг) - 450.00руб
Четыре сыра (0.450кг) - 450.00руб
'''
