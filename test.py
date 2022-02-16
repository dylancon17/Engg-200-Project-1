import matplotlib.pyplot as plt
import matplotlib.dates
import matplotlib
import numpy as np
import pandas
import datetime as DT

'''TODO 
HK School
Graph Colours Slightly Different
'''

def s_2_d(date):
    converted_date = matplotlib.dates.datestr2num(date)
    return converted_date

def Australia_restriction():
    
    plt.figure(figsize=(6, 6))
    plt.rcParams['font.size'] = '20'
    plt.xticks(rotation = 90, ha='center')
    plt.subplots_adjust(left=0.12, bottom=0.22, right=0.9, top=0.88, wspace=0.2, hspace=0.2)

    mask1 = [s_2_d('2020-07-22'),s_2_d('2022-01-01')] #July 22, 2020- Present
    travel1 = [s_2_d('2020-03-20'),s_2_d('2022-01-01')] #March 20, 2020 - Present
    school1 = [s_2_d('2020-03-10'),s_2_d('2022-01-01')] #March 10, 2020 - Present
    vaccine1 = [s_2_d('2021-01-25')] #Jan 25. 2021 Approved

    plt.plot_date(mask1, [1,1], 'bo-') 
    plt.plot_date(travel1, [2,2], 'o-', color = 'orange') 
    plt.plot_date(school1, [3,3], 'go-') 
    plt.plot_date(vaccine1, [4], 'ro-')

    plt.text(mask1[0],1.1, 'Mask Mandate')
    plt.text(travel1[0]-50,2.1, 'International Travel Restrictions')
    plt.text(school1[0],3.1, 'School Closures')
    plt.text(vaccine1[0]-200,4.1, 'First Vaccine Approved')

    plt.xlim(18262.0,18993.0)
    plt.ylim(0,5)

    ax = plt.gca()
    ax.axes.yaxis.set_visible(False)

    plt.title('Government Policy')

    plt.show()
    return

def USA_restriction():
    
    plt.figure(figsize=(6, 6))
    plt.rcParams['font.size'] = '20'
    plt.xticks(rotation = 90, ha='center')
    plt.subplots_adjust(left=0.12, bottom=0.22, right=0.9, top=0.88, wspace=0.2, hspace=0.2)

    mask1 = [s_2_d('2020-07-27'),s_2_d('2021-05-13')] #July 27, 2020-May 13,2021
    travel1 = [s_2_d('2020-03-11'),s_2_d('2022-01-01')] #March 11, 2020 - Present
    school1 = [s_2_d('2020-03-10'),s_2_d('2021-02-07')] #March 10, 2020 - Feb 7 2021
    vaccine1 = [s_2_d('2020-12-11')] #Dec 11. 2020 Approved

    plt.plot_date(mask1, [1,1], 'bo-') 
    plt.plot_date(travel1, [2,2], 'o-', color = 'orange') 
    plt.plot_date(school1, [3,3], 'go-') 
    plt.plot_date(vaccine1, [4], 'ro-')

    plt.text(mask1[0],1.1, 'Mask Mandate')
    plt.text(travel1[0]-25,2.1, 'International Travel Restrictions')
    plt.text(school1[0],3.1, 'School Closures')
    plt.text(vaccine1[0]-110,4.1, 'First Vaccine Approved')


    plt.xlim(18262.0,18993.0)    
    plt.ylim(0,5)

    ax = plt.gca()
    ax.axes.yaxis.set_visible(False)

    plt.title('Government Policy')

    plt.show()
    return

def HK_restriction():
    
    plt.figure(figsize=(6, 6))
    plt.rcParams['font.size'] = '20'
    plt.xticks(rotation = 90, ha='center')
    plt.subplots_adjust(left=0.12, bottom=0.22, right=0.9, top=0.88, wspace=0.2, hspace=0.2)
    
    mask1 = [s_2_d('2020-07-07'),s_2_d('2022-01-01')] #July 7 - ?
    travel1 = [s_2_d('2020-02-28'),s_2_d('2022-01-01')] #February 28 2020 - ?
    school1 = [s_2_d('2020-01-25'),s_2_d('2020-05-27')] #25/1/2020-27/5/2020
    school2 = [s_2_d('2020-07-13'),s_2_d('2020-09-23')] #13/7/2020-23/9/2020
    school3 = [s_2_d('2020-11-23'),s_2_d('2021-02-22')] #23/11/2020-22/2/2021
    vaccine1 = [s_2_d('2021-02-22')] #Feb 22, 2021

    plt.plot_date(mask1, [1,1], 'bo-') 
    plt.plot_date(travel1, [2,2], 'o-', color = 'orange') 
    plt.plot_date(school1, [3,3], 'go-')
    plt.plot_date(school2, [3,3], 'go-') 
    plt.plot_date(school3, [3,3], 'go-') 
    plt.plot_date(vaccine1, [4], 'ro-')

    plt.text(mask1[0],1.1, 'Mask Mandate')
    plt.text(travel1[0]-15,2.1, 'International Travel Restrictions')
    plt.text(school1[0],3.1, 'School Closures')
    plt.text(vaccine1[0]-180,4.1, 'First Vaccine Approved')


    plt.xlim(18262.0,18993.0)    
    plt.ylim(0,5)

    ax = plt.gca()
    ax.axes.yaxis.set_visible(False)

    plt.title('Government Policy')

    plt.show()
    return

def CAN_restriction():
    
    plt.figure(figsize=(6, 6))
    plt.rcParams['font.size'] = '20'
    plt.xticks(rotation = 90, ha='center')
    plt.subplots_adjust(left=0.12, bottom=0.22, right=0.9, top=0.88, wspace=0.2, hspace=0.2)
    
    mask1 = [s_2_d('2020-05-20'),s_2_d('2022-01-01')] #May 20, 2020 - Present
    travel1 = [s_2_d('2020-03-16'),s_2_d('2022-01-01')] #March 16, 2020 - Present
    school1 = [s_2_d('2020-03-16'),s_2_d('2020-06-30')] #March 16, 2020 - June 30 2020
    school2 = [s_2_d('2021-01-01'),s_2_d('2021-01-11')] #Jan 1 2021 - Jan 11 2021
    school3 = [s_2_d('2021-04-01'),s_2_d('2021-06-30')] #April 1 2021 - June 30 2021
    school4 = [s_2_d('2022-01-01'),s_2_d('2022-01-17')] #Jan 1 2022 - Jan 17 2022
    vaccine1 = [s_2_d('2020-12-09')] #Dec 9. 2020 Approved Adults

    plt.plot_date(mask1, [1,1], 'bo-') 
    plt.plot_date(travel1, [2,2], 'o-', color='orange') 
    plt.plot_date(school1, [3,3], 'go-') 
    plt.plot_date(school2, [3,3], 'go-') 
    plt.plot_date(school3, [3,3], 'go-') 
    plt.plot_date(school4, [3,3], 'go-') 
    plt.plot_date(vaccine1, [4], 'ro-')


    plt.text(mask1[0]-100,1.1, 'Mask Recommended')
    plt.text(travel1[0]-30,2.1, 'International Travel Restrictions')
    plt.text(school1[0],3.1, 'School Closures')
    plt.text(vaccine1[0]-110,4.1, 'First Vaccine Approved')




    plt.xlim(18262.0,18993.0)
    plt.ylim(0,5)

    ax = plt.gca()
    ax.axes.yaxis.set_visible(False)

    plt.title('Government Policy')

    plt.show()
    return

def AB_restriction():
    
    plt.figure(figsize=(6, 6))
    plt.rcParams['font.size'] = '20'
    plt.xticks(rotation = 90, ha='center')
    plt.subplots_adjust(left=0.12, bottom=0.22, right=0.9, top=0.88, wspace=0.2, hspace=0.2)
    
    
    mask1 = [s_2_d('2020-12-08'),s_2_d('2021-07-01')] #Dec 8 2020-July 1 2021
    mask2 = [s_2_d('2021-09-04'),s_2_d('2022-01-01')] #September 4 2021-Present
    travel1 = [s_2_d('2020-03-16'),s_2_d('2022-01-01')] #March 16, 2020 - Present
    school1 = [s_2_d('2020-03-16'),s_2_d('2020-06-30')] #March 16, 2020 - June 30 2020
    school2 = [s_2_d('2020-11-24'),s_2_d('2021-01-11')] #November 24 2020 - Jan 11 2021
    school3 = [s_2_d('2021-04-07'),s_2_d('2021-05-25')] #April 7 2021 - May 25 2021
    school4 = [s_2_d('2022-01-01'),s_2_d('2022-01-10')] #Jan 2022 - ?
    vaccine1 = [s_2_d('2020-12-09')] #Dec 9. 2020 Approved Adults

    plt.plot_date(mask1, [1,1], 'bo-') 
    plt.plot_date(mask2, [1,1], 'bo-') 
    plt.plot_date(travel1, [2,2], 'o-', color='orange') 
    plt.plot_date(school1, [3,3], 'go-') 
    plt.plot_date(school2, [3,3], 'go-') 
    plt.plot_date(school3, [3,3], 'go-') 
    plt.plot_date(school4, [3,3], 'go-') 
    plt.plot_date(vaccine1, [4], 'ro-')


    plt.text(mask1[0],1.1, 'Mask Mandate')
    plt.text(travel1[0]-30,2.1, 'International Travel Restrictions')
    plt.text(school1[0],3.1, 'School Closures')
    plt.text(vaccine1[0]-125,4.1, 'First Vaccine Approved')




    plt.xlim(18262.0,18993.0)    
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
