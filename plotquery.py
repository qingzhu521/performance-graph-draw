import numpy as np
import matplotlib.pyplot as plt
from pylab import *

# Exp-2 Vary Datasets

algs = ['CliqueJoin', 'PSgL', 'BigJoin', 'CystalJoin', 'MultiwayJoin', ]
label_algs = ['CliqueJoin', 'StarJoin', 'PSgL', 'BigJoin', 'CystalJoin', 'MultiwayJoin', 'MultiCFL']

############### unlabelled dataset ####################
vary_dataset_q0 = [
    # GP,         US,        LJ,       OK,       UK02
    [0.95, 1.046, 0.8, 2.6, 3, ],  # cliquejoin
    [111.61, 27.72, 50.12, 133.67, None, ],  # psgl
    [4.07, 1.08, 3.54, 13.04, 19.63, ],  # bigjoin
    [None, None, None, None, None, ],  # crystaljoin
    [155.06, 203.2, 254.41, 750.99, 3225.77, ],  # multiwayjoin

    [0.89, 1.043, 0.7, 2.6, 2.3, ],  # clique
    [64.43, 1.01, 18.18, 82.75, None, ],  # psgl
    [2.86, 0.49, 2.74, 11.67, 19.37, ],  # big
    [None, None, None, None, None, ],  # crystal
    [101.4, 153.452, 135.832, 400.65, 3100.33, ],  # multiwyjoin
]

vary_dataset_q1 = [
    # GP,   US,            LJ,       OK,         UK02
    [None, 12.14, 570, None, None, ],  # cliquejoin
    [None, 36.28, None, None, None, ],  # psgl
    [None, 1.51, 158.5, 1454.72, 2630.75, ],  # bigjoin
    [None, None, None, None, None, ],  # crystaljoin
    ["Timeout", 315.03, 1708.81, "Timeout", "Timeout", ],  # multiwayjoin

    [None, 2.1, 297, None, None, ],  # cliquejoin
    [None, 4.25, None, None, None, ],  # psgl
    [None, 0.74, 132.01, 1195.78, 2320.95, ],  # bigjoin
    [None, None, None, None, None, ],  # crystaljoin
    ["Timeout", 241.739, 1610.13, "Timeout", "Timeout", ],  # multiwayjoin
]

vary_dataset_q2 = [
    # GP,         US,       LJ,       OK,       UK02
    [206.45, 7.5, 57, 123, 759, ],  # clique
    [None, 26.25, None, None, None, ],  # psgl
    [1678.04, 2.02, 128.96, 379.12, 4027.17, ],  # big
    [None, None, None, None, None, ],  # crys
    ["Timeout", 342.39, 2601, "Timeout", "Timeout", ],  # multiway

    [166.91, 1.1, 34, 89, 566, ],  # clique
    [None, 1.02, None, None, None, ],
    [1434.41, 0.97, 101.34, 271.97, 2322.92, ],  # big
    [None, None, None, None, None, ],  # crys
    ["Timeout", 257.967, 2258.24, "Timeout", "Timeout", ],  # multiway
]

vary_dataset_q3 = [
    # GP,        US,        LJ,       OK,       UK02
    [47.92, 1.6, 3.3, 8, 23.4, ],  # clique
    [None, 29.41, None, None, None, ],  # psgl
    [301.83, 1.2, 43.19, 105.39, 625.92, ],  # big
    [None, None, None, None, None, ],  # crys
    ["Timeout", 322.97, 1113.85, "Timeout", "Timeout", ],  # multiway

    [47.83, 1.54, 9, 8, 23.1, ],  # clique
    [None, 1.09, None, None, None, ],  # psgl
    [247.48, 0.48, 31.49, 80.64, 448.27],  # big
    [None, None, None, None, None, ],  # cry
    ["Timeout", 231.732, 1021.44, "Timeout", "Timeout", ],  # multiway
]
vary_dataset_q4 = [
    # GP,   US,            LJ,       OK,       UK02
    [None, 22, None, None, None, ],  # clique
    [None, 39.29, None, None, None, ],  # psgl
    [None, 4.18, "Timeout", None, "Timeout", ],  # big
    [None, None, None, None, "Timeout", ],  # crys
    ["Timeout", 295.17, "Timeout", "Timeout", "Timeout", ],  # multiway

    [None, 4.2, None, None, None, ],
    [None, 8.02, None, None, None, ],
    [None, 1.03, "Timeout", None, None, ],
    [None, None, None, None, "Timeout", ],
    ["Timeout", 207.077, "Timeout", "Timeout", "Timeout", ],
]
vary_dataset_q5 = [
    # GP,               US,            LJ,       OK,       UK02
    [None, 5.7, None, None, None, ],  # clique
    [None, 25.68, None, None, None, ],  # psgl
    [None, 2.45, None, "Timeout", "Timeout", ],  # big
    ["Timeout", None, "Timeout", None, "Timeout", ],  # crys
    ["Timeout", 250.23, "Timeout", "Timeout", "Timeout", ],  # multiway

    [None, 2.6, None, None, None, ],  # clique
    [None, 1.08, None, None, None, ],  # psgl
    [None, 0.98, None, "Timeout", "Timeout", ],  # big
    ["Timeout", None, "Timeout", None, "Timeout", ],  # crys
    ["Timeout", 165.475, "Timeout", "Timeout", "Timeout", ],  # multiway

]
vary_dataset_q6 = [
    # GP,           US,           LJ,       OK,       UK02
    [2835.24, 2.3, 99, 43.6, 1253, ],  # clique
    [None, 27.11, None, "Timeout", None, ],  # psgl
    [None, 1.22, 1996.52, 622.47, "Timeout", ],  # big
    [None, None, None, None, "Timeout", ],  # crys
    ["Timeout", 240.1, "Timeout", "Timeout", "Timeout", ],  # multiway

    [2835.23, 2.28, 69, 41, 1189, ],
    [None, 0.17, None, "Timeout", None, ],
    [None, 0.48, 1363.66, 450.96, "Timeout", ],
    [None, None, None, None, "Timeout", ],
    ["Timeout", 140.554, "Timeout", "Timeout", "Timeout", ],
]
vary_dataset_q7 = [
    #  GP,       US,             LJ,       OK,       UK02
    [None, 12.2, None, None, None, ],  # clique
    [None, 26.81, None, "Timeout", None, ],  # psgl
    [None, 4.52, None, None, None, ],  # big
    [None, None, None, None, None, ],  # crys
    ["Timeout", 460.1, "Timeout", "Timeout", "Timeout", ],  # multiway

    [None, 1.2, None, None, None, ],
    [None, 2.03, None, "Timeout", None, ],
    [None, 1.99, None, None, None, ],
    [None, None, None, None, None, ],
    ["Timeout", 271.94, "Timeout", "Timeout", "Timeout", ],
]
vary_dataset_q8 = [
    # GP,           US,                LJ,           OK,       UK02
    ["Timeout", 3.2, 4671, 106, "Timeout", ],  # clique
    [None, 26.71, None, "Timeout", None, ],  # psgl
    [None, 1.3, "Timeout", None, None, ],  # big
    [None, None, None, None, None, ],  # crys
    ["Timeout", 556.1, "Timeout", "Timeout", "Timeout", ],  # multiway

    [None, 3.18, 2657, 102, "Timeout", ],  # clique
    [None, 0.08, None, None, None, ],  # psgl
    [None, 0.48, "Timeout", 2451.15, None, ],  # big
    [None, None, None, None, None, ],  # crys
    ["Timeout", 273.122, "Timeout", "Timeout", "Timeout", ],  # multiway
]
vary_dataset_q9 = [
    # GP,     US,                 LJ,       OK,       UK02
    [None, 12.77, None, None, None, ],  # clique
    [None, 27.78, None, None, None, ],  # psgl
    [None, 4.18, "Timeout", None, None, ],  # big
    ["Timeout", None, None, "Timeout", "Timeout", ],  # crys
    ["Timeout", 251.11, "Timeout", "Timeout", "Timeout", ],  # multiway

    [None, 1.1, None, None, None, ],  # clique
    [None, 2.09, None, None, None, ],  # psgl
    [None, 1.97, "Timeout", None, None, ],  # big
    ["Timeout", None, None, None, "Timeout", ],  # crys
    ["Timeout", 192.21, "Timeout", "Timeout", "Timeout", ],  # multiway
]

vary_query_gp = [
    # q0        1           2           3       4       5       6       7       8   9
    [0.95, None, 206.45, 47.92, None, None, 2835.24, None, None, None, ],
    # clique
    [111.61, None, None, None, None, None, None, None, None, None, ],
    # psgl
    [4.07, None, 1678.04, 301.83, None, None, None, None, None, None, ],  # bigjoin
    [None, None, None, None, None, None, None, None, None, None, ],  # crys
    [155.06, 'Timeout', 'Timeout', 'Timeout', 'Timeout', 'Timeout', 'Timeout', 'Timeout', 'Timeout', 'Timeout', ],
    # multiway

]
vary_query_us = [
    # q0    1       2           3       4       5       6       7       8   9
    [1.046, 12.14, 7.5, 1.6, 22, 5.7, 2.3, 12.2, 3.2, 413, ],  # clique
    [27.72, 36.28, 26.25, 29.41, 39.29, 25.68, 27.11, 26.81, 26.71, 27.78, ],  # psgl
    [1.08, 1.51, 2.02, 1.2, 4.18, 2.45, 1.22, 4.52, 1.3, 4.18, ],  # big
    [None, None, None, None, None, None, None, None, None, None, ],  # crystal
    [203.2, 315.03, 342.39, 322.97, 295.17, 250.23, 240.1, 460.1, 556.1, 251.11, ],  # multiway
]

############### labelled dataset ####################
labelled_dataset_q0 = [
    # DG01  DG03        DG10     DG30    DG60
    [0.45, 1.46, 4.52, 14.29, 35.52, ],  # clique
    [0.45, 1.46, 4.52, 14.29, 35.52, ],  # star
    [21.11, 36.12, 68.1, 127.79, None, ],  # psgl
    [1.12, 1.35, 9.69, 27.39, 14.93, ],  # bigjoin
    [None, None, None, None, None, ],  # crystal
    [99.81, 506.43, "Timeout", "Timeout", "Timeout", ],  # multiway
    [4.19, 13.22, 43.26, 141.87, 258.11, ],  # multicfl

    [0.42, 1.46, 4.52, 14.28, 34.92, ],  # clique
    [0.42, 1.46, 4.52, 14.28, 34.92, ],  # star
    [0.01, 0.18, 1.04, 6.04, None, ],  # psgl
    [0.05, 0.18, 0.71, 2.86, 7.52, ],  # big
    [None, None, None, None, None, ],  # crystal
    [54.19, 426.99, "Timeout", "Timeout", "Timeout", ],  # multiway
    [4.19, 13.22, 43.26, 141.87, 258.11, ],  # multicfl
]
labelled_dataset_q1 = [
    [12.84, 127.77, 2013.06, "Timeout", "Timeout", ],  # clique
    [12.84, 127.77, 2013.06, "Timeout", "Timeout", ],  # star
    [27.82, 44.85, 112.26, 304.95, None, ],  # psgl
    [3.09, 6.42, 18.65, 57.73, 121.11, ],  # big
    [None, None, None, None, None, ],  # crystal
    [3.19, 100.72, 922.56, 1077.7, "Timeout", ],  # multiay
    [0.66, 2.34, 8.09, 26.35, 46.37, ],  # multiwaycfl

    [12.53, 126.58, 2008.97, "Timeout", "Timeout", ],
    [12.53, 126.58, 2008.97, "Timeout", "Timeout", ],
    [0.68, 1.99, 6.87, 22.47, None, ],
    [1.98, 5.21, 17.07, 54.99, 110.23, ],
    [None, None, None, None, None, ],
    [2.177, 11.02, 8.63371, 795.429, "Timeout", ],
    [0.66, 2.34, 8.09, 26.35, 46.37, ],  # multiwaycfl
]

labelled_dataset_q2 = [
    [0.46, 1.48, 5.62, 19.14, 53.44, ],  # clique
    [5.23, 21.61, 83.79, 263.48, None, ],  # star
    [21.91, 32.14, 56.86, 145.97, None, ],  # psgl
    [1.73, 4.2, 17.61, 75.02, 255.78, ],  # big
    [None, None, None, None, None, ],  # crs
    [33.27, 52.99, 109.45, 306.86, 720.05, ],  # multiway
    [2.74, 10.45, 48.8, 171.13, 477.11, ],  # multiwycfl

    [0.44, 1.48, 5.62, 19.14, 53.43, ],  # clique
    [3.3, 12.11, 60.51, 222.56, None, ],  # star
    [0.09, 1.19, 5.96, 23.47, None, ],  # pslg
    [0.67, 2.99, 16.13, 72.39, 247.61, ],  # big
    [None, None, None, None, None, ],
    [1.36, 5.1, 67.59, 65.27, 381.64, ],
    [18.06, 22.67, 35.13, 67.28, 157.42, ],  # multiway
    [2.74, 10.45, 48.8, 171.13, 477.11, ],  # multiwycfl
]
labelled_dataset_q3 = [
    [12.24, 54.63, 169.14, None, None, ],  # clique
    [12.24, 54.63, 169.14, None, None, ],  # star
    [47.2, 104.55, None, None, None, ],  # psgl
    [131.19, 669.76, 4630.83, "Timeout", "Timeout", ],  # big
    [None, None, None, None, None, ],  # crs
    [105.17, 447.19, "Timeout", "Timeout", "Timeout", ],  # multiway
    [38.88, 278.46, 1647.96, "Timeout", "Timeout", ],  # multicfl

    [6.44, 27.85, 132.57, None, None, ],  # clique
    [6.44, 27.85, 132.57, None, None, ],  # star
    [12, 52.37, None, None, None, ],  # psgl
    [120.75, 629.39, 4448.2, "Timeout", "Timeout", ],  # big
    [None, None, None, None, None, ],  # crs
    [52.88, 317.63, "Timeout", "Timeout", "Timeout", ],  # multiway
    [38.88, 278.46, 1647.96, "Timeout", "Timeout", ],  # multicfl
]

labelled_dataset_q4 = [
    [499.38, 2384.96, 5873.22, "Timeout", "Timeout", ],  # clique
    [499.38, 2384.96, 5873.22, "Timeout", "Timeout", ],  # star
    [181.32, None, None, None, None, ],  # psgl
    [78.37, 381.04, 1013.16, 3405.27, 8315.56],  # big
    [None, None, None, None, None, ],  # crs
    [201.99, 1146.06, "Timeout", "Timeout", "Timeout", ],  # multiway
    [3.72, 12.68, 57.25, 198.51, 468.19],  # multiwaycfl

    [499.37, 2384.95, 5873.21, "Timeout", "Timeout", ],
    [499.37, 2384.95, 5873.21, "Timeout", "Timeout", ],
    [53.98, None, None, None, None, ],
    [69.15, 342.81, 885.15, 3038.39, 7430.86, ],
    [None, None, None, None, None, ],
    [161.88, 1051.5, "Timeout", "Timeout", "Timeout", ],
    [3.72, 12.68, 57.25, 198.51, 468.19],  # multiwaycfl
]

labelled_dataset_q5 = [
    [0.74, 2.05, 6.83, 21.11, 43.86],  # clique
    [0.74, 2.05, 6.83, 21.11, 43.86],  # star
    [21.87, 32.79, 84.19, 223.56, 0],  # psgl
    [2.61, 6.14, 28.96, 125.22, 419.64],  # big
    [None, None, None, None, None, ],  # crs
    [48.42, 69.05, 241.08, 508.78, 1555.33],  # multiway
    [0.93, 4.28, 34.86, 167.38, 586.72],  # multiwaycfl

    [0.6, 1.76, 5.72, 17.32, 37.13, ],
    [0.6, 1.76, 5.72, 17.32, 37.13, ],
    [0.04, 2.05, 11.43, 49.64, None, ],
    [1.04, 4.91, 27.23, 121.96, 411.5, ],
    [None, None, None, None, None, ],
    [3.98, 1.48, 8.35, 254.749, 916.436, ],
    [0.93, 4.28, 34.86, 167.38, 586.72],  # multiwaycfl
]
labelled_dataset_q6 = [
    [1.16, 3.85, 15.08, 54.69, 177.69, ],  # clique
    [982, 3544.03, "Timeout", "Timeout", "Timeout", ],  # star
    [22.28, 27.91, 51.46, 122.62, None, ],  # psgl
    [1.08, 1.16, 1.49, 2.88, 7.04, ],  # big
    [None, None, None, None, None, ],  # crs
    [52.49, 112.07, 306.42, 250.44, 807.09, ],  # multiway
    [0.65, 1.89, 7.07, 24.02, 57.76],  # multiwaycfl

    [1.13, 3.81, 15.03, 54.6, 177.5, ],
    [980.4, 3535.56, "Timeout", "Timeout", "Timeout", ],
    [0.07, 0.04, 0.04, 2.07, None, ],
    [0.01, 0.03, 0.17, 0.98, 4.24, ],
    [None, None, None, None, None, ],
    [10.45, 3.35, 10.975, 46.2638, 115.661, ],
    [0.65, 1.89, 7.07, 24.02, 57.76],  # multiwaycfl
]

labelled_dataset_q7 = [
    [1.24, 3.86, 14.63, 66.97, 240.47, ],  # cli
    [3.64, 36.47, 732.75, None, None, ],  # star
    [20.33, 47.03, 235.92, 2331.5, None, ],  # psgl
    [1.55, 7.06, 82.53, 980.91, 6607.21, ],  # big
    [None, None, None, None, None, ],  # crs
    [134.56, 356.33, 1264.34, "Timeout", "Timeout", ],  # multi
    [1.34, 9.98, 175.72, 2256.48, "Timeout", ],  # multiwaycfl

    [1.16, 3.72, 14.22, 65.71, 238.3, ],
    [2.69, 18.86, 297.14, None, None, ],
    [0.1, 2.65, 54.44, 850.16, None, ],
    [0.46, 5.77, 79.31, 960.84, 6520.95, ],
    [None, None, None, None, None, ],
    [16.44, 8.82, 167.536, "Timeout", "Timeout", ],
    [1.34, 9.98, 175.72, 2256.48, "Timeout", ],  # multiwaycfl
]
labelled_dataset_q8 = [
    [1.35, 4.29, 16.27, 55.63, 134.9, ],  # clique
    [1000.7, 3642.74, "Timeout", "Timeout", "Timeout", ],  # star
    [27.4, 58.95, 219.45, 932.3, None, ],  # psgl
    [681.84, 7265.93, "Timeout", "Timeout", "Timeout", ],  # big
    [None, None, None, None, None, ],  # crs
    [53.26, 138.1, 826.88, 6702, "Timeout", ],  # multi
    [8.2, 67.13, 665.73, 5651.29, "Timeout", ],  # multwaycfl

    [1.13, 3.55, 12.61, 39.94, 100.1, ],  # clique
    [984.28, 3558.21, "Timeout", "Timeout", "Timeout", ],  # star
    [5.01, 23.91, 128.6, 658.42, None, ],  # psgl
    [680.12, 7262.55, "Timeout", "Timeout", "Timeout", ],  # big
    [None, None, None, None, None, ],  # crystal
    [8.7, 69.801, 664.39, 6279.73, "Timeout", ],  # multiway
    [8.2, 67.13, 665.73, 5651.29, "Timeout", ],  # multwaycfl
]


############### program ##############
def assign_inf(data):
    inf = 0
    for each_data in data:
        for val in each_data:
            if val is not None and val != 'Timeout':
                inf = max(inf, val)
    ten = 10
    while inf * 10 >= ten:
        ten *= 10
    inf = ten

    inf_log = int(np.log10(inf)) - 1
    xinf = int(np.power(10, inf_log + 0.5))
    for each_data in data:
        for i in range(len(each_data)):
            if each_data[i] == "Timeout":
                each_data[i] = xinf
            elif each_data[i] is None:
                each_data[i] = 0.1

    return inf


patterns = {
    'CliqueJoin': '',
    'StarJoin': '-',
    'PSgL': '//',
    'BigJoin': '..',
    'CystalJoin': '\\\\',
    'MultiwayJoin': 'xx',
    'MultiCFL': '*'
}
revcolor = {
    'CliqueJoin': 'w',
    'StarJoin': 'w',
    'PSgL': 'w',
    'BigJoin': 'w',
    'CystalJoin': 'w',
    'MultiwayJoin': 'w',
    'MultiCFL': 'w',
}
color = {
    'CliqueJoin': '#E5E5E5',
    'StarJoin': '#E5E5E5',
    'PSgL': '#E5E5E5',
    'BigJoin': '#E5E5E5',
    'CystalJoin': '#E5E5E5',
    'MultiwayJoin': '#E5E5E5',
    'MultiCFL': '#E5E5E5',
}


# algs = ['CliqueJoin','PSgL','BigJoin','CystalJoin', 'MultiwayJoin', ]
# label_algs = ['CliqueJoin','StarJoin','PSgL', 'BigJoin','CystalJoin', 'MultiwayJoin', ]
### 实现名称， 数据集合名称， 第一横坐标（数据集），第二横坐标（算法），（数据集，算法）- 时间
def plot_bar(exp, title, x_labels, project, data, is_legend=False):
    plt.figure(figsize=(5, 2.55))
    num_x = len(x_labels)
    num_y = len(project)

    width = 0.2
    step = width * (num_y + 2)
    location = np.arange(start=0, stop=num_x * step, step=step)
    print("local", location)
    total_width = step * num_x

    ax = plt.gca()
    # Assign data and x array
    inf = assign_inf(data)
    # Assign y array
    inf_log = int(np.log10(inf)) - 1
    ylocs = []
    yticks = []
    for i in range(inf_log + 1):
        ylocs.append(int(np.power(10, i)))
        yticks.append("$10^" + str(i) + "$")

    ylocs.append(int(np.power(10, inf_log + 0.5)))
    yticks.append(">4h")
    plt.yscale('log')
    plt.yticks(ylocs, yticks, fontsize=14)

    # plot group
    for i, sub_proj in enumerate(project):
        cur_loc = location + i * width
        print("cur ", cur_loc, i, data[i])
        ax.bar(cur_loc, data[i], tick_label=x_labels, width=width, label=sub_proj, color=color[sub_proj], edgecolor='k',
               hatch=patterns[sub_proj], align="center")
        if exp.endswith("dataset"):
            ax.bar(cur_loc, data[i + num_y], tick_label=x_labels, width=width, label=sub_proj, color=revcolor[sub_proj],
                   edgecolor='k',
                   hatch=patterns[sub_proj], align="center")
        for j, eachd in enumerate(data[i]):
            if eachd != 0 and eachd < 0.1:
                ax.text(cur_loc[j] - 0.12, eachd, str(eachd), fontsize='8', fontweight='bold', va='bottom', rotation=90)

    # plot group spliter
    cur_loc = location + len(project) * width - 0.1
    array = [inf, ] * num_x
    ax.bar(cur_loc, array, tick_label=x_labels, width=0, edgecolor='#B5B5B5', align="edge", ls=':', lw=0.4)
    plt.xticks(location + (num_y / 2.0) * width, fontsize=14);

    plt.ylim(0, int(np.power(10, inf_log + 0.5)))
    plt.title("T (sec)", loc="left")
    # plt.show()
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
    # plot_bar('vary_data_q0dataset', 'q0', vary_dataset_datasets, algs, vary_dataset_q0, True);
    for name in vary_dataset_queries.keys():
        plot_bar('vary_dataset', name, vary_dataset_datasets, algs, vary_dataset_queries[name], is_legend)
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
        plot_bar('vary_labelled_dataset', name, vary_labelled_datasets, label_algs, vary_labelled_queries[name],
                 is_legend)
        plt.close()
        is_legend = False

    var_query_datasets = {
        'GP': vary_query_gp,
        'US': vary_query_us,
    }
    xlabel = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9']
    is_legend = True
    for name in var_query_datasets.keys():
        plot_bar('vary_queries', name, xlabel, algs, var_query_datasets[name], is_legend)
        plt.close()
        is_legend = False
