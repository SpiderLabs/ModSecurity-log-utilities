#!/usr/bin/python

"""

ModSecurity log parser, http://www.modsecurity.org/
Copyright (c) 2004-2016 Trustwave Holdings, Inc. (http://www.trustwave.com/)

You may not use this file except in compliance with
the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

If any of the files related to licensing are missing or if you have any
other questions related to licensing please contact Trustwave Holdings, Inc.
directly using the email address security@modsecurity.org.


"""

import argparse
import sys


def load_line(line):
    l = line.split(" ", 1)
    l[1] = l[1].strip()
    return l


def load(fname):
    content = {}
    f = open(fname, 'r')
    for line in f:
        (key, value) = load_line(line)
        if not key in content:
            content[key] = []
        content[key].append(value)
    f.close()
    return content


def print_help():
    print " "
    print "Use: modsec-log-compare.py [options] <file a> <file b> "
    print " "


def plog(a):
    for i in a:
        print " - " + str(i)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--missing', type=str)
    parser.add_argument('files', nargs='*')
    args = parser.parse_args()

    if len(args.files) < 2:
        print_help()
        return

    fileA = sys.argv[1]
    fileB = sys.argv[2]

    contentFileA = load(fileA)
    contentFileB = load(fileB)

    print "file A: " + fileA + ". Elements: " + str(len(contentFileA)) + "."
    print "file B: " + fileB + ". Elements: " + str(len(contentFileB)) + "."


    for i in contentFileA:
        if i in contentFileB:
            diff = False
            objA = contentFileA[i]
            objB = contentFileB[i]
            if len(objA) == len(objB):
                z = len(objA)
                while z < 0:
                    if objA[z] != objB[z]:
                        diff = True
                    z = z - 1
            else:
                diff = True

            if diff:
                print "*** diff at: " + str(i)
                print "In: " + str(fileA)
                plog(objA)
                print " "
                print "In: " + str(fileB)
                plog(objB)
                print " "
        else:
            #print "B does not have: " + str(i)
            pass


if __name__=="__main__":
    main()

