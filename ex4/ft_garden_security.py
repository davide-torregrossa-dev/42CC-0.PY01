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

    def get_age(self):
        return self._age_in_days

    def age(self, days:int):
        for day in range(days):
            print(f"=== Day {day+1} ===")
            if self._age_in_days == self.max_days+1:
                self.die()
                break
            self.grow()
            self.show()
            self._age_in_days += 1
        if days == 7:
            print("Growth this week: ", round(self.growth_speed*7, 1), "cm", sep="")

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

    def get_height(self):
        return self._height