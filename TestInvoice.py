import pytest

from Invoice import Invoice
from unittest.mock import patch


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

@pytest.fixture()
def input_value():
    userInput = 'y'
    return userInput

def test_CanCalculateTotalImpurePrice(products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38
    
def test_addProduct(invoice, products):
    invoice.addProduct(products,'price', 'discount')
    assert invoice.addProduct(products,'price','discount')
# this test case helps make sure that products are being added using the #add product method. price and discount are positional argument that
# are needed for the test case.

#This line creates input to be assigned as 'y' automatically, as opposed to needing user input manually.
# We chose to add this test case to make sure that inputs received were correct.
@patch('builtins.input', return_value='y')
def test_inputAnswer(input_value):
    invoice = Invoice
    # Assert that inputAnswer is called with our coded input above, and returns equal to 'y', if it does, return true
    assert invoice.inputAnswer(Invoice, input_value) == 'y'


