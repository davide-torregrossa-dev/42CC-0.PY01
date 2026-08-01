class Plant:
    def __init__(self, name:str, height:float, age_in_days:int, 
growth_speed=0.4, max_days=20, icon="🌱"):
        self.name = name
        self._height = height
        self._age_in_days = age_in_days
        self.growth_speed = growth_speed
        self.max_days = max_days
        self.icon = icon
        print("Created:", end="")
        self.show()

    def show(self):
        str = f"{self.icon} - {self.name}: {round(self._height, 1)}cm, \
{self._age_in_days} days old"
        print(str)

    def die(self):
        print("💀💀💀 Your plant died! 💀💀💀")

    def grow(self):
        self._height += self.growth_speed

    def age_is_valid(self, days:int):
            if days < 0:
                return 0
            if days >= self.max_days:
                return -1
            return True

    def set_age(self, days:int):
            match self.age_is_valid(days):
                case 0:
                    print(f"{self.icon} - {self.name}: Error, age can't be negative")
                    print("🚫 Age update rejected")
                    return
                case -1:
                    print(f"{self.icon} - {self.name}: Error, Your plant can't last so many days!")
                    print("🚫 Age update rejected")
                    return
            self._age_in_days = days
            print(f"Age updated: {self._age_in_days} days")

    def age(self, days:int):
        for day in range(days):
            print(f"=== Day {day+1} ===")
            if self._age_in_days == self.max_days+1:
                self.die()
                break
            self.grow()
            self.show()
            self._age_in_days += 1

    def height_is_valid(self, cm : float):
            if cm < 0:
                return False
            return True

    def set_height(self, cm : float):
            if not self.height_is_valid(cm):
                print(f"{self.icon} - {self.name}: Error, height can't be negative")
                print("🚫 Height rejected")
                return
            self._height = cm
            print(f"Height updated: {self._height}cm")

class Flower(Plant):
    def __init__(self, name:str, height:float, age_in_days:int, color:str, growth_speed=0.4, max_days=20, icon="🌱"):
        self.color = color
        self.blooming = False
        super().__init__(name, height, age_in_days, growth_speed, max_days, icon)

    def show(self):
        super().show()
        print("Color:", self.color)
    
    def bloom(self):
        insert = "was already"
        if not self.blooming:
            print(f"{self.name} has not bloomed yet")
            print(f"[asking the {self.name} to bloom]")
            insert = "is"
        self.show()
        print(f"The {self.name}", insert, "blooming beautifully!")
        self.blooming = True
        return

class Tree(Plant):
    def __init__(self, name:str, height:float, age_in_days:int, trunk_diameter:float, growth_speed=0.4, max_days=20, icon="🌱"):
        self.trunk_diameter = trunk_diameter
        super().__init__(name, height, age_in_days, growth_speed, max_days, icon)

    def show(self):
        super().show()
        print("trunk_diameter:", round(self.trunk_diameter, 1))
    
    def produce_shade(self):
        print(f"[asking the {self.name} to produce shade]")
        print(f"The {self.name} now produces a shade of {round(self._height, 1)}cm long and {round(self.trunk_diameter, 1)}cm wide.")
        return

class Vegetable(Plant):
    def __init__(self, name:str, height:float, age_in_days:int, harvest_season:str, growth_speed=0.4, max_days=20, icon="🌱"):
        self.harvest_season = harvest_season
        self.nutritional_value = 0
        super().__init__(name, height, age_in_days, growth_speed, max_days, icon)

    def show(self):
        super().show()
        print("Harvest season:", self.harvest_season)
        print("Nutritional value:", round(self.nutritional_value, 1))
    
    def grow(self):
        self.nutritional_value+=1
        super().grow()

if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 10, 5, "Red", icon="🌹")
    rose.bloom()
    print(""*5)
    print("=== Tree")
    pinetree = Tree("Pinetree", 200, 300, 5.45, icon="🌲")
    pinetree.produce_shade()
    print(""*5)
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 13, 5, "April", icon="🍅", max_days = 50)
    days_for_tomato = 20
    print(f"[making the {tomato} grow and age for {days_for_tomato} days]")
    tomato.age(days_for_tomato)
    tomato.show()