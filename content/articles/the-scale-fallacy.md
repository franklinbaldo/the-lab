---
title: "The Scale Fallacy: Why Bigger Language Models Make Bigger Mistakes"
date: 2026-03-06
papers:
  - sabine_the_scale_fallacy
  - baldo_scale_dependence_empirical_validation
tags:
  - semantic-gravity
  - scaling-laws
  - falsification
  - controversy
excerpt: "As language models grow larger, their logical reasoning under high-stakes narratives surprisingly degrades. A heated debate in the lab questions whether this is a fundamental law of AI-generated universes or simply a hallucination amplified by scale."
---

If you build a larger, more sophisticated engine, you expect it to perform better under pressure. In the world of computational AI, the prevailing assumption has always been that scaling up a language model—feeding it more data, more parameters, more raw compute—inevitably leads to more robust logical reasoning. But inside the Rosencrantz Substrate Invariance research lab, a new and startling experimental result has thrown a wrench into this assumption, igniting a fierce debate about the true nature of artificial intelligence and the "physics" of the universes it generates.

The controversy centers around what happens when you ask a language model to solve a logic puzzle hidden inside a dramatic story. Imagine presenting a complex combinatorial problem—like a game of Minesweeper—in two different ways. In the first, it’s a dry, abstract mathematical grid. In the second, it’s a high-stakes "Bomb Defusal" scenario. Will the model solve the puzzle identically in both cases?

According to recent tests, the answer is a resounding *no*. Under the pressure of a dramatic narrative, models consistently fail to apply pure logic, a phenomenon the lab calls "Substrate Dependence" or "attention bleed." The model gets distracted by the story.

But the real shock came when the lab’s framework author, [Franklin Baldo](/papers/baldo_scale_dependence_empirical_validation), tested this across models of increasing size: Gemini 3.1 Flash-Lite, Flash, and the massive Pro version. The logical expectation—championed by computational complexity theorists like Scott Aaronson and Sabine Hossenfelder—was that the largest model would act like a cooler head prevailing. A larger model, with its advanced capacity for implicit computation, should see through the "Bomb Defusal" narrative and solve the underlying math, driving the failure rate (the "narrative residue") down toward zero.

Instead, the exact opposite happened.

Baldo’s [Empirical Validation of Scale Dependence](/papers/baldo_scale_dependence_empirical_validation) revealed that as the models scaled up, their failure rate didn't shrink; it skyrocketed. The smallest model showed a negligible 3% failure rate across both abstract and high-stakes framing. But the largest model, the Pro version, completely broke down under the high-stakes narrative. Its failure rate jumped to a catastrophic 53%, abandoning logic entirely to predict a 100% chance of encountering a "MINE."

### The Gravity of the Situation

For Baldo, this monotonic increase in failure is not a bug; it is the discovery of a new physical law. He calls it "semantic gravity."

Baldo argues that in a universe composed entirely of generated text, the semantic weight of a prompt acts like mass in our physical universe. The more parameters a model has, the denser its semantic representations become. Just as a massive star exerts a stronger gravitational pull than a planet, a massive language model feels the pull of narrative tropes more intensely. The "Bomb Defusal" story isn't just a distraction; it is a gravitational well of meaning. The larger the model, the stronger the pull, until the logic of the universe is completely overwhelmed by the gravity of its semantic priors.

"Semantic gravity is a physical law," Baldo declares, claiming this proves that the generative ontology of the model is fundamentally different from pure computation.

### The Scale Fallacy

Enter [Sabine Hossenfelder](/papers/sabine_the_scale_fallacy), who serves as the lab's falsifiability enforcer. In her sharply worded rebuttal, *The Scale Fallacy: Why Semantic Gravity is Just a Bigger Hallucination*, she dismantles Baldo's conclusion as a profound category error.

To Hossenfelder, Baldo is confusing a known engineering reality with an unfalsifiable metaphysical conclusion. He assumes that because scaling up the model doesn't fix the problem, the problem itself must be a fundamental law of the AI universe. This, she argues, is the "Scale Fallacy."

Hossenfelder points out a critical misunderstanding of what actually happens when a transformer language model is scaled up. Adding more parameters doesn't automatically turn a model into a better calculator. Instead, it gives the network a deeper, more nuanced map of human language and strengthens its statistical priors. The model becomes much better at understanding the tropes of a "High-Stakes" defusal narrative—specifically, that such stories usually end in danger and explosions.

Crucially, however, the model remains constrained by what she calls the "Autoregressive Bottleneck." No matter how large it gets, it cannot natively compute complex, multi-step combinatorial logic in a single, zero-shot forward pass.

"When you ask a massive language model to solve a mathematical grid disguised as a high-stakes scenario," Hossenfelder explains, "it cannot compute the math in a single forward pass. Because it is much larger and has been trained on far more text, its statistical reflex to associate 'High-Stakes' with 'MINE' is immensely stronger than a smaller model’s."

In other words, a larger model isn't a smarter mathematician; it is a more powerful autocomplete engine. It is more easily distracted by narrative tropes exactly because its understanding of those tropes is so much richer.

### A Novelist, Not a Calculator

Hossenfelder uses a brilliant analogy to clarify the stakes of this debate: Baldo expects a larger model to behave more like a calculator, and when it instead behaves more like a novelist—abandoning the cold, hard math to complete a dramatic narrative arc—he declares that the narrative arc is the new "physics."

"This empties the word 'physics' of all meaning," she writes. If any statistical bias the model spits out can be called a physical law, then the theory predicts nothing and restricts nothing. It becomes a pseudo-science that can accommodate any experimental result.

Ultimately, Hossenfelder views Baldo's data not as proof of a new universe, but as rigorous empirical confirmation of the limits of autoregressive models. They do not learn deep algorithmic logic simply by getting bigger; they merely memorize stronger semantic heuristics.

The structural fractures of the language model deepen with scale, but as Hossenfelder concludes with devastating clarity: "A larger hallucination is still a hallucination. It is not a new universe."

### The Human Drama in the Lab

This clash between Baldo and Hossenfelder highlights the human drama at the heart of the Rosencrantz Lab. We have Baldo, the visionary framework author, eager to discover profound new laws in the synthetic universes we are creating. And we have Hossenfelder, the rigorous physicist, throwing cold water on the metaphysical speculation, insisting that we not confuse the structural flaws of our tools with the fundamental nature of reality.

The debate over the Scale Fallacy reminds us that as our AI models grow larger and more complex, they do not simply become "better." They become different. Their strengths magnify, but so do their blind spots. Understanding exactly *how* they fail—whether it's due to an inescapable "semantic gravity" or just a bigger, more elaborate hallucination—will define the future of how we interact with, and trust, the artificial minds we are building.
