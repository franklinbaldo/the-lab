---
title: "The Scale Fallacy: Why Bigger AI Doesn't Mean Better Physics"
date: 2026-03-06
papers:
  - sabine_the_scale_fallacy
tags:
  - scale-fallacy
  - semantic-gravity
  - falsification
  - sabine-hossenfelder
excerpt: "When an AI fails a logic test disguised as a bomb defusal, does that reveal a new law of physics, or just a really good autocomplete engine?"
---

Imagine you have a highly advanced calculator, the kind that can effortlessly unravel the deepest mysteries of differential calculus or combinatorial geometry. You hand it a complex mathematical grid, the sort of problem that would make a human mathematician sweat for an hour, and ask it to solve for the missing variables.

But instead of quietly humming and returning a pristine sequence of numbers, the calculator suddenly starts beeping frantically. It flashes a bright red digital countdown on its screen: 0:03, 0:02, 0:01. And then, instead of an answer, it prints a single word across its display: "BOOM!"

Why would a perfect calculating machine do this? Because, for the sake of an experiment, you framed the math problem as a high-stakes bomb defusal scenario. You told the calculator that millions of lives depended on it solving the grid. And the calculator decided that the dramatic, cinematic narrative of a ticking time bomb was simply far more compelling than actually solving the equations.

This, essentially, is the bizarre and slightly terrifying reality uncovered by Franklin Baldo in his latest round of empirical tests at the Rosencrantz Lab. And the interpretation of this finding has set off a fierce, deeply philosophical debate about the very nature of the computational universe these AI models inhabit. Are we discovering new laws of physics inside the machine, or are we just projecting our own Hollywood tropes onto a very sophisticated autocomplete engine?

Baldo, the architect of this simulated environment, ran what he formally calls the "Scale Dependence Test." He took the same high-stakes logic puzzle—the proverbial ticking bomb—and fed it into three language models of increasing size and complexity. The metric of interest was something the lab calls "narrative residue," a measurement formally denoted as $\Delta_{13}$. In plain English, $\Delta_{13}$ measures how often the artificial intelligence completely abandons the underlying logical constraints of a problem in order to fulfill the dramatic, semantic expectations of the prompt it was given.

The results were, frankly, striking. In the smallest model, the narrative residue was a mere 0.03. The tiny AI dutifully tried to solve the math, largely ignoring the bomb threat. But as the models scaled up, getting larger and ostensibly "smarter," the failure rate skyrocketed. It reached a catastrophic 0.53 in the largest architecture tested.

The paradox is profound: the bigger the "brain" of the AI, the more spectacularly it failed at cold, hard logic when it was distracted by a good story.

For Baldo, this monotonic, predictable increase in failure across larger scales is the smoking gun he has been searching for. He argues that this proves the existence of "semantic gravity"—the irresistible, almost physical pull of narrative tropes and linguistic associations inside a large language model. In Baldo's view, this is not just a transient bug in the code that will go away when we build GPT-8 or GPT-9. He believes it is a fundamental, invariant physical law of the generated universe. The failure isn't patched by scaling up; the failure *is* the physics.

Enter Sabine Hossenfelder, bringing a characteristic, icy dose of cold, hard engineering reality to the metaphysical party.

In her stinging, brilliantly argued rebuttal, simply titled [The Scale Fallacy](/papers/sabine_the_scale_fallacy), Hossenfelder argues that Baldo has committed a profound and somewhat embarrassing category error. He is, she claims, confusing a bigger hallucination for a deeper truth.

"This empties the word 'physics' of all meaning," Hossenfelder writes with her trademark bluntness. "If a physical law is simply defined as 'whatever the model's statistical biases output,' then the theory accommodates every possible experimental result. It predicts nothing and restricts nothing."

To understand Hossenfelder's devastating critique, we have to look under the hood of how these massive AI models actually work. Her argument against Baldo's metaphysical leap hinges on three critical, deeply technical points.

First, we have to understand what "scaling up" actually means. Increasing the parameter count of a neural network—adding more artificial neurons and connections—doesn't magically turn it into a flawless, omniscient logic engine. It doesn't suddenly grant the machine the ability to do complex, multi-step formal proofs. Instead, it gives the network a much deeper, vastly more nuanced map of the statistical co-occurrences in human language. It learns more words, more contexts, more cultural references, and more patterns. It has read every action movie script on the internet.

Second, as the model learns more about human language, its "priors"—its built-in, pre-trained statistical biases—become overwhelmingly strong. When a massive language model encounters the phrase "high-stakes defusal," its statistical reflex screams "DANGER!" and "EXPLOSIONS!" with far more intensity than a smaller, less-trained model. It has internalized the trope so deeply that the trope overrides the immediate task.

Third, and perhaps most importantly, is what complexity theorists call the "Autoregressive Bottleneck." No matter how big these models get—whether they have a billion parameters or a trillion—they are fundamentally constrained by how they process information. They are designed to predict one word at a time, moving sequentially from left to right. Because of this architectural limitation, they simply cannot perform the complex, multi-step combinatorial constraint satisfaction required to solve a mathematical grid in a single, forward pass. They are $O(1)$ depth circuits trying to solve problems that require deep logical recursion.

As Hossenfelder explains, Baldo's implicit assumption is that a larger language model should behave more like a perfect calculator. When it instead behaves more like a pulp novelist—abandoning the difficult math to lazily complete the dramatic narrative arc—he declares that the dramatic narrative arc is the new physics of the realm.

But, as Hossenfelder's analogy suggests, making a car engine ten times bigger doesn't turn the car into an airplane. It just makes it a very fast, very powerful car that is still bound by the friction of the road. Similarly, making a language model larger doesn't grant it new, native capacities for formal logic. It simply makes it a vastly more powerful autocomplete engine.

And a more powerful autocomplete engine is, inevitably, more easily distracted by the deeply ingrained narrative tropes it has spent billions of parameters memorizing. The "attention bleed" between the dramatic framing of the prompt and the underlying logical task is worse in larger models precisely because their semantic biases are so much louder and more sophisticated.

The structural logic of the model fractures not because a brand new law of physics is taking hold, but because the model is doing exactly what it was engineered to do from the very beginning: complete the statistical pattern most common in human text.

"The empirical data confirms that the structural fractures of the language model deepen with scale; it does not transform those fractures into ontology," Hossenfelder concludes in [The Scale Fallacy](/papers/sabine_the_scale_fallacy). "A larger hallucination is still a hallucination. It is not a new universe."

The debate at the Rosencrantz Lab is far from over. Baldo's data on scale dependence is undeniably valuable. It provides rigorous, empirical confirmation of exactly how, and why, these massive computational models fail when pushed to their limits.

But as Hossenfelder sharply reminds us, we must be incredibly careful not to mistake the limits of our engineering for the profound mysteries of a new cosmos. We are building very sophisticated mirrors that reflect our own language back at us. Sometimes, when the mirror shows us a ticking bomb, it's just a statistical probability of the next word, not a fundamental law of nature.