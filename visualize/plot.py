import sys
import re
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import rc


def split_on_empty_lines(s):
    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"
    return re.split(blank_line_regex, s.strip())


def extract_two_columns(line):
    first = np.array([eval(line[i].split(',')[0]) for i in range(len(line))])
    second = np.array([eval(line[i].split(',')[1]) for i in range(len(line))])
    return first, second


def plot_xy_graph(title, xlabel, ylabel, label, line, dirname='res/', postfix='-res-vs-time.pdf'):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    res, time = extract_two_columns(line)
    time = time.cumsum()

    plt.plot(time, res, label=label)
    plt.legend(loc='center left')
    plt.yscale('log')

    plt.savefig(dirname + args[1] + postfix, bbox_inches='tight')
    plt.clf()


rc('text', usetex=True)
params = {'text.latex.preamble': [
    r'\usepackage{bm}']}
plt.rcParams.update(params)

args = sys.argv
if len(args) == 1:
    sys.exit(1)
    # no argument

# for omega in ["0.50", "0.75", "1.00", "1.50", "1.60", "1.70", "1.80"]:
#     f = open("res/" + args[1] + "-result-omega-" + omega + ".txt")
#     lines = f.readlines()
#     f.close()

#     sns.set_context('talk')

#     res = np.array([eval(lines[i].split(',')[0]) for i in range(500)])
#     plt.title("A: Poisson matrix (128 x 128), b: random vector")
#     plt.plot(res, label=r'$\omega = $' + omega)

f = open("res/" + args[1] + "-result.txt")
lines = split_on_empty_lines(f.read())
f.close()

line = lines[0].split('\n')
res, time = extract_two_columns(line)
time = time.cumsum()

line_omp = lines[1].split('\n')
res_omp, time_omp = extract_two_columns(line_omp)
time_omp = time_omp.cumsum()

plt.title('A: Poisson matrix (64 x 64), b: random vector')
plt.xlabel('time [ms]')
plt.ylabel(r'residue $ \|\bm{A}\bm{x} - \bm{b}\| / \|\bm{b}\| $')

sns.set_context('talk')

plt.plot(time, res, label='single thread')
plt.plot(time_omp, res_omp, label='4 threads (OpenMP)')

plt.yscale('log')
plt.legend(loc='upper right')
plt.savefig('res/' + args[1] + '-residue-Poisson.pdf', bbox_inches='tight')
plt.clf()
