class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passenger=[]

    def add_pass(self,name) :
        if not self.open_seats() :
            return False        
        else: 
            self.passenger.append(name)
            return True
    
    def open_seats(self):
        return self.capacity-len(self.passenger)

flight=Flight(3)
people=["Faisal","Muti","Zahir","Papa","Uffaq"]

for p in people:
    results=flight.add_pass(people[p])
    if results :
        print("Sucess")
    else :
        print("No Seats")