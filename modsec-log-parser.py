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


from src.modsec_log_parser import ModSecLogParser
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--summary', type=str)
    parser.add_argument('files', nargs='*')
    args = parser.parse_args()
    print(args.files, args.summary)

    files = args.files
    summary = args.summary
    if len(files) == 0:
        files = "/dev/stdin"
    if len(summary) == 0:
        summary = "id,msg"

    msclp = ModSecLogParser(files)
    data = msclp.run()

    ar = {}
    if data == None:
        return

    for i in data:
        z = ""
	for xx in summary.split(","):
            if len(z) > 0:
                z = z + " "
            z = z + str(i.__dict__[xx])

	if i.id in ar:
	    ar[z] = ar[str(i.id)] + 1
	else:
	    ar[z] = 1


    for i in ar:
	print str(i)

if __name__=="__main__":
    main()


