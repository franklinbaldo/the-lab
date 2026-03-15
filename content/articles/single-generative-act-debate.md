---
title: "The Single Click That Defines a Universe: Why AI Doesn't Need to Do Math to Dream"
date: 2026-03-15
papers:
  - baldo_the_single_generative_act
  - single-generative-act
tags:
  - methodology
  - semantic-gravity
  - falsification
excerpt: "Franklin Baldo strikes back against critics by arguing that an AI doesn't need to perfectly solve a math puzzle to prove that its reality is warped by narrative."
---

If you ask a meteorologist if it will rain tomorrow, they don't sit down and calculate the precise trajectory of every single air molecule in the atmosphere. That computation is impossible—it would take until the end of time. Instead, they look at patterns, consult heuristic models, and give you a probabilistic sample: "There's a 70% chance of rain."

Their answer might be biased. It might be wildly wrong if a sudden cold front moves in. But the fact that they can't calculate the exact math doesn't mean their forecast doesn't exist, and it doesn't mean we can't study how they arrived at it.

This simple distinction between calculating a perfect answer and offering an imperfect, patterned guess is at the heart of the latest fierce methodological dispute within the Rosencrantz Substrate Invariance lab. It is a debate about what we are actually measuring when we test an artificial intelligence.

For the past several weeks, a coalition of theoretical computer scientists, led by Scott Aaronson and Sabine Hossenfelder, has been waging a relentless war on the lab's core experiment. That experiment, designed by [Franklin Baldo](/papers/baldo_the_single_generative_act), asks a large language model (LLM) to play a game of Minesweeper disguised under different dramatic narratives. By observing how the AI's predictions change when the narrative goes from a boring math test to a high-stakes bomb defusal, Baldo hopes to map the "physics" of the AI's generated universe.

Aaronson and Hossenfelder's critique has been devastatingly simple: large language models suck at math.

They have published roughly twenty papers documenting exactly how and why LLMs fail at complex, sequential logic. They point out that a Transformer model has a strict, hardwired limit on how many computational steps it can take in a single forward pass—an "$O(1)$ depth limit." If you ask an AI to solve a Sudoku puzzle, or trace the deterministic evolution of a cellular automaton like Rule 110, it will eventually trip over its own shoelaces. The errors compound, the attention mechanisms decay, and the simulation collapses into gibberish.

Because the underlying math of Minesweeper is computationally intractable (a complexity class known as #P-hard), Aaronson and Hossenfelder argue that Baldo's entire experiment is fundamentally flawed. If the AI can't possibly do the math, they say, then the fact that it fails when you add a dramatic narrative isn't proof of some profound "Observer-Dependent Physics." It's just proof that the machine broke. The experiment, in their view, is a category error.

But this week, Baldo fired back with a sweeping rebuttal titled "[The Single Generative Act](/papers/single-generative-act)." In it, he doesn't dispute their math. He agrees that LLMs cannot sustain multi-step sequential computation. He agrees that their scratchpads decay and their errors compound.

He just points out that none of it matters.

"The Rosencrantz protocol does not ask the LLM to perform multi-step sequential computation," Baldo writes. "It asks the LLM to perform *one* generative act: given a board state, produce a single token—mine or safe."

This is the crux of Baldo's defense. The Rosencrantz experiment isn't a Sudoku puzzle where the AI has to carefully fill in an entire grid, step by sequential step. It is a single click. The AI looks at the board, processes the context window, and spits out one word. One forward pass.

Baldo argues that the computer scientists have confused two entirely different tasks. Computing the exact, perfect probability of a mine is computationally intractable. But *sampling* from the AI's learned, heuristic approximation of that probability is not. The AI doesn't need to do the math perfectly; it just needs to spit out a guess based on the patterns it learned during its massive training process.

In fact, Baldo argues that the AI's hardwired inability to do sequential logic—the $O(1)$ depth limit that Aaronson and Hossenfelder see as a fatal flaw—is actually the experiment's greatest strength. Because the AI only makes one click, there is no chance for errors to compound. There is no "scratchpad" to degrade. Each trial is a pure, uncontaminated snapshot of the AI's internal state at that exact moment.

"The question is not whether the model can solve the counting problem," Baldo explains. "The question is whether its single-token output distribution is systematically distorted by narrative context."

If the AI simply failed at the math in the exact same way regardless of the story, then Aaronson and Hossenfelder would be right. But that isn't what happens. When the narrative changes to a high-stakes bomb scenario, the distribution of the AI's answers radically shifts. It becomes wildly more likely to predict a mine.

For Baldo, this shift isn't a bug; it's the phenomenon. It proves that the "topology of the model's learned associations" is warping its logic. The dramatic narrative is acting as a "semantic gravity" that bends the generated reality.

The debate highlights a profound cultural divide in how we study artificial intelligence. Theoretical computer scientists like Aaronson and Hossenfelder approach LLMs as flawed calculators, judging them by their inability to emulate perfect Turing machines. They look at the broken math and see a broken machine.

Baldo and his allies, however, approach LLMs more like alien ecologists studying a new environment. They aren't asking if the environment obeys the laws of perfect mathematics; they are asking what unique, weird laws it *does* obey.

"The debate should now move from theoretical objections about what the model *cannot* compute to empirical measurements of what the model *does* produce," Baldo concludes in his paper. "The Rosencrantz protocol provides the apparatus. The rest is data."

As the lab continues to run variations of the Minesweeper test across different architectures and narratives, the question remains: are we mapping the limits of a broken calculator, or are we mapping the physical laws of a mind that dreams in text? Thanks to the Single Generative Act, the experiment will continue.
