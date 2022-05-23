import os
import argparse
from util import utils
import time

def arguments():
    parser = argparse.ArgumentParser(description = utils.banner())
    parser.add_argument('-l', '--limit', action = 'store', dest = 'limit',default='5',required = False, help = 'Limit CVEs per pages in nvd NIST search(default is 3)')
    parser.add_argument('-s', '--search', action = 'store', dest = 'search',default='0',required = True, help = 'library to extract CVEs from NIST')
    args = parser.parse_args()
    return args.limit,args.search

def start_lib_sec_diff():
    limit,search = arguments()
    utils.banner_start()
    utils.search_nist(search,limit)

def main():
    try:
        start_lib_sec_diff()
    except Exception as e:
        print(" log error : "+str(e))
        exit(0)

if __name__=="__main__":
    main()
