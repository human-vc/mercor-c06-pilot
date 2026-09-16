import argparse

import itertools

import math

from statistics import NormalDist


import numpy as np


def ppi_halfwidth(n, big_n, sigma, rho, z=1.96):

    lam = rho / (1 + n / big_n)

    var = (lam**2) * sigma**2 / big_n + sigma**2 * (1 - 2 * lam * rho + lam**2) / n

    return z * math.sqrt(var)


def classical_halfwidth(n, sigma, z=1.96):

    return z * sigma / math.sqrt(n)


def author_checks_needed(target, big_n, sigma, rho, z=1.96, n_max=100000):

    for n in range(2, n_max):

        if ppi_halfwidth(n, big_n, sigma, rho, z) <= target:

            return n

    return None


def mean_rank_set_size(k, spread, halfwidth, sims, rng):

    sizes = []

    for _ in range(sims):

        true = rng.normal(0, spread, k)

        est = true + rng.normal(0, halfwidth / 1.96, k)

        lo, hi = est - halfwidth, est + halfwidth

        for i in range(k):

            best = 1 + int(np.sum(lo > hi[i]))

            worst = k - int(np.sum(hi < lo[i]))

            sizes.append(worst - best + 1)

    return float(np.mean(sizes))


def main():

    p = argparse.ArgumentParser()

    p.add_argument("--models", type=int, default=8)

    p.add_argument("--sim-runs", type=int, default=1000)

    p.add_argument("--spread", type=float, default=5.0)

    p.add_argument("--sims", type=int, default=2000)

    p.add_argument("--seed", type=int, default=0)

    a = p.parse_args()

    rng = np.random.default_rng(a.seed)

    z_bonf = NormalDist().inv_cdf(1 - 0.05 / (2 * a.models))

    print(f"models={a.models} simulated runs per model={a.sim_runs} spread of true model means SD={a.spread} points")

    print(f"per-model z for simultaneous 95% coverage (Bonferroni over {a.models}) = {z_bonf:.2f}\n")

    print("author-answered checks per model needed for a given 95% half-width (points), PPI++ vs author-only")

    print(f"{'run SD':>7} {'rho':>5} {'target':>7} {'PPI++ n':>8} {'author-only n':>14} {'saving':>7}")

    for sigma, rho, target in itertools.product([20, 30], [0.3, 0.5, 0.7, 0.9], [2, 3, 5]):

        n_ppi = author_checks_needed(target, a.sim_runs, sigma, rho)

        n_cls = math.ceil((1.96 * sigma / target) ** 2)

        save = f"{100 * (1 - n_ppi / n_cls):.0f}%" if n_ppi else "n/a"

        print(f"{sigma:>7} {rho:>5} {target:>7} {str(n_ppi):>8} {n_cls:>14} {save:>7}")

    print("\nmean plausible-rank-set size (1 = rank pinned) with simultaneous intervals")

    print(f"{'run SD':>7} {'rho':>5} {'n author':>9} {'half-width':>11} {'rank set':>9}")

    for sigma, rho, n in itertools.product([20, 30], [0.5, 0.8], [30, 100, 300]):

        hw = ppi_halfwidth(n, a.sim_runs, sigma, rho, z_bonf)

        size = mean_rank_set_size(a.models, a.spread, hw, a.sims // 10, rng)

        print(f"{sigma:>7} {rho:>5} {n:>9} {hw:>11.2f} {size:>9.2f}")


if __name__ == "__main__":

    main()
