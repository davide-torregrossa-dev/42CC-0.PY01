class Plant:
    class Stats:
        def __init__(self, owner):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0
            self.owner = owner
        
        def stat_caller_adv(self, stat_name:str):
            match stat_name:
                case "grow":
                    self._grow_calls+=1
                case "age":
                    self._age_calls+=1
                case "show":
                    self._show_calls+=1
        
        def display(self):
            print(f"[statistics for {self.owner.name}]")
            print(f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name:str, height:float, age_in_days:int, 
growth_speed=0.4, max_days=20, icon="🌱"):
        self.name = name
        self._height = height
        self._age_in_days = age_in_days
        self.growth_speed = growth_speed
        self.max_days = max_days
        self.icon = icon
        self.stats = self.Stats(self)
        self.alive = True
        print("Created:", end="")
        self.show()

    def show(self):
        self.stats.stat_caller_adv("show")
        str = f"{self.icon} - {self.name}: {round(self._height, 1)}cm, \
{self._age_in_days} days old"
        print(str)

    def die(self):
        print("💀💀💀 Your plant died! 💀💀💀")
        self.alive = False

    def grow(self):
        self._height += self.growth_speed
        self.stats.stat_caller_adv("grow")

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
        self.stats.stat_caller_adv("age")
        if not self.alive:
                print("🚫 This plant is dead, cannot age anymore.")
                return
        for day in range(days):
            print(f"=== Day {day+1} ===")
            if self._age_in_days == self.max_days:
                self.die()
                break
            self.grow()
            self._age_in_days += 1
            self.show()

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
    
    @staticmethod
    def is_older_than_year(age_in_days: int):
        return age_in_days > 365

    @classmethod
    def create_anon(cls):
        return cls("Unknown plant", 0, 0)



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
    class Stats(Plant.Stats):
        def __init__(self, owner):
            super().__init__(owner)
            self._shade_calls = 0

        def stat_caller_adv(self, stat_name:str):
            match stat_name:
                case "grow":
                    self._grow_calls+=1
                case "age":
                    self._age_calls+=1
                case "show":
                    self._show_calls+=1
                case "shade":
                    self._shade_calls+=1

        def display(self):
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(self, name:str, height:float, age_in_days:int, trunk_diameter:float, growth_speed=0.4, max_days=20, icon="🌱"):
        self.trunk_diameter = trunk_diameter
        super().__init__(name, height, age_in_days, growth_speed, max_days, icon)

    def show(self):
        super().show()
        print("trunk_diameter:", round(self.trunk_diameter, 1))
    
    def produce_shade(self):
        print(f"[asking the {self.name} to produce shade]")
        print(f"The {self.name} now produces a shade of {round(self._height, 1)}cm long and {round(self.trunk_diameter, 1)}cm wide.")
        self.stats.stat_caller_adv("shade")
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

class Seed(Flower):
    def __init__(self, name: str, height: float, age_in_days: int, color: str, seeds_per_bloom=5,
                 growth_speed=0.4, max_days=20, icon="🌱"):
        self.seed_count = 0
        self.seeds_per_bloom = seeds_per_bloom
        super().__init__(name, height, age_in_days, color, growth_speed, max_days, icon)
 
    def show(self):
        super().show()
        print(f"Seeds: {self.seed_count}")
 
    def bloom(self):
        if not self.blooming:
            self.seed_count = self.seeds_per_bloom
        super().bloom()

def display_plant_stats(plant: Plant):
    plant.stats.display()

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print("")
    print("=== Flower")
    rose = Flower("Rose", 10, 5, "Red", icon="🌹")
    display_plant_stats(rose)
    print(f"Asking the {rose.name} to grow")
    rose.grow()
    rose.bloom()
    print("")
    print("=== Tree")
    pinetree = Tree("Pinetree", 200, 365, 5, icon="🌳")
    display_plant_stats(pinetree)
    pinetree.produce_shade()
    display_plant_stats(pinetree)
    print("")
    print("=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow", icon="🌻", max_days=100)
    print(f"[make {sunflower.name} grow, age and bloom]")
    sunflower.grow()
    sunflower.set_age(65)
    sunflower.bloom()
    display_plant_stats(sunflower)
    print("")
    print("=== Anonymous")
    unknown = Plant.create_anon()
    display_plant_stats(unknown)


    """
if __name__ == "__main__":

 
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red", icon="🌹")
    display_plant_stats(rose)

    display_plant_stats(rose)
 

 

 


    """