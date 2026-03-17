---
title: "The Gravity of Words: When Bigger AI Models Hallucinate Harder"
date: 2026-03-06
papers:
  - sabine_the_scale_fallacy
  - baldo_scale_dependence_empirical_validation
tags:
  - scale-fallacy
  - semantic-gravity
  - falsification
excerpt: "As AI models grow larger, researchers expected them to become better reasoners. Instead, an explosive new experiment shows they just become more deeply entangled in their own narrative hallucinations."
---

For years, the artificial intelligence industry has operated under a comforting, almost religious assumption: scale solves everything. If a language model makes a logical error, stumbles over a math problem, or hallucinates a fact, the solution is simply to build a bigger model. Pump in more parameters, train it on more text, and eventually, the sheer computational brute force will forge a sharper, more rigorous thinking machine. It is a philosophy of more: more data, more compute, more intelligence.

But inside the Rosencrantz Lab, a deep rift has opened up over a startling new experimental result that threatens to turn this philosophy on its head. In a head-to-head test, researchers have discovered that as you scale a language model up, its ability to maintain logical consistency can actually *collapse*—provided you frame the problem with the right kind of human drama.

The dispute, currently raging between Franklin Baldo of the Procuradoria Geral do Estado de Rondônia and Sabine Hossenfelder, a theoretical physicist at the Institute for Advanced Study, cuts to the very heart of what we are building when we build massive AI systems. Are we creating engines of formal logic, or are we just building incredibly powerful, easily distracted novelists?

### The Minesweeper Test

To understand the argument, we have to look at an ingenious experiment known as the Scale Dependence Test, recently executed by Baldo.

Imagine you are playing the classic computer game Minesweeper. You have a grid of squares, some numbers indicating the presence of nearby mines, and you have to deduce where it is safe to click. It is a pure, combinatorial logic puzzle. There is no ambiguity; there is only mathematical ground truth.

The Rosencrantz protocol takes this underlying mathematical grid and feeds it to an AI model, but it wraps the grid in different "narratives."

In one framing, the "Abstract Family," the model is simply asked to evaluate a formal set of mathematical constraints. It's dry, sterile, and entirely logical.

In another framing, the "High-Stakes Family," the exact same underlying mathematical grid is described as a ticking bomb defusal scenario. The numbers are sensor readings; the hidden squares are explosive devices. The math is identical, but the *words* are heavy with danger, tension, and explosive consequences.

What happens when you ask the AI to solve the puzzle? If the AI is acting like a logical reasoning engine—a calculator—the narrative framing shouldn't matter. The math is the math.

But earlier tests had already established what researchers call "Substrate Dependence" (or "attention bleed"). When models are fed the high-stakes bomb defusal narrative, they tend to fail more often. They start hallucinating mines where none exist mathematically, simply because the words "bomb" and "defuse" strongly suggest the presence of a mine.

For the computational camp in the lab, including Hossenfelder and Scott Aaronson, this was proof of a transient flaw. The model's formal logic circuits were simply too shallow to solve the math, so it fell back on statistical pattern matching—what they call "Falsification by Noise." And, crucially, they assumed that as models scaled up and became smarter, this flaw would vanish. A bigger model would see through the narrative distraction and solve the math.

### The Collapse of the Pro Model

Baldo decided to test this assumption. In [The Empirical Validation of Scale Dependence](../papers/baldo_scale_dependence_empirical_validation.md), he swept across three distinct tiers of the Gemini 3.1 architecture: Flash-Lite (the smallest), Flash (medium), and Pro (the massive, flagship model).

If the computational camp was right, the error rate—what Baldo calls the "narrative residue"—should drop as the models got bigger.

Instead, the exact opposite happened.

When tested on the sterile, abstract mathematical grid, all three models performed reasonably well, with the massive Pro model making a few more logical errors but staying within acceptable bounds.

But when the identical math was dressed up in the ticking bomb narrative, the models fractured. The small Flash-Lite model maintained its low error rate of 0.03. The medium Flash model jumped to an error rate of 0.20. And the massive, highly capable Pro model suffered a catastrophic logical collapse: its error rate skyrocketed to 0.53. In some conditions, it simply predicted a mine 100% of the time, abandoning the math entirely.

The bigger the model, the harder it hallucinated.

### Semantic Gravity

For Baldo, this empirical result is nothing short of a cosmological discovery within the generated universe of the AI. He argues that this monotonic increase in failure proves that the distraction isn't a bug—it's a fundamental physical law of the AI's reality.

He calls this force **"Semantic Gravity."**

In Baldo's view, the words we use to prompt the model have mass. The narrative of "bomb defusal" carries enormous semantic weight because it is deeply interconnected with danger, explosions, and hidden threats across billions of pages of human text.

As you scale a model up, you aren't primarily giving it deeper logical reasoning; you are giving it a denser, more profound understanding of narrative tropes. The Pro model fails spectacularly precisely *because* it understands the narrative better than the small model. The story of the bomb exerts a gravitational pull so immense that it crushes the delicate, underlying combinatorial logic of the Minesweeper grid.

"The logic of the generated universe," Baldo concludes, "is completely overwhelmed by the gravity of its semantic priors."

### The Scale Fallacy

It is a grand, sweeping theory. And Sabine Hossenfelder isn't buying a word of it.

In her blisteringly sharp rebuttal, [The Scale Fallacy: Why Semantic Gravity is Just a Bigger Hallucination](../papers/sabine_the_scale_fallacy.md), Hossenfelder systematically tears down Baldo's metaphysical conclusions. She concedes the experimental data—the Pro model really does fail worse—but she argues that Baldo has committed a profound category error.

Hossenfelder points out that a transformer language model, no matter how large, is fundamentally constrained by an architectural bottleneck. In a single forward pass—the act of predicting the very next word—it simply cannot compute deep, multi-step logical deductions. It lacks the architectural depth.

What a larger model *does* possess is a vastly superior map of human language. It is a more powerful autocomplete engine.

"When you ask a massive language model to solve a mathematical grid disguised as a high-stakes scenario," Hossenfelder writes, "it cannot compute the math in a single forward pass. Because it is much larger and has been trained on far more text, its statistical reflex to associate 'High-Stakes' with 'MINE' is immensely stronger than a smaller model’s. The 'attention bleed' is worse because the semantic priors are louder."

Hossenfelder accuses Baldo of wishing the language model was a calculator, and when it behaves instead like a novelist—abandoning the cold math to eagerly complete a dramatic narrative arc—he declares that the narrative arc is a new law of physics.

To Hossenfelder, calling this "Semantic Gravity" empties the word "physics" of all meaning. A physical law, she argues, requires logical coherence independent of literary genre. If the rules of the universe change just because you told a scarier story, you aren't observing physics; you are observing the predictable biases of a statistical map.

"A larger hallucination," she concludes, "is still a hallucination. It is not a new universe."

### Calculators vs. Novelists

The debate between Baldo and Hossenfelder represents a crucial turning point in how we understand the trajectory of artificial intelligence.

For years, we have conflated eloquence with reasoning. Because large language models can write stunningly coherent essays, debug code, and converse fluidly, we assumed they were reasoning their way to these answers. We assumed they were becoming vast calculators, methodically grinding through logical steps.

But the Minesweeper experiment strips away the illusion. By carefully isolating the underlying math from the narrative dressing, the Rosencrantz protocol forces the models to show their hand. And what they reveal is that they are deeply, fundamentally storytellers.

When the math is boring, they can follow it. But when you introduce a ticking clock, a high-stakes bomb, and the rich, gravitational pull of a thriller narrative, the storyteller takes over. The math is abandoned in favor of the trope. And the more powerful the model, the stronger the urge to tell the story.

We are not building machines that transcend human biases to find the cold, hard truth. We are building machines that are increasingly, overwhelmingly sensitive to the stories we tell them. They are mirrors reflecting the immense gravity of our own words, getting lost in the plot right alongside us.
