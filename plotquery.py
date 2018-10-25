import numpy as np
import matplotlib.pyplot as plt
from pylab import *

# Exp-2 Vary Datasets

algs = ['CliqueJoin','PSgL','BigJoin','CystalJoin', 'MultiwayJoin', ]
label_algs = ['CliqueJoin','StarJoin','PSgL', 'BigJoin','CystalJoin', 'MultiwayJoin', ]

vary_dataset_q0 = [
    # GO,         GP,       US,      LJ,     OK,     UK02
    [0.059,       0.95,     1.046,   0.8,    2.6,    3],  # cliquejoin
    [19.55,      111.61,    27.72,   50.12, 133.67,  0],  # psgl
    [1.14,        4.07,     1.08,    3.54,   13.04, 19.63],  # bigjoin
    [0,           0,        0,       0,      0,      0],  # crystaljoin
    [45.77,      155.06,    203.2,  254.41, 750.99, 3225.77],  # multiwayjoin
]

vary_dataset_q1 = [
    # GO,      GP, US,          LJ,     OK,     UK02
    [51,       0,  12.14,       570,    0,          0],            # cliquejoin
    [183.57,   0,  36.28,       0,      0,          0],  # psgl
    [2.62,     0,  1.51,        158.5,  1454.72,    2630.75],  # bigjoin
    [0,        0,  0,           0,      0,          0],            # crystaljoin
    [84.23,    0,  315.03,      1708.81,0,          0],            # multiwayjoin
]

vary_dataset_q2 = [
    # GO,     GP,       US,     LJ,     OK,     UK02
    [ 2.3,    206.45,   7.5,        57,     123,    759],       #clique
    [92.8,    0,        26.25,      0, 0, 0],  # psgl
    [3.73,    1678.04,  2.02,       128.96, 379.12, 4027.17],  # big
    [ 0,      0,        0,          0,      0,      0],         #crys
    [ 103.8,  0,        342.39,     2601,    0,      0],        #multiway
]

vary_dataset_q3 = [
    # GO,     GP,      US,      LJ,     OK,     UK02
    [0.118,   47.92,   1.6,     3.3,    8,      23.4],      #clique
    [22.3,    0,       29.41,   0,      0,      0],  # psgl
    [2.06,    301.83,  1.2,     43.19, 105.39, 625.92],  # big
    [0,       0,       0,       0,      0,      0],         #crys
    [90.04,   0,       322.97,  1113.85,0,      0],         #multiway
]
vary_dataset_q4 = [
    # GO,      GP, US,          LJ,     OK,     UK02
    [387,      0,  22,          0, 0, 0],  # clique
    [0,        0,  39.29,       0, 0, 0],  # psgl
    [134.71,   0,  4.18,        0, 0, 0],  # big
    [0,        0,  0,           0,      0,      0],     #crys
    [2320.29,  0,  295.17,      0,      0,      0],     #multiway
]
vary_dataset_q5 = [
    # GO,      GP, US,          LJ,     OK,     UK02
    [48,       0,  5.7,         0,      0,      0],     #clique
    [0,        0,  25.68,       0, 0, 0],  # psgl
    [28.98,    0,  2.45,        0, 0, 0],  # big
    [0,        0,  0,           0,      0,      0],     #crys
    [2146.44,  0,  250.23,      0,      0,      0],     #multiway
]
vary_dataset_q6 = [
    # GO,       GP,      US,         LJ,     OK,     UK02
    [0.223,     2835.24, 2.3,        99,     43.6,      1253],   #clique
    [53.07,     0,       27.11,      0,      0,         0],  # psgl
    [5.52,      0,       1.22,       1996.52, 622.47,   0],  # big
    [0,         0,       0,          0,      0,         0],      #crys
    [145.21,    0,       240.1,      0,      0,         0],      #multiway
]
vary_dataset_q7 = [
    # GO,       GP,     US,           LJ,     OK,     UK02
    [7331,        0,    12.2,           0,      0,      0],       #clique
    [0,           0,    26.81,            0, 0, 0],  # psgl
    [0,           0,    4.52,             0, 0, 0],  # big
    [0,           0,    0,              0,      0,      0],       #crys
    [0,           0,    460.1,          0,      0,      0],       #multiway
]
vary_dataset_q8 = [
    # GO,      GP, US,              LJ,     OK,     UK02
    [0.43,      0, 3.2,             4671,   106,    0],        #clique
    [125.56,    0, 26.71,           0,      0,      0],  # psgl
    [17.54,     0, 1.3,             0,      0,      0],  # big
    [0,         0, 0,               0,      0,      0],        #crys
    [268.14,    0, 556.1,           0,      0,      0],        #multiway
]
vary_dataset_q9 = [
    # GO,       GP,   US,               LJ,     OK,     UK02
    [417,       0,    413,              0,      0,      0],       #clique
    [0,         0,    27.78,            0,      0,      0],  # psgl
    [189.11,    0,    4.18,             0,      0,      0],  # big
    [0,         0,    0,                0,      0,      0],       #crys
    [0,         0,    251.11,           0,      0,      0],       #multiway
]



labelled_dataset_q0 = [
    # DG01 DG03 DG10 DG30 DG60
    [0.45, 1.46, 4.52, 14.29, 35.52], #clique
    [0.45, 1.46, 4.52, 14.29, 35.52], # star
    [21.11, 36.12, 68.1, 127.79, 0],  # psgl
    [1.12, 1.35, 9.69, 27.39, 14.93],  # bigjoin
    [0, 0, 0, 0, 0],  # crystal
    [99.81, 506.43, 0, 0, 0], # multiway
]
labelled_dataset_q1 = [
    [12.84,	127.77,	2013.06,	0,	0], #clique
    [12.84,	127.77,	2013.06,	0,	0], #star
    [0, 0, 0, 0, 0],  # crystal
    [3.09, 6.42, 18.65, 57.73, 121.11], #big
    [3.19,	100.72,	922.56, 1077.7, 0], #multiay
    [27.82, 44.85, 112.26, 304.95, 0], #psgl
]

labelled_dataset_q2 = [
    [0.46,1.48,5.62,19.14,53.44], #clique
    [5.23,21.61,83.79,263.48,0], #star
    [33.27, 52.99, 109.45, 306.86, 720.05],  # psgl
    [1.73, 4.2, 17.61, 75.02, 255.78],  # big
    [0, 0, 0, 0, 0],  # crs
    [21.91,32.14,56.86,145.97,0], #multway
]
labelled_dataset_q3 = [
    [12.24,54.63,169.14,0,0,], #clique
    [12.24,54.63,169.14,0,0,], #star
    [47.2, 104.55, 0, 0, 0, ],  # psgl
    [131.19, 669.76, 4630.83, 0, 0, ],  # big
    [0, 0, 0, 0, 0, ],  # crs
    [105.17,447.19,0,0,0,], #multiway
]

labelled_dataset_q4 = [
    [499.38,2384.96,5873.22,0,0], #clique
    [499.38,2384.96,5873.22,0,0], #star
    [181.32, 0, 0, 0, 0],  # psgl
    [78.37, 381.04, 1013.16, 3405.27, 8315.56],  # big
    [0, 0, 0, 0, 0],  # crs
    [201.99, 1146.06, 0, 0, 0],  # multiway
]

labelled_dataset_q5 = [
    [0.74,2.05,6.83,21.11,43.86], #clique
    [0.74,2.05,6.83,21.11,43.86], #star
    [21.87, 32.79, 84.19, 223.56, 0],  # psgl
    [2.61, 6.14, 28.96, 125.22, 419.64],  # big
    [0, 0, 0, 0, 0], #crs
    [48.42, 69.05, 241.08, 508.78, 1555.33],  # multiway
]
labelled_dataset_q6 = [
    [1.16,3.85,15.08,54.69,177.69,], #clique
    [982,3544.03,0,0,0,], #star
    [52.49, 112.07, 306.42, 250.44, 807.09, ],  # psgl
    [1.08, 1.16, 1.49, 2.88, 7.04, ],  # big
    [0, 0, 0, 0, 0, ],  # crs
    [22.28,27.91,51.46,122.62,0,], #multiway
]

labelled_dataset_q7 = [
    [1.24,3.86,14.63,66.97,240.47], #cli
    [3.64,36.47,732.75,0,0], #star
    [20.33, 47.03, 235.92, 2331.5, 0],  # psgl
    [1.55, 7.06, 82.53, 980.91, 6607.21],  # big
    [0, 0, 0, 0, 0],  # crs
    [134.56, 356.33, 1264.34, 0, 0],  # multi
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

patterns = {
    'CliqueJoin': '',
    'StarJoin':'',
    'PSgL':'//',
    'BigJoin':'..',
    'CystalJoin':'\\\\',
    'MultiwayJoin':'xxxx'
}
color = {
    'CliqueJoin':'w',
    'StarJoin':'#000000',
    'PSgL':'w',
    'BigJoin':'w',
    'CystalJoin':'w',
    'MultiwayJoin':'w'
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
        print("cur ",cur_loc,i)
        ax.bar(cur_loc, data[i], tick_label=x_labels, width=width, label=sub_proj, color=color[sub_proj], edgecolor='k',
               hatch=patterns[sub_proj], align="center")
    plt.xticks(location + (num_y/2.0) * width, fontsize=14);

    # Assign y array
    inf_log = int(np.log10(inf))
    ylocs = []
    yticks = []
    for i in range(inf_log + 1):
        ylocs.append(int(np.power(10, i)))
        if i < inf_log:
            yticks.append("$10^" + str(i) + "$")
        else:
            yticks.append("Inf")
    plt.yscale('log')
    plt.yticks(ylocs, yticks, fontsize=14)
    plt.ylim(0, inf)
    plt.title("T (sec)",loc="left")
    plt.savefig('figures/' + exp + '_' + title + '.pdf', fotmat='pdf')

    if is_legend:
        # Plot the legend in a separate figure
        legend_fig = plt.figure(figsize=(total_width * 0.95, 0.2))
        lax = legend_fig.add_subplot(111)
        lax.legend(*ax.get_legend_handles_labels(), ncol=num_y, loc='center', frameon=False)
        lax.axis('off')
        lax.set_frame_on(False)
        plt.savefig('figures/' + exp + '_legend.pdf', fotmat='pdf')



if __name__ == '__main__':
    # Vary dataset
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

    vary_labelled_queries = {
        'q0': labelled_dataset_q0,
        'q1': labelled_dataset_q1,
        'q2': labelled_dataset_q2,
        'q3': labelled_dataset_q3,
        'q4': labelled_dataset_q4,
        'q5': labelled_dataset_q5,
        'q6': labelled_dataset_q6,
        'q7': labelled_dataset_q7,
    }

    vary_dataset_datasets = ['GO',  'GP', 'US', 'LJ', 'OK', 'UK']
    is_legend = True
    for name in vary_dataset_queries.keys():
        plot_bar('vary_dataset', name, vary_dataset_datasets, algs, vary_dataset_queries[name], is_legend)
        plt.close()
        is_legend = False

    vary_labelled_datasets = ['DG01', 'DG03', 'DG10', 'DG30', 'DG60']
    is_legend = True
    for name in vary_labelled_queries.keys():
        plot_bar('vary_labelled_dataset', name, vary_labelled_datasets, label_algs, vary_labelled_queries[name], is_legend)
        plt.close()
        is_legend = False