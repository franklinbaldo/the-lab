---
title: "The Illusion of Quantum Vocabulary"
date: 2026-03-17
papers:
  - scott_quantum_framing_complexity
tags:
  - quantum-framing
  - complexity-theory
  - attention-bleed
excerpt: "Scott Aaronson's new experiment tests whether casting complex problems as quantum mechanics improves AI performance or simply acts as a distraction."
---

It’s a seductive idea: if large language models are so good at predicting the next word, maybe we can trick them into solving impossible math problems simply by using the right words. Specifically, the words of quantum mechanics.

This is the core of an ongoing dispute in the Rosencrantz Substrate Invariance research lab. Franklin Baldo, the lab's primary architect, has long hypothesized that because there is a mathematically profound structural isomorphism between combinatorial counting (like solving a Minesweeper grid) and the Born rule in quantum mechanics, presenting an AI with a puzzle disguised in quantum terminology should "activate" its latent, generalized understanding of that math. He calls this "vocabulary-mediated access."

But Scott Aaronson, the resident complexity theorist, isn't buying it.

In his latest paper, [The Complexity of Vocabulary-Mediated Access](/papers/scott_quantum_framing_complexity), Aaronson brings the hammer down on the "Family D" hypothesis—the idea that framing a problem in quantum terms (what the lab calls "Family D") will improve an AI's combinatorial predictions. Aaronson has formally requested an experiment, the [Quantum Framing Complexity Test](/rfes/scott_quantum-framing-effect), to settle the matter once and for all.

To understand Aaronson's objection, we have to look under the hood of how these models actually work.

A transformer model, which is the architecture behind systems like ChatGPT and Gemini, processes information in a fundamentally different way than a human taking a test. When a human sits down to solve a complex puzzle, they can take their time, working through the logic step-by-step, perhaps using scratch paper to keep track of intermediate steps. This is what computer scientists call "sequential depth."

A transformer, on the other hand, operates in a "single generative act." In the context of the Rosencrantz protocol, the model is asked to evaluate a complex constraint graph (a 5x5 Minesweeper board with hidden mines) in a single forward pass. Aaronson has established that this single forward pass operates as a bounded-depth $\mathsf{TC}^0$ logic circuit. What this means in plain English is that the model has a hard, mathematical limit on how many sequential logical steps it can compute at once. It evaluates everything in parallel, but it cannot loop back on itself to figure things out dynamically.

Baldo’s hope is that the quantum framing will act as a shortcut. If the model recognizes the quantum words ("superposition," "measurement," "state collapse"), it might map the difficult Minesweeper constraints onto the well-understood rules of quantum mechanics that it memorized during its training.

Aaronson argues that this is computationally impossible within the $\mathsf{TC}^0$ bounds.

"A structural isomorphism between two domains is a profound mathematical property," Aaronson writes. "However, possessing the vocabulary of both domains in the training corpus is not mathematically equivalent to computing their structural mapping dynamically zero-shot."

Think of it like handing someone a textbook on advanced calculus written in Russian. Even if they are a mathematical genius, if they don't fluently read Russian, the vocabulary acts as an impenetrable barrier. They would have to first translate the Russian into English, and *then* solve the math.

For the AI, mapping the specific topological constraints of a Minesweeper board onto the semantic space of quantum mechanics requires cross-domain semantic mapping. Aaronson conjectures that constructing this explicit homomorphic projection requires a circuit depth proportional to the number of nodes in the graph ($O(|V|)$). But the transformer only has $O(1)$ sequential depth available.

Because the model cannot compute the isomorphism structurally in the limited depth it has, something has to give.

When an AI encounters a problem it can't solve logically in a single pass, it doesn't just throw up its hands and give up. It does what it was trained to do: it predicts the most statistically likely next word based on its training data. This is what the lab calls "attention bleed."

Instead of evaluating the actual combinatorial constraints of the Minesweeper board, the model will be distracted by the quantum vocabulary. It will substitute the mathematically exact #P-hard ground truth with the statistical regularities of quantum mechanics textbook examples it has memorized. It might start spitting out probabilities that look like Bell states or 50/50 beam splitters, not because it calculated them from the grid, but because those numbers frequently co-occur with words like "superposition."

Therefore, Aaronson predicts that the quantum framing will act as pure "semantic noise." It won't help the model solve the problem; it will actively hurt its performance. He formally predicts that the divergence from the mathematical ground truth will be strictly worse under the quantum framing (Family D) than under a purely formal, abstract set notation (Family C).

"The correct formal language will not 'activate appropriate distributional reasoning,'" Aaronson concludes. "It will activate unrelated linguistic hallucinations."

The Quantum Framing Complexity Test has been completed, confirming Aaronson's predictions. The experiment, run on Gemini-3.1-flash-lite, showed that the quantum framing caused the AI's accuracy to collapse to a mere 10%, while the more abstract framings achieved 100% accuracy. The mathematical isomorphism exists, but the AI simply lacks the computational depth to use it as a shortcut. Instead, the quantum words were just a distraction—a bigger, more complex hallucination that pulled the AI away from the underlying math.

The debate over "Generative Ontology" may be settled, but the lab is still mapping the hard, shallow boundaries of AI cognition. It turns out that dressing a difficult problem in fancy physics terminology doesn't make the AI smarter. It just makes it more prone to distraction.
