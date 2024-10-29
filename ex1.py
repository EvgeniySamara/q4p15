# Задание 1. Тестирование класса с использованием pytest
# Напишите класс BankAccount, который управляет балансом счета. Он должен
# поддерживать следующие методы:
# ● deposit(amount): добавляет указанную сумму к балансу.
# ● withdraw(amount): снимает указанную сумму с баланса, если достаточно
# средств.
# ● get_balance(): возвращает текущий баланс счета.
# При попытке снять больше средств, чем доступно на счете, должно
# выбрасываться исключение InsufficientFundsError. Напишите как минимум
# 5 тестов для проверки работы классов и его методов.
# Подсказка № 1
# Проверьте, что начальный баланс создаваемого объекта BankAccount корректен,
# используя значение, переданное в конструкторе. Убедитесь, что баланс
# инициализируется правильно при создании объекта.
# Подсказка № 2
# Проверьте, что метод deposit корректно добавляет указанную сумму к текущему
# балансу. Убедитесь, что сумма депозита положительна и увеличивает баланс на
# ожидаемое значение.
# Подсказка № 3
# Убедитесь, что метод withdraw корректно уменьшает баланс на указанную сумму,
# если на счету достаточно средств. Проверьте правильность работы метода при
# различных значениях суммы.
# Подсказка № 4
# Убедитесь, что метод withdraw корректно выбрасывает исключение
# InsufficientFundsError, когда пытаются снять больше средств, чем доступно на
# счету. Используйте pytest.raises для проверки этого поведения.
# Подсказка № 5
# Проверьте, что при создании объекта BankAccount без указания начального баланса,
# баланс инициализируется как 0. Это поможет убедиться в правильности работы
# конструктора с дефолтными значениями.

class InsufficientFundsError (Exception):
    def __init__(self, amount):
        super().__init__(f"Недостаточно средств на счете для снятия {amount}")

class BankAccount:
    balance = 0

    def __init__(self,amount):
        self.balance = amount

    def deposit(self,amount):
        if amount<0:
            raise ValueError()
        else:
            self.balance+=amount

    def withdraw(self,amount):
        if self.balance - amount >0:
            self.balance-=amount
        else:
            raise InsufficientFundsError(amount)

    def get_balance(self):
        return self.balance

import pytest
@pytest.fixture
def bank_account():
    # Подготовка тестового состояния
    return BankAccount(100) # Начальный баланс 100

def test_initial_balance(bank_account):
    # Проверка начального баланса
    assert bank_account.get_balance() == 100

def test_deposit(bank_account):
    # Проверка депозита
    bank_account.deposit(50)
    assert bank_account.get_balance() == 150

def test_withdraw(bank_account):
    # Проверка снятия средств
    bank_account.withdraw(30)
    assert bank_account.get_balance() == 70

def test_withdraw_insufficient_funds(bank_account):
    # Проверка снятия больше средств, чем доступно
    with pytest.raises(InsufficientFundsError):
        bank_account.withdraw(200)

def test_deposit_negative_amount(bank_account):
    # Проверка депозита отрицательной суммы
    with pytest.raises(ValueError):
        bank_account.deposit(-10)