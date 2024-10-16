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

'''


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


warrior1 = Warrior('Mahmut', 1231, 2131, 21, 21, 12)

wizard1 = Wizard('Kezban', 231, 3131, 21, 21, 10)

# print(warrior1.__str__())
print(wizard1.__str__())
