import matplotlib.pyplot as plt
import numpy as np
import pandas


def restriction():
    x_position1 = [2,3]
    x_position2 = [3,4]
    x_position3 = [1,4]

    plt.plot(x_position1, [1,1], 'o-')
    plt.plot(x_position2, [2,2], 'o-')
    plt.plot(x_position3, [3,3], 'o-')

    plt.text(x_position1[0],1.1, 'Restriction 1')
    plt.text(x_position2[0],2.1, 'Restriction 2')
    plt.text(x_position3[0],3.1, 'Restriction 3')

    plt.xlim(0,5)
    plt.ylim(0,4)

    ax = plt.gca()
    ax.axes.yaxis.set_visible(False)

    plt.title('Government Policy')

    plt.show()
    return

def canada_alberta_graph():
    #Just a test
    alberta_canada_all = np.genfromtxt('Canada,Alberta Daily Cases.csv',  dtype=(int,'U100',int,int,int), delimiter=',', skip_header = True)

    canada_case_list, alberta_case_list = [],[]
    canada_x_axis, alberta_x_axis = [],[]
    cx, ax = 0,0
    for row in alberta_canada_all:
        if row[0] == 1:
            canada_case_list.append(row[3])
            canada_x_axis.append(cx)
            cx += 1
        if row[0] == 48:
            alberta_case_list.append(row[3])
            alberta_x_axis.append(ax)
            ax += 1

    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    ax1.plot(canada_x_axis,canada_case_list, label = 'Canada')
    ax1.legend()
    ax2.plot(alberta_x_axis, alberta_case_list, label = 'Alberta')
    ax2.legend()
    

    plt.show()
    return


# restriction()
canada_alberta_graph()