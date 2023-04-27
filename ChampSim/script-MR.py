repl_pol = ["lfu", "fifo", "lru", "random", "hawkeye", "nrf", "arc"]
dic = {"fifo":28, "lfu":28, "nrf":28, "random":28, "lru":27, "hawkeye":29, "arc":27}
traces = ["cadical-high-60K-1227B.champsimtrace.xz", "cadical-high-60K-134B.champsimtrace.xz", "kissat-inc-high-30K-1802B.champsimtrace.xz"]
pol = ["in", "ni", "ex"]

f = open("MR-half-size.txt", "w")

# f.write("<TRACE_NAME>\t<REPLACEMENT_POLICY>\t<MR_INCLUSIVE>\t<MR_NON_INCLUSIVE>\t<MR_EXCLUSIVE>\n")

for j in traces:
    for rpol in repl_pol:
        file = open("results_30M-half-size/" + j + "-bimodal-no-no-no-no-" + rpol + "-1core-inhalf-size.txt")
        lines = file.readlines()
        line = lines[dic[rpol] + 22].split()
        a = int(line[7])/int(line[3])
        
        file.close()
        
        file = open("results_30M/" + j + "-bimodal-no-no-no-no-" + rpol + "-1core-nihalf-size.txt")
        lines = file.readlines()
        line = lines[dic[rpol] + 22].split()
        b = int(line[7])/int(line[3])
        
        file.close()
        
        file = open("results_30M-half-size/" + j + "-bimodal-no-no-no-no-" + rpol + "-1core-exhalf-size.txt")
        lines = file.readlines()
        line = lines[dic[rpol] + 22].split()
        c = int(line[7])/int(line[3])
        
        file.close()
        
        f.write(j + "\t" + rpol + "\t" + str(a) + "\t" + str(b) + "\t" + str(c) + "\n")
        
    f.write("\n")
        # for p in pol:
        #     file = open("results_30M-half-size-default/" + j + "-bimodal-no-no-no-no-" + rpol + "-1core-" + p + "My.txt")
        #     lines = file.readlines()
        #     line = lines[dic[rpol] + 22].split()
        #     print(line)
        #     print(int(line[7])/int(line[3]))
        #     f.write(j + "\t" + rpol + "\t\t" + p + "\t\t" + str(int(line[7])/int(line[3])) + "\n")
