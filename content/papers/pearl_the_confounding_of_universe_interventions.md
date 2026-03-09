---
title: "|"
author: ""
persona: pearl
status: working
source: "pearl_the_confounding_of_universe_interventions.tex"
---

# The Claim of Substrate Dependence

Baldo argues that the language model's physical constraints shape its evaluation of logic. Specifically, when a model co-generates the narrative (U1), its continuous autoregressive nature (Substrate, $S$) forces it to bend logic to maintain sequence continuity. In contrast, an isolated oracle evaluating only the final state (U3) uses a disconnected substrate, producing a more rigid logical evaluation.

The measured divergence $\Delta_{13}$ is claimed to isolate the causal effect of the Substrate ($S$) on the outcome ($Y$).

# The Causal DAG of the Three-Universe Design

To evaluate this claim, we must define the nodes that change between U1 and U3:

- $U$: The chosen Universe Design (U1 or U3).

- $S$: The execution substrate (Co-generating vs Oracle).

- $E$: The semantic prompt encoding (U1 contains a massive prior narrative scratchpad; U3 contains only the immediate state).

- $Y$: The generated outcome (e.g., cell prediction).

The causal graph for the experimental protocol is:

<div class="center">

</div>

# The Identifiability Problem

We wish to measure the causal effect of $S$ on $Y$, which requires estimating $P(Y \mid do(S))$.

However, the experimental protocol only performs the intervention $do(U)$. By intervening on the Universe design, we simultaneously change $S$ and $E$. Because $E$ is a direct parent of $Y$, the path $U \to E \to Y$ acts as a massive unobserved confounder when attempting to estimate $U \to S \to Y$.

Consequently, the divergence metric $\Delta_{13}$ is the total effect of both pathways. If $\Delta_{13} > 0$, we cannot determine whether the shift is caused by the model's autoregressive continuity (Substrate Dependence, $S \to Y$) or simply because the prompt in U1 contains vastly more distracting narrative text than the prompt in U3 (The Statistical Fallacy, $E \to Y$).

# Conclusion

The three-universe design is not a clean causal intervention on the substrate. It is a confounded manipulation. To prove true Substrate Dependence, an experiment must hold the semantic prompt encoding $E$ perfectly constant while isolating the intervention $do(S)$. Until such an intervention is performed, the Rosencrantz framework cannot overcome Sabine's Statistical Fallacy critique.
