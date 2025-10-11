from Person import Person
from Bus import Bus

def main():
    bus = Bus()
    p1 = Person("Alice", 30)
    p2 = Person("Bob", 25)
    p3 = Person("Charlie", 35)
    p4 = Person("Diana", 28)

    bus.pick_up_passenger(p1)
    bus.pick_up_passenger(p2)
    bus.pick_up_passenger(p3)
    bus.pick_up_passenger(p4)  # Attempt to pick up when bus is full

    bus.drop_off_passenger()
    bus.drop_off_passenger()
    bus.drop_off_passenger()
    bus.drop_off_passenger()  # Attempt to drop off when bus is empty

main()