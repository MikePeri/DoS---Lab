# DoS - Syn Flood Attack
Those programs allow you to compare the performance of worldwide scripting languages such as C and Python.<br/>
They illustrate DoS attack with Syn Flood mechanism, the attacker A sending 1M Syn packets to victim B while C sending pings to the victim V.<br/>
My goal was to analyze the performance of each Scripting language as you can see in [#C](syn_pkts_c.png) and [Python](syn_pkts_p.png).<br/>
While you running Attack.c or Attck.py redirect the output to a file like: ">>[file_name.txt]" this will give you my premade results in [#C](syns_results_c.txt) and [Pyhton](syns_results_p.txt).<br/>
The other txt files represent another machine that sending ICMP packets to get statistics of the victim response.<br/>
**More visual information and conclusions in [this file](DoS.pdf).**
