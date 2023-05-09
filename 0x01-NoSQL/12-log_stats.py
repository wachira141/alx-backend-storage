#!/usr/bin/env python3
"""
Log stats
"""
from pymongo import MongoClient


def print_req_logs(nginx_collection):
    """
    print Nginx request logs
    """
    print('{} logs'.format(nginx_collection.count_documents({})))
    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        requests_num = list(nginx_collection.find({'method' : method}))
        print('\tmethod {}: {}'.format(method, len(requests_num)))
        '''access to status path'''
        status_get = list(nginx_collection.find({'method' : 'GET', 'path': '/status'}))
        print('{} status check'.format(len(status_get)))



def main():
    """
    main func to run the program to count logs
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_req_logs(client.logs.nginx)

if __name__ == '__main__':
    main()
