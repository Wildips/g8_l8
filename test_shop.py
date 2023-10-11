"""
Протестируйте классы из модуля homework/models.py
"""
import pytest


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(quantity=1000), 'Ожидается значение True'
        assert not product.check_quantity(1001), 'Ожидается значение False'

    def test_product_buy(self, product):
        assert product.buy(quantity=1000) is None, 'Ожидается значение None'

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            assert product.buy(1001), 'Ожидается значение ValueError'


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    @pytest.mark.parametrize("count_of_item", [1, 10000])
    def test_add_product(self, product, cart, count_of_item):
        assert cart.add_product(product, count_of_item) is None, 'Ожидается значение None'
        assert cart.products, 'Ожидается что после добавления товара корзина не пуста'
        assert int(cart.products.get(product)) == count_of_item, \
            f'Ожидается что изначальное число товара: 0 ' \
            f'в результате работы метода должно быть: {count_of_item} ' \
            f'но имеет значение {cart.products.get(product)}'

    def test_remove_product(self, product, not_empty_cart):
        init_cart_amount_of_product = not_empty_cart.products.get(product)
        assert not_empty_cart.remove_product(product, 1) is None, 'Ожидается значение None'
        assert not_empty_cart.products, 'Ожидается что после удаления товара корзина не пуста'
        assert int(not_empty_cart.products.get(product)) == init_cart_amount_of_product - 1, \
            f'Ожидается что изначальное число товара: {init_cart_amount_of_product} ' \
            f'в результате работы метода должно быть: {init_cart_amount_of_product - 1} ' \
            f'но имеет значение {not_empty_cart.products.get(product)}'

    @pytest.mark.parametrize("count_of_item", [None, 10000])
    def test_remove_product_record(self, product, not_empty_cart, count_of_item):
        assert not_empty_cart.remove_product(product, count_of_item) is None, 'Ожидается значение None'
        assert not not_empty_cart.products, 'Ожидается что после удаления товара корзина пуста'

    def test_clear(self, product, not_empty_cart):
        assert not_empty_cart.clear() is None, 'Ожидается значение None'
        assert not not_empty_cart.products, 'Ожидается что после очистки корзина пуста'

    def test_get_total_price(self, product, not_empty_cart):
        result = not_empty_cart.get_total_price()
        assert result == 1000, 'Ожидается значение 1000'
        assert type(result).__name__ == "float", 'Ожидается тип данных float'

    def test_buy_for_empty_cart(self, cart):
        assert cart.buy() is None, 'Ожидается значение None'
        assert not cart.products, 'Ожидается что корзина пуста'

    def test_buy(self, not_empty_cart):
        assert not_empty_cart.buy() is None, 'Ожидается значение None'
        assert not not_empty_cart.products, 'Ожидается что корзина пуста'

    def test_buy_for_huge_amount(self, huge_cart):
        with pytest.raises(ValueError):
            assert huge_cart.buy(), 'Ожидается значение ValueError'
