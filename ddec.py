__author__ = 'adibb'

# Written by Alex Dibb
# Last edited 11/8/2017
# Debugging decorator for setclock, derived from A. Hornof's work
# Seperated for future work, and for early declaration

# Log event without dismissal
def log_event(func):
    def log_wrapper(self, event):
        if __debug__:
            print("----------------------------------")
            print("Event Dismissed")
            print("Time:\t", str(event.time))
            print("Event:\t", event)
            print("----------------------------------")
        return(func(self, event))
    return log_wrapper