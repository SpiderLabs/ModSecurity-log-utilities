
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

import re

class LogEntry:
    def __init__(self, string = None):
        self.client = None
        self.matchMessage = None
        self.variable = None
        self.file = None
        self.line = None
        self.id = None
        self.rev = None
        self.msg = None
        self.data = None
        self.severity = None
        self.ver = None
        self.maturiry = None
        self.accuracy = None
        self.tags = []
        self.hostname = None
        self.uri = None



        if string != None:
            a = re.findall(r"\[[^\]]+]", string)
            for i in a:
                b = re.findall(r"\[([^ ]+) \"(.*)\"\]$", i)
                if len(b) == 0:
                    continue
                b = b[0]
                if len(b) > 1:
                    if (b[0] == "tag"):
                        self.tags.append(b[1])
                    else:
                        self.__dict__[b[0]] = b[1]

    def __repr__(self):
        return str(self.id) + ": " + str(self.msg)

