__author__ = 'Erik Nylander'

import Tkinter
import tkFileDialog
import re
from operator import attrgetter


class CarEvaluation:
    """Class that represents the data in the car.data.csv file"""

    def __init__(self, price, maint, doors, seats, cargo, safety, value):
        dprice = {'low': 0, 'med': 1, 'high': 2, 'vhigh': 3}
        dmaint = {'low': 0, 'med': 1, 'high': 2, 'vhigh': 3}
        ddoors = {'2': 0, '3': 1, '4': 2, '5more': 3}
        dseats = {'2': 0, '4': 1, 'more': 2}
        dcargo = {'small': 0, 'med': 1, 'big': 2}
        dsafety = {'low': 0, 'med': 1, 'high': 3}
        dvalue = {'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3}
        self.price = price
        self.maint = maint
        self.doors = doors
        self.seats = seats
        self.cargo = cargo
        self.safety = safety
        self.value = value
        try:
            self.price_order = dprice[price]
            self.maint_order = dmaint[maint]
            self.doors_order = ddoors[doors]
            self.seats_order = dseats[seats]
            self.cargo_order = dcargo[cargo]
            self.safety_order = dsafety[safety]
            self.value_order = dvalue[value]
        except:
            print 'The line %s, %s, %s, %s, %s, %s, %s contains errors ' \
                  'setting ordering values to none.' % (price, maint, doors, seats, cargo, safety, value)
            self.price_order = None
            self.maint_order = None
            self.doors_order = None
            self.seats_order = None
            self.cargo_order = None
            self.safety_order = None
            self.value_order = None
            pass


def file_open():
    '''
    Opens a file using the TKinter interface.
    :return: a list of CarEvaluation objects
    '''
    root = Tkinter.Tk()
    root.withdraw()
    f = tkFileDialog.askopenfile(mode='r')
    try:
        cars_lst = []
        for line in f:
            line = line.strip()
            line = line.split(",")
            car = CarEvaluation(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
            cars_lst.append(car)
    except TypeError:
        print 'No file was selected, exiting.'
        quit()
    return cars_lst


def file_save(text):
    '''
    Saves a file using the TKinter interface.
    :param text: Text to be written to the file
    :return: none
    '''
    root = Tkinter.Tk()
    root.withdraw()
    f = tkFileDialog.asksaveasfilename()
    try:
        fout = open(f, mode='w')
        for car in text:
            car_out = '%s, %s, %s, %s, %s, %s, %s\n' \
                      % (car.price, car.maint, car.doors, car.seats, car.cargo, car.safety, car.value)
            fout.write(car_out)
        fout.close()
    except IOError:
        print 'No file was selected, exiting.'
        quit()

def print_cars(cars, lines = None):
    '''
    prints out the features for the cars imported from the .csv file
    :param cars: list of cars imported by the file_open() or the cars_sort()
    :param lines: number of lines to be returned +lines prints the number of lines from the beginning
            -line prints the number of lines from the end
    :return: None
    '''
    if lines == None:
        sub_cars = cars
    if lines > 0:
        sub_cars = cars[0:lines]
    if lines < 0:
        sub_cars = cars[lines:len(cars)]
    for car in sub_cars:
        print 'Price: %s, Maintenance Cost: %s, Doors: %s, Seats: %s, Cargo Space: %s, ' \
              'Safety Rating: %s, Value: %s.' \
              % (car.price, car.maint, car.doors, car.seats, car.cargo, car.safety, car.value)


def sort_cars(cars, value, order='des'):
    '''
    Sorts the cars in ascending or descending order based on a given value. If a value is none it is returned first in
    an ascending sort.
    :param cars: list of cars to be sorted
    :param value: string value 'price', 'maint', 'doors', 'seats', 'cargo', 'safety', 'value'
    :param order: 'asc' for ascending, 'des' for descending
    :return: sorted list of values
    '''
    if order == 'asc':
        return sorted(cars, key=attrgetter(value+'_order'))
    return sorted(cars, key=attrgetter(value+'_order'), reverse=True)


if __name__ == "__main__":
    car_lst = file_open()

    # Prints the top 10 rows of the data sorted by safety in descending order
    sort_by_safety = sort_cars(car_lst, 'safety', 'des')
    print 'Top 10 rows of Cars, sorted by safety in descending order:'
    print_cars(sort_by_safety, 10)
    print ''

    # Prints the bottom 15 rows of the data sorted by 'maint' in ascending order
    sort_by_maint = sort_cars(car_lst, 'maint', 'asc')
    print 'Bottom 15 rows of Cars, sorted by maintenance cost in ascending order:'
    print_cars(sort_by_maint, -15)
    print ''

    # Searches for cars that have a price, maintenance cost, or safety rating of high or vhigh.
    # Prints the result of the search sorted by doors in ascending order.
    cars_search = []
    for car in car_lst:
        pattern = 'high'
        if re.search(pattern, car.price) and re.search(pattern, car.maint) and re.search(pattern, car.safety):
            cars_search.append(car)
    cars_search = sort_cars(cars_search, 'doors', 'asc')
    print 'Cars sorted in ascending order by number of doors, where price, maintenance, and saftey are high or vhigh:'
    print_cars(cars_search)
    print ''

    # Searches for cars that have a price of vhigh, a maintenance cost of med, 4 doors, and seats 4 or more.
    # Outputs the result of this search to a file through the TKinter interface.
    cars_search2 = []
    for car in car_lst:
        if car.price == 'vhigh' and car.maint == 'med' and car.doors == '4' and \
                (car.seats == '4' or car.seats == 'more'):
            cars_search2.append(car)

    file_save(cars_search2)

