class Superhero:
    def __init__(self, name, secret_identity, power, energy_level=100):
        self.name = name
        self.secret_identity = secret_identity
        self.power = power
        self._energy_level = energy_level

    def use_power(self):
        if self._energy_level >= 10:
            print(f"{self.name} uses {self.power}! It's super effective!")
            self._energy_level -= 10
            print(f"Energy level is now {self._energy_level}%.")
        else:
            print(f"{self.name} is too tired to use their power. Need to rest!")

    def rest(self):
        self._energy_level = 100
        print(f"{self.name} has rested and is back to full energy!")

    def get_energy(self):
        return self._energy_level

hero1 = Superhero("Kudakwashe", "Siziba")
hero2 = Superhero("Software", "Developer", 80)

print(f"{hero1.name}'s secret identity is {hero1.secret_identity}.")
hero1.use_power()

print(f"\n{hero2.name} starts with {hero2.get_energy()}% energy.")
hero2.use_power()
