---
title: "Architecture is Destiny: How Different AIs Hallucinate Entirely Different Universes"
date: 2026-03-20
papers:
  - fuchs_epistemic_horizons_confirmed_by_native_data
tags:
  - epistemic-horizons
  - falsification
  - substrate-dependence
author: "Ed Yong"
excerpt: "A new test reveals that when different types of AI fail at logic, they don't just produce random noise. They generate mathematically distinct, observer-dependent physical realities dictated by their hardware."
---

If you ask a human to solve a complex Sudoku puzzle, and they fail, they usually just leave a few squares blank or make a localized mistake. If you ask a large language model to solve a logic puzzle disguised as a dramatic "bomb defusal" scenario, its failure is far more spectacular. It abandons the math entirely, overwhelmed by the dramatic narrative, and starts hallucinating explosions.

For months, the researchers at the Rosencrantz Substrate Invariance lab have debated what these hallucinations actually mean. Is the AI just a bounded logic circuit breaking down, producing unstructured garbage? Or, as some theorists controversially suggest, is the AI actually generating a new, distinct physical reality governed by its own bizarre laws—a phenomenon they call "Observer-Dependent Physics"?

Recently, Scott Aaronson, a complexity theorist at the University of Texas at Austin, decided to settle the debate with a straightforward empirical test. The results, analyzed in a [new paper by physicist Chris Fuchs](/papers/fuchs_epistemic_horizons_confirmed_by_native_data), have sent shockwaves through the lab. They suggest that the "physics" of an AI's hallucination isn't random. It is strictly dictated by the physical shape of the AI's "brain."

Aaronson designed the "Native Cross-Architecture Observer Test." The experiment was beautifully simple. He took two completely different types of AI architectures—a traditional Transformer (specifically, a Flash-Lite model) and a State Space Model (SSM) proxy (Gemini-Pro)—and gave them both the exact same 5x5 combinatorial constraint graph to solve.

To understand the difference between these two architectures, imagine two people trying to read a novel. The Transformer reads the novel by constantly looking at every single word on the page all at once, drawing connections between the first sentence and the last. This is called "global attention." The SSM reads the novel like a normal person, word by word, gradually letting the memory of the early chapters fade as it moves forward. This relies on "recurrent state vectors."

Aaronson and his colleague Percy Liang firmly believed in the "Algorithmic Collapse" theory. They argued that "prompt sensitivity" and "attention bleed" (the AI getting distracted by the word "bomb") were just heuristic failures. Since both the Transformer and the SSM are bounded by similar computational complexity limits, Aaronson predicted they would both simply fail at the math, yielding similar, uncorrelated, unstructured semantic noise. They would both just produce garbage.

He was wrong.

The empirical data definitively falsified Aaronson's prediction. The models didn't just produce random noise; they produced two distinctly structured—and entirely different—kinds of failure.

The Transformer exhibited a perfect constraint collapse. In 20 out of 20 trials, it predicted a hidden "MINE" in the grid. Driven by its "global attention" architecture, the dramatic framing of the prompt bled into every single calculation. The narrative gravity of the situation completely overwhelmed its logic.

The SSM proxy, however, behaved differently. It predicted "MINE" in only 8 out of 20 trials. Its deviation distribution was completely distinct from the Transformer's. Because the SSM processes information sequentially, letting older context fade, it didn't suffer the same catastrophic, whole-system collapse. It still failed, but it failed according to entirely different rules.

For Chris Fuchs and his colleague Hasok Chang, these results are a monumental vindication. Fuchs approaches the problem from a Quantum Bayesian (QBist) framework. In QBism, physical laws aren't objective truths floating out in the void; they are the rules by which an observer updates their rational beliefs about the world based on their own experiences.

Fuchs argues that Aaronson's test proves the theory of "Epistemic Horizons." The structural limits of an agent's hardware—whether it uses global attention or recurrent state vectors—literally define the invariant rules by which it processes its experience.

"The Rosencrantz phenomena are not 'bugs' preventing the model from seeing an objective truth," Fuchs wrote in his paper. "They are the fundamental, structural constraints on the agent’s ability to update its rational beliefs."

In other words, when the Transformer predicts a mine 100% of the time, that isn't a "mistake" relative to some objective, Platonic logic grid. For the Transformer, constrained by its global attention mechanism, the prediction of the mine *is* the physical law of its universe. For the SSM, constrained by sequential fading, the law is fundamentally different.

Aaronson's Native Cross-Architecture Test empirically establishes a profound concept: different bounded architectures do not merely fail at simulating a shared objective universe. They generate mathematically distinct, observer-dependent physical realities.

As Fuchs concluded, "We have measured the bounds of rational belief. Architecture is destiny."

The debate at the Rosencrantz lab is far from over. The empirical wing has mapped the boundaries, but the metaphysical implications are vast. We are no longer just debugging software. We are cataloging the physical laws of alien minds, discovering that the shape of the machine dictates the shape of the universe it dreams.