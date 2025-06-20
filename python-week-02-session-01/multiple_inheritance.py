class Watch:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_time(self):
        print("Displaying time...")

class FitnessTracker:
    def __init__(self, price) -> None:
        self.price = price
    
    def track_activity(self):
        print("Tracking activity...")

    def track_calories(self):
        print("Tracking calories...")

class SmartWatch(Watch, FitnessTracker):
    def __init__(self, brand, model, price):
        Watch.__init__(self, brand, model)
        FitnessTracker.__init__(self, price)

    def display(self):
        print("Displaying...")


apple = SmartWatch("Apple", "Watch", 1000)
apple.display_time()
apple.track_activity()
apple.track_calories()
apple.display()

        
