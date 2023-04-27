<p align="center">
  <h1 align="center"> ChampSim </h1>
  <p> ChampSim is a trace-based simulator for a microarchitecture study. You can sign up to the public mailing list by sending an empty mail to champsim+subscribe@googlegroups.com.<p>
</p>

# Clone ChampSim repository

```
git clone https://github.com/ChampSim/ChampSim.git
```

# Compile

ChampSim takes eight parameters: Branch predictor, L1D prefetcher, L2C prefetcher, LLC replacement policy, and the number of cores.
For example, `./build_champsim.sh bimodal no no lru 1` builds a single-core processor with bimodal branch predictor, no L1/L2 data prefetchers, and the baseline LRU replacement policy for the LLC.

```
$ ./build_champsim.sh bimodal no no no no lru 1 ex

$ ./build_champsim.sh ${BRANCH} ${L1I_PREFETCHER} ${L1D_PREFETCHER} ${L2C_PREFETCHER} ${LLC_PREFETCHER} ${LLC_REPLACEMENT} ${NUM_CORE} ${CACHE_CONFIG}

${CACHE_CONFIG} : It can take 3 values: in(for inclusive), ni(for Non-inclusive) and ex(exclusive)
${LLC_REPLACEMENT} : We have implemented 6 LLC Replacement policies. They are lru, lfu, fifo, nrf, hawkeye, random
```

# Traces

To run a trace, It has to be placed in folder named traces located outside our present working directory. Or else You can go to the `run_champsin.sh` file and change `TRACE_DIR` to your required

# Run simulation

Execute `run_champsim.sh` with proper input arguments. The default `TRACE_DIR` in `run_champsim.sh` is set to `$PWD/../traces`. `<br>`

The Code We've implemented is for the single core/`NUM_CORE` in above compilation is 1. So Run `run_champsim.sh` as follows

```
Usage: ./run_champsim.sh [BINARY] [N_WARM] [N_SIM] [TRACE] [OPTION]
$ ./run_champsim.sh bimodal-no-no-no-no-lru-1core-ex 1 10 400.perlbench-41B.champsimtrace.xz

${BINARY}: ChampSim binary compiled by "build_champsim.sh" (bimodal-no-no-lru-1core)
${N_WARM}: number of instructions for warmup (1 million)
${N_SIM}:  number of instructinos for detailed simulation (10 million)
${TRACE}: trace name (400.perlbench-41B.champsimtrace.xz)
${OPTION}: extra option for "-low_bandwidth" (src/main.cc)
```

Simulation results will be stored under `results_${N_SIM}M` as a form of `${TRACE}-${BINARY}-${OPTION}.txt`.`<br>`

# Add your own branch predictor, data prefetchers, and replacement policy

**Copy an empty template**

```
$ cp branch/branch_predictor.cc branch/mybranch.bpred
$ cp prefetcher/l1d_prefetcher.cc prefetcher/mypref.l1d_pref
$ cp prefetcher/l2c_prefetcher.cc prefetcher/mypref.l2c_pref
$ cp prefetcher/llc_prefetcher.cc prefetcher/mypref.llc_pref
$ cp replacement/llc_replacement.cc replacement/myrepl.llc_repl
```

**Work on your algorithms with your favorite text editor**

```
$ vim branch/mybranch.bpred
$ vim prefetcher/mypref.l1d_pref
$ vim prefetcher/mypref.l2c_pref
$ vim prefetcher/mypref.llc_pref
$ vim replacement/myrepl.llc_repl
```

**Compile and test**

```
$ ./build_champsim.sh mybranch mypref mypref mypref myrepl 1
$ ./run_champsim.sh mybranch-mypref-mypref-mypref-myrepl-1core 1 10 bzip2_183B
```

# Evaluate Simulation

ChampSim measures the IPC (Instruction Per Cycle) value as a performance metric. `<br>`

You can also have the values of LLC HIT, ACCESS, MISS, with which you can calculate the miss rate.
There are some other useful metrics printed out at the end of simulation. `<br>`

Good luck and be a champion! `<br>`

# Some Modifications

`run.sh` 

You can look into this run.sh file. You can change the values in it and run it for different traces, replacement policies and different cache policies at the same time just by running this file.

`script-IPC.py`

Running this file will get you the list of IPC after you run the `run.sh` file. Make sure you check properly before running it. It may lead to many errors otherwise. Similarly you have `script-MR.py`
