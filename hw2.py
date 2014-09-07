
class CarEvaluation:
    """A simple class that represents a car evaluation"""
    carCount = 0
    def __init__(self, brand, price, safety):
        self.__class__.carCount += 1
        self.brand = brand
        self.price = price
        self.safety = safety

    def showEvaluation(self):
        print "The %s has a %s price and it's safety is rated a %s" % (self.brand, self.price, self.safety)


def sortbyprice(cars, order="des"):
    """
    :param cars: list of CarEvaluation objects
    :param order: The sort order,by price, as a string to be returned "asc" = ascending and "des" = descending
    :return: a list of car makes in sorted order
    """
    high = []
    med = []
    low = []
    for car in cars:
        if car.price == "High":
            high.append(car.brand)
        elif car.price == "Med":
            med.append(car.brand)
        else:
            low.append(car.brand)
    if order == "des":
        return high + med + low
    else:
        return low + med + high


def searchforsafety(cars, safety_val):
    """
    :param cars: list of Car Evaluation objects
    :param safety_val: Safety Value that is being searched for
    :return: True or False based on the result of the search
    """
    for car in cars:
        if car.safety == safety_val:
            return True
    return False
    #return #return a value

# This is the main of the program.  Expected outputs are in comments after the function calls.
if __name__ == "__main__":
    eval1 = CarEvaluation("Ford", "High", 2)
    eval2 = CarEvaluation("GMC", "Med", 4)
    eval3 = CarEvaluation("Toyota", "Low", 3)

    print "Car Count = %d" % CarEvaluation.carCount # Car Count = 3

    eval1.showEvaluation() #The Ford has a High price and it's safety is rated a 2
    eval2.showEvaluation() #The GMC has a Med price and it's safety is rated a 4
    eval3.showEvaluation() #The Toyota has a Low price and it's safety is rated a 3

    L = [eval1, eval2, eval3]

    print sortbyprice(L, "asc"); #[Toyota, GMC, Ford]
    print sortbyprice(L, "des"); #[Ford, GMC, Toyota]
    print searchforsafety(L, 2); #true
    print searchforsafety(L, 1); #false