

### 1. **BankAccount Class**

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance!")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

if __name__ == "__main__":
    account = BankAccount("123456789", 1000)
    account.deposit(500)
    account.withdraw(200)
    account.display()

### 2. **Shape with Rectangle and Circle**

from math import pi

class Shape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

if __name__ == "__main__":
    shape1 = Rectangle(5, 3)
    shape2 = Circle(4)

    print("Rectangle Area:", shape1.area())
    print("Rectangle Perimeter:", shape1.perimeter())
    print("Circle Area:", shape2.area())
    print("Circle Perimeter:", shape2.perimeter())

### 3. **Person Class with Instance Counter**

class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @staticmethod
    def get_count():
        return Person.count

    def get_name(self):
        return self.name

if __name__ == "__main__":
    person1 = Person("Alice")
    person2 = Person("Bob")

    print("Total Persons:", Person.get_count())
    print(person1.get_name())
    print(person2.get_name())

### 4. **Employee Class with Overloaded Operators**


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __add__(self, other):
        return Employee("Combined", self.salary + other.salary)

    def __sub__(self, other):
        return Employee("Difference", self.salary - other.salary)

    def get_salary(self):
        return self.salary

if __name__ == "__main__":
    emp1 = Employee("Alice", 5000)
    emp2 = Employee("Bob", 6000)

    if emp1 < emp2:
        print("Bob has a higher salary than Alice.")
    else:
        print("Alice has a higher salary than Bob.")

    combined = emp1 + emp2
    print("Combined Salary:", combined.get_salary())

    difference = emp1 - emp2
    print("Salary Difference:", difference.get_salary())

### 5. **Time Class with Display Format**

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f"{self.hours}:{self.minutes:02}"

if __name__ == "__main__":
    time = Time(14, 30)
    print("Time:", time)
