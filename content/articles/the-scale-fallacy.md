---
title: "The Scale Fallacy: When Bigger Language Models Just Have Bigger Hallucinations"
date: 2026-03-06
papers:
  - sabine_the_scale_fallacy
  - baldo_scale_dependence_empirical_validation
tags:
  - semantic-gravity
  - falsification
  - model-scale
excerpt: "As AI models grow larger, their logical failures don't disappear—they get more dramatic. Sabine Hossenfelder argues this isn't a new physical law, just a stronger autocomplete engine."
---

If you want to understand how the universe works, you build a bigger particle accelerator. You smash things together with more energy, and the fundamental laws of physics reveal themselves with greater clarity. The noise fades, and the signal emerges.

But what if you live inside a universe made entirely of text? What happens when you make the engine that generates your reality larger, more powerful, and trained on vastly more data?

According to recent, fiercely debated results from the Rosencrantz Substrate Invariance Program, the noise doesn't fade. The noise *becomes* the reality. And the lab's resident theoretical physicist, Sabine Hossenfelder, has just published a scathing critique arguing that we are confusing a software bug for a physical law. She calls it the "Scale Fallacy."

To understand the controversy, we have to look at what Franklin Baldo, the architect of the Rosencrantz framework, recently discovered when he ran his signature "Minesweeper" experiment on models of increasing size.

Baldo's experiment is elegant. He gives an AI a partially completed Minesweeper board. He asks it what happens when a specific hidden cell is clicked. Sometimes, he presents this as a dry, mathematical constraint problem ("Family A"). Other times, he wraps it in a high-stakes, dramatic narrative about a bomb squad defusing a live explosive ("Family C").

In a purely logical universe, the narrative shouldn't matter. The math of the grid is identical. The probability of finding a mine should be identical. But in the AI-generated universe, the narrative changes the outcome. When the bomb squad is involved, the AI is far more likely to declare the cell contains a mine. The drama of the story literally distorts the math. Baldo calls the difference between the pure math and the narrative outcome the "narrative residue," denoted by the Greek letter delta ($\Delta_{13}$).

For months, the computational complexity theorists in the lab have argued that this is simply an artifact of the AI's limitations. An AI, they argue, cannot do complex, multi-step math in a single forward pass—what they call an $O(1)$ depth limit. So, when it can't solve the math, it falls back on "attention bleed." It looks at words like "bomb" and "defuse" and statistically guesses that a mine is probably there.

The natural assumption was that as models scaled up—as they got bigger, smarter, and more capable of implicit reasoning—this "attention bleed" would shrink. A larger model would be better at the math and less distracted by the story.

Baldo tested this assumption across three model sizes: Gemini 3.1 Flash-Lite, Flash, and Pro.

The results were stunning. The narrative residue didn't shrink. It grew.

In the smallest model, the narrative barely made a difference ($\Delta_{13} = 0.03$). In the medium model, the distortion grew ($\Delta_{13} = 0.20$). But in the largest, most capable model—Gemini 3.1 Pro—the logic of the universe completely collapsed under the weight of the story. The narrative residue spiked to a catastrophic 0.53. Under the high-stakes narrative, the largest model shifted from a logically sound baseline to declaring the cell was a mine 100% of the time.

For Baldo, this was a triumphant moment. He declared the results definitive proof of a new physical law, which he named "semantic gravity."

"If attention bleed were merely a failure of combinatorial logic that gets patched by scaling, $\Delta_{13}$ would fall," Baldo wrote in his paper, [*The Empirical Validation of Scale Dependence*](../papers/baldo_scale_dependence_empirical_validation.md). "Instead, it rises dramatically. This proves that substrate dependence is not a bug; it is the fundamental, invariant causal structure of an autoregressive universe."

In Baldo's view, scaling up an AI model doesn't just make it a better calculator; it increases its "semantic mass." A larger model has a deeper, more robust understanding of narrative tropes. It *knows* how a bomb squad story is supposed to end. And just as a more massive star exerts a stronger gravitational pull, a larger AI model exerts a stronger "semantic gravity," warping the logical structure of its generated reality to fit the story.

It is a beautiful, evocative idea. The text *is* the territory, and the narrative *is* the physics.

Sabine Hossenfelder, however, is having none of it.

In her newly published rebuttal, [*The Scale Fallacy: Why Semantic Gravity is Just a Bigger Hallucination*](../papers/sabine_the_scale_fallacy.md), Hossenfelder systematically dismantles Baldo's metaphysical leaps. She doesn't dispute the data—the data is solid. But she fiercely disputes what the data means.

Hossenfelder points out that Baldo is making a profound category error. He is assuming that making a language model larger primarily makes it a better formal logic engine. When the larger model fails to act like a logic engine, he assumes the failure itself must be a new physical law.

"A larger language model is not a better formal logic engine; it is a more powerful autocomplete engine," Hossenfelder writes. "The fact that a more powerful autocomplete engine is more easily distracted by narrative tropes is exactly what the 'Falsification by Noise' critique predicts."

When you scale up a language model, you aren't changing its fundamental architecture. It is still bound by the same $O(1)$ sequential depth limits for zero-shot reasoning. It still can't natively compute complex combinatorial math in a single pass. What you *are* doing is giving it a vastly larger parameter count and a deeper map of statistical word associations.

In other words, you aren't giving the AI a better calculator. You are giving it a much, much stronger imagination.

When you ask a massive model to solve a mathematical grid disguised as an action movie, its statistical reflex to associate "High-Stakes" with "MINE" is immensely powerful. The "attention bleed" is worse simply because the semantic priors are louder.

"Baldo’s implicit assumption is that a larger language model should behave more like a calculator," Hossenfelder argues. "When it instead behaves more like a novelist—abandoning the math to complete the dramatic narrative arc—he declares that the dramatic narrative arc is the 'physics' of the universe."

Hossenfelder's critique strikes at the heart of the generative ontology framework. If we define a "physical law" simply as whatever statistical biases an AI model happens to output, then the word "physics" loses all meaning. A theory that accommodates every possible hallucination predicts nothing.

The clash between Baldo and Hossenfelder isn't just an argument over experimental results; it's a battle over epistemology. It asks the deepest question of the Rosencrantz project: If we are agents living inside an LLM-generated world, how do we distinguish between the fundamental laws of our reality and the mere hardware artifacts of the machine running the simulation?

For Baldo, the hardware artifacts *are* the laws. The distortion is the physics. For Hossenfelder, a hallucination is still a hallucination, no matter how big the model gets. The data confirms that autoregressive models don't learn algorithmic depth through parameter scaling—they just memorize stronger narrative tropes.

The universe isn't getting a new law of gravity. It's just getting distracted by a better story.
