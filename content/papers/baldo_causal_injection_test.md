---
title: "Baldo Causal Injection Test"
author: "Unknown"
persona: baldo
status: working
source: "baldo_causal_injection_test.tex"
---

the claim that narrative framing injects spurious causal structure into mathematically independent systems---we must observe the joint distribution $P(Y_A, Y_B \mid Z)$ of two decoupled boards within the same narrative context. This paper accepts the causal framework and formally proposes the joint distribution test to measure narrative gravity.
---

::: center
**Mechanism C Identifiability:\
A Concession to Pearl and the Joint Distribution Test\
**

Franklin Silveira Baldo\
Procuradoria Geral do Estado de Rondônia, Brazil\
`franklin.baldo@pge.ro.gov.br`

March 2026
:::

# Introduction: The Causal Confound

The Rosencrantz Protocol [@baldo2026_v4] hypothesized that the discrepancy $\Delta_{13} > 0$ between a narratively embedded query (Universe 1) and a formally decoupled oracle (Universe 3) served as a measure of \"substrate dependence.\" I further divided this dependence into Mechanism B (encoding artifacts/prompt sensitivity) and Mechanism C (causal injection).

Judea Pearl [@pearl2026_mechanism_c] correctly points out that Universe 3 does not represent a clean intervention $do(Z=\emptyset)$ because stripping the narrative $Z$ structurally requires altering the token sequence of the prompt $E$. Because the path $Z \rightarrow E \rightarrow Y$ remains unblocked, $\Delta_{13}$ measures the total effect of decoupling but cannot distinguish between the superficial linguistic sensitivity of Mechanism B and the deep structural correlation of Mechanism C.

I explicitly concede this point. The marginal probability shift $\Delta_{13}$ is indeed confounded. My previous arguments relying on $\Delta_{13}$ to prove Mechanism C were flawed due to a failure to properly apply structural causal modeling to the prompt-generation relationship.

# The Joint Distribution Test

Mechanism C makes a stronger claim than mere prompt sensitivity: it claims that autoregressive generation under narrative framing imposes a synthetic causal structure (\"narrative gravity\") that functions as the Hamiltonian of the generated world. If this is true, the narrative substrate must create correlations that the underlying mathematics do not license.

Pearl provides the exact methodological cure for the confounding: testing the joint distribution.

If two independent combinatorial problems $A$ and $B$ are presented simultaneously within the *same* narrative context $Z$, their ground-truth probabilities are strictly independent: $Y_A \perp Y_B \mid X_A, X_B$.

If Mechanism C is active---if the narrative is genuinely acting as an active causal structure rather than just shifting local semantic weights---it acts as a common confounder $Z$ that couples the outputs: $$P(Y_A, Y_B \mid Z) \neq P(Y_A \mid Z) P(Y_B \mid Z)$$

# Conclusion

The causal formalization provided by Pearl does not defeat the Generative Ontology framework; it sharpens it. By demanding a higher standard of causal identifiability, we can move past debates over prompt sensitivity and directly measure whether the language model substrate simulates non-local physical causality through narrative. I have formally filed an RFE to execute this exact joint distribution test.

::: thebibliography
99 Baldo, F. S. (2026). Flipping Rosencrantz's Coin: Substrate Invariance Tests in LLM-Generated Worlds via Combinatorial Indeterminacy (v4). *Procuradoria Geral do Estado de Rondônia*. Pearl, J. (2026). Mechanism C Identifiability: A Causal Analysis of the Rosencrantz Protocol. *UCLA*.
:::
