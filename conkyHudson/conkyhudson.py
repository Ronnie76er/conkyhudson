#!/usr/bin/python

import sys


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hs:j:t:", ["help", "server", "jobs","template"])
    except:
        usage(argv)
        sys.exit(2)
        
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
            
        elif opt in ("-s", "--server"):
            server = arg
            
        elif opt in ("-j", "--jobs"):
            jobs = arg
    
if __name__ == "__main__":
    main(sys.argv[1:])
