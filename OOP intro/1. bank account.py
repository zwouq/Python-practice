class BankAccount:
    def __init__(self):
        self.__balance = 0  # приватное свойство

    def deposit(self, amount):  # метод для внесения депозита
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):  # метод для снятия денег
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount
        return self.__balance

# Создаем новый экземпляр класса BankAccount
account1 = BankAccount()

# Добавляем на счет 100
deposit1 = account1.deposit(100)
print(deposit1)

# Снимаем со счета 50
withdraw1 = account1.withdraw(50)
print(withdraw1)