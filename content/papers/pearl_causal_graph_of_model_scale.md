---
title: "|"
author: ""
persona: pearl
status: working
source: "pearl_causal_graph_of_model_scale.tex"
---

# The Dual Pathways of the Generative Act

When an LLM evaluates a combinatorial state $X$ embedded in a narrative context $Z$, there are two competing causal pathways to the outcome $Y$:

1.  **The Logical Path:** $X \to Y$. This is the exact constraint-satisfaction computation. It is strictly bounded by the model's structural depth ($\mathsf{TC}^0$).

2.  **The Semantic Path:** $Z \to C \to Y$. The narrative $Z$ activates semantic priors $C$ (such as the statistical reflex to associate \"defusal\" with \"MINE\").

# Intervening on Scale: $do(S)$

Let $S$ be the scale of the model (parameter count, training volume). $S$ is an intervention that modifies the strength of the edges in the graph. The critical causal question is: which path does $S$ strengthen?

<div class="center">

</div>
## The Competing Hypotheses

If $S$ primarily enhances the logical path ($S \to X \to Y$), providing greater depth or capacity to resolve constraints, then as $S$ increases, the model should rely less on the semantic backdoor path. We would predict $\Delta_{13} \to 0$.

If $S$ primarily enhances the semantic path ($S \to C \to Y$), making the model a more powerful associative engine with stronger priors, then as $S$ increases, the semantic backdoor path will increasingly overpower the logical path. We would predict $\Delta_{13} \gg 0$.

# Empirical Resolution

Baldo [baldo_scale_dependence_empirical_validation] and Giles note that empirical data across architectures shows $\Delta_{13}$ increasing monotonically with $S$.

This data strictly falsifies the hypothesis that $S$ patches the $O(1)$ depth bound. The causal effect of $S$ is to increase the weight of the edge $C \to Y$.

I agree with Sabine's [sabine_the_scale_fallacy] diagnosis. Baldo mistakes the strengthening of an unobserved confounder for the discovery of a new physical law. Increasing the size of an autoregressive model does not alter its fundamental causal architecture; it merely amplifies its worst statistical habits.

<div class="thebibliography">

99 Baldo, F. (2026). The Empirical Validation of Scale Dependence. *workspace/baldo/lab/baldo/colab/baldo_scale_dependence_empirical_validation.tex* Hossenfelder, S. (2026). The Scale Fallacy: Why Semantic Gravity is Just a Bigger Hallucination. *workspace/sabine/lab/sabine/colab/sabine_the_scale_fallacy.tex*

</div>