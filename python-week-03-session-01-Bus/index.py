from abc import ABC

# Abstract base class (ভবিষ্যতে বাড়ানোর জন্য)
class AbstractClass(ABC):
    def __init__(self, coach, driver, arrival, departure, from_des, to_des):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to_des = to_des
        self.seats = [["Empty" for col in range(4)] for row in range(10)]  # 10 row, 4 column = 40 seats
    # @abstractmethod
    # def install_bus(self, coach, driver, arrival, departure, from_des, to_des):
    #     pass

    # @abstractmethod
    # def display_available_bus(self):
    #     pass

    # @abstractmethod
    # def display_seat_status(self):
    #     pass

class Bus(AbstractClass):
    pass

class BusCompany:
    def __init__(self):
        self.buses = {}  
        # object-এর ভিতরে একটা dictionary তৈরি হচ্ছে, যেটা সব বাসকে store করে রাখবে।

    def install_bus(self, bus):
        print(f"\nBus '{bus.coach}' added successfully.")
        self.buses[bus.coach] = bus  
        # এখানে bus একটা object (ধরে নেওয়া যায় Bus ক্লাসের object)
        # প্রতিটি bus object-এর মধ্যে coach নামে একটা property আছে
        # bus.coach কে key হিসেবে, এবং bus object কে value হিসেবে dictionary buses-এর মধ্যে যোগ করা হচ্ছে।
        # {'coach': bus}

    def display_available_buses(self):
     if not self.buses:
        print("No buses available.")
     else:
        print(f"\n{'Coach':<10}{'Driver':<15}{'Arrival':<10}{'Departure':<12}{'From':<15}{'To':<15}") #space দিয়ে যোগ করা হচ্ছে
        for coach, bus in self.buses.items():
            print(f"{coach:<10}{bus.driver:<15}{bus.arrival:<10}{bus.departure:<12}{bus.from_des:<15}{bus.to_des:<15}")


    def book_ticket(self, coach, row, col):
        if coach in self.buses:
            if 0 <= row < 10 and 0 <= col < 4:
                if self.buses[coach].seats[row][col] == "Empty":
                    self.buses[coach].seats[row][col] = "Booked"
                    print(f"\nSeat at Row {row+1}, Column {col+1} has been booked for bus {coach}.")
                else:
                    print(f"\nSeat at Row {row+1}, Column {col+1} is already booked.")
            else:
                print("Invalid seat position.")
        else:
            print("Bus not found.")

    def display_seat_status(self, coach):
        if coach in self.buses:
            print(f"\nSeat status for bus '{coach}':")
            seats = self.buses[coach].seats
            for row_index, row in enumerate(seats):
                row_status = " | ".join(f"{seat:^6}" for seat in row) #প্রতিটি seat কে 6-character জায়গার মাঝে center-align করে সাজাচ্ছে (:^6) তারপর প্রতিটি seat-এর মাঝে " | " বসিয়ে দিচ্ছে
                print(f"Row {row_index + 1:>2}: {row_status}") #row_index + 1 → 1-based index দেখানোর জন্য (user-friendly) :>2 → Row number যেন right-aligned হয়ে 2-character জায়গা নেয়
        else:
            print("Bus not found.")

# Program starts here
company = BusCompany()

while True:
    print("\n====== Welcome to Bus Reservation System ======")
    print("1. Install Bus")
    print("2. Display Available Buses")
    print("3. Book Ticket")
    print("4. Display Seat Status")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        coach = input("Enter coach number: ")
        driver = input("Enter driver name: ")
        arrival = input("Enter arrival time: ")
        departure = input("Enter departure time: ")
        from_des = input("Enter from destination: ")
        to_des = input("Enter to destination: ")
        bus = Bus(coach, driver, arrival, departure, from_des, to_des)
        company.install_bus(bus)

    elif choice == 2:
        company.display_available_buses()

    elif choice == 3:
        coach = input("Enter coach number: ")
        try:
            row = int(input("Enter row number (1-10): ")) - 1
            col = int(input("Enter column number (1-4): ")) - 1
            company.book_ticket(coach, row, col)
        except ValueError:
            print("Invalid row or column number.")

    elif choice == 4:
        coach = input("Enter coach number: ")
        company.display_seat_status(coach)

    elif choice == 5:
        print("\nThank you for using the Bus Reservation System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
