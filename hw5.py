__author__ = 'Erik Nylander'


def file_open(file):
    '''
    Opens a file and reads the lines generating a list of tuples representing the points.
    :param file: The location of the brain - body file.
    :return: The list of tuples representing the points.
    '''
    f = open(file, 'r')
    bodybrain_lst = []
    for line in f:
        line = line.strip()
        line = line.split(',')
        if len(line[0]) > 2:
            point = (float(line[1]), float(line[2]))
            bodybrain_lst.append(point)
    return bodybrain_lst


def lsr(points):
    '''
    Calculates the ordinary least squares regression model for a data set.
    :param points: A list of tuples represent the points to be modeled.
    :return: The slope and y-intercept for the olsr model as a tuple.
    '''
    x_sum = 0
    y_sum = 0
    xy_sum = 0
    xsquare_sum = 0
    n = len(points)
    for point in points:
        x_sum += point[0]
        y_sum += point[1]
        xy_sum += point[0]*point[1]
        xsquare_sum += point[0]**2
    slope_num = n * xy_sum - x_sum * y_sum
    slope_den = n * xsquare_sum - x_sum ** 2
    slope = slope_num/slope_den
    y_int = (y_sum - slope * x_sum)/n
    return slope, y_int


if __name__ == '__main__':
    file_name = "D:/Erik/Documents/data/IS602/brainandbody.csv"
    brains = file_open(file_name)
    regression = lsr(brains)
    print 'Regression Equation:'
    print 'body = %f * brain + %f' % (regression[0], regression[1])
    print 'Slope: %f, Y-intercept: %f' % (regression[0], regression[1])