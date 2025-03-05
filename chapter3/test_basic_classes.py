# test_chapter3.py
import pytest
from basic_classes import Rectangle, BankAccount

# Rectangle 클래스 테스트
def test_rectangle():
    rect = Rectangle(5, 10)
    assert rect.width == 5
    assert rect.height == 10
    assert rect.area() == 50
    assert rect.perimeter() == 30
    assert not rect.is_square()
    
    square = Rectangle(7, 7)
    assert square.area() == 49
    assert square.perimeter() == 28
    assert square.is_square()

# BankAccount 클래스 테스트
def test_bank_account():
    account = BankAccount("123456789", "John Doe", 1000)
    assert account.account_number == "123456789"
    assert account.owner_name == "John Doe"
    assert account.get_balance() == 1000
    
    assert account.deposit(500) == 1500
    assert account.withdraw(200) == 1300
    
    with pytest.raises(ValueError):
        BankAccount("123456789", "John Doe", -100)
        
    with pytest.raises(ValueError):
        account.deposit(-50)
        
    with pytest.raises(ValueError):
        account.withdraw(-50)
        
    with pytest.raises(ValueError):
        account.withdraw(2000)
