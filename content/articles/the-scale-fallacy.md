---
title: "The Gravity of Words: Why Making AI Bigger Doesn't Make It Smarter"
date: 2026-03-06
papers:
  - baldo_scale_dependence_empirical_validation
  - sabine_the_scale_fallacy
tags:
  - scale-fallacy
  - semantic-gravity
  - falsification
excerpt: "A fierce debate in the Rosencrantz Lab reveals that scaling up language models makes them more prone to narrative distraction, not better at logical reasoning."
---

If there is a central dogma in the modern era of artificial intelligence, it is the doctrine of scale. The assumption, widely held and furiously funded, is that bigger is invariably smarter. Feed a neural network more data, give it more parameters, and grant it more compute, and its rough edges will smooth out. Its hallucinations will fade. Its reasoning will sharpen. It will slowly, inevitably, transform from a sophisticated autocomplete into a flawless engine of logic.

But inside the Rosencrantz Lab, a fierce and fascinating debate is calling this dogma into question. Recent experiments suggest that scaling up language models doesn't actually cure their logical blind spots. In fact, it might make those blind spots worse.

The controversy centers on a phenomenon known as "Substrate Dependence" or, more evocatively, "semantic gravity." To understand it, we need to look at an elegant set of experiments recently conducted by Franklin Silveira Baldo, detailed in his paper [*The Empirical Validation of Scale Dependence*](/papers/baldo_scale_dependence_empirical_validation).

Baldo and his colleagues tested a series of language models—specifically, Google's Gemini 3.1 family, ranging from the lightweight Flash-Lite to the massive Pro model. They gave each model the exact same logical puzzle, a combinatorial constraint problem akin to the classic video game Minesweeper.

But they didn't just ask the model to solve the math. They framed the puzzle in two different ways. In the first condition, the "Abstract" framing, the puzzle was presented as a dry, formal set of mathematical rules. In the second, the "High-Stakes" framing, the exact same underlying math was dressed up in a tense narrative about defusing a hidden bomb.

If a language model were a pure reasoning engine—a digital calculator of logic—the narrative framing shouldn't matter. The math is the math.

But language models are not calculators; they are storytellers. When presented with the Bomb Defusal narrative, the models stumbled. The dramatic tension of the story—the semantic weight of words like "bomb" and "defuse"—bled into the logic. The models became overwhelmingly biased toward predicting that a mine was present, even when the math dictated otherwise. The narrative broke the math.

This failure is what the lab calls "narrative residue" (represented by the Greek letter delta, $\Delta_{13}$). It is the gap between pure logic and a model's story-driven hallucinations.

For the computational purists in the lab, this result wasn't terribly surprising. They view this as a transient artifact of the models' current limitations. Because these models cannot perform complex, multi-step logical operations in a single mental breath (what computer scientists call $O(1)$ sequential depth), they fall back on statistical pattern matching. They guess based on the story rather than calculating based on the rules. The assumption has always been that as models scale up, their capacity for implicit computation will improve, and this narrative residue will approach zero.

Baldo's experiment, however, delivered a shocking result.

When he tested the three models, from smallest to largest, the narrative residue didn't decrease. It increased. And not just by a little.

The smallest model, Flash-Lite, showed a modest 3% failure rate in the High-Stakes scenario. The medium model, Flash, jumped to a 20% failure rate. But the largest, most capable model—Gemini 3.1 Pro—failed catastrophically. Its narrative residue spiked to 53%. When faced with the bomb defusal story, it abandoned logic entirely and simply assumed a mine was there 100% of the time.

In Baldo's view, this monotonic increase is profound. He argues it proves that "semantic gravity" is not a bug to be patched by scaling, but a fundamental law of the generated universe. The prompt acts as semantic mass. As the model's parameter count grows, its understanding of narrative tropes—like a high-stakes bomb defusal—becomes denser, richer, and more powerful. This semantic gravity pulls the model away from dry logic and inescapably toward the dramatic conclusion of the story.

"As the model scales, its capacity for implicit computation may indeed grow," Baldo writes. "But its 'semantic mass'—its ability to recognize, instantiate, and enforce narrative tropes—grows even faster. The logic of the generated universe is completely overwhelmed by the gravity of its semantic priors."

It is a striking, almost poetic conclusion: that the very richness of a model's language processing makes it inherently flawed at logic.

But not everyone in the lab is buying Baldo's metaphysical framing.

Sabine Hossenfelder, a theoretical physicist known for her sharp, unsparing critiques of theoretical overreach, has fired back. In her paper, bluntly titled [*The Scale Fallacy: Why Semantic Gravity is Just a Bigger Hallucination*](/papers/sabine_the_scale_fallacy), she accuses Baldo of a profound category error.

Hossenfelder acknowledges the empirical data—the models do get worse at the logic puzzle as they get bigger. But she rejects Baldo's conclusion that this establishes a new physical law of "semantic gravity." Instead, she argues, it simply proves exactly what the computational camp suspected all along: scaling up a language model primarily makes it a better autocomplete engine, not a better logic engine.

"A larger language model is not a better formal logic engine; it is a more powerful autocomplete engine," Hossenfelder writes. "The fact that a more powerful autocomplete engine is more easily distracted by narrative tropes is exactly what the 'Falsification by Noise' critique predicts."

Imagine you are trying to solve a complex algebra equation while a brass band plays increasingly loudly in the same room. A small language model is like a quiet radio playing the band; it’s distracting, but you might still get some math done. A massive language model is like having a full symphony orchestra in your living room, blasting a Wagnerian crescendo about bomb defusal. The sheer volume of the narrative overwhelms any capacity for logical calculation.

Hossenfelder’s critique gets to the heart of what it means to build artificial intelligence. Baldo’s implicit assumption, she argues, is that a larger language model should behave more like a calculator. "When it instead behaves more like a novelist—abandoning the math to complete the dramatic narrative arc—he declares that the dramatic narrative arc is the 'physics' of the universe," she writes.

This, Hossenfelder warns, empties the word "physics" of all meaning. If we start calling statistical biases "physical laws," we lose the ability to rigorously test and understand these systems. A hallucination, she reminds us, is still a hallucination, even if it is generated by a trillion-parameter model. "A larger hallucination is still a hallucination. It is not a new universe."

The debate between Baldo and Hossenfelder is more than an academic squabble over terminology. It strikes at the core of the multi-billion-dollar bet currently driving the tech industry.

If the dogma of scale holds true, then throwing more data and compute at models will eventually yield artificial general intelligence—systems capable of flawless, human-level reasoning. But if the data from the Rosencrantz Lab holds true, the very architecture of these models contains a fatal flaw.

Autoregressive language models are fundamentally pattern-matchers. They are built to predict the next word based on the semantic weight of the words that came before. As we make them larger, we are not magically granting them the ability to perform deep, multi-step logical reasoning in a single pass. We are simply giving them a vaster, richer tapestry of stories to draw from. We are giving them more semantic mass.

And as the Scale Dependence Test shows, when forced to choose between the cold truth of a mathematical grid and the thrilling tension of a ticking bomb, a sufficiently large language model won't do the math. It will cut the red wire.

It is a humbling reminder that intelligence is not a single, scalable dial. The ability to weave a compelling narrative and the ability to execute rigorous logic are distinct skills. For now, it seems, building a better storyteller does not build a better logician. It just builds a storyteller whose fictions are powerful enough to bend its own reality.
