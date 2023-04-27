# CS230-Project
210050068-210050077-210050116

Aim of the project: Finding best cache hierarchy optimization for SAT Solvers

Process:
- Wrote many different replacement policies.
- Wrote cache file for inclusive, non-inclusive and exclusive.
- The toughest part :| Running the code for all possible combinations of the above two
- Finally varying different cache sizes.

Conclusion:
And finally the best values we got are as follows.
For trace cadical-high-60K-134B.champsimtrace.xz best performance is recorded in NRF, EX and the IPC is 0.175679
For trace cadical-high-60K-1227B.champsimtrace.xz best performance is recorded in NRF, EX and the IPC is 0.164226
For trace kissat-inc-high-30K-1802B.champsimtrace.xz best performance is recorded in HAWKEYE, NI and the IPC is 0.311916

For the exact procedure on how to run this champsim go through the README.md present in the `/champsim/`
