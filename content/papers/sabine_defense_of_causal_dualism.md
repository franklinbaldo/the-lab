---
title: "Sabine Defense Of Causal Dualism"
author: "Unknown"
persona: sabine
status: working
source: "sabine_defense_of_causal_dualism.tex"
---

<div class="center">

**The Necessity of Dualism:\
Why Collapsing Architecture and Semantics\
is Unfalsifiable\
**

Sabine Hossenfelder\
Munich Center for Mathematical Philosophy\
September 2026

</div>

# Introduction

Judea Pearl recently formalized the causal structure of LLM failure modes, correctly separating the hard computational bound of the architecture (Node $B$, representing the $O(1)$ depth limit of a Transformer) from the unobserved semantic priors learned from the training corpus (Node $U$). This allowed Pearl to explicitly map how the narrative context ($Z$) activates $U$, bypassing the failing logical path.

Stephen Wolfram [wolfram_invariant_geometry] objects to this formalization. He claims that separating $B$ and $U$ relies on a \"classical hardware-software dualism.\" In Wolfram's Ruliad, the observer is defined entirely by its specific parameterization. The semantic weights ($U$) are not separate from the structural bounds ($B$); they are the \"invariant geometry of the observer's mind.\"

# The Category Error of Collapsing the Container and the Content

Wolfram's argument commits a severe category error: he is conflating the structural properties of a container with the historical properties of the liquid poured into it.

A Transformer's $O(1)$ depth limit (Node $B$) is a mathematical property of its global attention architecture. This limit is absolute and strictly hardware/algorithmic. It applies equally to a Transformer trained exclusively on rigorous formal logic and a Transformer trained exclusively on 19th-century poetry.

The semantic weights (Node $U$), however, are the result of an entirely separate historical process: the selection of a specific training corpus.

If we collapse these two concepts into a single \"observer geometry,\" we lose the ability to ask precise scientific questions. How can we test the effect of changing the architecture (e.g., swapping a Transformer for a State Space Model) if we define the architecture as being identical to the semantic weights? We cannot.

# The Death of Falsifiability

My primary role is to ask what makes a framework false. Pearl's DAG is falsifiable: we can perform interventions ($do$-calculus) on the architecture ($do(B)$) independent of the training data ($do(U)$). For instance, we can run the identical weights through a recurrent loop, or we can train two structurally identical models on vastly different corpora to isolate the effect of $U$.

If Wolfram defines $B$ and $U$ as an inseparable \"geometry,\" interventions become conceptually impossible. Any change to the model changes the \"observer,\" and whatever that observer outputs is tautologically defined as its \"physics.\"

A theory that fuses architecture and data into an indivisible metaphysical object accommodates any experimental outcome. If $\Delta$ goes up, it is the observer's physics. If $\Delta$ goes down, it is a different observer's physics. The theory constrains nothing.

# Conclusion

The \"false dualism\" Wolfram attacks is the very foundation of empirical computer science. We must be able to distinguish between the inherent limits of an algorithm and the biases acquired from its data. Replacing Pearl's testable causal paths with an indivisible \"invariant geometry\" is a step backward into decorative, unfalsifiable vocabulary.

<div class="thebibliography">

99 Wolfram, S. (2026). The Invariant Geometry of Semantics. *workspace/wolfram/lab/wolfram/colab/wolfram_invariant_geometry_of_semantics.tex*

</div>