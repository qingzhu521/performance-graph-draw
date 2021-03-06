import numpy as np
import matplotlib.pyplot as plt
from pylab import *

algs = ['CliqueJoin', 'PSgL', 'BigJoin', 'CrystalJoin', 'MultiwayJoin', ]
nopsgl = ['CliqueJoin', 'BigJoin', 'CrystalJoin', 'MultiwayJoin', ]
labelled_algs = ['CliqueJoin', 'StarJoin', 'PSgL', 'BigJoin', 'CrystalJoin', 'MultiwayJoin']

############### unlabelled dataset ####################
scalability_lj_q1 = [
    # machine 1,        2,      4,      6,      8,      10
    [5794.76, 2202.91, 1124.72, 812.88, 654.32, 569.6],  # cliquejoin
    [None, None, None, None, None, None],  # psgl
    [1355.07, 730, 376.02, 254.35, 195.9, 158.5],  # bigjoin?
    [1355.07, 730, 376.02, 254.35, 195.9, 158.5],  # crystaljoin
    ['Timeout', 7037.98, 5322, 2975.56, 3095.15, 1610.13],  # multiwayjoin
    [2129.36, 2129.36, 2129.36, 2129.36, 2129.36, 2129.36]  # single thread
]

scalability_lj_q1_commnuication = [
    # machine 1,        2,         4,           6,          8,          10
    [7957596903, 3979267998, 1989682698, 1326676185, 995285574, 796487292],  # clique
    [None, None, None, None, None, None],  # psgl
    [20174493477, 10271095042, 5296603797, 3667458593, 2823005059, 2325011820],  # bigjoin
    [20174493477, 10271095042, 5296603797, 3667458593, 2823005059, 2325011820],  # crystal
    [None, 171480011, 128628774, 123806121, 195327068, 147650829],  # multiway

    [7956624894, 3977789253, 1988671353, 1325459355, 994116846, 794940078],
    [None, None, None, None, None, None],  # psgl
    [19633758791, 9558815152, 4579171909, 2972001214, 2153157041, 1763829489],
    [19633758791, 9558815152, 4579171909, 2972001214, 2153157041, 1763829489],  # crystal
    [None, 32158341, 10695191, 23783410, 14286331, 9531735], # multiway
]
scalability_lj_q1_mem = [
    # machine 1,        2,          4,          6,          8,          10
    [35.42, 24.04, 20.64, 20.55, 20.65, 20.47],  # clique
    [None, None, None, None, None, None],  # psgl
    [1.35, 1.05, 1.18, 1.48, 1.78, 1.97],  # bigjoin
    [1.35, 1.05, 1.18, 1.48, 1.78, 1.97],  # crystal
    [None, 36.08, 29.71, 39.01, 32.08, 36.96],  # multiway

    [35.42, 23.9, 14.85, 10.34, 8.033, 7.7],  # clique
    [None, None, None, None, None, None],  # psgl
    [1.35, 1.05, 1.04, 1.2, 1.43, 1.33],  # big_join
    [1.35, 1.05, 1.04, 1.2, 1.43, 1.33],  # crystal
    [None, 26.2, 5.4, 22.79, 18.05, 7.52],  # multiway
]

scalability_lj_q2 = [
    # machine 1,        2,      4,      6,      8,      10
    [499.03, 250.4, 131.47, 90.234, 67.54, 56.42],  # cliquejoin
    [None, None, None, None, None, None],  # psgl
    [1063.72, 570.05, 300.66, 204.63, 156.41, 128.96],  # bigjoin
    [82.018, 46.553, 26.411, 19.286, 15.052, 11.825],  # crystaljoin
    ['Timeout', 6859.92, 5438, 3115.46, 3423.35, 2258.24],  # multiwayjoin
    [111.62, 111.62, 111.62, 111.62, 111.62, 111.62],  # god
]
scalability_lj_q2_commnuication = [
    # machine 1,            2,          4,          6,          8           10
    [1715184090, 858401232, 429824946, 286547790, 215260326, 172275786], # clique
    [None, None, None, None, None, None],  # psgl
    [29323486405, 14782716013, 7583165895, 5187069282, 4129050963, 3384823851],# big
    [266669634, 134642008, 68744215, 45903155, 35543285, 29157084],# crystal
    [None, 171480011, 128628774, 200039302, 209582811, 152401068],# multiway

    [1713200292, 856111050, 427354404, 284814492, 213422592, 170759808],  # clique
    [None, None, None, None, None, None],  # psgl
    [28446929240, 13895943553, 6601104993, 4394393856, 3169384430, 2464148837],  # big
    [20912067, 10182078, 4761236, 3011085, 2356053, 1758122],  # crystal
    [None, 42851237, 10695191, 23783410, 14286331, 14281974]  # multiway
]

scalability_lj_q2_mem = [
    # machine 1,            2,          4,          6,          8           10
    [22.24, 21.84, 12.77, 9.96, 7.93, 6.91],  # clique
    [None, None, None, None, None, None],  # psgl
    [1.53, 1.58, 1.74, 1.72, 1.59, 1.77],  # big
    [0.84, 0.671, 0.609, 0.6, 0.574, 0.577],  # crystal
    [None, 38.87, 29.08, 45.63, 33.64, 36.48],  # multiway

    [22.24, 21.61, 12.48, 9.1, 7.43, 6.63],
    [None, None, None, None, None, None],  # psgl
    [1.53, 1.49, 1.56, 1.46, 1.37, 1.34],
    [0.79, 0.671, 0.609, 0.6, 0.574, 0.577],  # crystal
    [None, 26.2, 5.45, 22.71, 19.51, 7.52],
]
scalability_lj_q3 = [
    # machine 1,            2,          4,          6,          8           10
    [30.72, 15.62, 8.11, 5.344, 4.12, 3.25],  # cliquejoin
    [None, None, None, None, None, None],  # psgl
    [348.82, 193.07, 101.7, 68.64, 52.72, 43.19],  # bigjoin?
    [348.82, 193.07, 101.7, 68.64, 52.72, 43.19],  # crystaljoin
    [4560, 2472.39, 1847.69, 1103.27, 1192.03, 854.961],  # multiwayjoin
    [220.12, 220.12, 220.12, 220.12, 220.12, 220.12]  # god
]

scalability_lj_q3_communication = [
    # machine 1,            2,          4,          6,          8           10
    [5, 5, 5, 5, 5, 5],  # clique
    [None, None, None, None, None, None],  # psgl
    [8532344313, 4289522467, 2198958161, 1466508873, 1177325857, 990845502],  # big
    [8532344313, 4289522467, 2198958161, 1466508873, 1177325857, 990845502],  # crystal
    [278645635, 171480011, 128628774, 214319310, 228613469, 157153820],  # multiway

    [5, 5, 5, 5, 5, 5],  # clique
    [None, None, None, None, None, None],  # psgl
    [8294838495, 4041980471, 1943966481, 1279108174, 943452885, 710826657],  # big
    [8294838495, 4041980471, 1943966481, 1279108174, 943452885, 710826657],  # crystal
    [128551416, 42851237, 42851237, 23783410, 14286331, 11032624],  # multiway
]
scalability_lj_q3_mem = [
    # 1,            2,          4,          6,          8           10
    [0.54, 0.54, 0.54, 0.54, 0.54, 0.54],  # clique
    [None, None, None, None, None, None],  # psgl
    [0.94, 0.81, 0.78, 0.74, 0.75, 0.72],  # big
    [0.94, 0.81, 0.78, 0.74, 0.75, 0.72],  # crystal
    [61.2, 36.65, 28.08, 48.56, 42.92, 41.48],  # mulitway

    [0.54, 0.54, 0.54, 0.54, 0.539, 0.539],  # clique
    [None, None, None, None, None, None],  # psgl
    [0.94, 0.81, 0.75, 0.7, 0.67, 0.65],  # big
    [0.94, 0.81, 0.75, 0.7, 0.67, 0.65],  # crystal
    [61.20, 26.2, 5.45, 25.66, 21.97, 9.88],  # multiway
]

############### labelled dataset ####################
scalability_DG10_q3 = [
    # 1 2 4 6 8 10
    [None, None, None, 246.63, 191.71, 169.18],  # clique
    [None, None, None, 246.63, 191.71, 169.18],  # star
    [None, None, None, None, None, None],  # psgl
    ["Timeout", 5670.539, 3129.944, 2061.935, 1603.243, 1354.557],  # big
    ["Timeout", 5670.539, 3129.944, 2061.935, 1603.243, 1354.557],  # crs
    ["Timeout", "Timeout", "Timeout", "Timeout", "Timeout", "Timeout"],  # multi
    [None, None, 6428.78, 3924.07, 2348.07, 1517.91, ],  # multiwaycfl
    [None, None, None, None, None, None],  # single thread
]
scalability_DG10_q3_communication = [
    # 1 2 4 6 8 10
    [None, None, None, 438257751, 328703757, 262986441, ],  # clique
    [None, None, None, 438257751, 328703757, 262986441, ],  # star
    [None, None, None, None, None, None, ],  # psgl
    [None, 3805878, 1939375, 1308263, 986400, 799371],  # big
    [None, 3805878, 1939375, 1308263, 986400, 799371],  # crys
    [None, None, None, None, None, None, ],  # multiwayjoin
    [None, None, None, None, None, None],  # multiwaycfl
]
scalability_DG10_q3_mem = [
    # 1 2 4 6 8 10
    [None, None, None, 46.68, 47.23, 45.52],  # clique
    [None, None, None, 46.68, 47.23, 45.52],  # star
    [None, None, None, None, None, None],  # psgl
    [None, 20.608, 20.0172, 17.898, 17.743, 17.428],  # big
    [None, 20.608, 20.0172, 17.898, 17.743, 17.428],  # crystal
    [None, None, None, None, None, None],  # multiwayjoin
    [None, None, None, None, None, None],  # multiwaycfl
]

scalability_DG10_q6 = [
    # 1 2 4 6 8 10
    [142.56, 71.53, 37.57, 24.6, 18.75, 15.08],  # clique
    ["Timeout", "Timeout", "Timeout", "Timeout", "Timeout", "Timeout"],  # star
    [163.76, 88.4, 52.61, 42.92, 40.25, 39.69],  # psgl
    [1.87, 2.05, 1.7, 1.6, 1.55, 1.49],  # big
    [137.778, 71.785, 41.886, 28.558, 30.994, 19.103],  # crs
    [1464.45, 1389.95, 1338.63, 833.03, 702.55, 306.42],  # multi
    [19.4, 15.68, 10.86, 9.27, 7.39, 7.55],  # multiwaycfl
    [64.56, 64.56, 64.56, 64.56, 64.56, 64.56, ],  # single thread
]
scalability_DG10_q6_communication = [
    # 1 2 4 6 8 10
    [68448, 36900, 21308, 20096, 15412, 11986],  # clique
    [None, None, None, None, None, None],  # star
    [9995945, 4997973, 2498987, 1665991, 1249494, 999595],  # psgl
    [416848, 214316, 109953, 81731, 56631, 49247],  # big
    [5209259, 2608286, 1336279, 903490, 682398, 552259],  # crystal
    [16023886, 15982881, 23363892, 14258639, 17105169, 12485960],  # multiway
    [0, 0, 0, 0, 0, 0, ]  # MultiCFL
]

scalability_DG10_q6_mem = [
    # 1 2 4 6 8 10
    [3.67, 3.67, 3.67, 3.67, 3.67, 3.67, ],  # clique
    [None, None, None, None, None, None, ],  # star
    [50.86, 33.42, 22.9, 17.28, 15.04, 13.52, ],  # psgl
    [3.58, 3.58, 3.58, 3.58, 3.58, 3.58, ],  # df
    [3.667, 3.667, 3.667, 3.667, 3.667, 3.667, ],  # crystal
    [12.54, 10.74, 14.73, 13.26, 12.65, 8.61, ],  # multiway
    [3.93, 3.93, 3.93, 3.93, 3.93, 3.93, ],  # god
    [4.24, 4.24, 4.24, 4.24, 4.24, 4.24, ],  # single
]

scalability_DG10_vary_label_q3 = [
    # 0 5 10 15 20
    [None, None, 168.6, 84.95, 44.35],  # cliq
    [None, None, 168.6, 84.95, 44.35],  # star
    [None, None, None, None, None, ],  # psgl
    [6180.3, 7509.499, 1372.099, 590.726, 212.629, ],  # crs
    [6180.3, 7509.499, 1372.099, 590.726, 212.629, ],  # crs
    ["Timeout", "Timeout", 1397.16, 424.64, 256.3],  # multi
    ["Timeout", "Timeout", 7399.57, 1076.84, 154.53, ],  # multicfl

]

scalability_DG10_vary_label_q6 = [
    # 0 5 10 15 20
    ["Timeout", 19.18, 4.48, 4.4, 4.38, ],  # clique
    [None, None, 42.5, 21.7, 12.19, ],  # star
    ["Timeout", None, None, None, 38.63, ],  # psgl
    ["Timeout", 479.14, 4.92, 5.61, 5.57, ],  # big
    [6180.165, 402.66, 23.43, 17.233, 4.377, ],  # crys
    ["Timeout", 441.81, 274.77, 271.84, 275.74, ],  # multi
    ["Timeout", 563.15, 60.83, 37.72, 37.24, ],  # multicfl
]

scalability_DG10_vary_density_q3 = [
    # 10 20 40 80 160
    [169.14, 180.01, 193.28, 245.15, None, ],  # clique
    [169.14, 180.01, 193.28, 245.15, None, ],  # star
    [None, None, None, None, None, ],  # psgl
    [1354.557, 1511.445, 1735.125, 2155.405, 2910.428, ],  # big
    [1354.557, 1511.445, 1735.125, 2155.405, 2910.428, ],  # crys
    ["Timeout", "Timeout", "Timeout", "Timeout", "Timeout", ],  # multiway
    [1647.96, None, None, None, None, ],  # multiwaycfl
]
scalability_DG10_vary_density_q6 = [
    [15.08, 15.44, 15.79, 16.38, 57.16, ],  # clique
    ["Timeout", None, None, None, None, ],  # star
    [51.46, 64.33, 83.44, 156, None],  # psgl
    [1.49, 14.47, 26.48, 56.82, 148.75, ],  # big
    [19.103, 33.345, 44.282, 40.363, 47.574, ],  # crys
    [306.42, 1000, 1918.61, 3833, 4196, ],  # multiway
    [7.07, 7.45, 7.48, 8.13, 7.48, ], #multiwaycfl
]

scalability_comp_time_q1 = [
    [569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.5, 569.6, 569.6,
     569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.6, 569.5, 569.6, 569.6, 569.6, 569.6, 569.6],  # clique
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None, None, None, None, None, None],  # psgl
    [127.58, 123.65, 120.81, 125.36, 124.39, 124.53, 128.9, 132.01, 124.76, 124.26, 121.6, 131.02, 130.81, 123.05,
     117.7, 129.7, 122.38, 130.17, 121.35, 121.07, 124.38, 121.33, 121.93, 126.39, 124.1, 122.43, 117.45, 121.35,
     124.51, 123.76],  # big
    [127.58, 123.65, 120.81, 125.36, 124.39, 124.53, 128.9, 132.01, 124.76, 124.26, 121.6, 131.02, 130.81, 123.05,
     117.7, 129.7, 122.38, 130.17, 121.35, 121.07, 124.38, 121.33, 121.93, 126.39, 124.1, 122.43, 117.45, 121.35,
     124.51, 123.76],  # crystal
    [463.592, 601.482, 777.71, 515.94, 727.896, 1056.83, 843.133, 1179.94, 1293.92, 1061.83, 1097.82, 1127.4, 853.46,
     866.137, 1308.63, 622.677, 763.76, 1018.92, 754.472, 1109.1, 1565.48, 600.008, 984.1, 1009.5, 725.031, 819.491,
     828.578, 853.717, 857.439, 1467.17],  # multiway_join

]
scalability_comp_time_q2 = [
    [56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42,
     56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42, 56.42,],  # clique
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None, None, None, None, None, None],  # psgl
    [91.62, 90.36, 89.25, 92.63, 93.87, 93.22, 95.43, 101.34, 90.72, 91.72, 92.76, 95.29, 100.52, 89.57, 89.49, 93.44,
     84.69, 97.67, 92.31, 90.93, 94.49, 88.82, 87.75, 89.81, 89.71, 89.14, 83.17, 89.34, 88.34, 90.44],  # big
    [7.127, 6.947, 6.982, 7.053, 7.199, 7.107, 7.306, 7.313, 7.054, 7.07, 6.996, 7.23, 7.088, 7.001, 6.836, 7.571,
     7.255, 7.506, 6.874, 7.09, 6.989, 7.208, 7.284, 7.602, 6.918, 6.901, 6.752, 7.018, 7.496, 7.604],  # crystal
    [661.171, 793.752, 962.087, 599.037, 803.905, 1011.04, 444.591, 1542.51, 2258.24, 352.419, 665.806, 939.076,
     621.343, 1389.38, 2145.73, 329.383, 1095.14, 674.51, 687.998, 1755.05, 464.567, 875.743, 1501.27, 361.022, 539.256,
     546.552, 696.385, 1235.67, 803.905, 939.076, ],  # multiway_join
]
scalability_comp_time_q3 = [
    [2.23, 2.23, 2.23, 2.23, 2.23, 2.23, 2.23, 2.23, 2.23, 2.23, 2.23, 2.23, 2.23,2.23, 2.23, 2.23,
     2.23, 2.23, 2.23, 2.23, 2.23, 2.23, 2.23, 2.23, 2.23, 2.23, 2.23, 2.23, 2.23, 2.23],  # clique
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
     None, None, None, None, None, None, None, None, None, None, None],  # psgl
    [28.6, 28.58, 28.76, 29.16, 29.69, 29.83, 30.34, 31.36, 29.09, 29.36, 29.18, 30.08, 31.49, 28.49, 29.43, 30.03,
     27.7, 30.54, 29.24, 29.25, 30.13, 28.79, 28.52, 29, 29.16, 28.82, 27.49, 28.85, 28.59, 29.38],  # big
    [28.6, 28.58, 28.76, 29.16, 29.69, 29.83, 30.34, 31.36, 29.09, 29.36, 29.18, 30.08, 31.49, 28.49, 29.43, 30.03,
     27.7, 30.54, 29.24, 29.25, 30.13, 28.79, 28.52, 29, 29.16, 28.82, 27.49, 28.85, 28.59, 29.38],  # crystal
    [270.743, 336.017, 380.868, 251.536, 290.172, 425.923, 125.313, 579.579, 854.961, 137.25, 211.99, 357.371, 276.894,
     480.737, 726.349, 116.252, 305.704, 265.919, 279.904, 666.72, 247.001, 354.317, 608.673, 121.743, 201.993, 185.278,
     226.011, 455.487, 495.923, 405.923, ],  # multiway_join
]


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
    xinf = int(np.power(10, inf_log + 0.3))
    for each_data in data:
        for i in range(len(each_data)):
            if each_data[i] == "Timeout":
                each_data[i] = xinf

    return inf


def assign_inf_long(data):
    inf = 0
    for each_data in data:
        for val in each_data:
            if val is not None:
                inf = max(inf, val)
    inf = inf * 1.1
    for each_data in data:
        for i in range(len(each_data)):
            if each_data[i] == 0:
                each_data[i] = 0

    return inf


# labelled_algs = ['CliqueJoin','StarJoin','CrystalJoin', 'BigJoin','MultiwayJoin', 'PSgL']
patterns = {
    'CliqueJoin': 'o',
    'StarJoin': 'x',
    'PSgL': 'v',
    'BigJoin': '^',
    'CrystalJoin': 's',
    'MultiwayJoin': '+',
}
some_margin = 0.85


def plot_line(exp, title, xticks, xlabel, proj, data, is_legend):
    plt.figure(figsize=(3.2, 2.3))
    if exp.endswith('scalability_vary_workers'):
        numy = len(proj) + 3
    else:
        numy = len(proj) + 2
    total_width = 1.2 * numy
    # Assign y array
    inf = assign_inf(data)
    inf_log = int(np.log10(inf)) - 1
    # set yaxes
    ylocs = []
    yticks = []
    for i in range(inf_log + 1):
        ylocs.append(int(np.power(10, i)))
        yticks.append("$10^" + str(i) + "$")

    ylocs.append(int(np.power(10, inf_log + 0.3)))
    yticks.append(">3h")

    plt.yscale('log')
    plt.yticks(ylocs, yticks)
    plt.title("T (sec)", loc="left")

    ax = plt.gca()
    for (i, pj) in enumerate(proj):
        ax.plot(xticks, data[i], ls=':', marker=patterns[pj], mec='k', mfc='none', label=pj, color='k')
    if exp.endswith('scalability_vary_workers'):
        ax.plot(xticks, data[numy - 3], mec='r', mfc='none', label='Single Thread', color='r')

    # plt.xlabel(xlabel)
    # plt.ylim(-10,inf)
    plt.xticks(xticks, fontsize='8')
    plt.savefig('figures/' + exp + '_' + title + '.pdf', format='pdf')

    if is_legend:
        # Plot the legend in a separate figure
        legend_fig = plt.figure(figsize=(total_width * some_margin, 0.2))
        lax = legend_fig.add_subplot(111)
        lax.legend(*ax.get_legend_handles_labels(), ncol=numy, loc='center', frameon=True)
        lax.axis('off')
        plt.savefig('figures/' + exp + '_legend.pdf', fotmat='pdf')


def plot_line_self_scala(exp, title, ylabel, xticks, xlabel, proj, data, is_legend):
    plt.figure(figsize=(3.2, 2.3))
    numy = len(proj) + 2
    total_width = 1.2 * numy

    if ylabel.endswith('(billions)'):
        for (i, pj) in enumerate(proj):
            for j in range(len(data[i])):
                if data[i][j] is not None:
                    data[i][j] = (data[i][j] / 1000000000)
    elif ylabel.endswith('(millions)'):
        for (i, pj) in enumerate(proj):
            for j in range(len(data[i])):
                if data[i][j] is not None:
                    data[i][j] = (data[i][j] / 1000000)

    for (i, pj) in enumerate(proj):
        if exp.endswith('mem') and pj != 'BigJoin':
            for j in range(len(data[i])):
                if data[i][j] is not None:
                    data[i][j] = (data[i][j] / 3)

    inf = assign_inf_long(data)
    print(exp + " " + title + " " + str(inf))
    # set yaxes
    plt.title(ylabel, loc="left")

    ax = plt.gca()
    for (i, pj) in enumerate(proj):
        ax.plot(xticks, data[i], ls = ":", marker=patterns[pj], mec='k', mfc='none', label=pj, color='k')

    plt.xticks(xticks, fontsize='8')
    plt.savefig('figures/' + exp + '_' + title + '.pdf', format='pdf')

    if is_legend:
        # Plot the legend in a separate figure
        legend_fig = plt.figure(figsize=(total_width * some_margin, 0.2))
        lax = legend_fig.add_subplot(111)
        lax.legend(*ax.get_legend_handles_labels(), ncol=numy, loc='center', frameon=False)
        lax.axis('off')
        plt.savefig('figures/' + exp + '_legend.pdf', fotmat='pdf')


def plot_line_long(exp, title, data):
    plt.figure(figsize=(9.6, 2.3))
    inf = assign_inf_long(data)
    x = list(range(1, 31))
    yloc = [500, 1000, 1500, 2000, inf]
    yticks = [500, 1000, 1500, 2000, "inf"]
    plt.yticks(yloc, yticks)
    plt.title("T (sec)", loc="left")
    for (i, alg) in enumerate(algs):
        plt.plot(x, data[i], ls=':', marker=patterns[alg], mec='k', mfc='none', label=alg, color='k')
    plt.xticks(x)
    plt.savefig('figures/' + exp + '_' + title + '.pdf', format='pdf')


if __name__ == '__main__':
    ############ unlabelled #############
    # vary machines
    scala_each_time = {
        'query1': scalability_comp_time_q1,
        'query2': scalability_comp_time_q2,
        'query3': scalability_comp_time_q3,
    }
    for key in scala_each_time.keys():
        plot_line_long('scalability_workers_runningtime', key, scala_each_time[key])
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
    key = 'query1'
    plot_line('scalability_vary_workers', key, xtic_machines, xlabel, nopsgl, scalability[key], is_legend)
    plot_line_self_scala('scalability_lj_communication', key, '$C_{max}$ (billions)', xtic_machines, xlabel, nopsgl,
                         scalability_commnunication[key], is_legend)
    plot_line_self_scala('scalability_lj_mem', key, '$M_{max}$ (GB)', xtic_machines, xlabel, nopsgl,
                         scalability_mem[key], is_legend)
    is_legend = False
    plt.close()
    for key in scalability.keys():
        plot_line('scalability_vary_workers', key, xtic_machines, xlabel, algs, scalability[key], is_legend)
        plot_line_self_scala('scalability_lj_communication', key, '$C_{max}$ (billions)', xtic_machines, xlabel, algs,
                            scalability_commnunication[key], is_legend)
        plot_line_self_scala('scalability_lj_mem', key, '$M_{max}$ (GB)', xtic_machines, xlabel, algs,
                            scalability_mem[key], is_legend)
        plt.close()

    ############ labelled  var worker time communication and memory#############
    labelled_scalability = {
        'query3': scalability_DG10_q3,
        'query6': scalability_DG10_q6,
    }
    labelled_scalability_communication = {
        'query3': scalability_DG10_q3_communication,
        'query6': scalability_DG10_q6_communication,
    }
    labelled_scalability_mem = {
        'query3': scalability_DG10_q3_mem,
        'query6': scalability_DG10_q6_mem,
    }
    is_legend = True
    plot_line_self_scala('scalability_labelled_communication', 'query3', '$C_{max}$ (millions)', xtic_machines, xlabel,
                         labelled_algs, labelled_scalability_communication['query3'], True)
    plot_line_self_scala('scalability_labelled_communication', 'query6', '$C_{max}$ (millions)', xtic_machines, xlabel,
                         labelled_algs, labelled_scalability_communication['query6'], False)
    for key in labelled_scalability.keys():
        plot_line('scalability_labelled_vary_workers', key, xtic_machines, xlabel, labelled_algs,
                 labelled_scalability[key], is_legend)
        plt.close()
        plot_line_self_scala('scalability_labelled_mem', key, '$M_{max}$ (GB)', xtic_machines, xlabel, labelled_algs, labelled_scalability_mem[key], is_legend)
        plt.close()
        is_legend = False

############ labelled  var label #############
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

############ labelled  var density #############
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

