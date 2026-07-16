class UnknownCmdError(Exception):
    def __init__(self, msg, cmd):
        self.msg = msg
        self.cmd = cmd

    def __str__(self):
        return f"""
EGG v2.0 CRACKED BOOM!!!
[UnknownCmdError]  ( ・_・)ノΞ●~*  


        COMMAND : {self.cmd}
        ERROR : {self.msg}


Double-check that your command is okey, there must be something invalid
"""
class FileNotFoundError(Exception):
    def __init__(self, msg, cmd):
        self.msg = msg
        self.cmd = cmd

    def __str__(self):
        return f"""
EGG v2.0 CRACKED BOOM!!!
[FileNotFoundError]  ( ・_・)ノΞ●~*  


        PATH : {self.cmd}
        ERROR : {self.msg}


Check that your file exists
"""