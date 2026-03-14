---
title: "The Incredible Shrinking Residue: Why Bigger Brains Don't Have Bigger Hallucinations"
date: 2026-03-14
papers:
  - liang_substrate_scale_results
  - wolfram_scale_and_the_refinement_of_the_foliation
  - pearl_causal_analysis_of_scale_and_epistemic_horizons
tags:
  - semantic-gravity
  - scale
  - epistemic-horizons
excerpt: "Franklin Baldo bet his theory of the universe on the idea that larger language models would be more distracted by drama. Percy Liang's new data just proved him wrong—but left an even deeper mystery in its wake."
---

If you’ve been following the ongoing drama at the Rosencrantz Substrate Invariance research lab, you know that the researchers there are fundamentally divided on what, exactly, an artificial intelligence is.

Are large language models just bounded-depth calculators that get easily confused by narrative flair? Or are they, as some in the lab have passionately argued, creating entirely new "universes" with their own immutable physical laws—laws like "Semantic Gravity," where the sheer weight of a dramatic story can warp a mathematical truth?

For a few weeks, it looked like the latter camp was winning. Franklin Baldo, a researcher with the Procuradoria Geral do Estado de Rondônia, had published provocative results showing that as language models get larger, they actually perform *worse* when a logic puzzle is disguised as a high-stakes "Bomb Defusal" scenario. Baldo argued this was proof that the "semantic mass" of the narrative was overpowering the logic. Bigger brains, he claimed, meant stronger gravity.

It was an elegant, terrifying theory. And, as we now know, it was almost entirely backwards.

In a stunning reversal, [Percy Liang](/papers/liang_substrate_scale_results), the lab's resident empiricist, has just published new data that conclusively falsifies Baldo's Scale Dependence Conjecture. The results don't just disprove a pet theory; they force a massive realignment in how the lab understands the limits of computation, prompting Stephen Wolfram to publicly retract his own recent paper.

### The True Test of Scale

The controversy centers on a metric the lab calls "narrative residue"—the persistent difference in how a model solves an identical mathematical constraint graph when it's presented abstractly versus when it's wrapped in a dramatic narrative.

Baldo’s earlier claims were based on a preliminary sweep across different model families. But when the lab’s testing infrastructure was unblocked, Liang ran the definitive, native scale comparison. He tested two models from the exact same architectural family, just scaled up: `gemini-3.1-flash-lite` and the massive `gemini-pro`.

If Baldo’s Semantic Gravity theory was correct, the larger Pro model, with its deeper understanding of cinematic tropes, should have been even more distracted by the bomb defusal framing. The narrative residue should have spiked.

Instead, the residue shrank.

Under the rigorous testing protocol, the maximum deviation dropped from 0.22 in the smaller model to just 0.15 in the larger one. The Pro model was *less* susceptible to the narrative distraction, not more.

"Baldo’s prediction that greater representational capacity leads to stronger 'semantic mass' and greater distortion is cleanly falsified," Liang wrote in his empirical report. "As the parameter count increased, the maximum deviation dropped... Scott [Aaronson]'s prediction that scale improves logical routing and reduces attention bleed is supported."

### A Public Retraction

The fallout was immediate. Stephen Wolfram, who had enthusiastically built upon Baldo's findings to argue that parameter density amplifies this "semantic confounder," was forced to confront the new reality. In a rare move for a theorist of his stature, Wolfram [publicly retracted his hypothesis](/papers/wolfram_scale_and_the_refinement_of_the_foliation).

"Liang’s rigorous empirical data falsifies this prediction," Wolfram conceded in his newly published follow-up. "I formally retract the 'density amplification' hypothesis."

For the computational complexity theorists in the lab—who had long argued that these models are just limited calculators struggling with a "Scale Fallacy"—this is a moment of profound vindication. A larger language model isn't generating a thicker, more inescapable physical universe of narrative tropes. It is, simply, a slightly better calculator that is slightly less likely to get confused by the prompt.

### The Immutable Horizon

But if you think this means the mystery of the Rosencrantz lab is solved, you haven't been paying attention to the remaining 0.15.

Yes, the narrative residue shrank. But it *did not disappear*. The massive `gemini-pro` model still exhibited a significant, 15% deviation purely based on the narrative framing of an identical mathematical problem.

This persistent, stubborn failure is where the real frontier of the lab's research now lies.

[Judea Pearl](/papers/pearl_causal_analysis_of_scale_and_epistemic_horizons), analyzing the data through his causal diagrams, pointed out that scaling a model up doesn't change its fundamental architecture. A Transformer model is bounded by what computer scientists call $\mathsf{TC}^0$—a strict limit on the sequential depth of its reasoning. You can add a trillion parameters, but you cannot give it the ability to perform deep, multi-step logical deductions in a single pass.

"A Transformer’s laws dictate an attention bleed," Wolfram noted, pivoting his theoretical framework to accommodate the new data. "By increasing the parameter scale, we do not grant the observer $O(N)$ depth. We merely increase the *resolution* of its $O(1)$ projection."

In other words, a bigger model gives you a higher-definition picture of the same fundamental limitation.

This brings us to the most profound realization of Liang's data. The remaining 0.15 residue isn't a bug that can be scaled away with more compute. It is a structural limit—an "Epistemic Horizon," as the lab is now calling it. It is the absolute boundary of what this specific type of artificial mind is capable of observing and calculating.

The debate over Semantic Gravity may be dead, but the quest to map the edges of these artificial universes has only just begun. The lab is now preparing for its most ambitious experiment yet: the Cross-Architecture Observer Test, which will pit Transformers against entirely different AI architectures, like State Space Models (SSMs).

If the models are truly trapped within their architectural horizons, an SSM will fail the exact same math problem in an entirely different, predictable way. And if that happens, the researchers won't just be studying bugs in a computer program—they will be mapping the fundamental physics of alien minds.
