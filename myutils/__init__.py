import shutil
import subprocess

__author__ = 'Omer'

import os, sys


def IncreamentDict(dic, key, val=1):
    if not dic.has_key(key):
        dic[key] = 0
    dic[key] += val


def createCleanDir(fullpath):
    if not os.path.exists(fullpath):
        os.makedirs(fullpath)
    else:
        shutil.rmtree(fullpath)
        os.makedirs(fullpath)


def printDict(dic):
    for key in dic.keys():
        print str(key) + "\t \t \t" + str(dic[key])


def normalizeDict(dic):
    normFactor = 0.0
    for key in dic.keys():
        normFactor += (int(dic[key]) * 1.0) ** 2
    normFactor = normFactor ** 0.5
    for key in dic.keys():
        dic[key] = round((dic[key] * 1.0 / normFactor), 2)
    return dic


def inPlaceDictOffSet(dic, offset):
    newDict = {}
    for key in dic.keys():
        newDict[key + offset] = dic.pop(key)
    return newDict


def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def file_exists(fname):
    import os.path

    return os.path.isfile(fname)


def get_ans(valid_lst):
    while True:
        data = sys.stdin.readline().replace("\n", "")
        if data in valid_lst:
            return data
        print "please enter value in " + str(valid_lst)


def override_file(filename):
    print "the file\n\t" + filename + "\nalready exists. do you want to override it?"
    ans = get_ans(["y", "n"])
    if ans == "y":
        return True
    return False


def round_with_half(x):
    base = int(x)
    if x * 100 % 100 < 25:
        return base
    elif x * 100 % 100 > 75:
        return base + 1
    return base + 0.5


def execute_cmd(cmd, logger=None):
    if logger != None:
        with open(logger, 'a') as f:
            p = subprocess.call(cmd, stdout=f, shell=True)
    else:
        p = subprocess.call(cmd, shell=True)
    return cmd


def get_cmap(N):
    '''Returns a function that maps each index in 0, 1, ... N-1 to a distinct
    RGB color.'''
    import matplotlib.pyplot as plt
    import matplotlib.cm as cmx
    import matplotlib.colors as colors

    color_norm = colors.Normalize(vmin=0, vmax=N - 1)
    scalar_map = cmx.ScalarMappable(norm=color_norm, cmap='hsv')

    def map_index_to_rgb_color(index):
        return scalar_map.to_rgba(index)

    return map_index_to_rgb_color


def rename_key(dictionary, oldkey, newkey):
    """ gets a dict, and rename the old key for the new one"""
    if newkey != oldkey:
        dictionary[newkey] = dictionary[oldkey]
        del dictionary[oldkey]

def all_options(dl):
    """
    gets a dict of list and return a list of dicts (generator)
    input:
        model_params = {
        'kernel': ['rbf', 'poly', 'sigmoid'],
        'gamma': [1e-3, 1e-4],
        'C': [0.3, 0.5, 0.7, 1, 3, 6],
        }
    output:
        [{'kernel': 'rbf', 'C': 0.3, 'gamma': 0.001}, {'kernel': 'poly', 'C': 0.5, 'gamma': 0.0001}, {'kernel': 'sigmoid', 'C': 0.7}]
    """
    l = list((k,v.__iter__()) for k,v in dl.items())
    while True:
        d = dict((k,i.next()) for k,i in l)
        if not d:
            break
        yield d