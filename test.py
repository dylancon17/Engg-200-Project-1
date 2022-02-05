import matplotlib.pyplot as plt
import numpy as np
import pandas


def Australia_restriction():
    mask1 = [2,3] #July 22, 2020- Present
    travel1 = [3,4] #March 20, 2020 - Present
    school1 = [1,4] #March 10, 2020 - Present
    vaccine1 = [4] #Jan 25. 2021 Approved

    plt.plot(mask1, [1,1], 'o-') 
    plt.plot(travel1, [2,2], 'o-') 
    plt.plot(school1, [3,3], 'o-') 
    plt.plot(vaccine1, [4], 'o-')

    plt.text(mask1[0],1.1, 'Mask Mandate')
    plt.text(travel1[0],2.1, 'International Travel Restrictions')
    plt.text(school1[0],3.1, 'School Closures')
    plt.text(vaccine1[0],4.1, 'First Vaccine Approved')


    plt.xlim(0,5)
    plt.ylim(0,5)

    ax = plt.gca()
    ax.axes.yaxis.set_visible(False)

    plt.title('Government Policy')

    plt.show()
    return

def USA_restriction():
    mask1 = [2,3] #July 27, 2020-May 13,2021
    travel1 = [3,4] #March 11, 2020 - Present
    school1 = [1,4] #March 10, 2020 - Present
    vaccine1 = [4] #Dec 11. 2020 Approved

    plt.plot(mask1, [1,1], 'o-') 
    plt.plot(travel1, [2,2], 'o-') 
    plt.plot(school1, [3,3], 'o-') 
    plt.plot(vaccine1, [4], 'o-')

    plt.text(mask1[0],1.1, 'Mask Mandate')
    plt.text(travel1[0],2.1, 'International Travel Restrictions')
    plt.text(school1[0],3.1, 'School Closures')
    plt.text(vaccine1[0],4.1, 'First Vaccine Approved')


    plt.xlim(0,5)
    plt.ylim(0,5)

    ax = plt.gca()
    ax.axes.yaxis.set_visible(False)

    plt.title('Government Policy')

    plt.show()
    return

def HK_restriction():
    mask1 = [2,3] #July 7 - ?
    travel1 = [3,4] #February 28 2020 - ?
    school1 = [1,4] #Jan 25 2020 - ?
    vaccine1 = [4] #Feb 22, 2021

    plt.plot(mask1, [1,1], 'o-') 
    plt.plot(travel1, [2,2], 'o-') 
    plt.plot(school1, [3,3], 'o-') 
    plt.plot(vaccine1, [4], 'o-')

    plt.text(mask1[0],1.1, 'Mask Mandate')
    plt.text(travel1[0],2.1, 'International Travel Restrictions')
    plt.text(school1[0],3.1, 'School Closures')
    plt.text(vaccine1[0],4.1, 'First Vaccine Approved')


    plt.xlim(0,5)
    plt.ylim(0,5)

    ax = plt.gca()
    ax.axes.yaxis.set_visible(False)

    plt.title('Government Policy')

    plt.show()
    return

def CAN_restriction():
    mask1 = [2,3] #?
    travel1 = [3,4] #March 16, 2020 - Present
    school1 = [1,4] #?
    vaccine1 = [4] #Dec 9. 2020 Approved Adults
    vaccine2 = [4.5] #Nov. 19 2021 Approved Kids

    plt.plot(mask1, [1,1], 'o-') 
    plt.plot(travel1, [2,2], 'o-') 
    plt.plot(school1, [3,3], 'o-') 
    plt.plot(vaccine1, [4], 'o-')
    plt.plot(vaccine2, [4], 'o-')


    plt.text(mask1[0],1.1, 'Mask Mandate')
    plt.text(travel1[0],2.1, 'International Travel Restrictions')
    plt.text(school1[0],3.1, 'School Closures')
    plt.text(vaccine1[0],4.1, 'First Vaccine Approved')
    plt.text(vaccine1[0],4.1, 'First Vaccine Approved for Youth')




    plt.xlim(0,5)
    plt.ylim(0,5)

    ax = plt.gca()
    ax.axes.yaxis.set_visible(False)

    plt.title('Government Policy')

    plt.show()
    return

def AB_restriction():
    mask1 = [2,3] #Dec 8 2020-July 7 2021
    mask2 = [4,5] #September 4 2021-Present
    travel1 = [3,4] #March 16, 2020 - Present
    school1 = [1,2] #March 16, 2020 - June 30 2020
    school2 = [2.5,3] #November 24 2020 - Jan 11 2021
    school3 = [4.5,5] #April 7 2021 - May 25 2021
    school4 = [0,1] #Jan 2022 - ?
    vaccine1 = [4] #Dec 9. 2020 Approved Adults
    vaccine2 = [4.5] #Nov. 19 2021 Approved Kids

    plt.plot(mask1, [1,1], 'o-') 
    plt.plot(mask2, [1,1], 'o-') 
    plt.plot(travel1, [2,2], 'o-') 
    plt.plot(school1, [3,3], 'o-') 
    plt.plot(school2, [3,3], 'o-') 
    plt.plot(school3, [3,3], 'o-') 
    plt.plot(school4, [3,3], 'o-') 
    plt.plot(vaccine1, [4], 'o-')
    plt.plot(vaccine2, [4], 'o-')


    plt.text(mask1[0],1.1, 'Mask Mandate')
    plt.text(travel1[0],2.1, 'International Travel Restrictions')
    plt.text(school1[0],3.1, 'School Closures')
    plt.text(vaccine1[0],4.1, 'First Vaccine Approved')
    plt.text(vaccine1[0],4.1, 'First Vaccine Approved for Youth')




    plt.xlim(0,5)
    plt.ylim(0,5)

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


Australia_restriction()
USA_restriction()
HK_restriction()
CAN_restriction()
AB_restriction()
# canada_alberta_graph()
