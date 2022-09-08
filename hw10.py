class Shop:
    def __init__(self):
        self.__product_list = []

    def product_supply(self, product):
        product_in_list = None
        for i in self.__product_list:
            if i.get_identifier() == product.get_identifier():
                self.__product_list[self.__product_list.index(i)].set_quantity(i.get_quantity() + product.get_quantity())
                product_in_list = True
        if not product_in_list:
            self.__product_list.append(product)
        print(f"Продукт {product.get_name()} поставлен в магазин в количестве {product.get_quantity()} шт.")

    def product_selling(self, product):
        for i in self.__product_list:
            if i.get_identifier() == product.get_identifier():
                if i.get_quantity() >= product.get_quantity():
                    i.set_quantity(i.get_quantity() - product.get_quantity())
                    print(f"Продукт {product.get_name()} продан в количестве {product.get_quantity()} шт.")
                else:
                    print(f"Продукта {product.get_name()} нет в таком количестве")
            else:
                print(f"Продукта {product.get_name()} нет в наличии")

    def add_product_to_sale_list(self, product, discount):
        for i in self.__product_list:
            if i.get_identifier() == product.get_identifier():
                try:
                    i.set_discount(int(discount))
                    i.set_cost(i.get_cost() - i.get_cost() * i.get_discount() / 100)
                    print(f"Продукт {product.get_name()} теперь продаётся со скидкой {discount}%")
                except ValueError:
                    print("Значение скидки должно быть указано в виде числа")
            else:
                print(f"Продукта {product.get_name()} нет в наличии")


class Products:
    def __init__(self, identifier, name, cost, quantity):
        self.__name = name
        self.__discount = 0
        try:
            self.__identifier = int(identifier)
        except ValueError:
            self.__identifier = -1
            print("Значение идентификатора должно быть указано в виде числа")
        try:
            self.__cost = float(cost)
        except ValueError:
            self.__cost = -1
            print("Значение стоимости должно быть указано в виде числа")
        try:
            self.__quantity = int(quantity)
        except ValueError:
            self.__quantity = -1
            print("Значение количества должно быть указано в виде числа")

    def __str__(self):
        return f"identifier: {self.__identifier}, name: {self.__name}, cost: {self.__cost}Р," \
               f" discount: -{self.__discount}%, quantity: {self.__quantity}"

    def get_identifier(self):
        return self.__identifier

    def get_name(self):
        return self.__name

    def get_cost(self):
        return self.__cost

    def get_quantity(self):
        return self.__quantity

    def get_discount(self):
        return self.__discount

    def set_cost(self, new_cost):
        self.__cost = new_cost

    def set_quantity(self, new_quantity):
        self.__quantity = new_quantity

    def set_discount(self, new_discount):
        self.__discount = new_discount


class FruitProduct(Products):
    def __init__(self, identifier, name, cost, quantity, country, best_before_date):
        super().__init__(identifier, name, cost, quantity)
        self.__country = country
        self.__best_before_date = best_before_date

    def __str__(self):
        return f"Fruit: {self.__identifier}, name: {self.__name}, cost: {self.__cost}Р, " \
               f"discount: -{self.__discount}%, quantity: {self.__quantity}, from: {self.__country}, " \
               f"best before: {self.__best_before_date}"


AzbukaVK = Shop()

eggs = Products(1, "Eggs", 70, 100)
eggs_to_buy = Products(1, "Eggs", 70, 20)
bread = Products(2, "Bread", 40, 1)

AzbukaVK.product_supply(eggs)
AzbukaVK.product_supply(eggs_to_buy)
print(eggs)
AzbukaVK.product_selling(bread)
AzbukaVK.add_product_to_sale_list(eggs, 10)
print(eggs)
