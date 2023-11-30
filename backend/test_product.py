import unittest
from product import  DigitalProduct, PackageProduct, PromotionalProduct


class TestProduct(unittest.TestCase):

    def test_price_screen(self):
        digital_product = DigitalProduct(name="Digital", number_of_assets=0, discount=0, free=False)
        assert digital_product.price() == 1000

    def test_price_package_one_asset(self):
        package_product = PackageProduct(name="Package - 1 asset", number_of_assets=1, discount=0, free=False)
        assert package_product.price() == 1000

    def test_price_package_five_assets(self):
        package_product = PackageProduct(name="Package - 5 assets", number_of_assets=5, discount=0, free=False)
        assert package_product.price() == 4500

    def test_price_package_zero_asset(self):
        package_product = PackageProduct(name="Package - 0 asset", number_of_assets=0, discount=0, free=False)
        assert package_product.price() == 100

    def test_price_promotional_10_percent(self):
        promotional_product = PromotionalProduct(name="Promotional - 10 percent", number_of_assets=0, discount=10, free=False)
        assert promotional_product.price() == 900

    def test_price_promotional_60_percent(self):
        promotional_product = PromotionalProduct(name="Promotional - 60 percent", number_of_assets=0, discount=60, free=False)
        assert promotional_product.price() == 500

    def test_price_promotional_free(self):
        promotional_product = PromotionalProduct(name="Promotional - 60 percent", number_of_assets=0, discount=60, free=True)
        assert promotional_product.price() == 0


if __name__ == '__main__':
    unittest.main()
