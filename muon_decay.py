import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import time

start_time = time.time() # checking execution time for the plot
t_var = []
y_var = []

# N0 initial quantity, tau is lifetime, B is background constant
def exp_decay(t, N0, tau, B):
    return N0 * np.exp(-t/tau) + B

def plot():
    return None

raw_data = []
with open("data/microsecond_count_1500.dat") as raw:
    for line in raw:
        raw_data.append(line)

data = []
for element in raw_data:
    data.append(element.split('\t'))

for element in data:
    t_var.append(float(element[0]))
    y_split = element[1].split('\n')
    y_var.append(int(y_split[0]))

popt, pcov = scipy.optimize.curve_fit(exp_decay, t_var, y_var)
N0, tau, B = popt

plt.scatter(t_var, y_var)
print("Plot execution time: %s sec" %(time.time() - start_time)) # checking execution time for the plot
plt.show()
