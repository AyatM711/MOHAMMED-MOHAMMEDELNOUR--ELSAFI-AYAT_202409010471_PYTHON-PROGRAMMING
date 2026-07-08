import pytest
from food_order import calculate_total

def test_order1():
    assert calculate_total(10, 2) == 20

#  Test if total food order is equal to 30
def test_order2():
    assert calculate_total(15, 2) == 30

# Test if total food order is equal to 100
def test_order3():
    assert calculate_total(25, 4) == 100

# Test if total food order is equal to 10
def test_order4():
    assert calculate_total(5, 2) == 10

#  Test if total food order is equal to "invalid price"
def test_order5():
    assert calculate_total(-10, 2) == "invalid price"

#  Test if total food order is equal to "invalid quantity"
def test_order6():
    assert calculate_total(10, 0) == "invalid quantity"