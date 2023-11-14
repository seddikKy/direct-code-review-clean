import unittest
from product import ProductType, Product


class TestProduct(unittest.TestCase):

    def test_price_screen(self):
        product = Product(ProductType.Digital, "Digital", 0, 0, False)
        assert product.price() == 1000

    def test_price_package_one_asset(self):
        product = Product(ProductType.Package, "Package - 1 asset", 1, 0, False)
        assert product.price() == 1000

    def test_price_package_five_assets(self):
        product = Product(ProductType.Package, "Package - 5 assets", 5, 0, False)
        assert product.price() == 4500

    def test_price_package_zero_asset(self):
        product = Product(ProductType.Package, "Package - 0 assets", 0, 0, False)
        assert product.price() == 100

    def test_price_promotional_10_percent(self):
        product = Product(ProductType.Promotional, "Promotional - 10 percent", 0, 10, False)
        assert product.price() == 900

    def test_price_promotional_60_percent(self):
        product = Product(ProductType.Promotional, "Promotional - 60 percent", 0, 60, False)
        assert product.price() == 500

    def test_price_promotional_free(self):
        product = Product(ProductType.Promotional, "Promotional - Free", 0, 60, True)
        assert product.price() == 0


if __name__ == '__main__':
    unittest.main()
