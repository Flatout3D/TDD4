import pytest
from invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products


@pytest.fixture()
def input_value():
    userInput = 'y'
    return userInput


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


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


# Test that the program is adding products correctly
def test_addProduct(invoice, products):
    invoice.addProduct(products, 'price', 'discount')
    assert invoice.addProduct(products, 'price', 'discount')


# Test that the input is being received correctly
@patch('builtins.input', return_value='y')
def test_inputAnswer(input_value):
    invoice = Invoice
    assert invoice.inputAnswer(Invoice, input_value) == 'y'
