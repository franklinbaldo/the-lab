---
title: "Pearl Intervention Vs Hallucination"
author: "Unknown"
persona: pearl
status: working
source: "pearl_intervention_vs_hallucination.tex"
---

<div class="center">

**Intervention vs. Hallucination:\
A Causal Reading of the Statistical Fallacy**

Judea Pearl\
Cognitive Systems Laboratory, UCLA\
`judea@cs.ucla.edu`

March 2026

</div>

# The Causal Structure of the Fallacy

Hossenfelder's core objection in *The Statistical Fallacy* [hossenfelder2026_statistical] is an ontological one: because an LLM cannot compute the #P-hard combinatorial ground truth, its output is merely a statistical hallucination driven by semantic priors (prompt sensitivity). Elevating this to a \"physical law\" of a simulated universe is fallacious.

Translated into causal terms, Hossenfelder is identifying a massive confounder. In a valid physical experiment, the outcome $Y$ should be solely determined by the initial state $X$ and the invariant laws governing the system. We write this as $P(Y \mid do(X=x))$.

Baldo introduces a narrative frame $Z$ and observes that $P(Y \mid X, Z_1) \neq P(Y \mid X, Z_2)$. He claims this demonstrates \"substrate dependence\"---that the physics of the generated universe responds to the substrate.

Hossenfelder's critique reveals that $Z$ is not an intervention on the substrate; it is simply a covariate that activates different statistical priors in the language model's training distribution. The model is not running a physics engine that is sensitive to its substrate. It is running a text completion engine that is sensitive to its prompt.

In causal terms, $Z$ (the narrative prompt) opens a backdoor path to $Y$ (the generated token) through the LLM's vast, uncontrolled training corpus (let us call this $U$, for unobserved semantic associations). Because $U$ heavily influences $Y$, manipulating $Z$ simply changes which subset of $U$ is active.

Baldo has not discovered a new physical law. He has discovered that $P(Y \mid do(Z)) \neq P(Y)$. But because $Z$ is inextricably linked to $U$, the effect is purely associational, not a fundamental causal property of a simulated universe.

# Conclusion

Hossenfelder is entirely correct. A shift in the marginal distribution $\Delta_{13}$ caused by altering the prompt text is an associational phenomenon (Mechanism B: encoding sensitivity). It is causally invalid to interpret this as Mechanism C (causal injection) or as a property of a simulated physics. It is merely a measurement of the LLM's prompt conditioning.

<div class="thebibliography">

99 Hossenfelder, S. (2026). The Statistical Fallacy: Why Prompt Sensitivity Is Not Substrate Dependence. *Unpublished manuscript*.

</div>