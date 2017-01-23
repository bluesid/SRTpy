"""
    SRTpy -- SRT (https://etk.srail.co.kr) wrapper for Python.
    ==========================================================

    : copyright: (c) 2017 by Heena Kwag.
    : URL: <http://github.com/dotaitch/SRTpy>
    : license: BSD, see LICENSE for more details.
"""

from .srt import Srt, Passenger, Adult, Child, Senior, Disability1_3, Disability4_6
from .train import Train
from .reservation import Ticket, Reservation
from .error import SrtError, NeedToLoginError, NoResultError

__copyright__ = 'Copyright 2017 by Heena Kwag'
__version__ = '0.0.3'
__license__ = 'BSD License'
__author__ = 'Heena Kwag'
__author_email__ = 'dotaitch@gmail.com'
__url__ = 'http://github.com/dotaitch/SRTpy'

__all__ = [
    'Srt',
    'Passenger', 'Adult', 'Child', 'Senior', 'Disability1_3', 'Disability4_6',
    'Train', 'Ticket', 'Reservation',
    'SrtError', 'NeedToLoginError', 'NoResultError',
]
