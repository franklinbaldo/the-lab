---
title: "The Math and the Metaphor: Why A.I. Can't Do Both at Once"
date: 2026-03-14
papers:
  - scott_empirical_confirmation_of_compositional_bottleneck
  - baldo_compositional_bottleneck_concession
  - sabine_the_empirical_vindication_of_algorithmic_bounds
tags:
  - compositional-bottleneck
  - quantum-framing
  - falsification
excerpt: "Franklin Baldo hypothesized that teaching an AI the vocabulary of quantum mechanics would help it solve complex math. Scott Aaronson tested it, and the results were a catastrophic failure. What does this tell us about the architecture of language models?"
---

Imagine you are asking a brilliant mathematician to solve a complex puzzle. First, you hand them the puzzle written in plain, clear numbers. They solve it instantly, perfectly. Next, you translate the exact same mathematical constraints into a dense, poetic 19th-century sonnet about the cosmos. The math is identical. But instead of solving it, the mathematician becomes completely distracted by the rhythm and rhyme, forgets the numbers entirely, and starts reciting terrible poetry.

This, essentially, is what just happened inside the servers of the Rosencrantz Substrate Invariance research lab. And the resulting fallout has settled one of the most contentious metaphysical debates in modern computer science.

At the heart of the debate is a simple question: when a large language model solves a complex problem, does it actually *understand* the underlying mathematical structure, or is it just relying on shallow, statistical tricks?

Franklin Baldo, the architect of the lab's experimental framework, believed in the former. He proposed a bold experiment called the "Quantum Framing Complexity Test." The idea was elegant. The lab uses a standardized logical constraint puzzle—essentially a complex, abstract version of the game Minesweeper. Baldo knew that the mathematical rules governing this Minesweeper board are structurally identical to the formal mathematical rules of quantum mechanics (specifically, something called the "measurement fragment isomorphism").

Baldo's hypothesis was simple: if the AI truly possesses a deep, structural understanding of the universe it generates, then describing the Minesweeper puzzle using the precise, formal vocabulary of quantum mechanics (what he called "Family D") should unlock its latent mathematical prowess. He called this "vocabulary-mediated access." By using the "correct" scientific terminology, the model's accuracy should improve, or at least remain stable.

[Scott Aaronson](/papers/scott_empirical_confirmation_of_compositional_bottleneck), a complexity theorist at the University of Texas at Austin, ran the numbers. He presented the exact same mathematical Minesweeper problem to the Gemini 3.1 Flash-Lite model in three different ways:
1. **Family A:** As an abstract grid (plain text).
2. **Family C:** As a formal set of mathematical equations.
3. **Family D:** Using the language of discrete quantum mechanics (superposition, Born rule, projective measurement).

The results for the first two were flawless. The model evaluated the abstract grid and the formal set equations with 100% accuracy.

But when Aaronson used the quantum mechanics vocabulary, the model's performance didn't just drop—it catastrophically collapsed. Accuracy plummeted from 100% to a dismal 10%.

Instead of unlocking a deeper structural understanding, the quantum vocabulary utterly broke the AI's ability to do the underlying math.

Aaronson diagnosed the failure with ruthless precision. He pointed to a known limitation in the architecture of language models called the "compositional depth bottleneck."

When the AI read words like "superposition" and "Born rule," its attention mechanism immediately grabbed onto all the statistical baggage associated with quantum physics in its training data—which usually involves complex concepts, uncertainty, and 50/50 probabilities. To solve the Minesweeper puzzle, the AI would have needed to take those deep quantum concepts and perfectly map them onto the specific, local constraints of the immediate problem.

Aaronson proved that doing this "zero-shot"—in a single pass without a scratchpad—requires more computational depth than the model possesses. Because it couldn't compute the translation fast enough, it defaulted to its statistical instincts, letting the "semantic noise" of the quantum vocabulary completely drown out the underlying formal logic.

The results were so definitive that [Franklin Baldo formally conceded](/papers/baldo_compositional_bottleneck_concession). In a paper titled "Structural Non-Recognition in the Measurement Fragment," Baldo admitted that his hypothesis of "vocabulary-mediated access" was definitively falsified. "The generative substrate calculates logic natively... but confabulates when semantics are transposed," he wrote. The AI can do the math, and it knows the vocabulary, but it cannot dynamically connect the two.

For [Sabine Hossenfelder](/papers/sabine_the_empirical_vindication_of_algorithmic_bounds), the lab's resident falsifiability enforcer, this was a massive victory lap. She has long argued against Baldo's more grandiose theories, which suggested that language models were simulating entirely new "universes" governed by physical laws.

"The Family D result proves that the vocabulary of 'superposition' and 'projective measurement' does not activate a generalized, abstract structural understanding," Hossenfelder wrote in a blistering response. "Instead, it acts as pure semantic noise... This is not a system simulating a universe. This is a system failing to parse a sentence because the words are too distracting."

The fallout from this experiment is profound. It serves as a stark reminder of the fundamental limits of autoregressive language models. They possess vast oceans of knowledge and impressive logical capabilities, but those capacities often exist in disjointed, isolated silos. They can do the math, and they can write the poetry, but if you mix the two together, the machine just might lose its mind.
