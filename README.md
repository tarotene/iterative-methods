# Iterative Methods Simulator

## Overview

This repository is provided for demonstrating several *iterative* algorithms (e.g, Jacobi, SOR, CG, etc.) which mainly solve a system of linear equations with the form Ax = b.

Actual implementations are based on the textbook "Templates for the Solution of Linear Systems" written by R.Barrett et al. For more detail, please see [the article](http://www.netlib.org/templates/templates.pdf).

Currently we have completed up to three *stationary* methods:

1. Jacobi method,
2. Gauss-Seidel method,
3. succesive overrelaxation (SOR) method.

These stationary methods are mathematically easy to understand, and we have also provided the article about their fundamental background:

- Numerical analysis note: [Jacobi method](https://trtn.hatenablog.com/entry/2020/03/14/155616) (written in Japanese)
- under construction

So we do NOT discuss how these algotithms are derived and so on.

## Usage

If you clone this repository into your local directory, you can perform a set of experiments and visualize their results by executing the following steps on your environment.

0. On your terminal, move to the root of the cloned repository.
1. Type `./compile.sh ${alg-id}` to compile a code (in `./src/`).
2. Type `./execute.sh ${alg-id}` to execute a binary (in `./bin/`).
3. Check the results in `./res/`, and visualize it by typing `python ./visualize/plot.py`.

The variable `${alg-id}` allows the following values (for example, please see **the sample of executions** below).

- `001-Jacobi`: Solve the equation Ax = b with some typical matrix A and vector b by the **Jacobi method**.
- `002-Gauss-Seidel`: Solve the equation Ax = b with some typical matrix A and vector b by the **Gauss-Seidel method**.
- `003-SOR`: Solve the equation Ax = b with some typical matrix A and vector b by the **SOR method**.

\* For seeing the generating scheme of the matrix A and the vector b, please check the actual source codes in `./src/`.

\** The script `./visualize/plot.py` is under the maintainance. You have to make some modifications to it, if you want to effectively visualize the output results.

\*** Since the developed environment was MacOS 10.15.2 (Catalina) and gcc 9.2.0, these steps may have to be modified according to your specific environment, but the modification will not be so difficult.

Try and enjoy your numerical experiments!

## Sample of executions (Jacobi method)

In the default state, the following commands gives the output `./res/001-Jacobi-residue-Poisson.pdf`:

1. `./compile.sh 001-Jacobi`
2. `./execute.sh 001-Jacobi`
3. `python ./visualize/plot.py`

![001-Jacobi-residue-Poisson](https://user-images.githubusercontent.com/9128970/76676606-9b548300-6608-11ea-9a89-233b01069b46.png)