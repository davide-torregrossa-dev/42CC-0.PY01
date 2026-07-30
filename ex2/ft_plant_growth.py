class Plant:
    def __init__(self, name, height, age_in_days, 
growth_speed, max_days):
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
            self.grow()
            self.show()
            self.age_in_days += 1
            if self.age_in_days == self.max_days+1:
                print("💀💀💀 Your plant died! 💀💀💀")
                break
        
        if days == 7:
            print("Growth this week: ", round(self.growth_speed*7, 1), "cm", sep="")

if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    plant = Plant("Rose", 25, 2, 0.2, 12)
    plant.age(20)
