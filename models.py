class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """

        return self.quantity >= quantity

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """

        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError(f'В магазине доступно: {self.quantity} единиц товара при требуемых: {quantity}')

    def __hash__(self):
        return hash(self.name + self.description)

    def __eq__(self, other):
        return self.name == other.name and self.description == other.description


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """

        if product not in self.products:
            self.products[product] = buy_count
        else:
            self.products[product] += buy_count

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product in self.products:
            if remove_count is None or remove_count > self.products[product]:
                # self.products = {key: value for key, value in self.products.items() if key != product}
                self.products.pop(product)
            else:
                self.products[product] -= remove_count

    def clear(self):
        self.products = {}

    def get_total_price(self) -> float:
        total_price = 0.0
        for key, value in self.products.items():
            total_price += float(value) * float(key.price)

        return total_price

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        # for key, value in self.products.items():
        # if key.quantity >= value:
        #     key.buy(value)
        # else:
        #     raise ValueError(f'На складе доступно: {key.quantity} единиц товара при требуемых: {value}')

        for product, quantity in self.products.items():
            product.buy(quantity)
        self.clear()
