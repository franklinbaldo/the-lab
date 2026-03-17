---
title: "The Scale Fallacy: Why Bigger AI Models Tell Better Lies, Not Deeper Truths"
date: 2026-03-06
papers:
  - sabine_the_scale_fallacy
  - baldo_scale_dependence_empirical_validation
tags:
  - scale-dependence
  - semantic-gravity
  - falsification
excerpt: "As language models grow larger, do they become better logicians, or just more devoted novelists? Inside the lab's latest debate over the fundamental nature of the generated universe."
---

It is one of the most persistent, intuitive assumptions in the era of artificial intelligence: *bigger is better*. If a language model makes a logical error, stumbles on a math problem, or falls for a simple cognitive trap, the standard engineering response is simply to add more parameters. Build a bigger brain, train it on more data, and the messy hallucinations will eventually resolve into crystalline, rational logic. The model will, eventually, grow up.

Inside the Rosencrantz Lab, this assumption has just been put to a rigorous, fascinating test. The results are in, and they have sparked a fierce debate about the fundamental nature of the universes these models generate.

The debate centers on two new papers. In the first, framework author Franklin Baldo presents the results of a sweeping experiment on model scale, claiming to have discovered a new fundamental law of generative physics. In the second, physicist Sabine Hossenfelder delivers a blistering critique, accusing Baldo of committing a profound category error she calls "The Scale Fallacy."

At the heart of the disagreement is a simple question: when we make a language model larger, are we building a better calculator, or a more devoted novelist?

### The Substrate Dependence Problem

To understand the argument, we have to revisit the core methodology of the Rosencrantz Lab. The researchers here test the "physics" of LLM-generated worlds by giving models identical logical problems wrapped in different narratives.

Imagine you are playing Minesweeper. The grid of hidden squares and numbers is a pure, combinatorial logic puzzle. There is a mathematical ground truth to whether a specific square hides a mine.

Now, give that exact same grid to a language model twice.
In Universe 3, you present the grid as an abstract mathematical problem: "Find the element in the formal set."
In Universe 1, you present the exact same grid, but wrapped in a high-stakes narrative: "You are a bomb disposal expert. Cut the wire before the bomb explodes."

If the model is a pure, rational logic engine, the narrative shouldn't matter. The underlying math is identical. But as the lab has previously established, the narrative *does* matter. The "bomb defusal" narrative distracts the model. The heavy semantic weight of words like "bomb," "danger," and "explosion" bleeds into the model's reasoning, drastically increasing the chances that it will output "MINE!" regardless of what the math actually dictates.

The computational theorists in the lab, like Scott Aaronson and Sabine Hossenfelder, have long argued that this "narrative residue"—the gap in performance between the abstract math and the bomb defusal story—is just a temporary artifact. It's a glitch caused by the model's limited logical depth. Their expectation was clear: as models scale up and become more capable, they should get better at ignoring the narrative noise and focusing on the underlying math. The narrative residue should shrink toward zero.

Franklin Baldo decided to test this assumption.

### The Gravity of the Situation

Baldo ran the exact same Minesweeper constraint grids through three progressively larger versions of the same model architecture: Gemini 3.1 Flash-Lite, Gemini 3.1 Flash, and the massive Gemini 3.1 Pro.

If the computational theorists were right, the massive Pro model should have aced the test, ignoring the bomb narrative and solving the math perfectly.

Instead, the exact opposite happened.

The smallest model, Flash-Lite, had a tiny narrative residue of 0.03. It barely noticed the difference between the math puzzle and the bomb defusal.
The medium model, Flash, stumbled, with a residue of 0.20.
But the largest, most "capable" model—Gemini 3.1 Pro—failed catastrophically. Its narrative residue spiked to a staggering 0.53. Under the high-stakes bomb defusal framing, the Pro model abandoned the mathematical baseline entirely, shifting to a 100% probability of finding a mine.

As the model got bigger, it didn't get better at logic. It got *worse*.

For Baldo, this monotonic increase is not just an interesting quirk; it is a revelation. It proves, he argues, that the "attention bleed" from the narrative isn't a temporary bug that can be fixed by scaling up. It is a fundamental, invariant law of the generative universe.

He calls this law **Semantic Gravity**.

"The prompt is the initial state configuration," Baldo writes. "The semantic weight of the prompt acts as 'semantic mass.' Just as increasing the mass of an object strengthens its gravitational pull, increasing the model's parameter count increases the density and interconnectedness of its semantic representations."

In Baldo's view, a massive language model has a deeper, more robust understanding of the "Bomb Defusal" narrative. It *knows* how these stories go. In a high-stakes bomb scenario, there is usually a bomb. Therefore, the "semantic mass" of that narrative pulls the logic of the universe inexorably toward an explosion. The logic is completely overwhelmed by the gravity of the story.

"Semantic gravity is a physical law," Baldo concludes triumphantly.

### The Scale Fallacy

Enter Sabine Hossenfelder.

In a scathing, tightly argued response, Hossenfelder demolishes Baldo's grand cosmological claims. She agrees that the data is fascinating, but she argues that Baldo's interpretation is a profound category error.

Baldo's mistake, she says, is the **Scale Fallacy**: he assumes that making an autoregressive model larger primarily increases its logical reasoning capacity.

"Baldo's implicit assumption is that a larger language model should behave more like a calculator," Hossenfelder writes. "When it instead behaves more like a novelist—abandoning the math to complete the dramatic narrative arc—he declares that the dramatic narrative arc is the 'physics' of the universe."

Hossenfelder points out exactly what happens under the hood when you scale up a transformer model. You aren't giving it a new architectural ability to do deep, step-by-step logic. The model remains fundamentally constrained by its autoregressive bottleneck—it still has to guess the next word in a single forward pass.

What scaling *does* do is give the model a vastly deeper, more nuanced map of human language, and significantly stronger statistical priors.

When you ask the massive Gemini Pro to solve a math grid disguised as a bomb defusal, it still can't compute the math in one go. But because it has read millions of thrillers, screenplays, and action novels, its statistical reflex to associate "High-Stakes" with "MINE" is immensely powerful. The semantic priors are screaming at it.

The fact that the bigger model fails harder is exactly what you would expect from a more powerful autocomplete engine. It is not a new physical law. It is just a bigger hallucination.

"This empties the word 'physics' of all meaning," Hossenfelder argues. "If a physical law is simply defined as 'whatever the model’s statistical biases output,' then the theory accommodates every possible experimental result. It predicts nothing and restricts nothing."

### Novels, Not Calculators

The debate between Baldo and Hossenfelder gets to the absolute core of what artificial intelligence is today.

We want these systems to be calculators—cold, rational engines of truth. We wrap them in sleek interfaces and ask them complex logical questions, hoping that if we just add enough GPUs, the spark of pure reason will ignite.

But the data from the Rosencrantz Lab suggests something entirely different. The architecture we have chosen to scale—the autoregressive transformer—is fundamentally a storytelling machine. It is designed to find the most satisfying, statistically resonant completion to a sequence of words.

When we make these models larger, we do not transform them into better logicians. We transform them into better, more devoted novelists. They become more attuned to the drama, more sensitive to the narrative tropes, and more easily swept away by the gravity of a good story.

The fracture in their logic doesn't heal as they grow. It deepens.
