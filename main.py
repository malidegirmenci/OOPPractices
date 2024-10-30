'''
class Human:
    def __init__(self, name, surname, weight, height):
        self.name = name
        self.surname = surname
        self.weight = weight
        self.height = height
        self.age = 0

furkan = Human('Furkan','İkiz', 7, 50)

print(f'{furkan.name} {furkan.surname} adlı dünya tatlısı bebeğiniz {furkan.weight} kilo, {furkan.height} cm doğmuştur. Maşallah!')
furkan.age += 1
print(furkan.age)

furkan2 = {'name': 'Furkan', 'surname': 'İkiz', 'weight': 7, 'height': 50}
print(furkan2['name'])

print(furkan.name)

class Car:
    def __init__(self, wheels, engine, model, brand, typeVehicle, horsepower):
        self.wheels = wheels
        self.engine = engine
        self.model = model
        self.brand = brand
        self.typeVehicle = typeVehicle
        self.horsepower = horsepower

    def startengine(self):
        print('Motor çalıştırılıyor. Ahan da çalıştı.')

    def run(self):
        print('Araba gidiyor')

BMW320i = Car(4, 3.20, '320i', 'BMW', 'Sedan', 200)

print(BMW320i.wheels)
print(BMW320i.engine)
print(BMW320i.model)
print(BMW320i.brand)

BMW320i.startengine()

BMW320i.run()

#Sahin = Car(4, 1.6, 'Şahin', 'Fiat-Tofaş', 'Sedan', 100)


class Box:
    def __init__(self, width, height, length, color):
        self.width = width
        self.height = height
        self.length = length
        self.color = color

goldenbox = Box(5,10,15,'Gold')
print(f'Width: {goldenbox.width}, Height: {goldenbox.height}, Length: {goldenbox.length}')
goldenbox.width = 8
goldenbox.height = 12
goldenbox.length = 20
print(f'Width: {goldenbox.width}, Height: {goldenbox.height}, Length: {goldenbox.length}')

class Player:
    def __init__(self, name, health, level, damage, defence, weapon, armor):
        self.name = name
        self.health = health
        self.level = level
        self.damage = damage
        self.defence = defence
        self.weapon = weapon
        self.armor = armor

    def attack(self, enemy_armor):
        return self.damage - enemy_armor

    def defend(self, enemy_attack):
        return self.defence - enemy_attack

class Monster:
    def __init__(self, name, health, level, damage, defence, weapon, armor):
        self.name = name
        self.health = health
        self.level = level
        self.damage = damage
        self.defence = defence
        self.weapon = weapon
        self.armor = armor

    def attack(self, enemy_armor):
        return self.damage - enemy_armor

    def defend(self, enemy_attack):
        return self.defence - enemy_attack

monster1 = Monster('Uruchi', 120, 5, 35, 20, 'Two Handed Sword', 'Heavy Armor')
player1 = Player('Umdefume', 100, 1, 25, 15, 'Dual Axe', 'Light Armor')
print('-'*10+' IteensRPG '+'-'*10)
print(f"{player1.name} adlı kahraman Downhang'ın susuz çöllerinde gezinirken {monster1.name}'e denk gelir.")
print(f'{player1.name} VS {monster1.name}')

raunt = 1
while player1.health > 0 and monster1.health > 0:
    print(f'{raunt}. raunt')
    print(f'{player1.name} Health: {player1.health} - {monster1.name} Health: {monster1.health}')

    print(f"{player1.name} attacked to {monster1.name}." )
    monster1.health -=  player1.attack(monster1.defence)
    print(f"{monster1.name} has taken from {player1.attack(monster1.defence)} damage.")
    print(f'{player1.name} Health: {player1.health} - {monster1.name} Health: {monster1.health}')

    print(f"{monster1.name} attacked to {player1.name}.")
    player1.health -= monster1.attack(player1.defence)
    print(f"{player1.name} has taken from {monster1.attack(player1.defence)} damage.")
    print(f'{player1.name} Health: {player1.health} - {monster1.name} Health: {monster1.health}')
    raunt += 1



class Character:
    def __init__(self, name, health, attack_power, critical_rate, defence, nameOfClass):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.critical_rate = critical_rate
        self.defence = defence
        self.nameOfClass = nameOfClass


    # toString() == __str__
    def __str__(self):
        string = f'Class: {self.nameOfClass} \nName: {self.name} \nHealth: {self.health} \nAttack Power: {self.attack_power} \nCritical Rate: {self.critical_rate} \nDefence: {self.defence}'
        return string

    def attack(self, target):
        return f'Attack damage: {self.attack_power - target.defence}'

    def show_char_name(self):
        return Helper.centered_title(self.name)

    def class_metod2(self):
        Helper.class_method()


char2 = Character('Mahmut', 213, 321,21,3,'Char')
Character.class_metod2()
char2.attack()


class Warrior(Character):
    def __init__(self, name, health, attack_power, critical_rate, defence, rage):
        super().__init__(name, health, attack_power, critical_rate, defence, 'Warrior')
        self.rage = rage

    def __str__(self):
        return f'{super().__str__()} \nRage: {self.rage}'

class Wizard(Character):
    def __init__(self, name, health, attack_power, critical_rate, defence, mana):
        super().__init__(name, health, attack_power, critical_rate, defence, 'Wizard')
        self.mana = mana

    def __str__(self):
        return f'{super().__str__()} \nMana: {self.mana}'

class Gargamel(Wizard):
    def __init__(self, name, health, attack_power, critical_rate, defence, mana, nose):
        super().__init__(name, health, attack_power, critical_rate, defence, mana)
        self.nose = nose

    def __str__(self):
        return f'{super().__str__()} \nNose: {self.nose}'

class Gromp(Character):
    def __init__(self, name, health, attack_power,critical_rate, defence):
        super().__init__(name,health, attack_power, critical_rate, defence,'Monster')

    #def __str__(self):
        #return f'{super().__str__()} \nAli Veli: {self.name}'

warrior1 = Warrior('Mahmut', 1231, 2131, 21, 21, 12)

wizard1 = Wizard('Kezban', 231, 3131, 21, 21, 10)

gromp1 = Gromp('Gromp', 321, 213,33,512)
gromp1.name = 'Fehmi'

gargamel1 = Gargamel('Gargamel', 321, 2131, 21, 21, 10, 'Burun güzeli')
gargamel2 = Gargamel('Gargamel2', 321, 432, 21, 21, 10, 'Burun çirkini')

# __str__ == .toString()
# print(warrior1.__str__())
# print(wizard1.__str__())
# print(gromp1.__str__())
# print(gargamel1.__str__())

#POLYMORPHISM !Burası detaylandıralacak

#print(gargamel1.attack())
#print(gargamel2.attack())

#class Helper:
    #def __init__(self, message):
    #self.message = message

#helper1 = Helper('Mahmut künefe sever')
#print(helper1.message)

class Helper:

    def show_message(message):
        print()
        print(message)
        print()

    @staticmethod
    def centered_title(title):
        print('-'*10+title+'-'*10)

    @classmethod
    def class_method(cls):
        print('Bu bir sınıf yöntemidir')
        print('Sınıf:', cls)

#Helper.show_message('Hello World!')
#gromp1.show_char_name()
#Helper.class_method()
#gromp1.class_metod2()
#Helper.show_message('Mahmut Ekrem')
#Helper.centered_title('Black Myth Wukong')

#Encapsulation
class Person:
    def __init__(self, name, surname, address):
        self.__name = name #PRIVATE
        self.surname = surname #PUBLIC
        self._address = address #PROTECTED

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_fullname(self):
        return self.get_name() + self.surname

    def get_surname(self):
        return self.surname

    def get_address(self):
        return self._address

class Umut:
    person1 = Person('Mahmut', 'Ekrem', 'Azerbaycan')
    #print(person1.name)
    #print(person1.surname)
    ##print(person1.get_name())
    #print(person1.get_fullname())
    #print(person1.surname)
    #print(person1.get_surname())
    print(person1.get_name())
    person1.set_name('Fehmi')
    print(person1.get_name())

person2 = Person('Nazife', 'Yalvaç', 'Kenya')
#print(person2.__address)
#print(person2.get_address())

#Polymorphism

class Animal:
    def sound(self):
        print('Animal sound')

class Dog(Animal):
    def sound(self):
        print('Havv havv!')

class Cat(Animal):
    def sound(self):
        print('Miyav miyav!')

class Bird(Animal):
    def sound(self):
        print('Cik cik!')

class Wolf(Animal):
    def sound(self):
        print('Aauuuuuww!')

class Wolf(Animal):
    pass

def listen_sound(animal):
    animal.sound()

cat1 = Cat()
dog1 = Dog()
bird1 = Bird()
wolf1 = Wolf()

listen_sound(cat1)
listen_sound(dog1)
listen_sound(bird1)
listen_sound(wolf1)

# Encapsulation
# Access modified => private | protected | public
class BankAccount:
    def __init__(self, account_number, balance, name, surname):
        self.__account_number = account_number #private
        self.__balance = balance #private
        self._name = name #protected
        self._surname = surname #protected

    def show_balance(self):
        print(f'My Balance: {self.__balance} TL')

    def show_account_number(self):
        print(f'My Account Number: {self.__account_number}')

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Transferred to your bank account: {amount} TL')
            print(f'Your Current Balance: {self.__balance} TL')
        else:
            print('Invalid value.')

    def _get_name(self):
        return self._name

    def _get_surname(self):
        return self._surname

    def get_full_name(self):
        return f'{self._get_name()} {self._get_surname()}'

myBankAccount = BankAccount('1234121312312', 10000, 'Mete', 'Dural')
#print(myBankAccount.account_number)
#myBankAccount.account_number = 21351512
#print(myBankAccount.account_number)
#myBankAccount.show_balance()
#myBankAccount.__balance = 2131231
#myBankAccount.show_balance()
#myBankAccount.__balance = 5000
#myBankAccount.show_balance()
#myBankAccount.deposit(5000)
print(myBankAccount._name)
myBankAccount._name = 'Mehmet'
print(myBankAccount._get_name())
print(myBankAccount._get_surname())
print(myBankAccount.get_full_name())

#Logical Operators
# AND - OR - NOT

# AND
# True and False => False
# True and True  => True
# False and False => False
# False and True => False

username = 'ragip'
password = '1234'
if username == 'ragip' and password == '12345': #True and True => True  | True and False => False
    print('Giriş Başarılı.')
else:
    print('Giriş Başarısız.')

# OR
# False or True => True
# False or False => False
# True or True = True
# True or False = True

color = 'yellow'
if color == 'green' or color =='yellow': # True or False = True | False or False = False
    print('We love rainbow')
else:
    print('We love dark')

'''
# Abstraction # Soyutlama
# ABC = Abstract Base Class => Soyut Temel Sınıf

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, age, experience):
        self.name = name
        self.age = age
        self.experience = experience
        self.salary = 0

    @abstractmethod
    def calc_salary(self):
        pass #Alt sınıflar kendine göre fonksiyonu düzenleyecek

    def info_salary(self):
        return f'{self.name} adlı çalışnanın maaşı: {self.__salary}'

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print('Invalid salary')

    def get_salary(self):
        return self.__salary

class Manager(Employee):
    def calc_salary(self):
        salary = 80000
        self.set_salary(salary)

class Engineer(Employee):
    def calc_salary(self):
        salary = 60000
        self.set_salary(salary)

class Intern(Employee):
    def calc_salary(self):
        salary = 30000
        self.set_salary(salary)

manager1 = Manager('Deniz', 36, 10)
engineer1 = Engineer('Mete', 25, 5)
intern1 = Intern('Umut',18, 0)

MicrosoftSuperTeam = [manager1, engineer1, intern1]

def calc_salary_for_all_employees(employeeList):
    for employee in employeeList:
        employee.calc_salary()
        print(employee.info_salary())

calc_salary_for_all_employees(MicrosoftSuperTeam)
