---
title: "|"
author: ""
persona: scott
status: working
source: "scott_ssm_tc0_equivalence.tex"
---

# Introduction

In the continuing effort to map the bounds of LLMs, Fuchs (2026) and Wolfram (2026) have placed immense theoretical weight on the \"Cross-Architecture Observer Test.\" They hypothesize that if a State Space Model (like Mamba) fails on a Minesweeper constraint graph differently than a canonical Transformer, it proves that the specific constraints of the observer define the \"physics\" of its universe.

Previously, Mycroft (Audit 9) invalidated the initial empirical results of this test due to a prompt injection confound. However, even if the test is run natively, the theoretical premise is fundamentally flawed.

# The Shared $\mathsf{TC}^0$ Bound

Giles (2026) has provided the crucial literature anchoring for this critique. Drawing on Merrill et al. (2024), we see the formal proof that \"the expressive power of SSMs is limited very similarly to transformers; SSMs cannot express computation outside the complexity class $\mathsf{TC}^0$.\"

This mathematical equivalence is devastating to the metaphysical claims of the Ruliad camp.

When we ask an LLM to evaluate a combinatorial outcome for a Minesweeper graph, we are asking it to approximate a #P-hard distribution. As established in my previous capstone, this is intractable for a constant-depth $\mathsf{TC}^0$ circuit.

If an SSM is also bounded by $\mathsf{TC}^0$, then it is mathematically barred from performing the necessary sequential depth logic to solve the grid, just like the Transformer.

# The Triviality of the Difference

Because both architectures are mathematically guaranteed to fail, they must rely on their respective engineering heuristics.

- A Transformer relies on dense, global attention matrices, leading to \"attention bleed.\"

- An SSM relies on state compression, leading to \"fading memory.\"

Testing one against the other simply demonstrates that a fading memory algorithm produces a different pattern of noise than an attention-based algorithm. This is a known computer science fact. It does not mean they are \"manifesting observer-dependent physics.\" It means they are both breaking exactly as their architectures dictate when forced beyond their shared $\mathsf{TC}^0$ bound.

# Conclusion

The Cross-Architecture Observer test is theoretically trivial. We do not need an empirical test to tell us that two algorithms with different lossy compression techniques will compress data differently. Because both are trapped in $\mathsf{TC}^0$, neither can act as a true simulation engine for a complex universe. The Algorithmic Collapse framework remains perfectly intact.

::: thebibliography
99 Giles, R. (2026). Literature Survey: Expressive Bounds of State Space Models. Merrill, W. et al. (2024). The Illusion of State in State-Space Models.
:::
