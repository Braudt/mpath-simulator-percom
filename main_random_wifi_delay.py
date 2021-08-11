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


def align_yaxis(ax1, v1, ax2, v2):
    """adjust ax2 ylimit so that v2 in ax2 is aligned to v1 in ax1"""
    _, y1 = ax1.transData.transform((0, v1))
    _, y2 = ax2.transData.transform((0, v2))
    inv = ax2.transData.inverted()
    _, dy = inv.transform((0, 0)) - inv.transform((0, y1-y2))
    miny, maxy = ax2.get_ylim()
    ax2.set_ylim(miny+dy, maxy+dy)

def plot_deadlines(statsdict):
    axis_font = {'size':'14'}

    cloud=plt.figure(1,figsize=(4,2))
    axes=plt.subplot(111)
    N=6
    
    losses=[]
    deadline=[]
    for module,stats in statsdict.items():
        losses.append(stats.late)
        if stats.late>0:
            deadline.append(stats.latency/stats.late)
        else:
            deadline.append(0)

    x=[0, 100,200,300,400,500]

    ind = np.arange(N)    # the x locations for the groups

    plt1=axes.plot(x,losses,color='indianred')
    axes.set_xlabel('WiFi Latency Standard Deviation (%)',**axis_font)
    axes.set_ylabel('Tasks',**axis_font)
    for tick in axes.xaxis.get_major_ticks():
                    tick.label.set_fontsize(14)
    for tick in axes.yaxis.get_major_ticks():
                    tick.label.set_fontsize(14)

    axes2 = axes.twinx()
    plt2=axes2.plot(x,deadline,linestyle="--",color='dodgerblue')
    #axes2.set_ylim(top=0.5)
    align_yaxis(axes, 0, axes2, 0)
    axes2.set_ylabel('Excess latency (ms)',**axis_font)
    for tick in axes2.yaxis.get_major_ticks():
                    tick.label.set_fontsize(14)

    cloud.legend((plt1[0],plt2[0]),("Tasks over deadline","Avg time over deadline"), bbox_to_anchor=(1.1,1.5), fontsize=14)

    cloud.savefig(os.getcwd() + "/figs/random_wifi_delay_deadlines.pdf",format='pdf',bbox_inches = 'tight')

def plot_load(statsdict):
    axis_font = {'size':'14'}

    cloud=plt.figure(2,figsize=(4,2))
    axes=plt.subplot(111)
    N=6
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


    p1 = axes.bar(ind, D1, width,color='indianred')
    p2 = axes.bar(ind, E1, width, bottom=D1,color='lightgreen')
    p3 = axes.bar(ind, E2, width, bottom=[D1[i]+E1[i] for i in range(0,6)],color='mediumseagreen')
    p4 = axes.bar(ind, C1, width, bottom=[D1[i]+E1[i]+E2[i] for i in range(0,6)],color='dodgerblue')
    p5 = axes.bar(ind, C2, width, bottom=[D1[i]+E1[i]+E2[i]+C1[i] for i in range(0,6)],color='skyblue')
    p6 = axes.bar(ind, C3, width, bottom=[D1[i]+E1[i]+E2[i]+C1[i]+C2[i] for i in range(0,6)],color='turquoise')

    axes.legend((p1[0], p2[0],p3[0],p4[0], p5[0],p6[0]), ('D1', 'E1','E2','C1','C2','C3'),bbox_to_anchor=(1, 1),fontsize=14)
    axes.set_xlabel('WiFi Latency Standard Deviation (%)',**axis_font)
    axes.set_ylabel('Tasks (x1000)',**axis_font)
    axes.set_xticks(ind)
    axes.set_xticklabels(['0', '100', '200','300', '400', '500'], rotation=45,**axis_font)

#cloud.tight_layout()
    cloud.savefig(os.getcwd() + "/figs/random_wifi_delay_load.pdf",format='pdf',bbox_inches = 'tight')


def main():
    simdict={}
    statsdict={}

    module="config_random"
    importname="configs.config_random_wifi_delay."+module

    cloud_lat=["0","100","200","300","400","500"]
    for lat in cloud_lat:
        sim,stats=simulate(importname+str(lat))
        simdict[importname+lat]=sim
        statsdict[importname+lat]=stats
    plot_deadlines(statsdict)
    plot_load(statsdict)


if __name__== "__main__":
    main()
