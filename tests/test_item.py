"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, KeyBoard
from src.phone import Phone


@pytest.fixture
def exemple():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def exemple2():
    return Phone("iPhone 14", 120_000, 5, 2)

@pytest.fixture
def exemple3():
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test_calculate_total_price(exemple):
    assert exemple.calculate_total_price() == 10000


def test_apply_discount(exemple):
    exemple.pay_rate = 0.8
    exemple.apply_discount()
    assert exemple.price == 8000


def test_str(exemple2):
    assert str(exemple2) == 'iPhone 14'


def test_repr(exemple2):
    assert repr(exemple2) == "Phone('iPhone 14', 120000, 5, 2)"


def test_add(exemple, exemple2):
    assert exemple + exemple2 == 25
    assert exemple2 + exemple2 == 10
    assert exemple + ("iPhone 14", 120_000, 5, 2) == None


def test_number_of_sim(exemple2):
    assert exemple2.number_of_sim == 2

def test_str(exemple3):
    assert str(exemple3) == "Dark Project KD87A"
    assert str(exemple3.language) == "EN"
    exemple3.change_lang()
    assert str(exemple3.language) == "RU"
    exemple3.change_lang().change_lang()
    assert str(exemple3.language) == "RU"

def test_Errors():
    assert Item.instantiate_from_csv() == 'Файл item.csv поврежден'