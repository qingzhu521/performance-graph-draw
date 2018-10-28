import numpy as np
import matplotlib.pyplot as plt
from pylab import *

# Exp-2 Vary Datasets

algs = ['CliqueJoin','PSgL','BigJoin','CystalJoin', 'MultiwayJoin', ]
label_algs = ['CliqueJoin','StarJoin','PSgL', 'BigJoin','CystalJoin', 'MultiwayJoin', 'MultiCFL']

############### unlabelled dataset ####################
vary_dataset_q0 = [
    # GP,       US,      LJ,     OK,     UK02
    [ 0.95,     1.046,   0.8,    2.6,    3],  # cliquejoin
    [111.61,    27.72,   50.12, 133.67,  0],  # psgl
    [ 4.07,     1.08,    3.54,   13.04, 19.63],  # bigjoin
    [ 0,        0,       0,      0,      0],  # crystaljoin
    [155.06,    203.2,  254.41, 750.99, 3225.77],  # multiwayjoin

    [0.89,   1.043,       0.7,       2.6,    2.3,], # clique
    [64.43,  1.01,        18.18,     82.75,  0, ],  # psgl
    [2.86,   0.49,        2.74,      11.67, 19.37, ],  # big
    [0,      0,           0,         0,   0,], #crystal
    [101.4,  153.452,     135.832,    400.65, 3100.33,], #multiwyjoin
]

vary_dataset_q1 = [
    # GP, US,          LJ,     OK,       UK02
    [0,  12.14,       570,    0,          0],            # cliquejoin
    [0,  36.28,       0,      0,          0],               # psgl
    [0,  1.51,        158.5,  1454.72,    2630.75],      # bigjoin
    [0,  0,           0,      0,          0],            # crystaljoin
    [0,  315.03,      1708.81,0,          0],            # multiwayjoin

    [0, 2.1, 297, 0, 0, ],               # cliquejoin
    [0, 4.25, 0, 0, 0, ],                   # psgl
    [0, 0.74, 132.01, 1195.78, 2320.95, ],               # bigjoin
    [0, 0, 0, 0, 0, ],               # crystaljoin
    [0, 241.739, 1610.13, 0, 0, ],               # multiwayjoin
]

vary_dataset_q2 = [
    # GP,       US,     LJ,     OK,     UK02
    [ 206.45,   7.5,        57,     123,    759],       #clique
    [ 0,        26.25,      0, 0, 0],  # psgl
    [ 1678.04,  2.02,       128.96, 379.12, 4027.17],  # big
    [ 0,        0,          0,      0,      0],         #crys
    [ 0,        342.39,     2601,    0,      0],        #multiway

    [166.91,    1.1,    34, 89, 566,], #clique
    [0,         1.02,   0,  0,  0,],
    [1434.41,   0.97,   101.34, 271.97, 2322.92, ], #big
    [0,         0,      0,      0,      0, ],  # crys
    [0,         257.967,2258.24, 0,    0, ],  # multiway
]

vary_dataset_q3 = [
    # GP,      US,      LJ,     OK,     UK02
    [ 47.92,   1.6,     3.3,    8,      23.4],      #clique
    [ 0,       29.41,   0,      0,      0],  # psgl
    [ 301.83,  1.2,     43.19, 105.39, 625.92],  # big
    [ 0,       0,       0,      0,      0],         #crys
    [ 0,       322.97,  1113.85,0,      0],         #multiway

    [47.83,     1.54,   9,        8,    23.1], #clique
    [0,         1.09,   0,        0,    0], #psgl
    [247.48,    0.48,   31.49,    80.64,448.27], #big
    [0,         0,      0,        0,    0], #cry
    [0,         231.732,1021.44,  0,    0], #multiway
]
vary_dataset_q4 = [
    # GP, US,          LJ,     OK,     UK02
    [ 0,  22,          0, 0, 0],  # clique
    [ 0,  39.29,       0, 0, 0],  # psgl
    [ 0,  4.18,        0, 0, 0],  # big
    [ 0,  0,           0,      0,      0],     #crys
    [ 0,  295.17,      0,      0,      0],     #multiway
    [0,     4.2,    0,  0,  0,],
    [0,     8.02,   0,  0,  0,],
    [0,     1.03,   0,  0,  0,],
    [0,     0,      0,  0,  0,],
    [0,     207.077,0,  0,  0,],
]
vary_dataset_q5 = [
    # GP, US,          LJ,     OK,     UK02
    [ 0,  5.7,         0,      0,      0],     #clique
    [ 0,  25.68,       0,      0,      0],  # psgl
    [ 0,  2.45,        0,      0,      0],  # big
    [ 0,  0,           0,      0,      0],     #crys
    [ 0,  250.23,      0,      0,      0],     #multiway
    [ 0,  2.6,          0,0,0,],
    [ 0,  1.08,         0,0,0,],
    [ 0,  0.98,         0,0,0,],
    [ 0,  0,            0,0,0,],
    [ 0,  165.475,      0,0,0,],

]
vary_dataset_q6 = [
    # GP,      US,         LJ,     OK,     UK02
    [ 2835.24, 2.3,        99,     43.6,      1253],   #clique
    [ 0,       27.11,      0,      0,         0],  # psgl
    [ 0,       1.22,       1996.52, 622.47,   0],  # big
    [ 0,       0,          0,      0,         0],      #crys
    [ 0,       240.1,      0,      0,         0],      #multiway

    [2835.23,2.28,69,41,1189,],
    [0,0.17,0,0,0,],
    [0,0.48,1363.66,450.96,0,],
    [0,0,0,0,0,],
    [0,140.554,0,0,0,],
]
vary_dataset_q7 = [
    #  GP,     US,           LJ,     OK,     UK02
    [ 0,    12.2,           0,      0,      0],       #clique
    [ 0,    26.81,          0,      0,   0],  # psgl
    [ 0,    4.52,             0, 0, 0],  # big
    [ 0,    0,              0,      0,      0],       #crys
    [ 0,    460.1,          0,      0,      0],       #multiway

    [0,1.2,             0,0,0,],
    [0,2.03,            0,0,0,],
    [0,1.99,            0,0,0,],
    [0,0,               0,0,0,],
    [0,271.94,          0,0,0,],
]
vary_dataset_q8 = [
    # GP, US,              LJ,     OK,     UK02
    [  0, 3.2,             4671,   106,    0],        #clique
    [  0, 26.71,           0,      0,      0],  # psgl
    [  0, 1.3,             0,      0,      0],  # big
    [  0, 0,               0,      0,      0],        #crys
    [  0, 556.1,           0,      0,      0],        #multiway


    [0,     3.18,       2657,       102,        0,],
    [0,     0.08,       0,      0,          0,],
    [0,     0.48,       0,      2451.15,    0,],
    [0,     0,          0,      0,      0,],
    [0,     273.122,    0,      0,      0,],
]
vary_dataset_q9 = [
    # GP,   US,               LJ,     OK,     UK02
    [ 0,    12.77,              0,      0,      0],       #clique
    [ 0,    27.78,            0,      0,      0],  # psgl
    [ 0,    4.18,             0,      0,      0],  # big
    [ 0,    0,                0,      0,      0],       #crys
    [ 0,    251.11,           0,      0,      0],       #multiway

    [0,     1.1,        0,0,0,],
    [0,     2.09,       0,0,0,],
    [0,     1.97,       0,0,0,],
    [0,     0,          0,0,0,],
    [0,     192.21,     0,0,0,],
]

vary_query_gp = [
    # q0    1       2           3       4       5       6       7       8   9
    [0.95,    0,    206.45,    47.92,    0,    0,    2835.24,    0,    0,    0,],#clique
    [111.61,    0,    0,    0,    0,    0,    0,    0,    0,    0,],#psgl
    [4.07, 0, 1678.04, 301.83, 0, 0, 0, 0, 0, 0, ],  # bigjoin
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],  # crys
    [155.06,    0,    0,    0,    0,    0,    0,    0,    0,    0,],#multiway

]
vary_query_us = [
    # q0    1       2           3       4       5       6       7       8   9
    [1.046, 12.14, 7.5, 1.6, 22, 5.7, 2.3, 12.2, 3.2, 413, ], #clique
    [27.72, 36.28, 26.25, 29.41, 39.29, 25.68, 27.11, 26.81, 26.71, 27.78, ],  # psgl
    [1.08, 1.51, 2.02, 1.2, 4.18, 2.45, 1.22, 4.52, 1.3, 4.18, ],  # big
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], #crystal
    [203.2, 315.03, 342.39, 322.97, 295.17, 250.23, 240.1, 460.1, 556.1, 251.11, ], #multiway
]

############### labelled dataset ####################
labelled_dataset_q0 = [
    # DG01 DG03 DG10 DG30 DG60
    [0.45, 1.46, 4.52, 14.29, 35.52], #clique
    [0.45, 1.46, 4.52, 14.29, 35.52], # star
    [21.11, 36.12, 68.1, 127.79, 0],  # psgl
    [1.12, 1.35, 9.69, 27.39, 14.93],  # bigjoin
    [0, 0, 0, 0, 0],  # crystal
    [99.81, 506.43, 0, 0, 0], # multiway
    [23.11, 30.85, 58.11, 168.38, 388.16,], #multicfl

    [0.42, 1.46, 4.52, 14.28, 34.92, ], #clique
    [0.42, 1.46, 4.52, 14.28, 34.92, ], #star
    [0.01, 0.18, 1.04, 6.04, 0,],     #psgl
    [0.05, 0.18, 0.71, 2.86, 7.52,], #big
    [0,     0,      0,    0,    0,], #crystal
    [54.19, 426.99, 0,    0,    0,], #multiway
    [23.11, 30.85, 58.11, 168.38, 388.16, ],  # multicfl
]
labelled_dataset_q1 = [
    [12.84,	127.77,	2013.06,	0,	0], #clique
    [12.84,	127.77,	2013.06,	0,	0], #star
    [27.82, 44.85, 112.26, 304.95, 0],  # psgl
    [3.09, 6.42, 18.65, 57.73, 121.11],  # big
    [0, 0, 0, 0, 0],  # crystal
    [3.19,	100.72,	922.56, 1077.7, 0], #multiay
    [18.06, 22.67, 35.13, 67.28, 157.42], #multiwaycfl

    [12.53, 126.58, 2008.97,    0,    0,],
    [12.53, 126.58, 2008.97,    0,    0,],
    [0.68,  1.99,   6.87,   22.47,  0,],
    [1.98,  5.21,   17.07,  54.99,  110.23,],
    [0,  0,   0,   0,   0,],
    [2.177, 11.02,  8.63371,    795.429,    0,],
    [18.06, 22.67, 35.13, 67.28, 157.42],  # multiwaycfl
]

labelled_dataset_q2 = [
    [0.46,1.48,5.62,19.14,53.44], #clique
    [5.23,21.61,83.79,263.48,0], #star
    [33.27, 52.99, 109.45, 306.86, 720.05],  # psgl
    [1.73, 4.2, 17.61, 75.02, 255.78],  # big
    [0, 0, 0, 0, 0],  # crs
    [21.91,32.14,56.86,145.97,0], #multway
    [21.63,29.63,48.8,146.27,402.93], #multiwycfl

    [0.44,  1.48,   5.62,   19.14,  53.43 ],
    [3.3,   12.11,  60.51,  222.56, 0],
    [0.09,  1.19,   5.96,   23.47,  0],
    [0.67,  2.99,   16.13,  72.39,  247.61],
    [0,  0,   0,   0,   0,],
    [1.36,  5.1,    67.59,  65.27,  381.64],
    [18.06, 22.67, 35.13, 67.28, 157.42],  # multiwaycfl
    [21.63, 29.63, 48.8, 146.27, 402.93],  # multiwycfl
]
labelled_dataset_q3 = [
    [12.24,54.63,169.14,0,0,], #clique
    [12.24,54.63,169.14,0,0,], #star
    [47.2, 104.55, 0, 0, 0, ],  # psgl
    [131.19, 669.76, 4630.83, 0, 0, ],  # big
    [0, 0, 0, 0, 0, ],  # crs
    [105.17,447.19,0,0,0,], #multiway
    [0,0,0,0,0], #multicfl

    [6.44,27.85,132.57,0,0],
    [6.44,27.85,132.57,0,0],
    [12,52.37,0,0,0],
    [120.75,629.39,4448.2,0,0],
    [0,0,0,0,0],
    [52.88,317.63,0,0,0],
    [0, 0, 0, 0, 0],  # multicfl
]

labelled_dataset_q4 = [
    [499.38,2384.96,5873.22,0,0], #clique
    [499.38,2384.96,5873.22,0,0], #star
    [181.32, 0, 0, 0, 0],  # psgl
    [78.37, 381.04, 1013.16, 3405.27, 8315.56],  # big
    [0, 0, 0, 0, 0],  # crs
    [201.99, 1146.06, 0, 0, 0],  # multiway
    [29.56, 63.7, 178.48, 603.59, 1417.19],  # multiwaycfl

    [499.37,2384.95,5873.21,0,0,],
    [499.37,2384.95,5873.21,0,0,],
    [53.98,0,0,0,0,],
    [69.15,342.81,885.15,3038.39,7430.86,],
    [0,0,0,0,0,],
    [161.88,1051.5,0,0,0,],
    [29.56, 63.7, 178.48, 603.59, 1417.19],  # multiwaycfl
]

labelled_dataset_q5 = [
    [0.74,2.05,6.83,21.11,43.86], #clique
    [0.74,2.05,6.83,21.11,43.86], #star
    [21.87, 32.79, 84.19, 223.56, 0],  # psgl
    [2.61, 6.14, 28.96, 125.22, 419.64],  # big
    [0, 0, 0, 0, 0], #crs
    [48.42, 69.05, 241.08, 508.78, 1555.33],  # multiway
    [210.27,    1634.61,64.46,280.12,850.52], #multiwaycfl

    [0.6,1.76, 5.72, 17.32, 37.13,],
    [0.6,1.76, 5.72, 17.32, 37.13,],
    [0.04,2.05, 11.43, 49.64, 0,],
    [1.04,4.91, 27.23, 121.96, 411.5,],
    [0,0, 0, 0, 0,],
    [3.98,1.48, 8.35, 254.749, 916.436,],
    [210.27, 1634.61, 64.46, 280.12, 850.52],  # multiwaycfl
]
labelled_dataset_q6 = [
    [1.16,3.85,15.08,54.69,177.69,], #clique
    [982,3544.03,0,0,0,], #star
    [52.49, 112.07, 306.42, 250.44, 807.09, ],  # psgl
    [1.08, 1.16, 1.49, 2.88, 7.04, ],  # big
    [0, 0, 0, 0, 0, ],  # crs
    [22.28,27.91,51.46,122.62,0,], #multiway
    [20.67, 26.01, 51.25, 136.38, 415.75], #multiwaycfl

    [1.13, 3.81, 15.03, 54.6, 177.5,],
    [980.4, 3535.56, 0, 0, 0,],
    [0.07, 0.04, 0.04, 2.07, 0,],
    [0.01, 0.03, 0.17, 0.98, 4.24,],
    [0, 0, 0, 0, 0,],
    [10.45, 3.35, 10.975, 46.2638, 115.661,],
    [20.67, 26.01, 51.25, 136.38, 415.75],  # multiwaycfl
]

labelled_dataset_q7 = [
    [1.24,3.86,14.63,66.97,240.47], #cli
    [3.64,36.47,732.75,0,0], #star
    [20.33, 47.03, 235.92, 2331.5, 0],  # psgl
    [1.55, 7.06, 82.53, 980.91, 6607.21],  # big
    [0, 0, 0, 0, 0],  # crs
    [134.56, 356.33, 1264.34, 0, 0],  # multi
    [22.86,31.6,144.55, 1887.29,0], #multiwaycfl

    [1.16, 3.72, 14.22, 65.71, 238.3,],
    [2.69, 18.86, 297.14, 0, 0,],
    [0.1, 2.65, 54.44, 850.16, 0,],
    [0.46, 5.77, 79.31, 960.84, 6520.95,],
    [0, 0, 0, 0, 0,],
    [16.44, 8.82, 167.536, 0, 0,],
    [22.86, 31.6, 144.55, 1887.29, 0],  # multiwaycfl
]
labelled_dataset_q8 = [
    [1.35,      4.29,       16.27,   55.63,  134.9], #clf
    [1000.7,    3642.74,        0,        0,    0], #star
    [27.4,      58.95,     219.45,    932.3,    0], #psgl
    [681.84,    7265.93,        0,        0,    0], #big
    [0,         0 ,      0 ,      0 ,   0], #crs
    [53.26,     138.1,      826.88,     6702,   0], #multi
    [33.14,     81.89,      796.34,     0,      0], #multwaycfl
    [1.13, 3.55, 12.61, 39.94, 100.1,],
    [984.28, 3558.21, 0, 0, 0,],
    [5.01, 23.91, 128.6, 658.42, 0,],
    [680.12, 7262.55, 0, 0, 0,],
    [0, 0, 0, 0, 0,],
    [8.7, 69.801, 664.39, 6279.73, 0,],
    [33.14, 81.89, 796.34, 0, 0],  # multwaycfl
]


############### program ##############
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
                each_data[i] = 0

    return inf

patterns = {
    'CliqueJoin': '',
    'StarJoin': '-',
    'PSgL':'//',
    'BigJoin':'..',
    'CystalJoin':'\\\\',
    'MultiwayJoin':'xx',
    'MultiCFL': '*'
}
color = {
    'CliqueJoin':'w',
    'StarJoin':'w',
    'PSgL':'w',
    'BigJoin':'w',
    'CystalJoin':'w',
    'MultiwayJoin':'w',
    'MultiCFL': 'w',
}
revcolor = {
    'CliqueJoin':'#E5E5E5',
    'StarJoin':'#E5E5E5',
    'PSgL':'#E5E5E5',
    'BigJoin':'#E5E5E5',
    'CystalJoin':'#E5E5E5',
    'MultiwayJoin':'#E5E5E5',
    'MultiCFL': '#E5E5E5',
}

#algs = ['CliqueJoin','PSgL','BigJoin','CystalJoin', 'MultiwayJoin', ]
#label_algs = ['CliqueJoin','StarJoin','PSgL', 'BigJoin','CystalJoin', 'MultiwayJoin', ]
### 实现名称， 数据集合名称， 第一横坐标（数据集），第二横坐标（算法），（数据集，算法）- 时间
def plot_bar(exp, title, x_labels, project, data, is_legend=False):
    plt.figure(figsize=(5,2.55))
    num_x = len(x_labels)
    num_y = len(project)

    width = 0.2
    step = width * (num_y + 2)
    location = np.arange(start=0, stop=num_x * step, step=step)
    print("local",location)
    total_width = step * num_x

    ax = plt.gca()
    # Assign data and x array
    inf = assign_inf(data)
    for i, sub_proj in enumerate(project):
        cur_loc = location + i * width
        print("cur ",cur_loc,i, data[i])
        ax.bar(cur_loc, data[i], tick_label=x_labels, width=width, label=sub_proj, color=color[sub_proj], edgecolor='k',
               hatch=patterns[sub_proj], align="center")
        if exp.endswith("dataset"):
            ax.bar(cur_loc, data[i + num_y], tick_label=x_labels, width=width, label=sub_proj, color=revcolor[sub_proj], edgecolor='k',
                   hatch=patterns[sub_proj], align="center")
        for j, eachd in enumerate(data[i]):
            if eachd != 0 and eachd < 0.1:
                ax.text(cur_loc[j] - 0.12, eachd, str(eachd),  fontsize='8', fontweight='bold',va ='bottom', rotation=90)

    cur_loc = location + len(project) * width - 0.1
    array = [inf,]*num_x
    ax.bar(cur_loc, array, tick_label=x_labels, width=0, edgecolor='#B5B5B5', align="edge", ls=':',lw=0.4)

    plt.xticks(location + (num_y/2.0) * width, fontsize=14);

    # Assign y array
    inf_log = int(np.log10(inf))
    plt.yscale('log')
    ylocs = []
    yticks = []
    for i in range(inf_log + 1):
        ylocs.append(int(np.power(10, i)))
        if i < inf_log:
            yticks.append("$10^" + str(i) + "$")
        else:
            yticks.append("$10^" + str(i) + "$")
    plt.yticks(ylocs, yticks, fontsize=14)
    plt.ylim(0, inf)
    plt.title("T (sec)",loc="left")
    #plt.show()
    plt.savefig('figures/' + exp + '_' + title + '.pdf', fotmat='pdf')

    if is_legend:
        # Plot the legend in a separate figure
        legend_fig = plt.figure(figsize=(total_width, 0.2))
        lax = legend_fig.add_subplot(111)
        lax.legend(*ax.get_legend_handles_labels(), ncol=num_y, loc='center', frameon=False)
        lax.axis('off')
        lax.set_frame_on(False)
        plt.savefig('figures/' + exp + '_legend.pdf', fotmat='pdf')



if __name__ == '__main__':
############### unlabelled #####################
    vary_dataset_queries = {
        'q0': vary_dataset_q0,
        'q1': vary_dataset_q1,
        'q2': vary_dataset_q2,
        'q3': vary_dataset_q3,
        'q4': vary_dataset_q4,
        'q5': vary_dataset_q5,
        'q6': vary_dataset_q6,
        'q7': vary_dataset_q7,
        'q8': vary_dataset_q8,
        'q9': vary_dataset_q9,
    }

    vary_dataset_datasets = ['GP', 'US', 'LJ', 'OK', 'UK']
    is_legend = True
    #plot_bar('vary_data_q0dataset', 'q0', vary_dataset_datasets, algs, vary_dataset_q0, True);
    for name in vary_dataset_queries.keys():
        #plot_bar('vary_dataset', name, vary_dataset_datasets, algs, vary_dataset_queries[name], is_legend)
        plt.close()
        is_legend = False

############### labelled #####################
    vary_labelled_queries = {
        'q0': labelled_dataset_q0,
        'q1': labelled_dataset_q1,
        'q2': labelled_dataset_q2,
        'q3': labelled_dataset_q3,
        'q4': labelled_dataset_q4,
        'q5': labelled_dataset_q5,
        'q6': labelled_dataset_q6,
        'q7': labelled_dataset_q7,
        'q8': labelled_dataset_q8
    }
    vary_labelled_datasets = ['DG01', 'DG03', 'DG10', 'DG30', 'DG60']
    is_legend = True
    for name in vary_labelled_queries.keys():
        plot_bar('vary_labelled_dataset', name, vary_labelled_datasets, label_algs, vary_labelled_queries[name], is_legend)
        plt.close()
        is_legend = False


    var_query_datasets = {
        'GP': vary_query_gp,
        'US': vary_query_us,
    }
    xlabel = ['q0','q1','q2','q3','q4','q5','q6','q7','q8','q9']
    is_legend = True
    for name in var_query_datasets.keys():
        #plot_bar('vary_queries', name, xlabel, algs, var_query_datasets[name],is_legend)
        plt.close()
        is_legend = False