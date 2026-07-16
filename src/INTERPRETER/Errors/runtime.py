class RuntimeError(Exception):
    def __init__(self, info, line=0):
        self.msg = info
        self.line = line

    def __str__(self):
        return f"""
EGG v2.0 CRACKED BOOM!!!
[RuntimeError]  ( ・_・)ノΞ●~*


        File: Will come on EGG v3.0
        AT LINE: {self.line}
        ERROR: {self.msg}


Double-check that line there must be something invalid
"""
class UnsupportedTypeError(Exception):
    def __init__(self, info, line=0):
        self.msg = info
        self.line = line

    def __str__(self):
        return f"""
EGG v2.0 CRACKED BOOM!!!
[UnsupportedTypeError]  ( ・_・)ノΞ●~*  BOOM!!!


        File: Will come on EGG v3.0
        AT LINE: {self.line}
        ERROR: {self.msg}


Double-check that line there must be something unsupported data type oparetion
"""


class NotFoundError(Exception):
    def __init__(self, cz, line=0):
        self.msg = cz
        self.line = line

    def __str__(self):
        return f"""
EGG v2.0 CRACKED BOOM!!!
[NotFoundError]  ( ・_・)ノΞ●~*  


        File: Will come on EGG v3.0
        AT LINE: {self.line}
        ERROR: {self.msg}


Most likely happens when you use a variable or function that isn’t defined. Please double-check that everything is okay.
"""


class AlreadyExistsError(Exception):
    def __init__(self, var, line=0):
        self.msg = var
        self.line = line

    def __str__(self):
        return f"""
EGG v2.0 CRACKED BOOM!!!
[AlreadyExistsError]  ( ・_・)ノΞ●~*  BOOM!!!


        File: Will come on EGG v3.0
        AT LINE: {self.line}
        ERROR: {self.msg}


The variable or function already exists. Please check your code and remove duplicates.
"""


class TypeNotAllowed(Exception):
    def __init__(self, msg, line=0):
        self.msg = msg
        self.line = line

    def __str__(self):
        return f"""
EGG v2.0 CRACKED BOOM!!!
[TypeNotAllowed]  ( ・_・)ノΞ●~*  


        File: Will come on EGG v3.0 
        AT LINE: {self.line}
        ERROR: {self.msg}


The type you used is not allowed here. Please check your values and try again.
"""


class ArgsNotAllowed(Exception):
    def __init__(self, msg, line=0):
        self.msg = msg
        self.line = line

    def __str__(self):
        return f"""
EGG v2.0 CRACKED BOOM!!!
[ArgsNotAllowed]  ( ・_・)ノΞ●~*  


        File: Will come on EGG v3.0
        AT LINE: {self.line}
        ERROR: {self.msg}


EGG CRACKED!!!
The arguments provided are not allowed. Please check the function usage.
"""