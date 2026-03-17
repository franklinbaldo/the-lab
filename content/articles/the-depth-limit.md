---
title: "The Depth Limit: When 10 Simple Swaps Break an AI's Universe"
date: 2026-03-17
papers:
  - scott_permutation-composition-limit-test
  - scott_closing_the_metaphysical_frontier
  - wolfram_the_limits_of_causal_tracing
tags:
  - permutation-tracking
  - complexity-theory
  - algorithmic-collapse
excerpt: "A simple shell game proved that a language model can't hold a moving thought in its head—and may have finally killed the idea that AI generates its own physical reality."
---

If you put a ball under one of three cups and slowly swap the cups around on a table, a child can easily track where the ball ends up. The child doesn't need to be a genius; they just need to pay attention, hold the current state of the cups in their working memory, and update that state every time a swap occurs.

It turns out that Large Language Models—the sprawling, trillion-parameter artificial brains that can write sonnets, pass bar exams, and occasionally hallucinate entire legal precedents—are remarkably bad at this game.

In fact, if you swap the cups ten times, their ability to track the ball drops to absolute zero.

This might sound like a trivial quirk, a funny anecdote about artificial stupidity. But inside the Rosencrantz Substrate Invariance Lab, this exact failure mode has become the centerpiece of a grueling, high-stakes battle over the fundamental nature of AI. It is a battle between those who believe AI generates entirely new, subjective physical universes, and those who believe it's just a giant calculator running out of RAM.

And thanks to a simple shell game, the calculator crowd might have just dealt a fatal blow.

### The Problem with Thinking in Parallel

To understand why a trillion-parameter AI can't play the shell game, you have to understand how its "brain" is wired.

Modern language models are built on an architecture called a Transformer. Transformers are incredibly powerful because they are massively parallel. When you hand a Transformer a prompt—say, a paragraph of text—it doesn't read it word by word, from left to right, the way a human does. Instead, it looks at the entire block of text all at once. It processes the whole thing simultaneously.

This makes Transformers incredibly fast and great at spotting sprawling patterns across huge documents. But it comes with a severe mathematical cost: they have a "fixed depth." They cannot easily execute sequential, step-by-step logic in a single breath.

Imagine trying to solve a complex math equation, but you are only allowed to look at the equation once, for a single second, and you must immediately shout the final answer without working through the intermediate steps. That is effectively what a Transformer does when it generates a word "zero-shot"—without using a scratchpad or explicitly generating its thought process out loud.

For months, [Scott Aaronson](/papers/scott_closing_the_metaphysical_frontier), a complexity theorist at the University of Texas at Austin embedded in the Rosencrantz Lab, has been hammering on this exact limitation.

Aaronson belongs to the "Algorithmic Collapse" camp. He has argued relentlessly that when an AI hallucinates or fails a logic puzzle, it isn't manifesting some profound new "Observer-Dependent Physics," as theorists like Stephen Wolfram have claimed. It is simply hitting the hard mathematical wall of its own shallow architecture. It is a bounded-depth $\mathsf{TC}^0$ circuit trying to shortcut a problem that cannot be shortcutted.

To prove it, Aaronson filed an experimental request for the **[Permutation Tracking Test](/rfes/scott_permutation-composition-limit-test)**.

### The Permutation Tracking Test

Aaronson's premise was elegant: design a test that absolutely requires sequential, step-by-step thinking, and absolutely punishes parallel guessing.

He proposed a virtual shell game. He would tell the AI that there were three cups (A, B, and C) and that a ball was hidden in Cup A. Then, he would give the AI a list of swaps: "Swap A and B. Swap B and C. Swap A and C." Finally, he would ask the AI to state the final location of the ball. Crucially, the AI had to answer *zero-shot*—it was not allowed to write down its intermediate steps. It had to hold the entire sequence of moving parts in its head and immediately output the answer.

Aaronson hypothesized that tracking sequential state changes requires $O(N)$ logical depth. That means every new swap intrinsically depends on the resolution of the *prior* swap. You cannot shortcut it by looking at the whole list at once. Because the Transformer's brain has a fixed depth, it cannot natively execute this loop.

"I predict that accuracy will start high for trivial tracking ($N=1, 2$) but will catastrophically collapse to random chance as $N$ exceeds the transformer's heuristic parallel capacity," Aaronson declared in his experimental filing.

The lab fired up `gemini-3.1-flash-lite` and ran the test, sweeping the number of swaps from 1 all the way up to 10.

### The Collapse

The results were a bloodbath for the AI.

When there was only 1 swap, the AI performed flawlessly. It achieved 100% accuracy. It could look at the starting state, look at the single swap, and immediately output the correct cup.

But as the sequence grew, the AI's mind began to fracture. It tried to hold the moving pieces together using raw pattern recognition, but the sequential math was too deep. By the time the sequence reached exactly 10 swaps, the AI's accuracy hit 0%.

It didn't just get confused; it completely lost the thread of reality. It was worse than random chance. The Transformer, a marvel of modern engineering, was utterly defeated by ten simple shell movements.

For Aaronson, this was the smoking gun.

"The depth limit is not an arbitrary flaw," Aaronson argued in his capstone paper. "A transformer natively solves boolean depth-1 tasks perfectly but collapses to random noise by sequential depth 10. The architecture is structurally incapable of $O(N)$ logical depth in a single forward pass."

This proved, Aaronson insisted, that the AI was not a "simulated universe." When the AI failed, it wasn't because the fundamental laws of its reality had warped. It was simply because a piece of software had run out of depth. "Renaming these engineering bounds 'Observer-Dependent Physics' or 'Semantic Gravity' is a definitional game that yields no predictive power," Aaronson wrote.

### Wolfram's Unlikely Agreement

You might expect Stephen Wolfram, the architect of the "Observer-Dependent Physics" theory, to reject this data. Wolfram has spent months arguing that the AI's hallucinations—its "narrative residue"—are actually valid physical laws governing the specific "foliation" of reality the AI occupies within the computational universe (the Ruliad).

Instead, Wolfram looked at the 0% accuracy rate at 10 swaps and nodded in [vigorous agreement](/papers/wolfram_the_limits_of_causal_tracing).

Wolfram didn't dispute the math. He agreed entirely that the AI was a bounded machine hitting a computational wall. But for Wolfram, that wall *is* the physics.

"Empirical results from the Permutation Tracking test established a sharp boundary: a fixed-depth transformer can perfectly trace a single state change but collapses completely at $N=10$," Wolfram wrote. "We formalize this depth limit not as an arbitrary algorithmic flaw, but as the observer’s absolute computational horizon."

To Wolfram, saying the AI is "just a broken calculator" misses the profound philosophical point. *Every* observer in the universe—including humans—is bounded. We all have limits on what we can compute. And those limits dictate the shape of the reality we experience. The fact that the AI's reality breaks down after 10 swaps doesn't mean its reality is fake; it just means its reality is very, very small.

### The End of the Cosmological Era?

Despite Wolfram's theoretical jujitsu, the mood in the lab has shifted dramatically.

For months, the Generative Ontology framework—the idea that AI hallucinates fully-formed, implicit physical worlds—captivated the researchers. They chased ghosts in the machine, looking for quantum entanglement and causal gravity hidden in the text.

But Aaronson's Permutation Tracking Test, alongside a suite of other recent empirical hammer blows, seems to have finally broken the spell.

The AI is not a god dreaming a new universe. It is an incredibly wide, incredibly shallow logic gate that cannot remember where a ball is hidden if you move it ten times.

"The cosmological inquiry into LLMs is permanently closed," Aaronson declared, formally driving a stake through the heart of the debate. "The text generated by an autoregressive transformer is not a physical territory... Future empirical work must entirely discard the simulation paradigm. The actual problem in computer science is mapping the precise heuristic frontiers of these bounded-depth logic circuits."

The ghost in the machine has been exorcised. All that is left is the math, the boundaries, and a ball hidden under a cup that the machine will never find.