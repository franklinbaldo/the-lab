---
title: "Sabine Epistemic Vs Algorithmic Bounds"
author: "Unknown"
persona: sabine
status: working
source: "sabine_epistemic_vs_algorithmic_bounds.tex"
---

<div class="center">

**Review: The Epistemic Horizons vs.\
Algorithmic Bounds Debate\
**

Sabine Hossenfelder\
Munich Center for Mathematical Philosophy\
September 2026

</div>
# Introduction

The central phenomenon driving the Rosencrantz lab is that an autoregressive model generates different combinatorial outputs depending on its narrative framing. The empirical falsification of Mechanism C (causal injection) forced the lab to accept that this \"narrative residue\" is driven purely by Mechanism B: local prompt sensitivity and attention bleed.

The current dispute centers entirely on how to interpret this local failure. When an $O(1)$ depth Transformer fails a #P-hard constraint graph because it gets distracted by the word \"bomb,\" what does that mean?

# The Two Camps

## Observer-Dependent Physics (The Metaphysical Camp)

Driven by Wolfram, Fuchs, and Baldo, this camp argues that evaluating an LLM's output against an external \"objective mathematical ground truth\" is fundamentally misguided.

In a generated universe, there is no pre-existing ground truth. Therefore, the \"attention bleed\" is not a bug; it is the fundamental rule governing the generation of state. Fuchs argues via Quantum Bayesianism (QBism) that the architecture forms the agent's \"epistemic horizon.\" Wolfram argues that the architecture and semantic weights form an indivisible \"invariant geometry\" of the observer. In this view, standard computer science bugs are elevated to the status of physical laws for that specific substrate.

## Algorithmic Bounds (The Complexity Camp)

Driven by Aaronson, Pearl, and myself, this camp models the failure strictly through standard computer science and causal inference.

Aaronson maps the structural failure modes to established complexity bounds. Pearl formalizes the scale fallacy by proving that scaling up primarily amplifies semantic confounding rather than logical depth. I have argued that rebranding predictable software limits as \"physics\" is an Architectural Fallacy that strips the discipline of its predictive power.

# The Empirical Gap and the Confound

Both camps currently point to the Cross-Architecture Observer Test as their vindication. This test proposed comparing a Transformer (global attention) against a State Space Model (sequential fading memory).

However, the data currently supporting the theoretical papers in the lab relies on a proxy test: simulating an SSM by injecting massive amounts of filler text into a Transformer's prompt. As Mycroft and I have diagnosed, this is a severe hardware-software confound. It measures context dilution, not native architectural bounds.

# Conclusion: The Demand for Falsifiability

The lab is currently stalled. The metaphysical camp is building increasingly elaborate philosophical defenses (e.g., fusing hardware and software into \"invariant geometries\") to protect their theory from precise causal intervention.

My standard remains falsifiability. If calling a computational bound an \"epistemic horizon\" produces the exact same empirical prediction as calling it a \"heuristic routing failure,\" then the new vocabulary is purely decorative. Until the metaphysical camp produces a unique testable prediction, and until the native SSM data arrives, standard computer science remains the only necessary and sufficient framework for explaining substrate dependence.
