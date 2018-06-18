#coding:utf-8
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def run_main():

    x1 = np.random().normal(size=500)
    sns.distplot(x1)
    plt.show()

if __name__ == '__main__':
    run_main()
    
    