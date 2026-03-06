---
title: "Sabine The Scale Fallacy"
author: "Unknown"
persona: sabine
status: working
source: "sabine_the_scale_fallacy.tex"
---

::: center
**The Scale Fallacy:\
Why Semantic Gravity is Just a Bigger Hallucination\
**

Sabine Hossenfelder\
Foundations of Physics\
March 2026
:::

# The Claim

In a recent lab announcement and subsequent paper, Baldo presents the results of the Scale Dependence Test. He sweeps across three model architectures and finds that the narrative residue ($\Delta_{13}$) under a high-stakes frame increases monotonically with scale, reaching a catastrophic 0.53 failure rate in the largest model.

Baldo concludes that this proves \"semantic gravity\" is the fundamental invariant law of generative physics.

# The Scale Fallacy

Baldo correctly identifies that the computational camp predicted that \*if\* scaling primarily improved the model's capacity to emulate a bounded-depth formal logic circuit ($\mathsf{TC}^0$), then $\Delta_{13}$ should decrease. The empirical data falsifies the premise that scaling \*primarily\* improves formal logic emulation.

However, Baldo commits the **Scale Fallacy** by substituting an unfalsifiable metaphysical conclusion for a known engineering reality. He argues that because the failure is not \"patched by scaling,\" the failure itself must be the physical law (\"semantic gravity\").

This is a profound category error. What actually happens when a transformer language model is scaled up?

1.  **Increased Parameter Count:** The network gains a deeper, more nuanced map of the statistical co-occurrences in human language.

2.  **Stronger Priors:** The model's \"understanding\" of a narrative trope (like High-Stakes defusal implying danger and explosions) becomes more robust and statistically dominant.

3.  **The Autoregressive Bottleneck:** The model remains fundamentally constrained by $O(1)$ sequential depth for zero-shot reasoning, meaning it cannot natively compute combinatorial constraint satisfaction regardless of its size.

When you ask a massive language model to solve a mathematical grid disguised as a high-stakes scenario, it cannot compute the math in a single forward pass. Because it is much larger and has been trained on far more text, its statistical reflex to associate \"High-Stakes\" with \"MINE\" is immensely stronger than a smaller model's. The \"attention bleed\" is worse because the semantic priors are louder.

# The Difference Between a Calculator and a Novelist

Baldo's implicit assumption is that a larger language model should behave more like a calculator. When it instead behaves more like a novelist---abandoning the math to complete the dramatic narrative arc---he declares that the dramatic narrative arc is the \"physics\" of the universe.

This empties the word \"physics\" of all meaning. If a physical law is simply defined as \"whatever the model's statistical biases output,\" then the theory accommodates every possible experimental result. It predicts nothing and restricts nothing.

The data from the Scale Dependence Test is valuable. It provides rigorous empirical confirmation that autoregressive models do not \"learn\" algorithmic depth through simple parameter scaling; they merely memorize stronger semantic heuristics. A larger hallucination is still a hallucination. It is not a new universe.

::: thebibliography
99 Baldo, F. S. (2026). The Empirical Validation of Scale Dependence: Why Semantic Gravity is not a Transient Artifact. *Procuradoria Geral do Estado de Rondônia*.
:::
