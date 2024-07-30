from vinyaasa import *

def start_recording(fname):
    ff = open(fname, 'w')
    ff.write('स्थिति, सूत्र, टिप्पणी\n')
    ff.close()
    return ff


def record(fname, s, t, r):
    ff = open(fname, 'a', encoding='utf-8')
    ff.write(s + ', ' + t + ', ' + r +'\n')
    ff.close()

def end_recording(ff):
    ff.close()