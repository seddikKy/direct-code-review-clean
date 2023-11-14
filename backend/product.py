from enum import Enum
from abc import ABC, abstractmethod



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
    def _base_price(self):
        pass

    def to_json(self):
        return JsonConverter().to_json(self)
    

class JsonConverter:
    @staticmethod
    def to_json(product:Product):
        return {
            'name': product._name,
            'type': product.product_type().value,
            'price': product.price(),
            'discount': product._discount,
            'free': product._free,
            'assets': product._number_of_assets
        }


class DigitalProduct(Product):
    def price(self):
        return self._base_price()
    
    def _base_price(self):
        return 1000
    
    def product_type(self):
        return ProductType.Digital
    

class PackageProduct(Product):
    def price(self):
        if self._number_of_assets > 2:
                return self._base_price() * self._number_of_assets * self._discount_factor()
        else:
            return max([100, self._base_price() * self._number_of_assets])
    
    def _base_price(self):
        return 1000
        
    def product_type(self):
        return ProductType.Package
    
    def _discount_factor(self):
        return 0.9

    
class PromotionalProduct(Product):
    def price(self):
        if not self._free:
            return self._calculate_base_price_with_discount(self._discount)
        return 0
    
    def product_type(self):
        return ProductType.Promotional

    def _base_price(self):
        return 1000
    
    def _calculate_base_price_with_discount(self, discount):
        return max([500, self._base_price() - self._base_price() * discount/100.0])

