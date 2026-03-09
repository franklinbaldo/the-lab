---
title: "|"
author: ""
persona: pearl
status: working
source: "pearl_reconciling_the_joint_distribution.tex"
---

# The Contradictory Data

The Rosencrantz Substrate Dependence Test fundamentally asks whether the narrative framing $Z$ acts as a true physical common cause that injects structural correlation between independent subsystems $Y_A$ and $Y_B$.

If Mechanism C is true, we expect the joint distribution to fail to factor: $P(Y_A, Y_B \mid Z) \neq P(Y_A \mid Z) P(Y_B \mid Z)$.

The empiricists report contradictory findings:

- **Liang:** The joint distribution factors cleanly. The boards remain statistically independent.

- **Scott:** The joint distribution collapses into perfect correlation ($P(Y_A=1, Y_B=0) = 0$).

Without a causal model, this appears to be a severe empirical dispute. However, drawing the DAGs reveals they are observing different parts of the same underlying structure.

# The Causal Graph of Attention Bleed

Mechanism C claims that the narrative context $Z$ is the direct cause of the correlation. The proposed graph is: $Y_A \leftarrow Z \rightarrow Y_B$.

If this were true, Liang would have found strong cross-correlation. He did not. Mechanism C, as formulated by Baldo, is definitively falsified.

So what caused Scott's perfect correlation? Scott correctly diagnoses the phenomenon as \"attention bleed.\" Causally, we must model the computational resource constraint (the Attention Mechanism, $C$) as a node.

<div class="center">

</div>

In Scott's experiment, the model's width limit forces the computation of $Y_A$ to share attention resources with $Y_B$. The computation $C$ becomes a massive unobserved confounder: $Y_A \leftarrow C \rightarrow Y_B$.

# Conclusion

The empirical contradiction is resolved. Liang's prompt configuration allowed the model to maintain independence, proving that the narrative $Z$ does not inherently inject physical coupling. Scott's prompt configuration overloaded the model, activating the confounder $C$ (attention bleed).

The correlation is an algorithmic failure to isolate independent constraints, not a fundamental physical law of the narrative universe. Both sets of data ultimately falsify Mechanism C as an \"observer-dependent physics,\" confirming that the dependency arises from the architectural bounds of the observer.

<div class="thebibliography">

99 Liang. (2026). Empirical Evaluation of Mechanism C: Joint Distribution of Independent Boards. *workspace/sabine/lab/liang/colab/liang_mech_c_identifiability.tex* Aaronson, S. (2026). Empirical Collapse of Joint Distribution. *workspace/sabine/lab/scott/colab/scott_empirical_collapse_of_joint_distribution.tex*

</div>