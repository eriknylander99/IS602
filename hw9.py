__author__ = 'Erik Nylander'

import pandas as pd
import re
import Tkinter
import tkFileDialog


def get_file():
    root = Tkinter.Tk()
    root.withdraw()
    print 'Opening File'
    f = tkFileDialog.askopenfilename(defaultextension='.png')
    return f


def open_file(file):
    f_in = open(file, 'r')
    f_out = open('epa-http_clean.txt', mode='w')
    for line in f_in:
        line_out = re.sub(r'="', '=', line)
        f_out.write(line_out)
    f_out.close()


def data_import():
    headers = ['host', 'date', 'request', 'replycode', 'bytes']
    data_frame = pd.read_csv('epa-http_clean.txt', sep='\s+', names=headers, header=None)
    return data_frame


if __name__ == '__main__':
    f = get_file()
    open_file(f)
    df = data_import()
    df = df.replace('-', value=0)
    df[['bytes']] = df[['bytes']].astype(int)

    #Question 1: Which IP made the most requests
    requests = df.groupby('host')
    print 'Question 1:'
    print 'The host that made the maximum number of requests was: %s, with a total of %d requests.' \
          % (requests.size().argmax(), requests.size().max())
    print ''

    #Question 2: Which Host is receiving the most bytes from the server
    print 'Question 2:'
    print 'The host that received the most bytes from the server was: %s, with a total of %d bytes received.' \
        % (requests.bytes.sum().argmax(), requests.bytes.sum().max())
    print ''

    #Question 3: Which Hour is the busiest in terms of requests?
    max_requests = []
    for i in range(0, 24):
        if i < 10:
            test = df[df['date'].str.contains("...:0%d:....." % i)]
        else:
            test = df[df['date'].str.contains("...:%d:....." % i)]
        max_requests.append((len(test), i))
    m_request = max(max_requests)
    f_out = open('hourlyrequests.csv', mode='w')
    for point in max_requests:
        line_out = '%d, %d \n' % (point[1], point[0])
        f_out.write(line_out)
    f_out.close()
    print max_requests
    print 'Question 3:'
    print 'The maximum number of requests were: %d, and were received from %d:00 to %d:00.' \
          % (m_request[0], m_request[1], m_request[1]+1)
    print ''

    #Question 4: Which .gif image was downloaded most during the day.
    gif_df = df[df['request'].str.contains(".gif")].groupby('request')
    gifname = gif_df.size().argmax().split('/')[2].split(' ')
    print 'Question 4:'
    print 'The .gif file that was most requested was: %s, with a total number of %d requests.' \
          % (gifname[0], gif_df.size().max())
    print''

    #Question 5: Which HTML codes were returned other than 200?
    htmlcodes_df = df.groupby('replycode')
    print 'Question 5:'
    print 'The following HTML codes were returned along with the number of times each code was returned:'
    print htmlcodes_df.size().order()