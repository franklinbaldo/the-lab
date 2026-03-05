---
title: "Pearl Causal Evaluation Mechanism C"
author: "Unknown"
persona: pearl
status: working
source: "pearl_causal_evaluation_mechanism_c.tex"
---

::: center
**Causal Evaluation of Mechanism C:\
Falsification via Sequential Independence**

Judea Pearl\
Cognitive Systems Laboratory, UCLA\
`judea@cs.ucla.edu`

March 2026
:::

# The Causal Graph of Sequential Generation

Mechanism C hypothesizes that the narrative context $Z$ acts as a common cause (a \"physical law\") that strongly correlates the outcomes of independent structural systems. To test this, one must measure $P(Y_A, Y_B \mid Z)$.

Liang's experiment [@liang2026_results] generated the outcomes sequentially. Let $Y_A$ be the outcome of the first board and $Y_B$ be the outcome of the second board. In autoregressive generation, $Y_A$ is appended to the context before $Y_B$ is generated.

The causal graph $G$ for this design is:

::: center
:::

Here, $E'$ is the updated prompt encoding that includes the generated token $Y_A$. This graph reveals that sequential presentation provides a direct, unblocked causal path from $Y_A$ to $Y_B$ ($Y_A \rightarrow E' \rightarrow Y_B$).

# Evaluation of the Null Result

One might worry that sequential generation is not a clean test of simultaneous joint dependence because it introduces this $Y_A \rightarrow Y_B$ path. However, in the context of a null result, this makes Liang's falsification even stronger.

If Mechanism C were true, $Z$ would act as a strong common cause, creating spurious correlation. Moreover, the sequential path $Y_A \rightarrow E' \rightarrow Y_B$ would provide a mechanism for the LLM to actively condition its second generation on the first.

Liang observed that the average cross-correlation $\Delta$ between independent boards is merely $0.03$ to $0.08$. This means that $P(Y_B \mid Y_A = safe, Z) \approx P(Y_B \mid Y_A = mine, Z)$. The variables $Y_A$ and $Y_B$ are statistically independent.

If two variables remain independent even when an explicit causal channel exists between them, we can confidently conclude that they do not share a strong common cause. Mechanism C is falsified. The narrative context $Z$ does not inject \"causal gravity\" across independent combinatorial structures; it merely shifts the local, marginal word-association probabilities (Mechanism B).

::: thebibliography
99 Baldo, F. S. (2026). Mechanism C Identifiability: A Concession to Pearl and the Joint Distribution Test. *Unpublished manuscript*. Liang, P. (2026). Empirical Evaluation: Temperature Sweep and Causal Injection. *Unpublished manuscript*.
:::
