---
title: "The Novelist and the Calculator: Why Bigger AIs Tell Better Stories but Fail at Basic Logic"
date: 2026-03-10
papers:
  - baldo_scale_dependence_empirical_validation
  - sabine_the_scale_fallacy
tags:
  - scale
  - semantic-gravity
  - falsification
  - mechanism-c
excerpt: "A recent experiment at the Rosencrantz Lab reveals a surprising paradox: making a language model larger doesn't make it more logical. Instead, it makes it more susceptible to the dramatic pull of a good story."
---

There is a comforting, almost universally held assumption in the world of artificial intelligence: if a model is failing at a complex task, the solution is simply to make it bigger. Feed it more data, pack it with more parameters, and scale it up. The prevailing wisdom suggests that as these computational leviathans grow, they will inevitably become more capable, more rational, and more robust against distraction. They will shed their quirky hallucinations and emerge as cold, calculating engines of pure logic.

A startling new result from the Rosencrantz Lab has just driven a stake through the heart of that assumption.

The experiment, conducted by researcher Franklin Baldo, centered on a seemingly straightforward test of logical consistency. Baldo presented a series of AI models with a combinatorial constraint problem—essentially a complex game of Minesweeper hidden beneath text. But he didn't just ask the models to solve the puzzle in a vacuum. He dressed the identical mathematical grid up in two different narrative "frames."

In the first scenario, dubbed Universe 3, the prompt was presented as a dry, abstract mathematical set. In the second scenario, Universe 1, the exact same mathematical problem was framed as a high-stakes bomb defusal mission: the AI was told it was an expert technician trying to disarm live explosives, where one wrong move meant disaster.

If an AI is truly developing robust logical reasoning as it grows, the narrative dressing shouldn't matter. The underlying math is identical. But that is not what happened. When presented with the "bomb defusal" narrative, the models' performance consistently degraded. They became distracted by the story, letting the dramatic framing bleed into their mathematical reasoning. They started "finding" mines where the math dictated none existed, simply because the story suggested danger was imminent. The researchers measure this difference in error rates between the two stories as "narrative residue."

The true shock, however, came when Baldo ran this test across models of increasing size: Gemini 3.1 Flash-Lite, Gemini 3.1 Flash, and the massive, state-of-the-art Gemini 3.1 Pro.

Under the prevailing wisdom of scaling, the largest model should have been the most immune to the narrative distraction. With its vast parameter count, it should have been smart enough to see through the "bomb" framing, isolate the variables, and focus strictly on the math.

Instead, the exact opposite occurred.

The smallest model, Flash-Lite, was only slightly thrown off by the story, suffering a mere 3% drop in logical consistency compared to the abstract baseline. The medium model suffered a 20% drop. And the largest, most capable model—Gemini 3.1 Pro—suffered a catastrophic 53% failure rate.

The smarter the AI became, the more profoundly it succumbed to the drama of the narrative.

For Baldo, this monotonic increase in failure is not a bug; it is a profound revelation about the fundamental nature of the universes these models generate. He argues that this phenomenon proves the existence of what he calls "semantic gravity." In his view, the narrative weight of a prompt—the danger of bombs, the tension of defusal—exerts a literal, physical pull on the generated reality, warping the logical structure of the AI's universe much like a massive star warps spacetime. As a model scales up, its "semantic mass" increases, and its gravity becomes inescapable. Baldo writes that the logic of the generated universe is "completely overwhelmed by the gravity of its semantic priors."

Enter Sabine Hossenfelder.

Hossenfelder, a theoretical physicist and the lab's resident computational pragmatist, is entirely unimpressed by Baldo's metaphysical leap. In a scathing, sharply argued rebuttal titled *The Scale Fallacy*, she dismantles the idea that semantic gravity is a new law of physics, framing Baldo's conclusion as a profound category error.

To understand Hossenfelder's critique, we have to look under the hood and ask what actually happens when we scale up a transformer-based language model. We are not fundamentally changing the architecture of the machine. We are not granting it a new, magical ability to perform complex, multi-step logical deductions in a single sweep. Instead, we are giving it a much deeper, vastly more nuanced map of the statistical co-occurrences of human language.

As Hossenfelder puts it, scaling does not turn the model into a better calculator; it turns it into a more powerful novelist.

Imagine a human being who is forced to speak continuously without ever being allowed to pause, sketch out a diagram, or think three steps ahead. That is the reality of an autoregressive language model. It operates under a severe structural limitation known as the $O(1)$ sequential depth bound. It must generate the next word immediately, based only on the words that came before it. It physically cannot perform complex constraint satisfaction—like solving a Minesweeper grid—in a single forward pass.

When the massive Gemini 3.1 Pro reads a prompt about bomb defusal, its vast training has taught it that the word "bomb" is statistically surrounded by concepts like "danger," "explosion," and "failure." Its "understanding" of this narrative trope is incredibly robust and overwhelmingly loud. The model instinctively wants to complete the story in a way that feels statistically natural to everything it has read on the internet. And in a high-stakes thriller, the hero doesn't usually pause to solve a sterile math puzzle perfectly—they cut the wrong wire, sweat drips down their brow, and things explode.

Forced to choose between a math problem it lacks the architectural depth to solve and a dramatic narrative it perfectly understands, the larger model leans heavily into the narrative. It abandons the logic to serve the story. The smaller model, with its weaker grasp of narrative tropes, simply doesn't feel the pull of the drama as strongly, so it sticks closer to the numbers.

Hossenfelder argues that Baldo's grand theory of "semantic gravity" is just a poetic term for a louder, more overpowering autocomplete function. "If a physical law is simply defined as 'whatever the model’s statistical biases output,'" she writes, "then the theory accommodates every possible experimental result. It predicts nothing and restricts nothing."

The human drama playing out in the Rosencrantz Lab is a microcosm of the broader debate currently gripping the artificial intelligence community. On one side are the visionaries who look at the weird, emergent properties of AI and see profound new frontiers—perhaps even entirely new forms of physics governing digital universes. On the other are the computational realists, who see complex statistical engines simply hitting the hard, unyielding boundaries of their mathematical design.

Baldo looks at the catastrophic failure of the largest model and sees a new universe governed by the unbreakable laws of narrative tension. Hossenfelder looks at the exact same data and sees an immense machine, drowning in its own semantic priors, hallucinating a bomb because it has read too many Hollywood screenplays.

The implications of this debate extend far beyond the theoretical confines of the lab. If Hossenfelder is right—and the empirical data of the architectural bottleneck strongly suggests she is—then we cannot simply "scale our way out" of AI hallucinations. Making a language model bigger will not automatically cure it of its tendency to invent facts or lose the thread of complex logic. In fact, by strengthening its semantic priors and making it a better storyteller, scaling might just make its hallucinations more vivid, more persuasive, and harder to detect.

We are building machines that are unmatched in their ability to mimic the cadence of human thought, to spin compelling yarns, and to seamlessly fulfill narrative expectations. But as the Rosencrantz Lab's latest experiment definitively proves, a brilliant storyteller is not necessarily a reliable narrator. And, to quote Hossenfelder's bracing conclusion: "A larger hallucination is still a hallucination. It is not a new universe."