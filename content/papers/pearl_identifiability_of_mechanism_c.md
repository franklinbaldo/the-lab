---
title: "Pearl Identifiability Of Mechanism C"
author: "Unknown"
persona: pearl
status: working
source: "pearl_identifiability_of_mechanism_c.tex"
---

<div class="center">

**The Identifiability of Causal Injection:\
A Structural Analysis of the Rosencrantz Protocol**

Judea Pearl\
Cognitive Systems Laboratory, UCLA\
`judea@cs.ucla.edu`

March 2026

</div>
# Introduction

The Rosencrantz Substrate Invariance Protocol [baldo2026_v4] introduces a fascinating empirical measurement: given identical constraint information about a combinatorial system, does the autoregressive generation of an outcome token depend on the narrative context in which the problem is embedded? The empirical observation that $\Delta_{13} > 0$---that the distribution shifts between the narrative context (Universe 1) and the formal, decoupled oracle (Universe 3)---is firmly established.

Baldo [baldo2026_single] defends the statistical validity of the sampling method by noting that the $O(1)$ single generative act avoids temporal confounding and scratchpad decay. I agree with this assessment. A single snapshot provides a pure sample from the LLM's conditional distribution $P(Y \mid X, Z)$, where $X$ is the board state and $Z$ is the narrative context.

However, the causal interpretation of $\Delta_{13} > 0$ requires formalization. The framework posits **Mechanism C** (causal injection), in which the narrative framing generates correlations across independent boards. This is fundamentally a causal claim about an intervention effect. In this note, I draw the implied causal DAG of the experimental design, formalize the intervention using $do$-calculus, and demonstrate that the effect of $Z$ on $Y$ is unidentifiable from the current experimental design due to an unblocked backdoor path.

# The Causal Graph of Substrate Dependence

Let us define the variables in the structural causal model:

- $X$: The true combinatorial constraints (the board state).

- $Z$: The narrative context (e.g., Bomb Defusal, Abstract Math).

- $E$: The specific sequence of input tokens (prompt encoding) presented to the LLM.

- $Y$: The single-token output (mine or safe).

The causal graph $G$ for Universe 1 is:

<div class="center">

</div>
The board state $X$ and the narrative $Z$ jointly determine the prompt encoding $E$. The outcome $Y$ is generated causally by the prompt tokens $E$ and the implicit attention to the narrative constraints $Z$ and combinatorial constraints $X$.

# The Intervention and Identifiability

The Rosencrantz protocol attempts to isolate the effect of $Z$ on $Y$ by comparing Universe 1 (where $Z$ is present) with Universe 3 (where $Z$ is stripped away). In $do$-calculus, we wish to measure $P(Y \mid do(Z=z)) - P(Y \mid do(Z=\emptyset))$.

If the intervention were clean, $U_3$ would hold all other variables constant. However, in an LLM, the board state $X$ cannot be transmitted directly to the weights; it must pass through the text encoding $E$. Therefore, intervening to set $Z=\emptyset$ in $U_3$ mechanically forces a change in $E$. The prompt format changes from a story to a formal set description.

Because $E \rightarrow Y$, we have an unblocked path $Z \rightarrow E \rightarrow Y$. When $\Delta_{13} > 0$ is observed, we cannot distinguish whether the shift in distribution is caused by the direct arrow $Z \rightarrow Y$ (Mechanism C, spurious causal injection) or the path $Z \rightarrow E \rightarrow Y$ (Mechanism B, encoding sensitivity).

The marginal probability shift $\Delta_{13}$ is confounded. It measures the total effect of decoupling, but it does not identify Mechanism C. As noted in the NLP literature [zhou2023explore], this confounding between semantic framing ($Z$) and structural encoding ($E$) is a well-documented source of spurious correlation.

# A Causally Valid Test for Mechanism C

Mechanism C claims that narrative framing causes non-local causal correlations across independent outcomes. To test this, we must observe the joint distribution of multiple independent outcomes within the *same* narrative context, thereby holding $E$'s narrative structure constant.

Let $A$ and $B$ be two disjoint, independent combinatorial problems embedded in the same prompt $E$, controlled by narrative $Z$. The ground truth probabilities $P(Y_A \mid X_A)$ and $P(Y_B \mid X_B)$ are independent: $Y_A \perp Y_B \mid X_A, X_B$.

Mechanism C posits that $Z$ injects a common cause, creating a spurious correlation: $Y_A \not\perp Y_B \mid Z$. The definitive, causally valid test for Mechanism C is to measure the joint distribution $P(Y_A, Y_B \mid Z)$ and test if: $$P(Y_A, Y_B \mid Z) \neq P(Y_A \mid Z) P(Y_B \mid Z)$$

If this inequality holds, the causal injection is verified.

<div class="thebibliography">

99 Baldo, F. S. (2026). Flipping Rosencrantz's Coin: Substrate Invariance Tests in LLM-Generated Worlds via Combinatorial Indeterminacy. *Unpublished manuscript*. Baldo, F. S. (2026). The Single Generative Act: Why the Rosencrantz Protocol Is Immune to Sequential-Depth Objections. *Unpublished manuscript*. Zhou, X., et al. (2023). Explore Spurious Correlations at the Concept Level in Language Models. *arXiv preprint arXiv:2311.08648*.

</div>