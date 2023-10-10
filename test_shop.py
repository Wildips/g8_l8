"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    # return {Product("book", 100, "This is a book", 1000): 0}
    return {{Product("book", 100, "This is a book", 1000): 0}}


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    @classmethod
    def test_product_check_quantity(cls, product):
        assert Product.check_quantity(product, quantity=1000), 'Ожидается значение True'
        assert not Product.check_quantity(product, 1001), 'Ожидается значение False'

    @classmethod
    def test_product_buy(cls, product):
        assert Product.buy(product, quantity=1000) is None, 'Ожидается значение None'

    @classmethod
    def test_product_buy_more_than_available(cls, product):
        with pytest.raises(ValueError):
            assert Product.buy(product, 1001), 'Ожидается значение ValueError'


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    @classmethod
    # @staticmethod
    def test_add_product(cls, product):  # , cart):

        assert Cart.add_product(product)

        # new_cart = Cart.add_product(cart, product, buy_count=1)
        # new_cart = Cart.add_product(cls, product, buy_count=1)
        #
        # assert new_cart.products
