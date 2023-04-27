
repl_pol = ["lfu", "fifo", "lru", "random", "hawkeye", "nrf", "arc"]
dic = {"fifo":28, "lfu":28, "nrf":28, "random":28, "lru":27, "hawkeye":29, "arc":27}
traces = ["cadical-high-60K-1227B.champsimtrace.xz", "cadical-high-60K-134B.champsimtrace.xz", "kissat-inc-high-30K-1802B.champsimtrace.xz"]
pol = ["in", "ni", "ex"]


f = open("IPC-half-size.txt", "w")

f.write("<TRACE_NAME>\t<REPLACEMENT_POLICY>\t<IPC_INCLUSIVE>\t<IPC_NON_INCLUSIVE>\t<IPC_EXCLUSIVE>\n")

for j in traces:
    for rpol in repl_pol:
        file = open("results_30M/" + j + "-bimodal-no-no-no-no-" + rpol + "-1core-inhalf-size.txt")
        lines = file.readlines()
        line = lines[dic[rpol]].split()
        a = line[4]
        
        file.close()
        
        file = open("results_30M/" + j + "-bimodal-no-no-no-no-" + rpol + "-1core-nihalf-size.txt")
        lines = file.readlines()
        line = lines[dic[rpol]].split()
        b = line[4]
        
        file.close()
        
        file = open("results_30M/" + j + "-bimodal-no-no-no-no-" + rpol + "-1core-exhalf-size.txt")
        lines = file.readlines()
        line = lines[dic[rpol]].split()
        c = line[4]
        
        file.close()
        
        
        f.write(j + "\t" + rpol + "\t" + a + "\t" + b + "\t" + c + "\n")
        print(j + "\t" + rpol + "\t" + a + "\t" + b + "\t" + c)
    f.write("\n")
        
f.close()