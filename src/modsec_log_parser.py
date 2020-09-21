
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

import fileinput
from log_entry import LogEntry

class ModSecLogParser:
    def __init__(self, watch = None):
        self.watch = watch
        self.logs = []

    def run(self):
	for line in fileinput.input(self.watch):
            if line.strip().startswith("ModSecurity"):
                l = LogEntry(string = line)
                self.logs.append(l)
        return self.logs

        self.sumarize()
