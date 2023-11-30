from abc import ABC, abstractmethod
from enum import Enum


class ProductType(Enum):
    Digital = 1
    Package = 2
    Promotional = 3


class Product(ABC):
    def __init__(self, name, number_of_assets, discount, free):
        self._name = name
        self._number_of_assets = number_of_assets
        self._discount = discount
        self._free = free

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def product_type(self):
        pass

    @abstractmethod
    def base_price(self):
        pass

    def to_json(self):
        return JsonConverter().to_json(self)


class ProductDiscountFactor(Product):
    @abstractmethod
    def discount_factor(self):
        pass


class DigitalProduct(Product):
    def price(self):
        return self.base_price()

    def product_type(self):
        return ProductType.Digital.value

    def base_price(self):
        return 1000


class PackageProduct(ProductDiscountFactor):
    def price(self):
        if self._number_of_assets > 2:
            return self.base_price() * self._number_of_assets * self.discount_factor()
        else:
            return max([100, self.base_price() * self._number_of_assets])

    def product_type(self):
        return ProductType.Package.value

    def discount_factor(self):
        return 0.9

    def base_price(self):
        return 1000


class PromotionalProduct(Product):
    def price(self):
        if not self._free:
            return self._calculate_base_price_with_discount(self._discount)
        return 0

    def product_type(self):
        return ProductType.Promotional.value

    def _calculate_base_price_with_discount(self, discount):
        return max([500, self.base_price() - self.base_price() * discount/100.0])

    def base_price(self):
        return 1000


class JsonConverter:
    @staticmethod
    def to_json(product: Product):
        return {
            'name': product._name,
            'type': product.product_type(),
            'price': product.price(),
            'discount': product._discount,
            'free': product._free,
            'assets': product._number_of_assets
        }

