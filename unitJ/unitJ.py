class ParkingLot:
    # initialize the values of an object
    def __init__(self, name,  totalSpaces, filledSpaces):
        self.name = name
        self.totalSpaces = totalSpaces
        self.filledSpaces = filledSpaces
    
    # print the info about the object
    def __str__(self):
        return "Lot: " + str(self.name) + "\nFilled spaces: " + str(self.filledSpaces) + "\nTotalSpaces: " + str(self.totalSpaces) + "\n"

    # if there are available spaces, add one to the filled total and open the gate
    def letCarIn(self):
        if (self.totalSpaces > self.filledSpaces):
            self.filledSpaces += 1
            return "Open gate"
        else:
            return "Lot full, gate stays closed"

    # return the status of the parking lot
    def lotStatus(self):
        if (self.totalSpaces > self.filledSpaces):
            return "Spaces available"
        else:
            return "No spaces available"

    # substract 1 from the total filled and open the gate
    def letCarOut(self):
        self.filledSpaces -= 1
        return "Open gate"

    # return the value of filledSpaces data
    def getFilledSpaces(self):
        return self.filledSpaces

# test parameters
lot1 = ParkingLot("Downtown", 80, 79)
lot2 = ParkingLot("Northside", 40, 20)
print(lot1)
print(lot1.lotStatus())
gateAction = lot1.letCarIn()
print(gateAction)
print(lot1.lotStatus())
gateAction = lot1.letCarIn()
print(gateAction)
gateAction = lot1.letCarOut()
print(gateAction)
print(lot1)
print(lot2)

# test output
'''
Lot: Downtown
Filled spaces: 79
TotalSpaces: 80

Spaces available
Open gate
No spaces available
Lot full, gate stays closed
Open gate
Lot: Downtown
Filled spaces: 79
TotalSpaces: 80

Lot: Northside
Filled spaces: 20
TotalSpaces: 40
'''
    
