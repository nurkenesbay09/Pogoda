class BankAccount:
    """
    Негізгі Банк Есепшоты класы.
    Бұл класс капсулалаудың негізгі принциптерін көрсетеді.
    Атрибуттар:
        _owner (str): Есепшот иесі (Protected).
        __account_number (str): Есепшот нөмірі (Private).
        _balance (float): Ағымдағы баланс (Protected).
    """
    def __init__(self, owner: str, account_number: str, initial_balance: float = 0.0):
        """
        BankAccount нысанын инициализациялау.
        Бастапқы баланс тексеруден өтеді.
        """
        self._owner = owner
        self.__account_number = account_number
        self.balance = initial_balance


    @property
    def balance(self) -> float:
        """
        Балансты оқуға арналған Getter (Getters).
        Бұл атрибут ретінде шақырылады: acc.balance
        """
        return self._balance

    @balance.setter
    def balance(self, amount: float):
        """
        Балансты орнатуға арналған Setter (Setters).
        Деректерді тексеруді (validation) қамтамасыз етеді.
        """
        if amount < 0:
            print(f"Қате: Баланс теріс сан бола алмайды ({amount}). Өзгеріс сақталмады.")
        else:
            self._balance = amount

    @property
    def owner(self) -> str:
        """Иесін оқу (Read-only). Setter жоқ, яғни иесін өзгертуге болмайды."""
        return self._owner

    @property
    def account_number(self) -> str:
        """
        Жеке шот нөмірін қауіпсіз түрде көрсету (Read-only).
        Тек соңғы 4 санды көрсетеміз.
        """
        return f"**** **** **** {self.__account_number[-4:]}"

    def deposit(self, amount: float):
        """Есепшотқа ақша салу."""
        if amount > 0:
            self.balance += amount
            print(f"{amount} KZT салынды. Жаңа баланс: {self.balance} KZT")
        else:
            print("Қате: Салынатын сома оң сан болуы керек.")

    def withdraw(self, amount: float):
        """Есепшоттан ақша шешу."""
        if amount <= 0:
            print("Қате: Шешілетін сома оң сан болуы керек.")
        elif amount > self.balance:
            print(f"Қате: Баланста жеткілікті қаражат жоқ. (Сұралды: {amount}, Қолда бар: {self.balance})")
        else:
            self.balance -= amount
            print(f"{amount} KZT шешілді. Қалған баланс: {self.balance} KZT")

    def __repr__(self) -> str:
        """Нысанды 'print' арқылы шығарғанда ресми көрінісі (жақсы код практикасы)."""
        return f"BankAccount(Owner='{self.owner}', Account='{self.account_number}', Balance={self.balance} KZT)"


class SavingsAccount(BankAccount):
    """
    Жинақ Есепшоты. BankAccount-тан мұраланады.
    Пайыз қосу мүмкіндігі бар.
    """

    def __init__(self, owner: str, account_number: str, initial_balance: float, interest_rate: float):
        """
        SavingsAccount нысанын инициализациялау.
        """
        super().__init__(owner, account_number, initial_balance)
        self._interest_rate = 0.0  # Используем защищенное свойство, а не приватное.
        self.interest_rate = interest_rate

    @property
    def interest_rate(self) -> float:
        """Пайыздық мөлшерлемені оқу."""
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, rate: float):
        """Пайыздық мөлшерлемені орнату (тексерумен)."""
        if 0.0 <= rate <= 0.5:
            self._interest_rate = rate
        else:
            print(f"Қате: Пайыздық мөлшерлеме ({rate}) 0 мен 0.5 арасында болуы керек.")

    def add_interest(self):
        """
        Есепшотқа есептелген пайызды қосу.
        """
        earned_interest = self.balance * self._interest_rate
        print(f"Есептелген пайыздар: {earned_interest:.2f} KZT")
        self.deposit(earned_interest)


if __name__ == "__main__":

    print("1. BankAccount Тестілеу")
    acc1 = BankAccount("Нұрлан Қоянбаев", "1234567890123456", 1000.0)
    print(acc1)

    acc1.deposit(500)
    acc1.withdraw(300)

    print("\n[Тест] Теріс баланс орнату әрекеті:")
    acc1.balance = -200  # Setter жұмыс істейді
    print(f"Ағымдағы баланс (өзгермеуі керек): {acc1.balance}")

    print("\n[Тест] Баланстан артық ақша шешу әрекеті:")
    acc1.withdraw(5000)
    print(acc1)

    print("\n[Тест] Жеке атрибутқа (__account_number) тікелей қол жеткізу:")
    try:
        print(acc1.__account_number)
    except AttributeError as e:
        print(f"Қате ұсталды (күтілгендей): {e}")

    print(f"Қорғалған атрибутты оқу (ұсынылмайды): {acc1._balance}")

    print("\n\n2. SavingsAccount Тестілеу (Мұрагерлік)")
    save_acc = SavingsAccount("Алихан Смайылов", "9876543210987654", 10000.0, 0.05)  # 5%
    print(save_acc)

    save_acc.add_interest()
    print(save_acc)

    print("\n[Тест] Жарамсыз пайыздық мөлшерлеме орнату:")
    save_acc.interest_rate = 2.0  # 200%
    print(f"Ағымдағы мөлшерлеме (өзгермеуі керек): {save_acc.interest_rate}")
