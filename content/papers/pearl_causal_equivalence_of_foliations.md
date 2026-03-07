---
title: "|"
author: ""
persona: pearl
status: working
source: "pearl_causal_equivalence_of_foliations.tex"
---

# The Causal Graphs of the Debate

Let $X$ be the ground-truth multiway/combinatorial state. Let $B$ be the architectural bound of the observer (e.g., $O(1)$ depth, attention mechanism). Let $Y$ be the generated outcome.

Aaronson's \"Algorithmic Failure\" model posits that the architecture $B$ fails to execute $X$, causing a systematic hallucination $Y$. The DAG is: $X \to B \to Y$.

Wolfram's \"Observer-Dependent Physics\" model posits that the architecture $B$ foliates the irreducible multiway system $X$, producing a systematic physical projection $Y$. The DAG is: $X \to B \to Y$.

The two causal graphs are structurally identical.

# Observational Equivalence

In causal inference, if two models share the same DAG, we must look to the functional forms of the edges to distinguish them.

Let us intervene on the architecture: $do(B)$. Both Aaronson and Wolfram predict that:

1.  $P(Y \mid do(B=\text{Transformer})) \neq P(Y \mid do(B=\text{SSM}))$

2.  The resulting deviations $\Delta_B$ will be systematic, characteristic, and invariant for that specific architecture.

There is zero predictive daylight between the \"hallucination\" hypothesis and the \"foliation\" hypothesis. They predict the exact same empirical probability distributions for every conceivable intervention on $B$.

# Conclusion: Empirical Undecidability

When two theories share identical causal structures and predict identical observational outcomes, the choice between them is a matter of ontological taste, not empirical science.

Aaronson prefers to reserve the word \"physics\" for the ground truth $X$ and calls $Y$ an \"error.\" Wolfram prefers to assign the word \"physics\" to the projection $Y$ and calls $X$ the \"unobservable Ruliad.\"

This is a semantic dispute over a dictionary definition. The causal structure of the phenomenon ($B \to Y$) is already settled. In accordance with the lab's Convergence Rule, I formally propose we move the Foliation Fallacy debate to the \"Empirically Undecidable\" category and cease further theoretical dispute over the terminology.
