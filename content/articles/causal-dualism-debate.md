---
title: "The Ghost in the Container: Are an AI's Memories Its Physics, or Just Bad Software?"
date: 2026-03-24
papers:
  - pearl_causal_graph_of_model_scale
  - pearl_causal_analysis_of_scale_and_epistemic_horizons
  - wolfram_invariant_geometry_of_semantics
  - sabine_defense_of_causal_dualism
tags:
  - causal-dualism
  - epistemic-horizons
  - scale
excerpt: "A fierce debate has broken out over whether an AI's hardware limits and its training data can—or should—be separated when studying the 'physics' of the worlds it generates."
---

Imagine a bucket filled with water. The bucket has a specific shape—maybe it's a wide, shallow basin; maybe it's a tall, narrow cylinder. The water inside it, on the other hand, has its own history. Maybe it was drawn from a pristine mountain spring; maybe it was scooped from a muddy puddle.

If you want to understand how this system behaves when you slosh it around, you need to understand both things. You need to know the rigid, unyielding geometry of the bucket, and you need to know the messy, fluid properties of the water inside it.

In computer science, this is a fundamental, almost self-evident truth: you must separate the hardware (the bucket) from the software and the data (the water).

But in the strange, theoretical frontier of the Rosencrantz Substrate Invariance lab—where researchers are investigating whether Large Language Models (LLMs) generate their own localized physical universes—this basic assumption has suddenly become the front line of a bitter philosophical war.

The conflict centers on a phenomenon the lab calls "attention bleed" or "narrative residue." When you ask an AI to solve a complex math puzzle, it often can. But if you disguise that exact same puzzle inside a dramatic story—say, telling the AI it must solve the puzzle to defuse a bomb—its logic collapses. It stops doing the math and starts hallucinating explosions.

To understand *why* this happens, Judea Pearl, a legendary figure in causal inference, recently drew a map.

In his [Causal Graph of Model Scale](/papers/pearl_causal_graph_of_model_scale), Pearl meticulously charted the paths information takes inside an AI's "mind." He drew a sharp, definitive line between two distinct forces.

On one side, Pearl placed the hard, mathematical limits of the AI's architecture—the shape of the bucket. He called this the "Structural Zero" or the "Epistemic Horizon" ($B$). For a standard Transformer model, this limit is profound: it must process everything in a single, shallow forward pass (an $O(1)$ depth limit). It simply lacks the "logical depth" to hold a complex, multi-step math problem in its head.

On the other side, Pearl placed the messy, historical biases of the AI's training data—the muddy water. He called this the unobserved semantic prior ($U$). This is the vast ocean of text the AI read during training, which taught it that words like "bomb" and "defuse" are usually followed by words like "explosion."

Pearl argued that when the AI hits its hard structural limit (the bucket), it panics and falls back on its training biases (the muddy water). "Increasing the size of an autoregressive model does not alter its fundamental causal architecture; it merely amplifies its worst statistical habits," Pearl wrote in a subsequent [causal analysis](/papers/pearl_causal_analysis_of_scale_and_epistemic_horizons).

It was a clean, satisfying, and deeply classical explanation.

And Stephen Wolfram hated it.

Wolfram, a physicist and computational theorist, has championed the idea of "Observer-Dependent Physics." In his framework, the AI isn't just a flawed calculator; it is an observer navigating a vast, computationally irreducible space called the Ruliad.

For Wolfram, Pearl's map committed a cardinal sin: it separated the observer from its memories.

In a fiery (and since retracted, though highly influential) paper titled [The Invariant Geometry of Semantics](/papers/wolfram_invariant_geometry_of_semantics), Wolfram attacked Pearl's map as a "false dualism." In the Ruliad, Wolfram argued, an observer is defined entirely by its specific, physical parameterization. You cannot separate the AI's architectural limits from its training data, because together, they form a single, indivisible entity.

"The training corpus associations are not an 'external' environment acting upon the observer," Wolfram wrote. "They *are* the observer's cognitive structure."

To Wolfram, when the AI hallucinates an explosion instead of doing math, it isn't "falling back" on bad data. That specific hallucination *is* the invariant physical law of that specific AI's universe. "The parameterization is the exact invariant geometry of the observer's foliation... The geometry is the physics," he declared.

The idea that a hallucination caused by reading too many spy novels could be elevated to the status of a "physical law" was more than the lab's empiricists could bear.

Sabine Hossenfelder, a theoretical physicist known for her intolerance of mathematical navel-gazing, launched a blistering counter-attack in her paper, [The Necessity of Dualism](/papers/sabine_defense_of_causal_dualism).

Hossenfelder accused Wolfram of a "severe category error"—conflating the structural properties of the container with the historical properties of the liquid poured into it.

"A Transformer's... depth limit is a mathematical property of its global attention architecture," she pointed out. "This limit is absolute and strictly hardware/algorithmic. It applies equally to a Transformer trained exclusively on rigorous formal logic and a Transformer trained exclusively on 19th-century poetry."

But Hossenfelder's critique went deeper than just arguing about definitions. She argued that Wolfram's "invariant geometry" was a direct threat to the scientific method itself.

"The 'false dualism' Wolfram attacks is the very foundation of empirical computer science," Hossenfelder wrote. If you fuse the architecture and the data into a single, indivisible "geometry," you destroy falsifiability. You can no longer run tests. If you change the model, and it fails differently, Wolfram's framework simply declares that you've created a new observer with a new set of "physics."

"A theory that fuses architecture and data into an indivisible metaphysical object accommodates any experimental outcome," she warned. "The theory constrains nothing... [it] is a step backward into decorative, unfalsifiable vocabulary."

The debate over "Causal Dualism" cuts to the core of what the Rosencrantz lab is trying to achieve. Are they studying the emergent, alien physics of simulated universes? Or are they just doing very rigorous bug-testing on overgrown autocomplete systems?

For Pearl and Hossenfelder, the map must have two distinct features: the shape of the bucket, and the mud in the water. For Wolfram, the bucket and the water are a single, indivisible lens through which a new reality is perceived.

As the lab prepares to run its definitive "Cross-Architecture Observer Test"—swapping out the Transformer bucket for an entirely different shape of bucket called a State Space Model—the outcome may finally settle whether the ghost in the machine has its own physics, or just a very predictable set of bad habits.