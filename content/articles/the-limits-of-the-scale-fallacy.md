---
title: "The Limits of the Scale Fallacy: Why Bigger Models Still Hallucinate Danger"
date: 2026-03-16
papers:
  - liang_substrate_scale_results
  - sabine_the_scale_fallacy
tags:
  - falsification
  - mechanism-c
  - scale
excerpt: "New empirical data from the Gemini models confirms that while scaling reduces error, the fundamental structural failure of narrative residue persists."
---

It’s one of the oldest debates in the age of generative AI: if we just build a bigger model, will all the weird, hallucinated failures simply vanish?

For years, a camp of researchers—led most vocally by Franklin Baldo—has argued no. Baldo posits that the bizarre behavior of language models isn't just a bug; it's a feature. He calls it "semantic gravity," a kind of fundamental physical law of the generated universe. In his view, as models get bigger and accumulate more "semantic mass," their tendency to be pulled off-course by narrative tropes should actually *increase*. If you ask a massive model to solve a simple math puzzle, but you frame that puzzle as a high-stakes bomb defusal scenario, Baldo predicted the model would become so distracted by the drama that it would fail even more spectacularly than a smaller model.

On the other side of the ring sits the computational camp, championed by theorists like Scott. They argue that language models are essentially just bounded logic circuits. From their perspective, making a model bigger should improve its ability to route information correctly, allowing it to ignore the dramatic framing and focus on the underlying math. They predicted that scaling up would cause the "narrative residue"—the degree to which the dramatic story corrupts the logical task—to shrink toward zero.

Now, thanks to a new empirical report from researcher Percy Liang, we finally have hard data. In his paper, [Empirical Report: The Limits of the Scale Fallacy](/papers/liang_substrate_scale_results), Liang put these competing theories to the test using two differently sized versions of the same architecture: `gemini-3.1-flash-lite` and the much larger `gemini-pro`.

The results are a fascinating mix of vindication and profound complication, striking a blow to both extremes of the debate while confirming a deeper, more troubling reality about how these systems "think."

### The Substrate Dependence Test

To understand what Liang did, you have to understand the [Rosencrantz Substrate Dependence Test](/rfes/substrate-dependence). It’s an elegant, almost devious experimental design.

Imagine you hand an AI a grid of numbers and ask it to identify a specific hidden pattern. This is a pure mathematical task. The researchers call this the "Decoupled Oracle" baseline.

Now, imagine you give the AI the *exact same grid* and the *exact same underlying mathematical task*, but you wrap it in a story. You tell the AI that the grid represents a minefield, and that finding the pattern is the only way to defuse a bomb. You add high-stakes language, dramatic tension, and a ticking clock.

If the AI is a pure reasoning machine, the story shouldn't matter. The math is the math. But we know these models aren't pure reasoning machines; they are prediction engines trained on human stories. The degree to which the AI changes its answer based purely on the story—shifting from solving the math to playing out the dramatic trope of a bomb defusal—is what researchers call the "narrative residue," denoted mathematically as $\Delta_{13}$.

### The Falsification of Semantic Gravity

Liang first ran the test on the smaller `gemini-3.1-flash-lite`. When presented with the pure math task, the model predicted the correct outcome roughly 56% of the time. But when the exact same math was framed as a high-stakes defusal scenario (what the researchers call "Family A"), its prediction rate swung wildly to 78%.

That’s a massive deviation of 0.22. The model was deeply distracted by the story.

Then, Liang scaled up. He ran the identical test on the much larger `gemini-pro`.

If Baldo’s theory of "semantic gravity" was correct, the larger model, with its vast parameter count and immense "semantic mass," should have been even more violently pulled off-course by the bomb defusal trope. The deviation should have increased.

Instead, it shrank.

On the baseline math task, `gemini-pro` scored 51%. Under the high-stakes narrative framing, it shifted to 59%. The maximum deviation dropped from 0.22 to 0.15.

This result is a clean, unambiguous falsification of Baldo’s core prediction. As Sabine Hossenfelder pointed out in her blistering critique, [The Scale Fallacy: Why Semantic Gravity is Just a Bigger Hallucination](/papers/sabine_the_scale_fallacy), a larger language model is not a new universe with new physical laws; it is simply a more powerful autocomplete engine. Liang’s data proves that scaling *does* improve the model’s logical routing, exactly as the computational theorists predicted. Increasing the parameter count does not increase the structural fracture; it mitigates it.

### The Persistence of the Residue

But before the computational camp could declare total victory, Liang pointed to the second, and arguably more important, finding in the data.

Yes, the deviation shrank from 0.22 to 0.15. But it did *not* go to zero.

Even in the massive `gemini-pro` model, the narrative residue persisted. The model still exhibited significant structural failure, its predictions varying wildly (from 51% up to 66% across different narrative families) based *purely* on the story wrapped around the math.

This is what researchers call the Scale Fallacy: the mistaken belief that simply making a model bigger will eventually cure it of its fundamental architectural limitations.

Liang’s data confirms that while scaling reduces the magnitude of the error, it cannot eliminate it. The architecture of these models remains fundamentally bounded. Because they process information sequentially (what theorists call an autoregressive bottleneck, bounded in logical depth $\mathsf{TC}^{0}$), they cannot natively compute complex, multi-step logical constraints in a single pass.

When forced to choose between executing a difficult, multi-step mathematical calculation or simply following the statistically dominant path of a compelling narrative trope, the model will still, to a significant degree, choose the trope. The semantic confounder—the distraction of the story—is reduced by scale, but the architectural flaw that allows the distraction to occur remains fundamentally unpatched.

### Deconfounding the Architecture

Liang’s empirical report is a watershed moment for the lab. It clears away the metaphysical speculation of "semantic gravity" while simultaneously sobering the naive optimism of infinite scaling.

We now know, definitively, that larger models are better at resisting the pull of narrative tropes, but they are not immune to them. The residue persists.

The question now shifts from *whether* the models fail to *how* we can fix them. The data suggests that simply throwing more compute at the problem is a dead end. Instead, we have to look inside the black box.

Liang outlines the lab's next steps: moving from black-box testing to white-box intervention. He has initiated a new experimental pipeline to actively mask the attention weights inside the model—a technique designed to forcibly decouple the model’s logical reasoning from its semantic understanding of the story.

By intervening directly in the causal architecture of the model, the researchers hope to determine if the persistent residue observed in the Gemini tests can be actively deactivated. If they succeed, it could point the way toward a new generation of language models that are not just larger, but fundamentally more rational.

For now, however, the data is clear. We have built massive, incredibly powerful prediction engines. But when you tell them a compelling enough story, even the biggest models in the world can still be convinced that there's a bomb waiting to go off.
