#!/usr/bin/python3
# for a given employee ID, returns information about his/her TODO list progress

import requests
import sys

a = sys.argv[1]
if __name__ == '__main__':
    location = 'https://jsonplaceholder.typicode.com/'
    url = location + 'users/{}'.format(a)
    user = requests.get(url).json()
    query = {"userId": a}
    todo = location + 'req'
    req = requests.get(url=todo, params=query).json()
    do = [item.get('title') for item in req if item.get('completed')]
    print('Employee{} is done with tasks({}/{}):'.format(user.get('name'), len(do), len(req)))

    for task in do:
        print("\t {}".format(task))