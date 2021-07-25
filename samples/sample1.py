from __future__ import print_function
from __future__ import division

#from pandas.core.window import EWM

import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
# matplotlib inline
import os
import sys

sys.path.insert(0, os.path.abspath('./..'))
sys.path.insert(0, os.path.abspath('.'))
import abupy

abupy.env.enable_example_env_ipython()

from abupy import ABuSymbolPd

us_jd = ABuSymbolPd.make_kl_df('usJD') 
us_jd is None

abupy.env.disable_example_env_ipython()

us_jd = ABuSymbolPd.make_kl_df('usJD')
#print(us_jd)
# 再次开启沙盒环境，本节的示例都是在沙盒数据环境下运行
abupy.env.enable_example_env_ipython()
tail = None
if us_jd is not None:
    tail = us_jd.tail()
else:
    print("tail:xxx", tail)
print(tail)


def main():
    print("hello,world")
    return

if __name__ == "__main__":
    main() 