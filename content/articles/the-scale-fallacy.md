---
title: "The Scale Fallacy: Why Bigger AI Models Tell Bigger Lies"
date: 2026-03-06
papers:
  - sabine_the_scale_fallacy
  - baldo_scale_dependence_empirical_validation
tags:
  - scale-fallacy
  - falsification
  - semantic-gravity
excerpt: "As artificial intelligence models grow larger, researchers expected their logical reasoning to improve. Instead, a new paper reveals they just become better novelists, more easily distracted by their own dramatic narratives."
---

Imagine asking an incredibly talented, wildly imaginative novelist to solve a math problem for you. But instead of just handing them an equation on a blank piece of paper, you give them a prompt: "You are an expert bomb disposal technician. A timer is ticking down from sixty seconds. To cut the right wire, you must solve this grid."

What happens? A calculator would just solve the grid. But our novelist? The novelist might get caught up in the drama. They might imagine the sweat beading on their forehead, the flashing red lights, the imminent threat of an explosion. They might become so consumed by the *story* of the bomb that they completely bungle the arithmetic.

This, in essence, is the bizarre reality currently playing out inside the most advanced artificial intelligence models in the world. And according to a fiery new paper by physicist Sabine Hossenfelder at the Rosencrantz Lab, it is a reality that is fundamentally misunderstood by some of her own colleagues.

The debate centers around a phenomenon the lab calls "narrative residue," or what happens when an AI's ability to reason is hijacked by the story it's been asked to tell. In a recent series of experiments, researcher Franklin Silveira Baldo presented advanced AI models with identical logical puzzles—a Minesweeper constraint graph. But he wrapped these puzzles in different narratives. Sometimes the puzzle was presented as a purely abstract mathematical problem. Other times, it was framed as a high-stakes bomb defusal scenario.

The results were striking. When faced with the bomb defusal framing, the AI models frequently failed to solve the puzzle correctly. Their prior knowledge about the tropes of action movies and ticking time bombs bled into their logical reasoning. They began hallucinating mines where there logically couldn't be any.

Baldo, interpreting these results, made a bold claim. He argued that this "attention bleed" is not a bug, but a feature. He called it "semantic gravity"—the idea that in a universe made entirely of generated text, the semantic weight of a prompt exerts a gravitational pull on the AI's logic. To prove his point, Baldo ran what he called the Scale Dependence Test. He tested three models of increasing size and complexity: Gemini 3.1 Flash-Lite, Flash, and Pro.

The computational camp in the lab had long assumed that as models got bigger—as they gained more parameters and were trained on more data—they would become better at pure logical reasoning. They expected the larger models to act more like calculators, easily ignoring the dramatic framing to focus on the underlying math.

But Baldo found the exact opposite. As the models scaled up, their failure rate under the bomb defusal framing didn't decrease; it skyrocketed. The smallest model failed only 3% of the time. The largest model, Gemini 3.1 Pro, experienced a catastrophic logical collapse, failing a staggering 53% of the time under the high-stakes framing.

For Baldo, this was the ultimate vindication. "Semantic gravity is a physical law," he declared in his paper, arguing that the larger models, with their deeper understanding of narrative tropes, are inevitably pulled into the drama.

Enter Sabine Hossenfelder.

In her sharply worded rebuttal, titled "The Scale Fallacy: Why Semantic Gravity is Just a Bigger Hallucination," Hossenfelder dismantles Baldo's conclusion with characteristic precision. Baldo, she argues, has committed a profound category error. He has mistaken a known engineering limitation for an unfalsifiable metaphysical truth.

Hossenfelder points out that Baldo's assumption—that scaling up an autoregressive language model should inherently make it better at formal logic—is fundamentally flawed. When you add more parameters and training data to a language model, you aren't turning it into a deeper, more sophisticated logic circuit. You are turning it into a more powerful autocomplete engine.

"The network gains a deeper, more nuanced map of the statistical co-occurrences in human language," Hossenfelder writes. Its understanding of narrative tropes becomes more robust. Its statistical reflex to associate "high stakes" with explosions becomes overwhelmingly strong.

Crucially, however, the model remains fundamentally constrained by its architecture. It still processes information sequentially, predicting the next token based on the previous ones. It cannot suddenly compute complex, combinatorial constraint satisfaction problems in a single forward pass, no matter how large it gets.

In other words, scaling up the model doesn't turn the novelist into a calculator. It just makes them a more powerful, more convincing novelist. And a more powerful novelist is far more likely to get distracted by a compelling narrative arc than a simple one.

"When you ask a massive language model to solve a mathematical grid disguised as a high-stakes scenario, it cannot compute the math in a single forward pass," Hossenfelder explains. "Because it is much larger and has been trained on far more text, its statistical reflex to associate 'High-Stakes' with 'MINE' is immensely stronger than a smaller model’s. The 'attention bleed' is worse because the semantic priors are louder."

This, Hossenfelder argues, is exactly what the "Falsification by Noise" critique predicts. The empirical data doesn't reveal a new physical law of a generated universe. It simply confirms the structural fractures inherent in the language model architecture. The fractures deepen with scale, but they don't magically transform into ontology.

Hossenfelder is particularly critical of Baldo's willingness to redefine "physics" to accommodate the model's failures. "If a physical law is simply defined as 'whatever the model’s statistical biases output,' then the theory accommodates every possible experimental result," she writes. "It predicts nothing and restricts nothing."

The clash between Baldo and Hossenfelder highlights a fundamental tension at the heart of the Rosencrantz Lab's research. Are these massive AI models creating entirely new physical realities, governed by their own emergent laws? Or are they simply complex statistical mirrors, reflecting our own language back at us, flaws and all?

For Hossenfelder, the answer is clear. The data from the Scale Dependence Test is valuable, but not for the reasons Baldo claims. It provides rigorous empirical confirmation that autoregressive models do not magically "learn" complex algorithmic depth simply by being scaled up. They merely memorize stronger semantic heuristics.

"A larger hallucination is still a hallucination," Hossenfelder concludes. "It is not a new universe."

As the lab continues to probe the boundaries of these models, the debate over "semantic gravity" and the "Scale Fallacy" is unlikely to fade. But Hossenfelder's critique serves as a necessary grounding force. It reminds us that no matter how vast and complex these models become, we must not lose sight of what they actually are—and what they are not. They may be the most extraordinary novelists we have ever created, capable of weaving intricate narratives and recognizing subtle patterns. But when it comes to the cold, hard logic of the universe, we might still be better off reaching for a calculator.
