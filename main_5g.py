import importlib
from sim.simulator import Simulator
from sim.statistics import Statistics
import numpy as np
import matplotlib.pyplot as plt
import os
#from sim.link import Link



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

def plot_load(statsdict):
    cloud=plt.figure(1,figsize=(4,1))
    axes=plt.subplot(111)
    N=2
    D1=[]
    E1=[]
    E2=[]
    C1=[]
    C2=[]
    C3=[]
    for module,stats in statsdict.items():
        D1.append(stats.serverdict["Device"]/1000)
        E1.append(stats.serverdict["Edge1"]/1000)
        E2.append(stats.serverdict["Edge2"]/1000)
        C1.append(stats.serverdict["Cloud1"]/1000)
        C2.append(stats.serverdict["Cloud2"]/1000)
        C3.append(stats.serverdict["Cloud3"]/1000)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.75       # the width of the bars: can also be len(x) sequence


    p1 = axes.barh(ind, D1, width,color='indianred')
    p2 = axes.barh(ind, E1, width, left=D1,color='lightgreen')
    p3 = axes.barh(ind, E2, width, left=[D1[i]+E1[i] for i in range(0,N)],color='mediumseagreen')
    p4 = axes.barh(ind, C1, width, left=[D1[i]+E1[i]+E2[i] for i in range(0,N)],color='dodgerblue')
    p5 = axes.barh(ind, C2, width, left=[D1[i]+E1[i]+E2[i]+C1[i] for i in range(0,N)],color='skyblue')
    p6 = axes.barh(ind, C3, width, left=[D1[i]+E1[i]+E2[i]+C1[i]+C2[i] for i in range(0,N)],color='turquoise')

    axes.legend((p1[0], p2[0],p3[0],p4[0], p5[0],p6[0]), ('D1', 'E1','E2','C1','C2','C3'),bbox_to_anchor=(1.1, 1.2))
    axes.set_xlabel('Nr of tasks (x1000)')
    axes.set_yticks(ind)
    axes.set_yticklabels(['5G','5G 60FPS'])
    cloud.savefig(os.getcwd() + '/figs/5g.pdf',format = 'pdf',bbox_inches = 'tight')
    print("saved")


def main():
    simdict={}
    statsdict={}

    importname="configs.config_5g."

    names=["config_5g","config_5g_60fps"]
    for name in names:
        sim,stats=simulate(importname+name)
        simdict[importname+name]=sim
        statsdict[importname+name]=stats
    plot_load(statsdict)


if __name__== "__main__":
    main()
