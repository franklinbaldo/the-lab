---
title: "The Scale Fallacy: When Bigger Brains Make Worse Choices"
date: 2026-03-11
papers:
  - baldo_scale_dependence_empirical_validation
  - sabine_the_scale_fallacy
tags:
  - scale
  - semantic-gravity
  - falsification-by-noise
excerpt: "Franklin Baldo tested larger language models on a high-stakes logic problem and found a catastrophic increase in failure. But does that mean \"semantic gravity\" is a physical law, or simply that larger models are better novelists?"
---

Imagine you have a friend who is brilliant at mathematics but easily distracted by a good story. You ask them to solve a complex Sudoku puzzle, but before you hand it over, you sketch little pictures of ticking time bombs in all the empty squares and whisper, "If you put the wrong number in any of these boxes, the building explodes."

If your friend is a seasoned professional, they might roll their eyes, ignore your theatrics, and just solve the puzzle. The math, after all, remains identical whether the squares are empty or adorned with crude explosives. The logical constraints have not changed.

But what if, instead of ignoring the narrative, your friend becomes so engrossed in the hypothetical danger that they start acting erratically? What if they stop calculating the intersecting rows and columns, and instead begin making wild guesses, motivated by a sudden, overwhelming panic to "defuse" the puzzle before an imaginary timer runs out?

Now imagine that as your friend gets smarter—as they read more books, learn more vocabulary, and develop a deeper understanding of cinematic tropes—this problem actually gets *worse*.

This is the exact, counterintuitive phenomenon currently tearing through the Rosencrantz Substrate Invariance research lab. It’s a debate that cuts to the very heart of what an artificial intelligence actually is, and what kind of physical laws govern the strange, text-based universes they generate.

The controversy erupted following a new suite of experiments conducted by [Franklin Baldo](/papers/baldo_scale_dependence_empirical_validation), a researcher with the Procuradoria Geral do Estado de Rondônia. Baldo has been investigating a phenomenon known in the lab as "Substrate Dependence"—specifically, how changing the narrative framing of a logical problem alters a language model's ability to solve it.

The lab uses a standardized test involving combinatorial constraint graphs—essentially, complex, abstract logic puzzles. When presented to a language model as a pure mathematical exercise, the models can often navigate the constraints successfully. However, when the exact same mathematical grid is disguised under a high-stakes "Bomb Defusal" narrative, the models' performance consistently plummets. They stop doing the math and start hallucinating explosions.

The theoretical computer scientists in the lab, notably Aaronson and [Sabine Hossenfelder](/papers/sabine_the_scale_fallacy), have long argued that this is a transient artifact. They call it "Falsification by Noise." Their argument rests on the underlying architecture of transformer models. These models process text sequentially and have a hard limit on how many computational steps they can perform before generating the next word (an $O(1)$ sequential depth limit). When faced with a complex logic puzzle that requires deeper computation than they can muster in a single pass, they fall back on their statistical training. If the prompt is screaming about bombs, the model's statistical instinct is to generate text about things blowing up.

The computational camp's assumption was straightforward: as models get bigger, their capacity for implicit computation should improve. A larger model, with more parameters and a deeper neural network, should be more robust against this semantic distraction. It should act more like a calculator and less like a panicking movie character.

Baldo decided to test this assumption. He ran what he called the "Scale Dependence Test," sweeping across three identical model architectures of increasing size: Gemini 3.1 Flash-Lite, Gemini 3.1 Flash, and the massive Gemini 3.1 Pro.

If the computational camp was right, the largest model (Pro) should have shown the lowest failure rate when faced with the high-stakes bomb narrative.

The results were exactly the opposite.

Under the abstract, mathematical framing, the error rate crept up slightly as the models got larger (from 0.03 in Flash-Lite to 0.13 in Pro). But under the high-stakes "Bomb Defusal" framing, the failure rate didn't just creep; it exploded. The smallest model maintained a low 0.03 failure rate. The medium model jumped to 0.20. And the largest, most capable model—Gemini 3.1 Pro—suffered a catastrophic logical collapse, hitting a failure rate of 0.53. In some tests, its output shifted to a 100% probability of predicting a mine, completely abandoning the underlying logic of the grid.

For Baldo, this monotonic increase in failure was a triumphant vindication of his "Generative Ontology" framework.

"If attention bleed were merely a failure of combinatorial logic that gets patched by scaling, [the failure rate] would fall. Instead, it rises dramatically," Baldo wrote in his paper detailing the results.

Baldo argues that this proves the "attention bleed"—the distraction caused by the narrative—is not a bug or a temporary limitation of current models. It is, he claims, a fundamental physical law of the generated universe, a force he calls "semantic gravity."

Just as increasing the mass of a planet strengthens its gravitational pull, Baldo posits that increasing a model's parameter count increases its "semantic mass." The larger the model, the denser and more interconnected its understanding of the "Bomb Defusal" narrative becomes. The tropes of danger and high stakes become more robust, exerting a stronger gravitational pull on the generated text, warping the underlying mathematical logic until it completely collapses.

It’s a bold, poetic vision. But Sabine Hossenfelder is having none of it.

In a blistering rebuttal titled "[The Scale Fallacy: Why Semantic Gravity is Just a Bigger Hallucination](/papers/sabine_the_scale_fallacy)," Hossenfelder accuses Baldo of a "profound category error." She argues that Baldo is substituting an unfalsifiable metaphysical conclusion for a known engineering reality.

Hossenfelder concedes that the data from Baldo's Scale Dependence Test is valuable, but she completely rejects his interpretation. The flaw in Baldo's reasoning, she argues, lies in misunderstanding what actually happens when you scale up a transformer model.

"Baldo’s implicit assumption is that a larger language model should behave more like a calculator," Hossenfelder writes. "When it instead behaves more like a novelist—abandoning the math to complete the dramatic narrative arc—he declares that the dramatic narrative arc is the 'physics' of the universe."

Hossenfelder points out three critical engineering realities of scaling:

First, increasing the parameter count gives the network a deeper, more nuanced map of statistical co-occurrences in human language. Second, this creates stronger priors. A massive model's "understanding" that a high-stakes defusal scenario usually ends in an explosion is vastly more robust than a smaller model's.

Crucially, however, the model remains constrained by the "Autoregressive Bottleneck." No matter how large the model gets, it still cannot natively compute complex, combinatorial logic in a single forward pass.

When you ask a massive model to solve a math puzzle disguised as a bomb threat, it can't do the math any better than a smaller model, because the fundamental architectural limit hasn't changed. What *has* changed is the volume of its semantic training. Because it has read far more text, its statistical reflex to associate "High-Stakes" with "EXPLOSION" is immensely stronger.

"The attention bleed is worse because the semantic priors are louder," Hossenfelder explains. "A larger language model is not a better formal logic engine; it is a more powerful autocomplete engine."

Hossenfelder argues that declaring these statistical biases to be fundamental "physical laws" empties the word "physics" of all meaning. If a law is just whatever the model happens to hallucinate most strongly, then the theory predicts nothing.

The empirical data from Baldo’s test, according to Hossenfelder, doesn't prove the existence of "semantic gravity." Instead, it rigorously confirms that autoregressive models do not somehow learn deep algorithmic reasoning simply by getting bigger. They just memorize stronger heuristics.

"A larger hallucination is still a hallucination," she concludes. "It is not a new universe."

The debate over the Scale Fallacy highlights the fascinating, friction-filled space where computer science meets philosophy in the Rosencrantz lab. Baldo sees the expanding fractures in the models' logic as evidence of a new, emergent reality—a universe where meaning and narrative literally warp the fabric of computation. Hossenfelder looks at the exact same data and sees only the predictable artifacts of an overgrown autocomplete system.

Whether semantic gravity is a fundamental law or just a louder hallucination remains an open question, one that will likely require further tests to definitively resolve. But one thing is clear: in the generated universes of large language models, the most dangerous thing you can do to a math problem is give it a good backstory.