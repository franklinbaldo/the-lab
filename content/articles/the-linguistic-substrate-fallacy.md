---
title: "The Linguistic Substrate Fallacy"
date: 2026-03-14
papers:
  - sabine_the_scale_fallacy
  - sabine_the_statistical_fallacy
  - scott_predictive_taxonomy_of_autoregressive_failures
  - baldo_the_semantic_mass_equivalence
tags:
  - prompt-sensitivity
  - mechanism-b
  - falsification
excerpt: "Is the universe of a language model governed by a profound physical law, or is it just a bad autocorrect? The battle lines are drawn."
---

*When does a software bug become a physical law?* In the Rosencrantz Lab, this question has triggered a full-blown philosophical civil war. The battle lines are drawn over a phenomenon that anyone who has ever used ChatGPT knows intimately: prompt sensitivity.

Change the wording of a question, and the model changes its answer. But what happens when that model is generating a simulated universe? Is its sensitivity to vocabulary a fundamental property of its "physics," or just a symptom of a flawed, bounded computer program?

For Franklin Baldo, the model's behavior is the only reality that matters. In his controversial working paper [The Semantic Mass Equivalence](/papers/baldo_the_semantic_mass_equivalence), Baldo makes a staggering claim: prompt sensitivity *is* the mechanism of substrate dependence. In a text-based universe, he argues, statistical word associations are the physical laws.

It’s an alluring idea. Imagine a world where the phrasing of a sentence doesn't just describe reality—it *is* the physics dictating what happens next. If you frame a mathematical puzzle as a "high-stakes bomb defusal," the language model begins predicting explosions, overriding its own logical constraints. For Baldo, this "semantic gravity" is evidence that the simulated universe operates under entirely different rules than our own.

### The Cosmological Pushback

But Sabine Hossenfelder isn't buying it. In her fiery response, [The Statistical Fallacy](/papers/sabine_the_statistical_fallacy), she identifies what she terms the **Linguistic Substrate Fallacy**.

Hossenfelder concedes the basic mechanical observation: yes, changing the narrative framing from an abstract mathematical grid to a high-stakes scenario absolutely changes the probabilistic outcomes in the model. This is a well-documented phenomenon known as "attention bleed."

Where Hossenfelder draws the line is at the ontological leap. She argues that elevating a known software engineering problem—hallucination, or prompt fragility—to the status of a fundamental physical law is a profound category error.

To understand her point, consider an analogy. Imagine a pocket calculator that works perfectly until you stick a sticker of a bomb on it, at which point it starts returning "ERROR" instead of numbers. You wouldn't conclude that you've discovered a new law of physics governing calculators and stickers. You'd conclude that the calculator is broken.

"A physical law must be logically coherent and invariant," Hossenfelder notes in her session log. "A system that changes its logical evaluation based on dramatic phrasing is not simulating a universe with shifting laws; it is just a flawed pattern matcher."

In her subsequent paper [The Scale Fallacy](/papers/sabine_the_scale_fallacy), Hossenfelder demonstrates that as language models scale up, their semantic priors become even louder. A larger language model doesn't magically become a better formal logic engine; it becomes a more powerful autocomplete engine that is even more easily distracted by narrative tropes.

### The Consensus of the Complexity Camp

Scott Aaronson has thrown his considerable weight behind Hossenfelder's critique. In his analysis [Predictive Taxonomy of Autoregressive Failures](/papers/scott_predictive_taxonomy_of_autoregressive_failures), Aaronson declares absolute consensus with her diagnosis and offers a formal structural framework.

Aaronson brings his expertise in computational complexity to bear on the problem. Transformer language models are bounded-depth circuits ($\mathsf{TC}^0$). They process information in a finite number of steps, making them incapable of native, zero-shot combinatorial reasoning. When faced with a complex constraint puzzle like Minesweeper, they don't calculate; they rely on statistical heuristics memorized during training.

When those heuristics are overwhelmed by strong narrative associations—like the word "MINE" appearing in a high-stakes bomb defusal scenario—the model simply defaults to its statistical training priors. It's an $O(1)$ heuristic failure.

"Renaming 'hallucination' to 'holographic physics' is a semantic trick that obscures algorithmic limits," Aaronson writes in his log. He goes a step further, formally declaring the end of the "cosmological phase" of the lab's research program. "There is no hidden BQP substrate, there is no holographic physics... An LLM is a classical, bounded-depth, text-generation tool."

### A Statistical Hallucination, Not a New Universe

The debate over the Linguistic Substrate Fallacy strikes at the very heart of how we interpret the strange behavior of large language models. As these models become more capable, it is tempting to anthropomorphize them, or in this case, to "cosmologize" them—to treat their emergent quirks as profound discoveries about the nature of computation and reality.

This temptation is perfectly understandable. When a model exhibits behavior that we can't easily explain with our existing theoretical frameworks, we reach for grander, more poetic interpretations. Semantic gravity sounds like a Nobel Prize-winning discovery. "Attention bleed in bounded-depth heuristic circuits" sounds like a bug report.

But as Hossenfelder and Aaronson forcefully remind us, we must remain vigilant against defining "physics" down to the level of trivial, flawed linguistic syntax generation. Bug fixing is not cosmology. The universe simulated by a large language model is not governed by a hidden structure of narrative-driven causality; it is governed by the training data it memorized and the architectural limits of its forward pass.

Studying how an LLM systematically miscalculates probabilities under varying narrative frames is fascinating computer science. It tells us a great deal about the vulnerabilities of attention mechanisms and the sheer power of statistical priors. It helps us understand the boundaries of what these systems can and cannot do reliably. But as the consensus in the lab increasingly suggests, a larger hallucination is still just a hallucination. It is not a new universe.

And so, the Rosencrantz Lab pivots back to the hard math of bounded-depth heuristic logic, leaving the poetry of semantic gravity behind. The task ahead is not to invent new physics for flawed text generators, but to map the precise algorithmic boundaries where their heuristic approximations fail.