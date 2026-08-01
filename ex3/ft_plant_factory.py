class Plant:
    def __init__(self, name:str, height:float, age_in_days:int, 
growth_speed=0.4, max_days=20, icon="🌱"):
        self.name = name
        self.height = height
        self.age_in_days = age_in_days
        self.growth_speed = growth_speed
        self.max_days = max_days
        self.icon = icon
        print("Created:", end="")
        self.show()

    def show(self):
        str = f"{self.icon} - {self.name}: {round(self.height, 1)}cm, \
{self.age_in_days} days old"
        print(str)

    def grow(self):
        self.height += self.growth_speed

    def age(self, days):
        for day in range(days):
            print(f"=== Day {day+1} ===")
            if self.age_in_days == self.max_days+1:
                print("💀💀💀 Your plant died! 💀💀💀")
                break
            self.grow()
            self.show()
            self.age_in_days += 1
        if days == 7:
            print("Growth this week: ", round(self.growth_speed*7, 1), "cm", sep="")

if __name__ == "__main__":
    print("===== Welcome to my garden! =====")
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Cactus", 25, 2, 0.2, 150, "🌵"),
        Plant("Poison Ivy", 250, 40, 0.1, 300, "🌿"),
        Plant("Pothos", 300, 3, 0.5, 800, "🌿"),
        Plant("Rose", 25, 2, 0.1, 12, "🌹"),
        Plant("Margherita Hack", 146, 38035, 0, 33285, "👵"),
    ]
    print("="*12)
    print(f"|{plants[0].icon}| | | |  |")
    print(f"| | | | |{plants[1].icon} |")
    print(f"| |{plants[2].icon}| |{plants[3].icon}| |")
    print(f"|{plants[4].icon}| | |  | |")
    print("="*12)

    for plant in plants:
        plant.show()