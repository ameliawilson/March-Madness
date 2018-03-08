################################################
# March  Madness
# Day 1 - Making a Connection
#
# Create a connection to a webpage 
# Print out what the servers says back to you
################################################

import requests
import sys


def MakeConnection(URL):
    '''URL: string that is a website URL
    returns response object
    Make request to spcified URL using python requests module'''
    
    
    name = 'Amelia'
    email = 'ameliawilson17@gmail.com'
    user_agent = 'python-requests/2.18.4 (Compatible; {}; mailto:{})'.format(name, email)
    
    # Your header should include your info
    myHeader = {'User-Agent': user_agent}

    # Submit a get request to the URL, return Response Object
    r = requests.get(URL, headers=myHeader)

    # If the status code is not 200 something went wrong
    # print Rejected and exit the program
    if r.status_code != 200:
        print('Rejected')
        sys.exit()

    # return the response object
    return r




# Website you want to make a request to
URL = 'https://www.google.com'

# Get the response object for your URL/robots.txt
response = MakeConnection(URL + '/robots.txt')

# Print out the text of the response object
#print(response.status_code)
print(response.text)