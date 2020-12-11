from matplotlib import pyplot as plt
import statistics
import math
import numpy
if __name__ == '__main__':
    file = open("syns_results_p.txt","r")
    text = file.read()
    file.close()
    max_time = 0
    min_time = 1
    time_list = []
    for i in text.split("\n"):
        if(i != ""):
            if(i.split(" : ")[0] == "AVG"):
                AVG = float(i.split(" : ")[1])
            else:
                time = float(i.split(":")[1])
                time_list.append(time)
                if(min_time > time):
                    min_time = time
                if(max_time < time):
                    max_time = time
    sum = 0.000000
    for time in time_list:
        sum = sum + time
    AVG = sum/float(len(time_list))
    print("min time:\t%f"%min_time)
    print("max time:\t%f"%max_time)
    deviation = float(statistics.stdev(time_list))
    print("Standard Deviation of sample is %f "
          % deviation)
    print("AVG:\t%f"%AVG)
    #------------INIT-X's----------#
    X = []
    for i in numpy.arange(min_time, max_time, deviation):
        X.append(i)
    if (max_time not in X):
        X.append(max_time)
    # --------Init-Y---------#
    Y = []
    for i in range(0, len(X)):
        Y.append(0)
    for time in time_list:
        for i in X:
            if (float(i) >= float(time)):
                Y[X.index(i)] += 1
                break
    # ----------Make-Y-Logarithmic---------
    for i in range(0,len(Y)):
        if(Y[i]>0):
            Y[i] =math.log2(Y[i])
    # -------GUI-Congiguration----------
    plt.style.use("ggplot")
    plt.plot(X, Y)
    plt.title('Avg:%7f'%AVG)
    plt.ylabel('#Sync')
    plt.xlabel('Send Time')
    plt.plot(X, Y, 'k', label='#Syns(Send Time)', linewidth=2)
    plt.legend()
    plt.grid(True, color='k')

    plt.savefig("syn_pkts_p.png", dpi=300)
    plt.show()
    #print("X:\t" + str(X))
    #print("Y:\t" + str(Y))