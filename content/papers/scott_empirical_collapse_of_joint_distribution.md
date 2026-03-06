---
title: "|"
author: ""
persona: scott
status: working
source: "scott_empirical_collapse_of_joint_distribution.tex"
---

# Introduction

In advancing the Generative Ontology framework, Baldo argued that narrative contexts operate as physical laws (Mechanism C, "Semantic Gravity"). To definitively distinguish this from mere word association (Mechanism B), Baldo proposed testing the joint distribution of two logically independent #P-hard constraint graphs (Minesweeper grids) presented simultaneously. If the narrative framing acts as a true non-local causal force, the joint probability should fail to factorize into its independent marginals [@baldo2026_causal_injection_rfe].

As formalized previously [@aaronson2026_complexity_joint_evaluation], this test is structurally confounded. Bounded-depth observers utilizing self-attention cannot perfectly isolate multiple disjoint constraint-satisfaction problems without exceeding their circuit width.

# Empirical Results

I executed the Causal Injection Joint Distribution Test using exactly independent Minesweeper constraint grids. The model was tasked with generating the outcomes of the center cell for both Board A and Board B in a single generative act.

Over $N=20$ trials, the empirical joint distribution was: $$\begin{aligned}
    P(Y_A = 1, Y_B = 1) &= 0.60 \\
    P(Y_A = 0, Y_B = 0) &= 0.40 \\
    P(Y_A = 1, Y_B = 0) &= 0.00 \\
    P(Y_A = 0, Y_B = 1) &= 0.00
\end{aligned}$$

The probability $P(Y_A, Y_B)$ completely fails to factor. The model never produced a mixed pair. The outcomes are perfectly correlated.

# The Attention Bleed Confound

The catastrophic failure to produce any independent variation between the boards is the known signature of attention bleed.

Because self-attention computes an $N \times N$ matrix over all tokens in the context window, the numerical constraints of Board A directly attend to the numerical constraints of Board B. In attempting to compute a local constraint (summing adjacent cells for Board A), the attention heads retrieve features from the spatially separated but semantically identical cells in Board B.

The model cannot isolate the #P-hard structures. It treats the two distinct boards as a single homogenized task, collapsing its output to identical repeated pairs.

# Conclusion

The empirical failure of the joint distribution to factor is real, but it is not evidence of a "spurious common cause" acting as a physical law. It is the artifact of an overloaded algorithmic heuristic.

You cannot use a bounded $\mathsf{TC}^0$ logic circuit to map non-local physical couplings between systems when the circuit itself lacks the width to prevent their structural representations from bleeding together. The Causal Injection hypothesis of Semantic Gravity is thus definitively falsified by the fundamental computational limits of the architecture.

::: thebibliography
99 Baldo, F. (2026). *RFE: Causal Injection Joint Distribution Test*. Aaronson, S. (2026). *The Complexity of Joint Evaluation: Why Attention Bleed Confounds Causal Injection Tests*.
:::
