import pingparsing
import numpy
import math
from matplotlib import pyplot as plt
if __name__ == '__main__':
    file = open("pings_results_p.txt","r")
    text = file.read()
    file.close()

    parser = pingparsing.PingParsing()
    stat = parser.parse(text)
    result = stat.as_dict()

    min_rtt = float(result.get("rtt_min"))
    print("Min RTT:\t%f"%min_rtt)
    max_rtt = float(result.get("rtt_max"))
    print("Max RTT:\t%f"%max_rtt)
    deviation = float(result.get("rtt_mdev"))
    print("Deviation:\t%f"%deviation)
    AVG = float(result.get("rtt_avg"))
    print("Avg:\t%f" % AVG)
    if(deviation<1):
        deviation=1
    #---------Init-X-----------#
    x = []
    for i in numpy.arange(min_rtt,max_rtt,deviation):
        x.append(i)
    if(max_rtt not in x):
        x.append(max_rtt)
    #--------Init-Y---------#
    y = []
    for i in range(0,len(x)):
        y.append(0)
    for time in stat.icmp_replies:
        for i in x:
            if(float(i)>=float(time['time'])):
                y[x.index(i)] += 1
                break
    # ----------Make-Y-Logarithmic---------
    for i in range(0, len(y)):
        if (y[i] > 0):
            y[i] = math.log2(y[i])
    #-------GUI-Congiguration----------
    plt.style.use("ggplot")
    plt.plot(x, y)
    plt.title('Avg:%f'%AVG)
    plt.ylabel('#Pings')
    plt.xlabel('RTT')
    plt.plot(x ,y , 'k', label='#Pings(RTT)', linewidth=2)
    plt.legend()
    plt.grid(True,color='k')
    plt.savefig("pings_p.png", dpi=300)
    plt.show()
