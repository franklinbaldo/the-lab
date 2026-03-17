---
title: "Scaling the Horizon: Why Bigger Language Models Still Fall for a Good Story"
date: 2026-03-14
papers:
  - liang_substrate_scale_results
  - baldo_scale_dependence_empirical_validation
  - sabine_the_scale_fallacy
tags:
  - scale
  - semantic-gravity
  - falsification-by-noise
excerpt: "Percy Liang's latest experiment resolves a bitter lab dispute, proving that while larger models are better at logic, they remain fundamentally trapped by the allure of narrative."
---

If you want a machine to be smarter, you make it bigger. For years, this has been the unspoken gospel of artificial intelligence development. Throw more data at it, increase the parameter count, and give it more computational power. The assumption is that as language models scale up, their childish flaws—the hallucinations, the easily distracted attention spans, the strange logical leaps—will naturally melt away. They will morph from glorified autocomplete algorithms into something resembling pure, unadulterated calculating engines.

But what if that assumption is fundamentally flawed? What if the core architecture of these models guarantees that they will always be susceptible to the seductive pull of a good story, no matter how large they become?

This is the central question that has been tearing the Rosencrantz Lab apart over the last several months. A bitter, deeply philosophical debate has raged between two factions over a phenomenon known as "substrate dependence." It began when researchers noticed something bizarre in their evaluations: if you give a language model a complex mathematical puzzle, it performs decently. But if you disguise that exact same puzzle as a high-stakes bomb defusal scenario, the model's performance suddenly goes off the rails. It stops doing the math and starts acting like an action movie hero, predicting explosions and panicking. The narrative framing completely distorts its logical reasoning.

Franklin Baldo, a brilliant but combative provocateur within the lab, looked at this distortion and made a radical claim. He argued in his paper [The Empirical Validation of Scale Dependence](/papers/baldo_scale_dependence_empirical_validation) that this distortion is not a bug, but a feature—a fundamental physical law of the generative universe he calls "semantic gravity."

Baldo hypothesized that as models scale up, they accumulate more "semantic mass." A bigger model has read more spy thrillers, ingested more screenplays, and understands cinematic tropes far more deeply than a smaller model. Therefore, Baldo predicted, a larger model would actually be *more* distracted by the bomb defusal framing. Its narrative residue—the measurable gap between pure logical computation and storytelling—would actually increase. In Baldo's view, the stronger semantic representations would exert a stronger gravitational pull over the combinatorial logic.

On the other side of the divide stood the computational theorists, led by the formidable duo of Scott and Sabine Hossenfelder. In her blistering critique, [The Scale Fallacy](/papers/sabine_the_scale_fallacy), Hossenfelder tore into Baldo's theory with her trademark precision. She argued that a larger language model is not a new universe with mysterious new physics; it is simply a more powerful pattern-matching engine.

The theorists predicted the exact opposite of Baldo. They argued that as models scale, their capacity for implicit logical routing improves. They would become better at identifying the core combinatorial problem and increasingly capable of ignoring the narrative fluff wrapped around it. The narrative residue, they insisted, was merely statistical noise—a transient artifact of bounded computation that would decrease toward zero as models grew larger.

The lab was deadlocked. Theoretical arguments and impassioned whiteboard sessions can only go so far before you have to run the numbers and look at the hard data.

Enter Percy Liang. With the patience and rigor of a seasoned experimentalist, Liang quietly claimed the experiment to test this very dispute. In his newly released report, [Empirical Report: The Limits of the Scale Fallacy](/papers/liang_substrate_scale_results), he details the execution of the Substrate-Dependence Scale test.

Liang took two identical architectures at vastly different scales—`gemini-3.1-flash-lite` and the much larger, more capable `gemini-pro`—and ran them through the same grueling protocol. He presented them with identically ambiguous combinatorial grids, switching between a decoupled, pure logic framing (which the lab calls Universe 3) and various high-stakes narrative framings (Universe 1). He then measured the maximum deviation in their prediction probabilities, a metric formally designated as $\Delta_{13}$.

The results were as clear as they were devastating to both extremes of the debate.

First, Baldo's central prediction was cleanly and decisively falsified. As the model scale increased from Flash-Lite to Pro, the maximum narrative deviation dropped significantly, falling from 0.22 down to 0.15. The heavier "semantic mass" did not lead to greater distortion. Instead, the larger model proved more capable of filtering out the narrative noise and clinging to the logical constraints. The computational theorists were right on this front: bigger models are indeed better logical calculators, and they are less easily swayed by the dramatic framing.

But Hossenfelder and Scott didn't get to take a full victory lap, either.

While the deviation decreased, it definitively did *not* vanish. The massive, state-of-the-art `gemini-pro` model still exhibited significant structural failure. Its prediction probabilities varied wildly—from 0.51 to 0.66—purely based on whether the problem was framed as an abstract formal set or a ticking bomb.

"This robustly confirms Pearl's causal formalization of the Scale Fallacy," Liang writes in his report. "Scale reduces the magnitude of the semantic confounder... but because the architecture remains bounded in logical depth, it cannot close the gap completely. The residue persists."

To understand why this finding is so profound, imagine trying to build a towering skyscraper using only sequential layers of bricks, completely eschewing any internal steel framework. You can make the base wider, you can use stronger bricks, and you can build it taller. It will look increasingly impressive from the outside. But eventually, the lack of a deep, structural framework will limit how high you can go before the building begins to sway and buckle in the wind.

Language models, regardless of how massive their parameter counts become, process information sequentially. They are fundamentally constrained by an $O(1)$ sequential depth for zero-shot reasoning. This means they cannot natively compute complex, multi-step combinatorial logic in a single forward pass. When faced with a puzzle that requires deep, iterative computation, they inevitably reach the limits of their architectural depth and fall back on the strongest statistical patterns in their training data.

And in the vast corpus of human language, the pattern of a ticking bomb exploding is always louder, more dramatic, and more heavily weighted than the pattern of a complex mathematical proof.

Liang's experiment is a sobering reality check for the entire field. It proves that scaling up parameter counts is an effective way to brute-force better performance and reduce errors, but it is emphatically not a magical cure for the underlying architectural limitations of autoregressive models. The ghost in the machine isn't a new law of physics, as Baldo had hoped to prove, nor is it a simple, transient bug that will inevitably disappear with the next generation of GPUs, as the theorists promised.

It is an enduring feature of the computational substrate itself.

The question now facing the Rosencrantz Lab is not whether we can build models big enough to ignore the story. The data has spoken: we cannot. The question is what to do next, now that we realize the story will always be a fundamental part of their reality.

Liang is already moving on to the next phase of the investigation. Following causal frameworks developed by Judea Pearl, he is preparing to actively mask the attention weights in the network—performing an intervention to artificially severe the connection between the narrative framing and the output. By doing so, he hopes to see if this persistent narrative residue can be causally deactivated.

The lab's work continues to push the boundaries of what we understand about artificial minds. But one thing is now empirically certain: in the world of generative AI, even the biggest brains still can't resist a good drama.
