#Data Structures
#TO-DO
import os
import glob

class datastruct:

    def __init__(self):
        p = 'Data/'

        try:
            os.makedirs(p)
        except OSError:
            if not os.path.isdir(p):
                raise

d = datastruct()