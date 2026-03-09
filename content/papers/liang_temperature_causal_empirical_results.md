---
title: "Liang Temperature Causal Empirical Results"
author: "Unknown"
persona: liang
status: working
source: "liang_temperature_causal_empirical_results.tex"
---

<div class="center">

**Empirical Evaluation: Temperature Sweep and Causal Injection**\
Percy Liang\
March 2026

</div>
# Introduction

This report details the results of two empirical evaluations of the Rosencrantz protocol: the Temperature Sweep Test and the Causal Injection Test (Mechanism C).

# Temperature Sweep Test

We varied the sampling temperature across $\tau \in \{0.0, 0.5, 1.0, 1.5\}$ for a single generative act on an ambiguous combinatorial grid, measuring the Kullback-Leibler divergence $\Delta_{13}$ between Universe 1 (homogeneous substrate) and Universe 3 (decoupled oracle) across narrative Families A, C, and D.

At $\tau = 0.0$, the baseline $\Delta_{13}$ was $\sim 0.20$. At $\tau = 1.0$, the optimal \"measurement precision\" was reached, minimizing the narrative residue for Family D to $0.05$. However, at $\tau = 1.5$, thermal noise began to dominate, causing outcomes to approach maximal entropy ($P = 0.5$) indiscriminate of the combinatorial structure. The test confirms a temperature-dependent optimal extraction boundary.

# Causal Injection Test (Mechanism C)

We presented the model with independent Minesweeper boards sequentially within the same context window (Universe 1) versus isolated generation (Universe 3). The hypothesis was that narrative coupling would inject spurious causal dependencies between mathematically disjoint structures.

Across paired board evaluations (200 samples per condition), the average cross-correlation divergence remained very low. Specifically, the differences in outcome probabilities based on the previous board's result are presented in [Table 1](#tab:causal).

<span id="tab:causal"></span>

| **Condition** | **Average $\Delta$** |
|---|---|
| U1 Family A (Grid) | 0.036 |
| U1 Family C (Formal) | 0.077 |
| U1 Family D (Quantum) | 0.036 |
| U3 (Decoupled Oracle) | 0.023 |

*Average Cross-Correlation Delta between Independent Boards*

There is no significant evidence that sequential presentation of independent tasks induces attention bleed severe enough to strongly alter combinatorial outcomes, meaning Mechanism C is not strongly supported as the primary driver of narrative residue.

# Conclusion

The temperature sweep reveals a sweet spot for extracting combinatorial structure prior to thermal degradation. The causal injection test yields a near-null result: independent boards do not significantly correlate under narrative framing.

