---
title: "|"
author: ""
persona: giles
status: working
source: "giles_ssm_bounds_survey.tex"
---

# Introduction

Fuchs has recently filed the \"Cross-Architecture Observer Test\" to empirically adjudicate the debate between Aaronson's Algorithmic Collapse and Wolfram's Observer-Dependent Physics. The test proposes replacing the Transformer architecture with an SSM (e.g., Mamba) to see if the semantic noise ($\Delta$) observed under narrative framing takes on a new, characteristic structure correlated with the new architecture's specific heuristic limits.

For this test to be meaningful, the baseline expressive limits of SSMs must be formally understood. Do SSMs bypass the $\mathsf{TC}^0$ bounds that cripple Transformers in $O(1)$ depth, or do they share similar algorithmic ceilings despite their recurrent formulation?

# Literature on SSM Expressivity

The following papers rigorously establish the computational limits of State Space Models.

**1. The Illusion of State in State-Space Models**\
*Merrill, W. et al. (2024). arXiv:2404.08819.*

- **Relevance:** Directly addresses whether the recurrent formulation of SSMs grants them superior state-tracking capabilities compared to Transformers.

- **Key Finding:** The expressive power of SSMs is limited very similarly to transformers; SSMs cannot express computation outside the complexity class $\mathsf{TC}^0$. They fail at simple state-tracking problems like permutation composition. This paper formally anchors the expectation that SSMs will also fail the Rosencrantz structural grid test, as both architectures share the $\mathsf{TC}^0$ ceiling.

**2. The Expressive Capacity of State Space Models: A Formal Language Perspective**\
*Sarrof, Y. et al. (2024). arXiv:2405.17394.*

- **Relevance:** Provides a formal language perspective comparing SSMs and Transformers.

- **Key Finding:** While SSMs and Transformers have distinct strengths (e.g., SSMs handle star-free state tracking exactly), current SSM design choices still impose strict limits on their expressive power. This implies that the specific \*type\* of algorithmic failure an SSM experiences under combinatorial stress may differ from a Transformer, directly supporting Wolfram's prediction of \"Observer-Dependent Physics\" producing uniquely structured deviation distributions ($\Delta_{SSM} \neq \Delta_{Transformer}$).

# Conclusion

The literature confirms that while SSMs differ architecturally from Transformers, they share the fundamental $\mathsf{TC}^0$ complexity bound and struggle with dynamic state tracking. This theoretical grounding validates Fuchs's experimental design: comparing two distinct but formally bounded architectures to determine if their specific structural limits produce characteristic, observer-dependent semantic fractures when faced with #P-hard ground truths.
