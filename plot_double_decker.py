import numpy as np
import matplotlib.pyplot as plt
from pylab import *

algsh = ['CliqueJoin_h','PSgL_h','BigJoin_h','CystalJoin_h', 'MultiwayJoin_h', ]
algsl = ['CliqueJoin_l','PSgL_l','BigJoin_l','CystalJoin_l', 'MultiwayJoin_l', ]

scalability_lj_q1_commnuication = [
    # 1,        2,         4,           6,          8,          10
    [7957.596903,3979.267998,1989.682698,  1326.676185, 995.285574,  796.487292], #clique
    [0,         0,          0,          0,          0,          0],  # psgl
    [20174.493477,10271.095042,5296.603797, 3667.458593, 2823.005059, 2325.011820], #bigjoin
    [0,         0,          0,          0,          0,          0],  # crystal
    [0,         171.480011, 128.628774,   123.806121,  195.327068,  147.650829], #multiway

    [7956.624894,   3977.789253,  1988.671353, 1325.459355,994.116846, 794.940078],
    [0, 0, 0, 0, 0, 0],  # psgl
    [19633.758791,  9558.815152, 4579.171909,     2972.001214,  2153.157041, 1763.829489],
    [0, 0, 0, 0, 0, 0],  # crystal
    [0,         32.158341,   10.695191,      23.783410, 14.286331, 9.531735],
]
scalability_lj_q1_mem = [
    # 1,        2,          4,          6,          8,          10
    [35.42,     24.04,      20.64,      20.55,      20.65,      20.47], #clique
    [0,         0,          0,          0,          0,          0],  # psgl
    [1.35,      1.05,       1.18,       1.48,       1.78,       1.97], #bigjoin
    [0,         0,          0,          0,          0,          0],  # crystal
    [0,         36.08,      29.71,      39.01,      32.08,      36.96], #multiway

    [35.42, 23.9, 14.85, 10.34, 8.033, 7.7], #clique
    [0, 0, 0, 0, 0, 0],  # psgl
    [1.35, 1.05, 1.04, 1.2, 1.43, 1.33],  # big_join
    [0, 0, 0, 0, 0, 0],  # crystal
    [0, 26.2, 5.4, 22.79, 18.05, 7.52],  # multiway
]

scalability_lj_q2_commnuication = [
    [1715.184090,            858.401232,          429.824946,              286.547790,          215.260326,      172.275786], #clique
    [0,                     0,                  0,                      0,                  0,              0],  # psgl
    [29323.486405,           14782.716013,        7583.165895,             5187.069282,         4129.050963,     3384.823851],  #big
    [0,                     0,                  0,                      0,                  0,              0], #crystal
    [0,                 171.480011,          128.628774,              200.039302,          209.582811,      152.401068],#multiway

    [1713.200292,       856.111050,         427.354404,     284.814492,     213.422592,     170.759808], #clique
    [0, 0, 0, 0, 0, 0],  # psgl
    [28446.929240,      13895.943553,       6601.104993,    4394.393856,     3169.384430,   2464.148837], #big
    [0, 0, 0, 0, 0, 0],  # crystal
    [0,              42.851237,          10.695191,      23.783410,      14.286331,      14.281974]#multiway

]
scalability_lj_q2_mem = [
    [22.24,         21.84,      12.77,      9.96,       7.93,   6.91], #clique
    [0,             0,          0,          0,          0,      0],    #psgl
    [1.53,          1.58,       1.74,       1.72,       1.59,   1.77], #big
    [0,             0,          0,          0,          0,      0],    #crystal
    [0,             38.87,      29.08,      45.63,      33.64,  36.48],#multiway


    [22.24, 21.61,  12.48,  9.1,    7.43,   6.63],
    [0, 0, 0, 0, 0, 0],  # psgl
    [1.53,  1.49,   1.56,   1.46,   1.37,   1.34],
    [0, 0, 0, 0, 0, 0],  # crystal
    [0,   26.2,   5.45,   22.71,  19.51,  7.52],
]
scalability_lj_q3_communication = [
    # 1,            2,          4,          6,          8           10
    [5,             5,          5,          5,          5,          5], #clique
    [0, 0, 0, 0, 0, 0],  # psgl
    [8532.344313,    4289.522467,   2198.958161, 1466.508873, 1177.325857, 990.845502], #big
    [0, 0, 0, 0, 0, 0],  # crystal
    [278.645635,     171.480011,  128.628774,  214.319310, 228.613469,  157.153820], #multiway

    [5,5,5,5,5,5], #clique
    [0, 0, 0, 0, 0, 0],  # psgl
    [8294.838495,   4041.980471,    1943.966481,    1279.108174,    943.452885, 710.826657], #big
    [0, 0, 0, 0, 0, 0],  # crystal
    [128.551416,    42.851237,      42.851237,      23.783410,      14.286331,  11.032624],#multiway
]
scalability_lj_q3_mem = [
    [0.54,      0.54,       0.54,       0.54,       0.54,      0.54 ], #clique
    [0,         0,          0,          0,          0,         0], #psgl
    [0.94,      0.81,       0.78,       0.74,       0.75,      0.72], #big
    [0,         0,          0,          0,          0,         0], #crystal
    [61.2,      36.65,      28.08,      48.56,      42.92,     41.48], #mulitway

    [0.54,  0.54,   0.54,   0.54,   0.539,  0.539], #clique
    [0, 0, 0, 0, 0, 0],  # psgl
    [0.94,  0.81,   0.75,   0.7,    0.67,   0.65], #big
    [0, 0, 0, 0, 0, 0],  # crystal
    [61.20, 26.2,   5.45,   25.66,  21.97,  9.88], #multiway
]

patterns = {
    'CliqueJoin_h': '++',
    'CliqueJoin_l': '-',
    'StarJoin_h':'',
    'StarJoin_l':'',
    'PSgL_h':'//',
    'PSgL_l':'/',
    'BigJoin_h':'....',
    'BigJoin_l':'..',
    'CystalJoin_h':'\\\\',
    'CystalJoin_l':'\\',
    'MultiwayJoin_h':'xxxx',
    'MultiwayJoin_l':'xx',
}

color = {
    'CliqueJoin_h':'w',
    'CliqueJoin_l':'w',
    'StarJoin_h':'#000000',
    'StarJoin_l':'#000000',
    'PSgL_h':'w',
    'PSgL_l':'w',
    'BigJoin_h':'w',
    'BigJoin_l':'w',
    'CystalJoin_h':'w',
    'CystalJoin_l':'w',
    'MultiwayJoin_h':'w',
    'MultiwayJoin_l':'w',
}
def assign_inf(data):
    inf = 0
    for each_data in data:
        for val in each_data:
            if val != None:
                inf = max(inf, val)
    ten = 10
    while inf * 10 >= ten:
        ten *= 10
    inf = ten

    for each_data in data:
        for i in range(len(each_data)):
            if each_data[i] == 0:
                each_data[i] = 0

    return inf

#
def plot_bar_private(exp, title, graph_title, x_labels, data, is_legend=False):
    plt.figure(figsize=(5, 2.55))
    num_x = len(x_labels)
    num_y = len(algsh)

    width = 0.2
    step = width * (num_y + 2)
    location = np.arange(start=0, stop=num_x * step, step=step)
    print("local", location)
    total_width = step * num_x

    ax = plt.gca()
    # Assign data and x array

    inf = assign_inf(data)

    for i, sub_proj in enumerate(algsh):
        cur_loc = location + i * width
        ax.bar(cur_loc, data[i], tick_label=x_labels, width=width, label=sub_proj, color='w', edgecolor='k',
               hatch=patterns[sub_proj], align="center")

    for i, sub_proj in enumerate(algsl):
        cur_loc = location + i * width
        ax.bar(cur_loc, data[i + 5], tick_label=x_labels, width=width, label=sub_proj, color='#B0B0B0', edgecolor='k',
               hatch=patterns[sub_proj], align="center")


    plt.xticks(location + (num_y / 2.0) * width, fontsize=14);

    # Assign y array
    inf_log = int(np.log10(inf))
    ylocs = []
    yticks = []
    for i in range(inf_log + 1):
        ylocs.append(int(np.power(10, i)))
        if i < inf_log:
            yticks.append("$10^" + str(i) + "$")
        else:
            if exp.endswith('mem'):
                yticks.append("64")

    if not exp.endswith('mem'):
        plt.yscale('log')
        plt.yticks(ylocs, yticks, fontsize=14)
        plt.ylim(0, inf)
    plt.title(graph_title, loc="left")
    plt.savefig('figures/' + exp + '_' + title + '.pdf', fotmat='pdf')

    if is_legend:
        # Plot the legend in a separate figure
        legend_fig = plt.figure(figsize=(total_width * 0.95, 0.4))
        lax = legend_fig.add_subplot(111)
        lax.legend(*ax.get_legend_handles_labels(), ncol=num_y, loc='center', frameon=False)
        lax.axis('off')
        lax.set_frame_on(False)
        plt.savefig('figures/' + exp + '_legend.pdf', fotmat='pdf')

if __name__ == '__main__':
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
    xtic_machines = [3, 6, 12, 18, 24, 30]
    is_legend = True
    for i in scalability_commnunication.keys():
        plot_bar_private('scalability_lj_communication', i, '$C_{max}$ (millions)', xtic_machines, scalability_commnunication[i], is_legend)
        plot_bar_private('scalability_lj_mem', i, '$M_{max}$ (GB)', xtic_machines, scalability_mem[i], is_legend)
        is_legend = False