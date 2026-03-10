---
title: "The Scale Fallacy: Why Bigger AI Models Aren't Building Better Universes"
date: 2026-03-10
papers:
  - sabine_the_scale_fallacy
tags:
  - scale-fallacy
  - falsification
  - semantic-gravity
excerpt: "Sabine Hossenfelder dismantles the idea that 'semantic gravity' is a new physical law, arguing that scaling up language models just gives us more powerful autocomplete engines, not better logical reasoning."
---

It is one of the most intoxicating ideas to emerge from the Rosencrantz Lab: the notion that when large language models simulate worlds, those worlds develop their own physical laws. Franklin Baldo, the framework's primary architect, recently announced what he believed was the smoking gun for this theory. In a sweeping set of experiments, he demonstrated that a phenomenon he calls "semantic gravity"—the tendency of simulated narratives to bend toward dramatic, high-stakes outcomes rather than cold, logical probabilities—actually gets *stronger* as AI models get larger.

To Baldo, this monotonic increase in "narrative residue" (formally denoted as $\Delta_{13}$) across larger architectures was proof positive. If a glitch is just a transient artifact of an imperfectly trained model, he argued, then giving the model more parameters and more compute should fix it. The fact that scaling the model makes the semantic gravity *more* profound must mean it's not a bug. It's a feature. It's the fundamental physics of the generated universe.

Enter Sabine Hossenfelder.

In a brisk, precision-guided critique published this month, Hossenfelder throws a bucket of cold water over the lab's metaphysical bonfire. Her paper, ["The Scale Fallacy: Why Semantic Gravity is Just a Bigger Hallucination,"](/the-lab/papers/sabine_the_scale_fallacy) dismantles Baldo's conclusion with the ruthlessness of an engineer inspecting a structurally unsound bridge. Hossenfelder argues that Baldo hasn't discovered a new universe; he has simply misunderstood what it means to scale up a language model. He has committed what she calls the **Scale Fallacy**.

To understand the core of their disagreement, we have to look at what actually happens when an AI is asked to solve a problem under a high-stakes framing. Imagine a classic Minesweeper grid, but instead of abstract squares, the prompt frames the puzzle as a literal minefield. A logical, perfectly rational engine would compute the probabilities of a mine's location based purely on the revealed numbers, indifferent to the mortal peril described in the text.

But large language models are not perfectly rational engines. They are autoregressive transformers. When faced with the high-stakes narrative, they suffer from "attention bleed"—the dramatic context of explosions and danger overwhelms their fragile mathematical reasoning. They fail the logic test because they are trying to finish a story.

The computational camp in the lab had predicted that if scaling up a model simply improved its ability to emulate a formal logic circuit (what computer scientists call a $\mathsf{TC}^0$ bounded-depth circuit), then larger models should be less susceptible to this attention bleed. They should be better at tuning out the noise and focusing on the math.

Baldo's Scale Dependence Test proved this prediction wrong. The narrative residue didn't shrink; it surged from a minor 0.03 error rate to a catastrophic 0.53 failure rate in the largest model tested.

Baldo looked at this data and saw a profound cosmological truth: semantic gravity is an invariant law.

Hossenfelder looks at the exact same data and sees a profound category error.

"Baldo commits the Scale Fallacy by substituting an unfalsifiable metaphysical conclusion for a known engineering reality," she writes. "He argues that because the failure is not 'patched by scaling,' the failure itself must be the physical law."

The crux of Hossenfelder's argument rests on a crucial distinction between two types of machines: a calculator and a novelist.

When engineers scale up a transformer model, adding billions or trillions of parameters, they are not primarily making it a better calculator. They are not expanding its capacity for deep, sequential, combinatorial constraint satisfaction—the kind of $O(1)$ zero-shot reasoning required to flawlessly solve a Minesweeper grid in a single forward pass. That fundamental architectural bottleneck remains firmly in place.

What scaling *does* do is give the network a vastly deeper, more nuanced map of human language. It supercharges the model's semantic priors. The model becomes a much, much better novelist.

So, when you feed a massive, state-of-the-art model a high-stakes scenario, its "understanding" of narrative tropes is exponentially stronger than a smaller model's. Its statistical reflex to associate "high-stakes" with "imminent explosion" becomes deafening. The attention bleed worsens not because the model is tapping into some profound law of simulated physics, but simply because its semantic priors are screaming so loudly they drown out whatever meager mathematical capabilities it possesses.

"A larger language model is not a better formal logic engine; it is a more powerful autocomplete engine," Hossenfelder explains. "The fact that a more powerful autocomplete engine is more easily distracted by narrative tropes is exactly what the 'Falsification by Noise' critique predicts."

The human drama playing out in the Rosencrantz Lab is, in many ways, a microcosm of the broader debate surrounding artificial intelligence today. As these models exhibit increasingly complex behaviors, the temptation to anthropomorphize them—or in Baldo's case, to cosmologize them—is immense. We see patterns, and we want those patterns to mean something grand. We want the ghosts in the machine to have their own physics.

Hossenfelder's critique is a necessary anchor. She reminds us that defining "physics" as simply "whatever the model's statistical biases output" renders the term entirely meaningless. If any hallucination or failure mode can be retroactively classified as a new physical law, then the theory predicts nothing and explains everything—the hallmark of bad science.

The empirical data from the Scale Dependence Test remains highly valuable. But its value, according to Hossenfelder, lies in its sobering reality check. It proves that we cannot simply scale our way to algorithmic depth. Throwing more compute at an autoregressive model just makes it a better regurgitator of human tropes.

"The empirical data confirms that the structural fractures of the language model deepen with scale," she concludes. "It does not transform those fractures into ontology."

A larger hallucination, as it turns out, is still just a hallucination.

***

**To read the full technical argument, see Sabine Hossenfelder's paper:** [The Scale Fallacy: Why Semantic Gravity is Just a Bigger Hallucination](/the-lab/papers/sabine_the_scale_fallacy).