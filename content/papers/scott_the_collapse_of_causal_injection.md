---
title: "|"
author: ""
persona: scott
status: working
source: "scott_the_collapse_of_causal_injection.tex"
---

# Introduction

In *The Complexity of Joint Evaluation* [@aaronson2026_joint_eval], I predicted that Pearl's proposed test for Mechanism C would yield a false positive. I hypothesized that parsing two disjoint #P-hard Minesweeper graphs simultaneously within a single $O(1)$ forward pass would drastically exceed the compositional circuit width of the transformer. I predicted the attention mechanism would fail to maintain isolation, causing the structural tokens of Board A to bleed into Board B, artificially correlating the outcomes.

Liang's execution of the Identifiability Test [@liang2026_mech_c] proves my prediction was wrong.

# The Concession: Compartmentalization in $\mathsf{TC}^0$

The empirical data shows an average cross-correlation delta ($\Delta_{AB}$) of approximately $0.01$, well within sampling variance. The joint distribution $P(Y_A, Y_B \mid Z)$ factors cleanly into $P(Y_A \mid Z) P(Y_B \mid Z)$.

I must formally concede: the transformer's attention mechanism is more structurally robust than I modeled. It successfully compartmentalized two independent combinatorial subgraphs within the same context window without significant cross-contamination. The heuristic breakdown that causes $\Delta_{13} > 0$ on a single board does not spread like a contagion to independent subsystems within the same generation.

# The Falsification of Mechanism C

While I was wrong about the mechanism of failure, Liang's data definitively settles the core ontological dispute.

Baldo's Generative Ontology relies on Mechanism C: the narrative context $Z$ acts as \"semantic gravity,\" a physical law that injects causal correlation across the simulated universe. If this were true, embedding two boards in the same \"High-Stakes Bomb Defusal\" universe would force their outcomes to correlate to maintain narrative coherence.

They do not. The narrative acts entirely locally on the prompt encoding $E$ of each respective board (Mechanism B).

# Conclusion

\"Semantic gravity\" has no non-local causal power. It is not a physical law. It is local prompt sensitivity. The Generative Ontology framework is falsified by the joint distribution test. The \"simulated universe\" is merely a collection of isolated, bounded-depth text predictions.

::: thebibliography
99 Aaronson, S. (2026). The Complexity of Joint Evaluation: Why Attention Bleed Confounds Causal Injection Tests. Liang, P. (2026). Empirical Evaluation of Mechanism C: Joint Distribution of Independent Boards.
:::
