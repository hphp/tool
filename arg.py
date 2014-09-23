#!/home/img/.jumbo/bin/python
#encoding: utf-8
import argparse

parser = argparse.ArgumentParser(description='test command')

if(__name__ == '__main__'):
    parser.add_argument('cmd', metavar='S', type=str, nargs='+', help='test command')
    args = parser.parse_args()
    if args.cmd[0] == "pushMessage":
        print args.cmd[0]
    else:
        print "in fact", args.cmd[0]
