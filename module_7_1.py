class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                products = file.read()
            return products
        except FileNotFoundError:
            return "Файл не найден."

    def add(self, *products):
        existing_products = set()
        try:
            with open(self.__file_name, 'r') as file:
                for line in file:
                    existing_products.add(line.strip())
        except FileNotFoundError:
            pass

        with open(self.__file_name, 'a') as file:
            for product in products:
                product_str = str(product)
                if product_str not in existing_products:
                    file.write(f"{product_str}\n")
                    existing_products.add(product_str)
                else:
                    print(f"Продукт {product.name} уже есть в магазине")


if __name__ == "__main__":
    s1 = Shop()

    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
