"""
    SRTpy -- SRT (https://etk.srail.co.kr) wrapper for Python.
    ==========================================================

    : copyright: (c) 2017 by Heena Kwag.
    : URL: <http://github.com/dotaitch/SRTpy>
    : license: BSD, see LICENSE for more details.
"""

class SrtError(Exception):
    def __init__(self, message, description=None):
        self.message = message
        self.description = description

    def __str__(self):
        description = ' - ' + self.description if self.description else ""
        return "{}{}".format(self.message, description)

class NeedToLoginError(SrtError):
    def __init__(self, message):
        SrtError.__init__(self, message)

class NoResultError(SrtError):
    def __init__(self, message):
        SrtError.__init__(self, message)
