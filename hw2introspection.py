__author__ = 'Erik Nylander'

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
    def output(data, func):
        output_function = getattr(CarEvaluation, func, CarEvaluation.showEvaluation)
        if not callable(output_function):
            return output_function
        return output_function(data)

    eval1 = CarEvaluation("Ford", "High", 2)
    eval2 = CarEvaluation("GMC", "Med", 4)
    eval3 = CarEvaluation("Toyota", "Low", 3)

    L = [eval1, eval2, eval3]

    print "Car Count = %d" % (output(CarEvaluation, "carCount"))

    # Outputs the vehicle evaluations for all vehicles in the list
    for car in L:
        output(car, "showEvaluation")

    print sortbyprice(L, "asc"); #[Toyota, GMC, Ford]
    print sortbyprice(L, "des"); #[Ford, GMC, Toyota]
    print searchforsafety(L, 2); #true
    print searchforsafety(L, 1); #false