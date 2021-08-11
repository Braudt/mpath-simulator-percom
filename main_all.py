import importlib
from sim.simulator import Simulator
from sim.statistics import Statistics
import numpy as np
import matplotlib.pyplot as plt
import os


def simulate(config_module):
    config=importlib.import_module(config_module)
    print(config.NAME)
    sim=Simulator(config.tasklist,config.combinations)
    sim.run()
    stats=Statistics(config.NAME,config.tasklist,config.combinations)
    stats.compute()
    stats.printstats()
    print("================")
    return sim, stats

def plot_results(statsdict):
    # Get Values
    latetasks=[]
    latetimes=[]
    completiontimes=[]
    for key,value in statsdict.items():
        latetasks.append(value.late/1000)
        if value.late!=0:
            latetimes.append(value.latency/value.late)
        else:
            latetimes.append(0)
        completiontimes.append(value.completion/value.total)

    # Plot Figure
    cloud=plt.figure(1,figsize=(4,2))
    axes=plt.subplot(111)
    N=7
    ind = np.arange(N)    # the x locations for the groups
    width = 0.75       # the width of the bars: can also be len(x) sequence

    p1 = axes.bar(ind, latetasks, width/3,color='indianred')
    axes2 = axes.twinx()
    p2 = axes2.bar(ind+width/3, latetimes, width/3,color='dodgerblue')
    p3 = axes2.bar(ind+width*2/3, completiontimes, width/3,color='seagreen')

    axis_font = {'size':'12'}
    axes.legend((p1[0], p2[0],p3[0]), ("Nr of tasks over deadline","Avg time over deadline","Avg completion time"),bbox_to_anchor=(0.3, 1.1))
    axes.set_ylabel('Tasks (x1000)',**axis_font)
    axes2.set_ylabel('Excess latency (ms)',**axis_font)
    axes.set_xticks(ind+width/4)
    axes.set_xticklabels(['D2D','E1','E2','E1+E2','C1','C1-3','All'], rotation=30,**axis_font)
    axes2.set_yscale('log')

    cloud.savefig(os.getcwd() + "/figs/offloading.pdf",format='pdf',bbox_inches = 'tight')


def main():
    module_list=["config_d2d",
            "config_e1",
            "config_e2",
            "config_e1e2",
            "config_c1",
            "config_c1c2c3",
            "config_all"]

    simdict={}
    statsdict={}

    for module in module_list:
        importname="configs.config_all."+module
        sim,stats=simulate(importname)
        simdict[importname]=sim
        statsdict[importname]=stats


    plot_results(statsdict)

import subprocess
import sys
if __name__== "__main__":
    print("main_all")
    main()

