class Bus:
    max_passengers = 3
    passengers = []

    def pick_up_passenger(self,person):
        try:
            if len(self.passengers) < self.max_passengers:
                self.passengers.append(person)
                print(f"Passenger {person.name} picked up. Current passagers in the bus {len(self.passengers)}")
            else:
                print("The bus is full, cannot pick up this passenger")
        except Exception as e:
            print(f"An error picking up passenger: {e}")

    def drop_off_passenger(self):
        try:
            if len(self.passengers) > 0:
                self.passengers.pop(0)
                print(f"Person dropped. Current passagers in the bus {len(self.passengers)}")
            else:
                print("The bus is empty, no passenger to drop of")
        except Exception as e:
            print(f"An error dropping off passenger: {e}")