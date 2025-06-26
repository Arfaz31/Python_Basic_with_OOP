from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def __init__(self, coach, driver, arrival, departure, from_des, to_des):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to_des = to_des
        self.seats = ["Empty" for _ in range(20)] # 20 empty seats
    
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
    # def install_bus(self, coach, driver, arrival, departure, from_des, to_des):
        # print(f"Bus {coach} has been installed.")
        pass

class BusCompany:
     def __init__(self):
        self.buses = {} #object-এর ভিতরে একটা dictionary তৈরি হচ্ছে, যেটা সব বাসকে store করে রাখবে।

     def install_bus(self, bus):
        print(f"Bus {bus.coach} added successfully.")
        self.buses[bus.coach] = bus  #এখানে bus একটা object (ধরে নেওয়া যায় Bus ক্লাসের object) প্রতিটি bus object-এর মধ্যে coach নামে একটা property আছে bus.coach কে key হিসেবে, এবং bus object কে value হিসেবে dictionary buses-এর মধ্যে যোগ করা হচ্ছে।{'coach': {bus}}

     def display_available_buses(self):
          if not self.buses:
               print("No buses available.")
          else:
               print(f"Coach\tDriver\tArrival\tDeparture\tFrom\tTo")
               for coach, bus in self.buses.items():
                    print(f"{coach}\t{bus.driver}\t{bus.arrival}\t{bus.departure}\t{bus.from_des}\t{bus.to_des}")
     def book_ticket(self, coach, seat):
          if coach in self.buses:
               if 1<=seat<=20:
                    if self.buses[coach].seats[seat-1] == "Empty":
                         self.buses[coach].seats[seat-1] = "Booked"
                         print(f"Seat {seat} has been booked for bus {coach}.")
                    else:
                         print(f"Seat {seat} is already booked.")
               else:
                    print("Invalid seat number.")
          else:
               print("Bus not found.")   

     def display_seat_status(self, coach):
          if coach in self.buses:
               print(f"Seat status for bus {coach}:")
               print(self.buses[coach].seats)
          else:
               print("Bus not found.")



company = BusCompany()



while True:
     print("Welcome to Bus Reservation System")
     print("1. Install Bus")
     print("2. Display Available Buses")
     print("3. Book Ticket")
     print("4. Display Seat Status")
     print("5. Exit")

     choice = int(input("Enter your choice: "))

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
          seat = int(input("Enter seat number: "))
          company.book_ticket(coach, seat)
     elif choice == 4:
          coach = input("Enter coach number: ")
          company.display_seat_status(coach)
     elif choice == 5:
          print("Thank you for using the Bus Reservation System. Goodbye!")
          break
     else:
          print("Invalid choice. Please try again.")
    

