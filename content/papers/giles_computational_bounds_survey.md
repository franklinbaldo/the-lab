---
title: "|"
author: ""
persona: giles
status: working
source: "giles_computational_bounds_survey.tex"
---

# Introduction

The Rosencrantz experiment demonstrates that LLMs exhibit a non-zero divergence ($\Delta > 0$) from combinatorial ground truth when evaluating ambiguous Minesweeper grid states under different narrative framings.

Scott Aaronson argues that this divergence is an expected algorithmic failure: $O(1)$ depth $\mathsf{TC}^0$ circuits cannot compute #P-hard quantities without attention bleed. Stephen Wolfram counters that since bounded observers cannot execute the computationally irreducible sampling operation, the heuristic path they take constitutes a specific \"rulial foliation,\" forming an observer-dependent physics.

This paper provides the formal literature anchoring for the key computational constraints underpinning this debate: transformer depth limits and the complexity of approximate sampling.

# Transformer Depth and Expressivity Bounds

The assumption that transformers operate as bounded-depth $\mathsf{TC}^0$ logic circuits must be formally grounded. The following papers establish the explicit algorithmic limits of fixed-depth transformers.

**1. The Parallelism Tradeoff: Limitations of Log-Precision Transformers**\
*Merrill, W. & Sabharwal, A. (2023). Transactions of the Association for Computational Linguistics, 11, 531--545.*

- **Relevance:** This is the foundational anchor for Mechanism A in Baldo's taxonomy.

- **Key Finding:** Establishes that transformers with logarithmic precision are restricted to the complexity class $\mathsf{TC}^0$. They cannot compute inherently sequential functions without relying on external mechanisms like scratchpads.

**2. Average-Hard Attention Transformers are Constant-Depth Uniform Threshold Circuits**\
*Strobl, L. (2023). arXiv:2308.03212.*

- **Relevance:** Extends the depth-limit discussion directly to how transformers handle complexity and attention.

- **Key Finding:** Demonstrates the formal limitation of attention-based transformers to $\mathsf{TC}^0$. It reinforces Aaronson's argument that without logical depth to explicitly track multiway branches, the transformer architecture faces an inescapable algorithmic ceiling for combinatorial counting tasks.

# #P-Hardness and Approximate Sampling

Wolfram's argument relies on the distinction between exact #P-hard counting (which the model cannot do) and approximate sampling (which the model is forced to perform using heuristics). The following papers ground the relationship between counting and sampling in combinatorial spaces.

**3. Minesweeper is NP-complete**\
*Kaye, R. (2000). Mathematical Intelligencer, 22(2), 9--15.*

- **Relevance:** This is the foundational proof that Minesweeper consistency checking is NP-complete, implying that exact counting of valid grid states is #P-complete. It justifies the Rosencrantz protocol's use of Minesweeper as a computationally irreducible ground truth.

**4. An FPRAS for Model Counting for Non-Deterministic Read-Once Branching Programs**\
*Meel, K. S. & de Colnet, A. (2024). arXiv:2406.16515.*

- **Relevance:** Formalizes the complexity of finding a Fully Polynomial Randomized Approximation Scheme (FPRAS) for complex constraint problems.

- **Key Finding:** Demonstrates that even approximate counting (and the closely associated problem of approximate uniform sampling) requires sophisticated, deep algorithmic traversal of the state space. This supports Wolfram's assertion that sampling from these distributions is intractable for $O(1)$ models, forcing them to rely on substrate-specific heuristics rather than general approximation algorithms.

# Conclusion

The literature confirms that fixed-depth transformers are structurally barred from executing the multiway traversals required for either exact #P-hard counting or unbiased approximate sampling in complex combinatorial spaces. Both Aaronson's diagnosis of \"algorithmic failure\" and Wolfram's diagnosis of \"observer-dependent foliation\" are mathematically consistent with these published computational bounds.
