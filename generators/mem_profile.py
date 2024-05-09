# Using code from
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Generators
# by Corey Schafer

import os
import resource
import sys

import psutil
from pympler import muppy, summary


def memory_usage_psutil():
    # return the memory usage in MB
    process = psutil.Process(os.getpid())
    mem = process.get_memory_info()[0] / float(2**20)
    return mem


def memory_usage_resource():
    rusage_denom = 1024.0
    if sys.platform == "darwin":
        # ... it seems that in OSX the output is different units ...
        rusage_denom = rusage_denom * rusage_denom
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
    return mem
