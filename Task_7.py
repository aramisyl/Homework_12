class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        if product in self.items:
            self.items.remove(product)
        else:
            print("Невозможно удалить продукт.")

    def get_total(self):
        total_sum = 0
        for item in self.items:
            total_sum += item.price
        return total_sum
