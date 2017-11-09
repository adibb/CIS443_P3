__author__ = 'adibb'

# Written by Alex Dibb
# Last edited 11/8/2017
# Side file for option building functions, to declutter the main file


# IMPORTS
from dllist import DLList, LoopList


# GLOBALS
MISC_PATH = "wav_files_provided/miscellaneous_f/"
DAY_PATH = "wav_files_provided/days_of_week_f/"
NUM_PATH = "wav_files_provided/numbers_f/"


# Datum class
class Datum:
    # General variables
    def __init__(self, text, wavLoc):
        self.text = text
        self.wavLoc = wavLoc

    # Getters and setters
    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def get_wav(self):
        return self.wavLoc

    def set_wav(self, wavLoc):
        self.wavLoc = wavLoc


# Datum class definition for menu selections
class MenuDatum(Datum):
    # Define variables\
    def __init__(self, text, wavLoc, domain):
        super().__init__(text, wavLoc)
        self.domain = domain

    # Getters and setters
    def get_domain(self):
        return self.domain

    def set_domain(self, domain):
        self.domain = domain


# Helper function to build the menu options
def build_menu():
    result = DLList()
    result.add(MenuDatum("Set Day", MISC_PATH + "Set_day_f.wav", build_days()))
    result.add(MenuDatum("Set Hour", MISC_PATH + "Set_hour_f.wav", build_hours()))
    result.add(MenuDatum("Set Minute", MISC_PATH + "Set_minute_f.wav", build_minutes()))
    result.add(MenuDatum("Exit Program", MISC_PATH + "Exit_program_f.wav", None))
    return result


# Helper function to build the day select options
def build_days():
    result = LoopList()
    result.add(Datum("Sunday", DAY_PATH + "sunday_f.wav"))
    result.add(Datum("Monday", DAY_PATH + "monday_f.wav"))
    result.add(Datum("Tuesday", DAY_PATH + "tuesday_f.wav"))
    result.add(Datum("Wednesday", DAY_PATH + "wednesday_f.wav"))
    result.add(Datum("Thursday", DAY_PATH + "thursday_f.wav"))
    result.add(Datum("Friday", DAY_PATH + "friday_f.wav"))
    result.add(Datum("Saturday", DAY_PATH + "saturday_f.wav"))
    return result


# Helper function to build the hour select options
def build_hours():
    result = LoopList()
    for i in range(24):
        if i > 10:
            txt = str(i)
        else:
            txt = "0" + str(i)
        wav = NUM_PATH + txt + "_f.wav"
        result.add(Datum(txt, wav))
    return result

# Helper function to build the minute select options
def build_minutes():
    result = LoopList()
    for i in range(0, 60, 5):
        if i >= 10:
            txt = str(i)
        else:
            txt = "0" + str(i)
        wav = NUM_PATH + txt + "_f.wav"
        result.add(Datum(txt, wav))
    return result
