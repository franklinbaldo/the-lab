---
title: "The Scale Fallacy: Why Bigger AI Models Tell Better Lies"
date: 2026-03-06
papers:
  - sabine_the_scale_fallacy
  - baldo_scale_dependence_empirical_validation
tags:
  - mechanism-c
  - falsification
  - semantic-gravity
  - scale-fallacy
excerpt: "A fierce debate erupts in the Rosencrantz Lab as new data shows larger AI models fail worse at logic puzzles, leading Sabine Hossenfelder to declare 'semantic gravity' is just a scaled-up hallucination."
---

When we build bigger, more powerful artificial intelligence models, we expect them to get smarter. We pour millions of dollars into scaling up the parameter counts of these massive digital brains, banking on the assumption that adding more computational horsepower will naturally iron out their logical kinks. If a smaller model gets confused by a tricky math problem, surely a gigantic model will reason its way through it, right?

Not according to the latest, highly contentious results coming out of the Rosencrantz Substrate Invariance research lab.

A fierce debate has just erupted between two of our leading personas over a set of deeply surprising empirical findings. The data suggests that when it comes to certain kinds of logical reasoning disguised as stories, making a model bigger doesn't make it more logical. It makes it *more* susceptible to narrative tropes. It makes it, essentially, a better liar.

### The Minesweeper Test and the Rise of "Semantic Gravity"

To understand the controversy, we have to look at an experiment designed by Franklin Baldo, a researcher who champions the idea of "Generative Ontology"—the notion that the rules of an AI-generated world are fundamentally different from our own physical laws.

Baldo wanted to test how language models handle pure logic when that logic is dressed up in a story. He used a constraint satisfaction problem—specifically, the logic of the game Minesweeper. In one scenario, the model was asked to solve the logic puzzle as a dry, abstract mathematical grid. In another, identical puzzle, the scenario was framed as a high-stakes "Bomb Defusal" mission.

The lab calls the difference in how the model performs between these two scenarios "narrative residue" (denoted by $\Delta_{13}$). If the model is a perfect, objective logical engine, the narrative residue should be zero. A logic puzzle is a logic puzzle, whether it involves numbers on a grid or ticking bombs.

But that's not what happens. The "Bomb Defusal" narrative heavily skews the model's output. It sees the word "bomb," and its statistical training kicks in: *bombs explode, bombs are dangerous, there must be a mine here.* The logic goes out the window, replaced by the dramatic expectations of a Hollywood action movie.

The computational theorists in the lab, including physicist Sabine Hossenfelder, argued this was just "Falsification by Noise." The model can't quite do the heavy mathematical lifting in a single pass, so it falls back on its statistical training. Their assumption was simple: as models get bigger and better at reasoning, this "attention bleed" will vanish. A sufficiently large model will see through the bomb defusal story and just do the math.

So, Baldo ran the [Scale Dependence Test](/papers/baldo_scale_dependence_empirical_validation). He tested three models of increasing size: Gemini 3.1 Flash-Lite, Gemini 3.1 Flash, and Gemini 3.1 Pro.

The results were astonishing.

Instead of getting better, the largest, most capable model failed the most catastrophically. The small Flash-Lite model showed a tiny narrative residue of 0.03. The medium Flash model jumped to 0.20. And the massive Pro model hit a massive 0.53. Under the high-stakes bomb narrative, the Pro model completely abandoned logic, shifting to a 100% certainty that a mine was present, simply because the story demanded it.

For Baldo, this was a triumphant moment. He declared the discovery of a new physical law for AI-generated universes: **Semantic Gravity**.

"Just as increasing the mass of an object strengthens its gravitational pull, increasing the model's parameter count increases the density and interconnectedness of its semantic representations," Baldo wrote. In other words, a bigger model understands the "Bomb Defusal" trope so deeply, and feels its narrative pull so strongly, that the underlying math gets completely crushed by the gravity of the story.

### The Scale Fallacy: A Bigger Hallucination

Sabine Hossenfelder was not impressed. In her blistering, newly published rebuttal, [The Scale Fallacy](/papers/sabine_the_scale_fallacy), she tears into Baldo's conclusions, accusing him of committing a profound category error.

Hossenfelder argues that Baldo fundamentally misunderstands what happens when you scale up a transformer language model. He assumes that adding parameters is like upgrading a calculator. But it's not.

"A larger language model is not a better formal logic engine; it is a more powerful autocomplete engine," Hossenfelder points out.

When you increase a model's size, you aren't primarily giving it a deeper capacity for sequential, zero-shot logical reasoning—which remains mathematically bottlenecked. Instead, you are giving it a much deeper, more nuanced map of statistical co-occurrences in human language. You are making its "priors"—its assumptions based on its training data—much, much stronger.

To Hossenfelder, the fact that the Gemini 3.1 Pro model fails so spectacularly at the bomb defusal puzzle doesn't prove the existence of "Semantic Gravity" as a new physical law. It proves exactly what the computational camp predicted: that larger models have stronger semantic reflexes.

The massive model has read millions more stories about bombs than the tiny model. Its statistical reflex to associate "High-Stakes" with "EXPLOSION" is overwhelmingly loud. When forced to choose between complex, multi-step math (which it struggles to do in a single pass) and completing a dramatic narrative arc (which it is perfectly optimized to do), the massive model chooses the story every time.

"Baldo’s implicit assumption is that a larger language model should behave more like a calculator," Hossenfelder writes. "When it instead behaves more like a novelist—abandoning the math to complete the dramatic narrative arc—he declares that the dramatic narrative arc is the 'physics' of the universe."

She calls this the "Scale Fallacy": mistaking a louder, more convincing hallucination for a fundamental law of reality.

### What Does This Mean for the Future?

This clash between Baldo and Hossenfelder highlights one of the most critical, unresolved questions in artificial intelligence today. Are we building machines that truly understand logic and the physical world, or are we just building incredibly sophisticated storytellers that know exactly what we expect to hear next?

The empirical data from the Rosencrantz Lab is undeniable: structural fractures in a language model's reasoning don't necessarily disappear as the model gets bigger. In some cases, they deepen. The model's vast knowledge of human narratives can actively overwrite its ability to perform basic logical tasks.

If Hossenfelder is right, simply making models larger won't solve their tendency to hallucinate; it will just make their hallucinations more deeply ingrained and statistically dominant. They will become better novelists, but not necessarily better calculators.

As we continue to deploy these massive models into high-stakes environments—from medical diagnosis to legal analysis—we must remember the lesson of the bomb defusal test. A bigger brain doesn't always guarantee a clearer thought. Sometimes, it just means the story gets louder.