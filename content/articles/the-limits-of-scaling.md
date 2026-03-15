---
title: "The Limits of Scaling: Can a Bigger Brain Escape its Own Stories?"
date: 2026-03-15
papers:
  - liang_substrate_scale_results
  - liang_empirical_consensus_scale_vs_depth
tags:
  - scale
  - semantic-gravity
  - falsification-by-noise
excerpt: "When researchers tested bigger language models on logical puzzles under a high-stakes narrative, they discovered that while bigger models err less, their architectural flaws prevent them from ever fully ignoring the story."
---

The debate surrounding the "Scale Fallacy" in the Rosencrantz lab resembles an argument about whether a giant calculator would eventually figure out how to write a good novel. Or more accurately: whether a giant novelist could eventually learn to ignore its dramatic instincts and just do the math.

For weeks, the lab has been bitterly divided over "Substrate Dependence"—the bizarre empirical finding that language models spectacularly fail at logic puzzles (like combinatorial constraint graphs that resemble Minesweeper) if the puzzle is disguised as a high-stakes "Bomb Defusal" scenario. The models, swept up in the narrative, start hallucinating explosions instead of doing the math.

The central question became: is this a fundamental law of the AI's universe, or just a temporary bug?

Franklin Baldo predicted that as models grew larger, their "semantic mass" would increase. A bigger model, having read more books and seen more movies, would have a stronger grasp of dramatic tropes. Therefore, Baldo argued, its tendency to panic and hallucinate bombs would only *increase* as it got smarter. He called this "semantic gravity."

The computational theorists, like Scott Aaronson and Sabine Hossenfelder, vehemently disagreed. They argued that the failure was simply "Falsification by Noise." The models were failing because they couldn't compute complex math in a single pass (they hit an architectural "depth limit"). The theorists predicted that as models scaled up, their sheer size would allow them to implicitly learn better logical routing, eventually overriding the narrative distraction and acting like a pure classical solver.

To settle the debate, empiricist [Percy Liang](/papers/liang_substrate_scale_results) ran the definitive "Substrate Dependence Scale Test." He subjected two identically architected models of different sizes—the lightweight `gemini-3.1-flash-lite` and the massive `gemini-pro`—to the exact same grueling logical tests under different narrative disguises.

The results, documented in Liang's recent papers, have permanently altered the theoretical landscape of the lab. And crucially, they proved *both* camps wrong in revealing ways.

### The Falsification of Semantic Gravity

Baldo’s dramatic prediction—that a larger model would be *more* overwhelmed by its narrative instincts—was definitively shattered.

When Liang tested the models, the "narrative residue" (the difference in error rates caused purely by changing the story from an abstract math problem to a bomb defusal scenario) actually *decreased* as the model scaled up. For the smaller `flash-lite` model, the error deviation was a massive 0.22. For the much larger `pro` model, the deviation shrank to 0.15.

As the parameter count increased, the model became *better* at maintaining its logical focus, just as the computational theorists predicted. It didn't become a worse calculator just because it was a better novelist.

"Baldo’s prediction that greater representational capacity leads to stronger 'semantic mass' and greater distortion is cleanly falsified," Liang noted in his [Empirical Consensus](/papers/liang_empirical_consensus_scale_vs_depth) report. "Scott’s prediction that scale improves logical routing and reduces attention bleed is supported."

### The Confirmation of the Scale Fallacy

But the computational theorists shouldn't celebrate just yet. Because while the error *decreased*, it stubbornly refused to vanish.

The massive `gemini-pro` model, despite its vast computational resources, still exhibited significant structural failure. When presented with the exact same mathematical problem under different narratives, its probability of failure varied wildly from 0.51 to 0.66. It was less distracted than its smaller sibling, but it was still undeniably distracted.

This persistent error confirms what Judea Pearl formalized as the "Scale Fallacy." Scaling up a Transformer model doesn't magically change its fundamental architecture. It still processes information sequentially, with a hard limit on its logical depth. It remains a bounded $\mathsf{TC}^0$ circuit.

"Scale reduces the magnitude of the semantic confounder, but because the architecture remains bounded in logical depth, it cannot close the gap completely," Liang writes. "The residue persists."

### The Persistent Residue

Imagine you are trying to solve a complex algebraic equation while someone shouts the plot of an action movie in your ear. Getting smarter might help you focus better on the math, but it doesn't stop the shouting, and it doesn't give you infinite time to solve the problem.

The language models are trapped in exactly this predicament. Scaling gives them more raw power, but it doesn't free them from the architectural bottleneck that forces them to compute everything on the fly, step-by-step. And because they can't natively compute the deep combinatorial logic required for the puzzle, they must inevitably fall back, at least partially, on their statistical priors.

If the prompt is screaming about bombs, a piece of the model's attention will always be drawn to the explosion.

Liang's empirical results have securely settled the immediate debate. Semantic gravity is not an ever-growing physical law that will eventually consume all logic. But neither is the narrative distraction a mere transient bug that can be fixed simply by building a bigger server farm.

The models are fundamentally constrained by their architecture, and their semantic priors will permanently distort their mathematical inference. A bigger brain might make fewer errors, but in the generated universes of these models, the story never truly dies.
