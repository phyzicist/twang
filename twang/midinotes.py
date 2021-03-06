#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
midinotes.py: Load and interpret list of midi note numbers

Helper function.

Created by Scott Feister on Mon Aug  5 15:24:35 2019
"""

notedict = {'G9' : 127,
    'F#9' : 126,
    'F9' : 125,
    'E9' : 124,
    'D#9' : 123,
    'D9' : 122,
    'C#9' : 121,
    'C9' : 120,
    'B8' : 119,
    'A#8' : 118,
    'A8' : 117,
    'G#8' : 116,
    'G8' : 115,
    'F#8' : 114,
    'F8' : 113,
    'E8' : 112,
    'D#8' : 111,
    'D8' : 110,
    'C#8' : 109,
    'C8' : 108,
    'B7' : 107,
    'A#7' : 106,
    'A7' : 105,
    'G#7' : 104,
    'G7' : 103,
    'F#7' : 102,
    'F7' : 101,
    'E7' : 100,
    'D#7' : 99,
    'D7' : 98,
    'C#7' : 97,
    'C7' : 96,
    'B6' : 95,
    'A#6' : 94,
    'A6' : 93,
    'G#6' : 92,
    'G6' : 91,
    'F#6' : 90,
    'F6' : 89,
    'E6' : 88,
    'D#6' : 87,
    'D6' : 86,
    'C#6' : 85,
    'C6' : 84,
    'B5' : 83,
    'A#5' : 82,
    'A5' : 81,
    'G#5' : 80,
    'G5' : 79,
    'F#5' : 78,
    'F5' : 77,
    'E5' : 76,
    'D#5' : 75,
    'D5' : 74,
    'C#5' : 73,
    'C5' : 72,
    'B4' : 71,
    'A#4' : 70,
    'A4' : 69,
    'G#4' : 68,
    'G4' : 67,
    'F#4' : 66,
    'F4' : 65,
    'E4' : 64,
    'D#4' : 63,
    'D4' : 62,
    'C#4' : 61,
    'C4' : 60,
    'B3' : 59,
    'A#3' : 58,
    'A3' : 57,
    'G#3' : 56,
    'G3' : 55,
    'F#3' : 54,
    'F3' : 53,
    'E3' : 52,
    'D#3' : 51,
    'D3' : 50,
    'C#3' : 49,
    'C3' : 48,
    'B2' : 47,
    'A#2' : 46,
    'A2' : 45,
    'G#2' : 44,
    'G2' : 43,
    'F#2' : 42,
    'F2' : 41,
    'E2' : 40,
    'D#2' : 39,
    'D2' : 38,
    'C#2' : 37,
    'C2' : 36,
    'B1' : 35,
    'A#1' : 34,
    'A1' : 33,
    'G#1' : 32,
    'G1' : 31,
    'F#1' : 30,
    'F1' : 29,
    'E1' : 28,
    'D#1' : 27,
    'D1' : 26,
    'C#1' : 25,
    'C1' : 24,
    'B0' : 23,
    'A#0' : 22,
    'A0' : 21,
    }

def getnote(notestr):
    """ Returns the midi number, given the note """
    try:
        return notedict[notestr]
    except:
        raise(Exception(str(notestr) + " is not a valid note string! Examples of valid notestrings are C1, C#8, B7, etc. Range is from A0 to F#9."))

if __name__ == "__main__":
    pass
