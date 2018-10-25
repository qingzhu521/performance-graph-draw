import numpy as np
import matplotlib.pyplot as plt
from pylab import *

algs = ['CliqueJoin', 'PSgL', 'BigJoin','CystalJoin','MultiwayJoin',]
labelled_algs = ['CliqueJoin','StarJoin', 'PSgL','BigJoin','CystalJoin', 'MultiwayJoin']
# 每个算法是一个单位。


# Exp-4 Scalability
scalability_lj_q1 = [
    # 1,        2,      4,      6,      8,      10
    [5794.76,   2202.91,1124.72,812.88, 654.32, 569.6],  # cliquejoin
    [0,         0,      0,      0,      0,      0],  # psgl
    [1355.07,   730,    376.02, 254.35, 195.9,  158.5],  # bigjoin?
    [0,         0,      0,      0,      0,      0],  # crystaljoin
    [0,         7037.98,5322,   2975.56,3095.15,1610.13],  # multiwayjoin
    [2129.36,   2129.36,2129.36,2129.36,2129.36,2129.36] #single thread
]

scalability_lj_q1_commnuication = [
    # 1,        2,         4,           6,          8,          10
    [7957.596903,3979.267998,1989.682698,  1326.676185, 995.285574,  796.487292], #clique
    [None,         None,          None,          None,          None,          None],  # psgl
    [20174.493477,10271.095042,5296.603797, 3667.458593, 2823.005059, 2325.011820], #bigjoin
    [None,         None,          None,          None,          None,          None],  # crystal
    [None,         171.480011, 128.628774,   123.806121,  195.327068,  147.650829], #multiway


    [7956.624894,   3977.789253,  1988.671353, 1325.459355,994.116846, 794.940078],
    [None, None, None, None, None, None],  # psgl
    [19633.758791,  9558.815152, 4579.171909,     2972.001214,  2153.157041, 1763.829489],
    [None, None, None, None, None, None],  # crystal
    [None,         32.158341,   10.695191,      23.783410, 14.286331, 9.531735],
]
scalability_lj_q1_mem = [
    # 1,        2,          4,          6,          8,          10
    [35.42,     24.04,      20.64,      20.55,      20.65,      20.47], #clique
    [None,         None,          None,          None,          None,          None],  # psgl
    [1.35,      1.05,       1.18,       1.48,       1.78,       1.97], #bigjoin
    [None,         None,          None,          None,          None,          None],  # crystal
    [None,         36.08,      29.71,      39.01,      32.08,      36.96], #multiway

    [35.42, 23.9, 14.85, 10.34, 8.033, 7.7], #clique
    [None, None, None, None, None, None],  # psgl
    [1.35, 1.05, 1.04, 1.2, 1.43, 1.33],  # big_join
    [None, None, None, None, None, None],  # crystal
    [None, 26.2, 5.4, 22.79, 18.05, 7.52],  # multiway
]


scalability_lj_q2 = [
    # 1,        2,      4,      6,      8,      10
    [499.03,    250.4,  131.47, 90.234, 67.54,  56.42],  # cliquejoin
    [0,         0,      0,      0,      0,      0],  # psgl
    [1063.72,   570.05, 300.66, 204.63, 156.41, 128.96],  # bigjoin
    [0,         0,      0,      0,      0,      0],  # crystaljoin
    [0,         6859.92,5438,   3115.46,3423.35,2258.24],  # multiwayjoin
    [111.62,    111.62, 111.62, 111.62, 111.62, 111.62], # god
]
scalability_lj_q2_commnuication = [
    [1715.184090,            858.401232,          429.824946,              286.547790,          215.260326,      172.275786], #clique
    [None,                     None,                  None,                      None,                  None,              None],  # psgl
    [29323.486405,           14782.716013,        7583.165895,             5187.069282,         4129.050963,     3384.823851],  #big
    [None,                     None,                  None,                      None,                  None,              None], #crystal
    [None,                 171.480011,          128.628774,              200.039302,          209.582811,      152.401068],#multiway


    [1713.200292,       856.111050,         427.354404,     284.814492,     213.422592,     170.759808], #clique
    [None, None, None, None, None, None],  # psgl
    [28446.929240,      13895.943553,       6601.104993,    4394.393856,     3169.384430,   2464.148837], #big
    [None, None, None, None, None, None],  # crystal
    [None,              42.851237,          10.695191,      23.783410,      14.286331,      14.281974]#multiway

]
scalability_lj_q2_mem = [
    [22.24,         21.84,      12.77,      9.96,       7.93,   6.91], #clique
    [None,             None,          None,          None,          None,      None],    #psgl
    [1.53,          1.58,       1.74,       1.72,       1.59,   1.77], #big
    [None,             None,          None,          None,          None,      None],    #crystal
    [None,             38.87,      29.08,      45.63,      33.64,  36.48],#multiway


    [22.24, 21.61,  12.48,  9.1,    7.43,   6.63],
    [None, None, None, None, None, None],  # psgl
    [1.53,  1.49,   1.56,   1.46,   1.37,   1.34],
    [None, None, None, None, None, None],  # crystal
    [None,   26.2,   5.45,   22.71,  19.51,  7.52],
]
scalability_lj_q3 = [
    # 1,    2,     4,     6,    8,    10
    [30.72, 15.62, 8.11, 5.344, 4.12, 3.25],  # cliquejoin
    [0, 0, 0, 0, 0, 0],  # psgl
    [348.82, 193.07, 101.7,68.64, 52.72, 43.19],  # bigjoin?
    [0, 0, 0, 0, 0, 0],  # crystaljoin
    [4560,2472.39,1847.69,1103.27,1192.03,854.961],  # multiwayjoin
    [220.12,220.12,220.12,220.12,220.12,220.12] #god
]
scalability_lj_q3_communication = [
    # 1,            2,          4,          6,          8           10
    [5,             5,          5,          5,          5,          5], #clique
    [None, None, None, None, None, None],  # psgl
    [8532.344313,    4289.522467,   2198.958161, 1466.508873, 1177.325857, 990.845502], #big
    [None, None, None, None, None, None],  # crystal
    [278.645635,     171.480011,  128.628774,  214.319310, 228.613469,  157.153820], #multiway

    [5,5,5,5,5,5], #clique
    [None, None, None, None, None, None],  # psgl
    [8294.838495,   4041.980471,    1943.966481,    1279.108174,    943.452885, 710.826657], #big
    [None, None, None, None, None, None],  # crystal
    [128.551416,    42.851237,      42.851237,      23.783410,      14.286331,  11.032624],#multiway
]
scalability_lj_q3_mem = [
    [0.54,      0.54,       0.54,       0.54,       0.54,      0.54 ], #clique
    [None,         None,          None,          None,          None,         None], #psgl
    [0.94,      0.81,       0.78,       0.74,       0.75,      0.72], #big
    [None,         None,          None,          None,          None,         None], #crystal
    [61.2,      36.65,      28.08,      48.56,      42.92,     41.48], #mulitway

    [0.54,  0.54,   0.54,   0.54,   0.539,  0.539], #clique
    [None, None, None, None, None, None],  # psgl
    [0.94,  0.81,   0.75,   0.7,    0.67,   0.65], #big
    [None, None, None, None, None, None],  # crystal
    [61.20, 26.2,   5.45,   25.66,  21.97,  9.88], #multiway
]
scalability_DG10_q3 = [
    [0,0,0,246.63,191.71,169.18], #clique
    [0,0,0,246.63,191.71,169.18],#star
    [0, 0, 0, 0, 0, 0],  # psgl
    [0,0,10594.28,7079.94,5518.08,4630.83], #big
    [0, 0, 0, 0, 0, 0],  # crs
    [0, 0, 0, 0, 0, 0],  # multi
]

scalability_DG10_q6 = [
    [142.56,71.53,37.57,24.6,18.75,15.08], #clique
    [0, 0, 0, 0, 0, 0],  # star
    [163.76, 88.4, 52.61, 42.92, 40.25, 46.69],  # psgl
    [1.87, 2.05, 1.7, 1.6, 1.55, 1.49],  # big
    [0, 0, 0, 0, 0, 0],  # crs
    [1464.45, 1389.95, 1338.63, 833.03, 702.55, 306.42],  # multi
]

scalability_DG10_vary_label_q3 = [
    [0, 0, 168.6, 84.95, 44.35],  # cliq
    [0, 0, 168.6, 84.95, 44.35],  # star
    [0, 0, 0, 0, 0],  # psgl
    [0, 0, 4677.5, 2027.49, 717.88],  # big
    [0, 0, 0, 0, 0],  # crs
    [0, 0, 1397.16, 424.64, 256.3],  # multi
]

scalability_DG10_vary_label_q6 = [
    [0, 19.18, 4.48, 4.4, 4.38],  # clique
    [0, 0, 42.5, 21.7, 12.19],  # star
    [0, 0, 0, 0, 38.63],  # psgl
    [0, 479.14, 4.92, 5.61, 5.57],  # big
    [0, 0, 0, 0, 0],  # crys
    [0, 441.81, 274.77, 271.84, 275.74],  # multi
]

scalability_DG10_vary_density_q3 = [
    [169.14, 180.01, 193.28, 0, 0],  # clique
    [169.14, 0, 0, 0, 0 ],  # star
    [0, 0, 0, 0, 0 ],  # psgl
    [4630.83, 5129.1, 5634.45, 6377.6, 0, ],  # big
    [0, 0, 0, 0, 0 ],  # crys
    [0, 0, 0, 0, 0 ],  # multiway
]
scalability_DG10_vary_density_q6 = [
    [15.08,  15.44,15.79,16.38,0],#clique
    [0,  0, 0, 0, 0],  # star
    [51.46, 64.33, 83.44, 156, 0],  # psgl
    [1.49, 14.47, 26.48, 56.82, 148.75],  # big
    [0, 0, 0, 0, 0],  # crys
    [306.42, 1000, 1918.61,3833,4196],#multiway
]
#Exp scalability computation time
scalability_comp_time_q1 = [
    [569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.5, 569.6, 569.6,
     569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.5, 569.6, 569.6, 569.6, 569.6, 569.6], #clique
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # psgl
    [127.58, 123.65, 120.81, 125.36, 124.39, 124.53, 128.9, 132.01, 124.76, 124.26, 121.6, 131.02, 130.81, 123.05,
     117.7, 129.7, 122.38, 130.17, 121.35, 121.07, 124.38, 121.33, 121.93, 126.39, 124.1, 122.43, 117.45, 121.35,
     124.51, 123.76],  # big
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # crystal
    [463.592, 601.482, 777.71, 515.94, 727.896, 1056.83, 843.133, 1179.94, 1293.92, 1061.83, 1097.82, 1127.4, 853.46,
     866.137, 1308.63, 622.677, 763.76, 1018.92, 754.472, 1109.1, 1565.48, 600.008, 984.1, 1009.5, 725.031, 819.491,
     828.578, 853.717, 857.439, 1467.17],  # multiway_join

]
scalability_comp_time_q2 = [
    [569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.5, 569.6, 569.6,
     569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.5, 569.6, 569.6, 569.6, 569.6, 569.6], #clique
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # psgl
    [91.62, 90.36, 89.25, 92.63, 93.87, 93.22, 95.43, 101.34, 90.72, 91.72, 92.76, 95.29, 100.52, 89.57, 89.49, 93.44,
     84.69, 97.67, 92.31, 90.93, 94.49, 88.82, 87.75, 89.81, 89.71, 89.14, 83.17, 89.34, 88.34, 90.44],  # big
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # crystal
    [661.171, 793.752, 962.087, 599.037, 803.905, 1011.04, 444.591, 1542.51, 2258.24, 352.419, 665.806, 939.076,
     621.343, 1389.38, 2145.73, 329.383, 1095.14, 674.51, 687.998, 1755.05, 464.567, 875.743, 1501.27, 361.022, 539.256,
     546.552, 696.385, 1235.67, 803.905, 939.076, ],  # multiway_join
]
scalability_comp_time_q3 = [
    [569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.5, 569.6, 569.6,
     569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.5, 569.6, 569.6, 569.6, 569.6, 569.6], #clique
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # psgl
    [28.6, 28.58, 28.76, 29.16, 29.69, 29.83, 30.34, 31.36, 29.09, 29.36, 29.18, 30.08, 31.49, 28.49, 29.43, 30.03,
     27.7, 30.54, 29.24, 29.25, 30.13, 28.79, 28.52, 29, 29.16, 28.82, 27.49, 28.85, 28.59, 29.38],  # big
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # crystal
    [270.743, 336.017, 380.868, 251.536, 290.172, 425.923, 125.313, 579.579, 854.961, 137.25, 211.99, 357.371, 276.894,
     480.737, 726.349, 116.252, 305.704, 265.919, 279.904, 666.72, 247.001, 354.317, 608.673, 121.743, 201.993, 185.278,
     226.011, 455.487, 495.923, 405.923, ],  # multiway_join
]
def assign_inf(data):
    inf = 0
    for each_data in data:
        for val in each_data:
            inf = max(inf, val)
    ten = 10
    while inf * 10 >= ten:
        ten *= 10
    inf = ten

    for each_data in data:
        for i in range(len(each_data)):
            if each_data[i] == 0:
                each_data[i] = inf

    return inf

def assign_inf_long(data):
    inf = 0
    for each_data in data:
        for val in each_data:
            if is_numlike(val):
                inf = max(inf, val)
    inf = inf * 1.25

    for each_data in data:
        for i in range(len(each_data)):
            if each_data[i] == 0:
                each_data[i] = inf

    return inf

#labelled_algs = ['CliqueJoin','StarJoin','CystalJoin', 'BigJoin','MultiwayJoin', 'PSgL']
patterns = {
    'CliqueJoin': 'o',
    'StarJoin': 'x',
    'PSgL':'v',
    'BigJoin': '^',
    'CystalJoin': '*',
    'MultiwayJoin': 'p',
}

def plot_line(exp, title, xticks, xlabel, proj, data, is_legend):
    plt.figure(figsize=(3.2,2.3))
    numx = len(xticks)
    numy = len(proj) + 2
    total_width = 0.2 * numy * numx
    inf = assign_inf(data)
    inf_log = int(np.log10(inf))
    #set yaxes
    ylocs = []
    yticks = []
    for i in range(inf_log + 1):
        ylocs.append(int(np.power(10, i)))
        if i < inf_log:
            yticks.append("$10^" + str(i) + "$")
        else:
            yticks.append("Inf")
    plt.yscale('log')
    plt.yticks(ylocs, yticks)
    plt.title("T (sec)",loc="left")

    ax = plt.gca()
    for (i, pj) in enumerate(proj):
        print(i, pj)
        ax.plot(xticks, data[i], ls=':',marker=patterns[pj], mec='k', mfc='w', label=pj, color='k')
    if exp.startswith('scalability_vary_workers'):
        ax.plot(xticks, data[5], mec='r', mfc='w', label='Single Thread', color='r')

    #plt.xlabel(xlabel)
    #plt.ylim(0,inf)
    plt.xticks(xticks, fontsize='8')
    plt.savefig('figures/' + exp + '_' + title + '.pdf', format='pdf')

    if is_legend:
        # Plot the legend in a separate figure
        legend_fig = plt.figure(figsize=(total_width*1.3 ,0.2))
        lax = legend_fig.add_subplot(111)
        lax.legend(*ax.get_legend_handles_labels(), ncol = numy,loc='center', frameon=True)
        lax.axis('off')
        plt.savefig('figures/' + exp + '_legend.pdf', fotmat='pdf')


def plot_line_self_scala(exp, title, ylabel, xticks, xlabel, proj, data, is_legend):
    plt.figure(figsize=(4.5,2.3))
    numx = len(xticks)
    numy = len(proj) + 2
    total_width = 0.2 * numy * numx
    inf = assign_inf_long(data)

    #set yaxes
    plt.title(ylabel,loc="left")
    plt.ylim((-1,inf + 0.2))
    yloc = list(np.arange(0, inf, step=inf / 4))
    ytics = list(np.arange(0, inf, step=inf / 4))
    ytics = [str(int(x)) for x in ytics]
    print(yloc,ytics)
    if exp.endswith('mem') :
        yloc.append(inf)
        ytics.append('64')

    ax = plt.gca()
    for (i, pj) in enumerate(proj):
        print(i, pj)
        ax.plot(xticks, data[i], ls=':',marker=patterns[pj], mec='k', mfc='w', label=pj, color='k')
        ax.plot(xticks, data[i + 5], ls='-.',marker=patterns[pj], mec='k', mfc='w', label=pj, color='k')

    #plt.xlabel(xlabel)
    plt.yticks(yloc, ytics)
    plt.xticks(xticks, fontsize='8')
    plt.savefig('figures/' + exp + '_' + title + '.pdf', format='pdf')

    if is_legend:
        # Plot the legend in a separate figure
        legend_fig = plt.figure(figsize=(total_width*1.3 ,0.2))
        lax = legend_fig.add_subplot(111)
        lax.legend(*ax.get_legend_handles_labels(), ncol = numy,loc='center', frameon=True)
        lax.axis('off')
        plt.savefig('figures/' + exp + '_legend.pdf', fotmat='pdf')

def plot_line_long(exp, title, data):
    plt.figure(figsize=(9.6, 2.3))
    inf = assign_inf_long(data)
    x = list(range(1,31))
    yloc = [500, 1000, 1500, inf]
    yticks = [500, 1000, 1500, "inf"]
    plt.yticks(yloc, yticks)
    plt.title("T (sec)",loc="left")
    for (i, alg) in enumerate(algs):
        print(i, alg)
        plt.plot(x, data[i], ls=':',marker=patterns[alg], mec='k', mfc='w', label=alg, color='k')
    plt.xticks(x)
    plt.savefig('figures/' + exp + '_' + title + '.pdf', format='pdf')


if __name__ == '__main__':
    # vary machines
    scala_each_time = {
        'query1': scalability_comp_time_q1,
        'query2': scalability_comp_time_q2,
        'query3': scalability_comp_time_q3,
    }
    for key in scala_each_time.keys():
        #plot_line_long('scalability_workers_runningtime', key, scala_each_time[key])
        plt.close()



    xtic_machines = [3, 6, 12, 18, 24, 30]
    xlabel = '# Workers, machines * 3 workers/per machine'
    scalability = {
        'query1': scalability_lj_q1,
        'query2': scalability_lj_q2,
        'query3': scalability_lj_q3,
    }
    scalability_commnunication = {
        'query1': scalability_lj_q1_commnuication,
        'query2': scalability_lj_q2_commnuication,
        'query3': scalability_lj_q3_communication,
    }
    scalability_mem = {
        'query1': scalability_lj_q1_mem,
        'query2': scalability_lj_q2_mem,
        'query3': scalability_lj_q3_mem,
    }
    is_legend = True
    for i in scalability.keys():
        #plot_line('scalability_vary_workers', i, xtic_machines, xlabel, algs, scalability[i], is_legend)
        plot_line_self_scala('scalability_lj_communication', i, '$C_{max}$ (millions)', xtic_machines, xlabel, algs, scalability_commnunication[i], is_legend)
        plot_line_self_scala('scalability_lj_mem', i, '$M_{max}$ (GB)', xtic_machines, xlabel, algs, scalability_mem[i], is_legend)
        is_legend = False

'''
    labelled_scalability = {
        'query3': scalability_DG10_q3,
        'query6': scalability_DG10_q6,
    }
    is_legend = True
    for key in labelled_scalability.keys():
        plot_line('scalability_labelled_vary_workers', key, xtic_machines, xlabel, labelled_algs, labelled_scalability[key], is_legend)
        plt.close()
        is_legend = False
    
    xtic_labels = [0, 5, 10, 15, 20]
    xlabel = '#Node Labels'
    labelled_var_labels = {
        'query3': scalability_DG10_vary_label_q3,
        'query6': scalability_DG10_vary_label_q6,
    }
    is_legend = True
    for key in labelled_var_labels.keys():
        plot_line('scalability_labelled_var_labelled', key, xtic_labels, xlabel, labelled_algs, labelled_var_labels[key], is_legend)
        plt.close()
        is_legend = False

    xtic_density = [10, 20, 40, 80, 160]
    xlabel = '#Density'
    labelled_var_density = {
        'query3': scalability_DG10_vary_density_q3,
        'query6': scalability_DG10_vary_density_q6,
    }
    is_legend = True
    for key in labelled_var_density.keys():
        plot_line('scalability_labelled_var_density', key, xtic_density, xlabel, labelled_algs, labelled_var_density[key], is_legend)
        plt.close()
        is_legend = False
'''