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


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    print("=== Garden Plant Registry ==")
    for plant in plants:
        plant.show()
