class Plant:
    def __init__(
            self,
            name: str,
            height: int,
            age_in_days: int,
            growth_speed=0.4,
            max_days=20):
        self.name = name
        self.height = height
        self.age_in_days = age_in_days
        self.growth_speed = growth_speed
        self.max_days = max_days

    def show(self):
        str = f"{self.name}: {round(self.height, 1)}cm, \
{self.age_in_days} days old"
        print(str)

    def grow(self):
        self.height += self.growth_speed

    def age(self, days):
        for day in range(days):
            print(f"=== Day {day+1} ===")
            if self.age_in_days == self.max_days:
                print("💀💀💀 Your plant died! 💀💀💀")
                break
            self.grow()
            self.age_in_days += 1
            self.show()


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    plant = Plant("Rose", 0, 2, 0.2)
    plant.age(7)
    print(
        "Growth this week: ",
        round(plant.growth_speed*7, 1),
        "cm", sep="")
