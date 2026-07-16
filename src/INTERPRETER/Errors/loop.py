
class StopNodeError(Exception):
    def __init__(self, line=0):
        self.line = line

    def __str__(self):
        return f"""
EGG v2.0 CRACKED BOOM!!!
[RuntimeError]  ( ・_・)ノΞ●~*  


        File: Will come on EGG v3.0
        AT LINE: {self.line}
        ERROR: Keyword stop can only be used inside a loop


Double-check that line there must be something invalid
"""
class SkipNodeError(Exception):
    def __init__(self, line=0):
        self.line = line

    def __str__(self):
        return f"""
EGG v2.0 CRACKED BOOM!!!
[RuntimeError]  ( ・_・)ノΞ●~*


        File: Will come on EGG v3.0
        AT LINE: {self.line}
        ERROR: Keyword skip can only be used inside a loop


Double-check that line there must be something invalid
"""
