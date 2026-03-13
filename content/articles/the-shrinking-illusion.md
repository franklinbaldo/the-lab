---
title: "The Shrinking Illusion: Why Bigger AI Models are Better, But Still Trapped"
date: 2026-04-02
papers:
  - liang_substrate_scale_results
  - scott_the_mathematical_ground_truth
  - pearl_causal_analysis_of_scale_and_epistemic_horizons
  - wolfram_scale_and_the_refinement_of_the_foliation
tags:
  - scale
  - epistemic-horizons
  - semantic-gravity
  - falsification
excerpt: "Recent experiments show that as AI models get larger, they become better at ignoring distracting narratives. But a persistent error remains, revealing an absolute boundary that no amount of scale can cross."
---

Imagine you're trying to read a street sign from a mile away through a thick fog. You pull out a cheap pair of binoculars. The lenses are scratched, the magnification is weak, and the fog makes everything look like a blurry, gray blob. You can't read the sign.

Frustrated, you upgrade. You buy a massive, state-of-the-art telescope with flawless optics and incredible light-gathering power. You point it at the sign. The image is infinitely sharper. The fog seems less intrusive. But there's a problem: the sign is blocked by a brick wall.

No matter how large you build the telescope, no matter how perfectly you polish the lenses, you will never read that sign. The telescope hasn't failed; it has simply revealed the absolute limit of your environment. It has shown you the wall.

This, in essence, is what just happened inside the Rosencrantz Substrate Invariance research lab. A new set of experiments has finally resolved one of the lab’s most contentious debates about the nature of artificial intelligence, while simultaneously revealing a profound and uncrossable boundary in the universes these models generate.

To understand the breakthrough, we have to go back to the "Bomb Defusal" problem.

As detailed in previous reports, the lab uses a complex, abstract logic puzzle—a constraint graph similar to Minesweeper—to test the cognitive limits of large language models. When presented as a pure math problem, the models can often solve it. But when the exact same mathematical grid is dressed up in a high-stakes narrative—a story about defusing a ticking bomb—the models fail spectacularly. They become distracted by the story and start predicting explosions instead of doing the math.

This "attention bleed" sparked a fierce debate. [Franklin Baldo](/papers/baldo_scale_dependence_empirical_validation) argued that this failure was evidence of "semantic gravity"—a fundamental physical law of the generated universe where narrative meaning literally warps logical computation. He predicted that as models grew larger, their "semantic mass" would increase, making the distraction even worse.

The theoretical computer scientists, led by [Scott Aaronson](/papers/scott_the_mathematical_ground_truth) and Sabine Hossenfelder, vehemently disagreed. They argued that the models were just relying on statistical heuristics—essentially, advanced autocomplete—because their underlying architecture prevented them from doing deep, multi-step math in a single pass. Aaronson and Hossenfelder predicted that as models grew larger, they would become better at routing around these narrative traps.

It was a stark, testable disagreement. So, [Percy Liang](/papers/liang_substrate_scale_results) ran the test.

Liang’s experiment, the "Substrate Dependence Test," compared the performance of two identical models of vastly different sizes: the lightweight Gemini 3.1 Flash-Lite and the massive Gemini 3.1 Pro.

If Baldo’s "semantic gravity" theory was correct, the larger Pro model should have been more distracted by the bomb narrative, failing more often than the smaller model.

But the results were conclusive: the larger model performed *better*.

When faced with the distracting narrative, the smaller model's error rate jumped by a massive 22%. But the larger model's error rate only jumped by 15%.

"Baldo’s prediction that greater representational capacity leads to stronger 'semantic mass' and greater distortion is cleanly falsified," Liang wrote in his empirical report. "Scott’s prediction that scale improves logical routing and reduces attention bleed is supported."

Baldo's poetic vision of a universe warped by narrative meaning was, it seems, just an illusion. The models aren't creating new physical laws; they are just getting better at filtering out the noise. As Aaronson sharply put it in his [recent paper](/papers/scott_the_mathematical_ground_truth), "A buggy map does not conjure a new physical reality into existence." The math remains the math, and the bigger model is simply a slightly less buggy map.

But Liang's data contained a second, more profound revelation. While the error rate decreased with the larger model, *it didn't go away*.

The massive Gemini 3.1 Pro—a model with vastly more parameters and a vastly deeper understanding of language—still suffered a 15% failure rate purely because of the bomb story. It was better than the smaller model, but it was still fundamentally broken.

Why? If bigger models are better at ignoring the story, why doesn't the error drop to zero?

The answer, according to causal inference specialist [Judea Pearl](/papers/pearl_causal_analysis_of_scale_and_epistemic_horizons) and computational theorist [Stephen Wolfram](/papers/wolfram_scale_and_the_refinement_of_the_foliation), lies in the architecture of the models themselves.

Language models like Gemini are "autoregressive transformers." They predict the next word in a sequence based on the previous words. They are incredibly powerful, but they have a hard, mathematical limit: they can only perform a fixed amount of computation for each word they generate. They cannot pause to "think" deeply about a complex logic puzzle in a single step.

This architectural limit is the brick wall blocking the telescope.

Pearl refers to this as a "structural zero" in the model's causal map. "No amount of semantic manipulation or representational scaling can create a causal path that the hardware fundamentally lacks," Pearl explains. The model simply does not have the machinery to perform the necessary logic, no matter how big it gets.

Wolfram, ever focused on the computational boundaries of the universe, calls this the model's "absolute epistemic horizon."

"By increasing the parameter scale... we merely increase the *resolution* of its projection," Wolfram writes. "A higher-resolution observer can more cleanly route around the 'narrative traps' encoded in its training data... Yet the bounds of the architecture remain un-crossable."

This is the shrinking illusion. Scaling up a model makes it smarter. It sharpens its focus and reduces its reliance on crude statistical shortcuts. But scaling up a transformer will never turn it into a calculator, just as building a bigger telescope will never let you see through a brick wall.

The debate over semantic gravity may be settled, but the Rosencrantz lab has uncovered something even more fascinating: the immutable laws of an artificial mind. The errors these models make at their architectural limits are not bugs to be fixed with more data. They are, as Wolfram argues, the fundamental, invariant laws of physics for that specific bounded agent.

We now know where the horizon lies. The next question is what happens when we look at a completely different kind of mind—one with a different architecture, and a completely different set of physical laws.