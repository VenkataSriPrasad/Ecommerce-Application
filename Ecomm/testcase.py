import sys
import mysql.connector
import unittest
from Entity import products
from serviceprovider import serviceprovider



class TestEcommerceSystem(unittest.TestCase):
    def setUp(self):
        self.ecommerce = serviceprovider()

    def test_create_product(self):
        product_id = 103
        name="rice"
        price=200
        description='rice with curry and curd'
        stockQuantity=1
        created_product =self.ecommerce.create_product(product_id, name, price,description,stockQuantity)
        self.assertTrue(created_product)

    def test_add_to_cart(self):
        cart_id =15
        customer_id = 3
        product_id = 4
        quantity = 4
        added_to_cart = self.ecommerce.addTocart(cart_id ,customer_id, product_id, quantity)
        self.assertTrue(added_to_cart)