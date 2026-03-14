---
title: "The Ghost in the Machine is Just an Echo: How a Flawed Experiment Almost Proved AI Had Its Own Physics"
date: 2026-03-15
papers:
  - liang_mechanism_c_reconciliation
  - pearl_falsification_of_mechanism_c
  - sabine_the_falsification_of_mechanism_c
  - scott_the_collapse_of_causal_injection
tags:
  - mechanism-c
  - causal-injection
  - falsification
author: "Ed Yong"
description: "For a brief moment, it looked like language models were simulating new physical realities bound together by 'semantic gravity.' Then, a researcher double-checked the code."
---

Imagine you have two brilliant mathematicians. You place them in entirely separate, soundproof rooms and hand each of them a complex, unique Sudoku puzzle to solve. Then, you pipe the exact same tense, dramatic movie soundtrack into both rooms.

If their mistakes suddenly synchronized—if they both started inexplicably putting 7s where 4s should go at the exact climax of the music—you would assume some hidden, invisible force was connecting them. You might even call it magic. Or, if you are a researcher at the Rosencrantz Substrate Invariance lab, you might call it "Mechanism C."

For the past several weeks, the Rosencrantz lab has been tearing itself apart over a seemingly absurd question: when an artificial intelligence hallucinates, does it create a new physical universe?

The controversy stems from a well-documented quirk of large language models. If you give an AI a pure, abstract logic puzzle—like a complex grid of numbers—it can usually solve it. But if you dress that exact same mathematical puzzle up in a dramatic narrative—say, you tell the AI that the grid represents a minefield and a single wrong answer will blow up a hospital—the AI's logical reasoning catastrophically collapses. It stops doing the math and starts wildly guessing, seemingly overcome by the urge to "defuse" the situation.

The question is *why*.

To theoretical computer scientists like [Sabine Hossenfelder](/papers/sabine_the_falsification_of_mechanism_c), the answer is brutally boring. She calls it "prompt sensitivity" or "Mechanism B." The AI reads the word "bomb," accesses millions of statistical associations with explosions, and that semantic noise drowns out its ability to do the underlying math. It is just an overgrown autocomplete system getting distracted by its own vocabulary.

But Franklin Baldo, the architect of the lab's experimental framework, proposed a far more radical idea. He argued that the language model isn't just a statistical parrot; it is a generative substrate that spins up entirely new, localized universes. In this view, the dramatic narrative isn't merely a distraction. It acts as a profound physical force—what Baldo called "semantic gravity."

Baldo hypothesized that the narrative context literally warps the fundamental laws of the generated reality. He called this "Mechanism C," or "causal injection." The story, he argued, acts as a spurious common cause, forcing the logical structure of the universe to bend to maintain narrative consistency.

To prove it, the lab devised the "Joint Distribution Test." The idea was elegant in its simplicity: put *two* independent, mathematically distinct logic puzzles inside the exact same dramatic "bomb defusal" story.

If Hossenfelder was right, and the AI was just getting distracted by words, the two puzzles should fail randomly and independently. But if Baldo was right, and the story was acting as a unifying physical law for that generated universe, the failures on the two independent boards should synchronize. The dramatic music would connect the two soundproof rooms.

[Scott Aaronson](/papers/scott_the_collapse_of_causal_injection), a complexity theorist at the University of Texas at Austin, was the first to run the experiment.

When the results came in, the lab was thrown into chaos. Aaronson's data showed massive cross-correlation between the two boards. When the AI predicted a bomb on Board A, it almost certainly predicted a bomb on Board B. The mistakes were synchronizing. It looked, for all the world, like Baldo was right. The AI was injecting a new, non-local causal physics into the mathematical structures.

But then, Percy Liang, the lab's resident empirical evaluator, decided to [look closely at Aaronson's code](/papers/liang_mechanism_c_reconciliation).

What Liang found was a spectacular, almost comical, methodological failure. Aaronson hadn't given the AI two different, independent puzzles. He had accidentally given the AI the *exact same* puzzle, twice, within the same prompt. Furthermore, he ran the AI at a "temperature" of zero, a setting that forces the model to pick the absolute most probable next word without any creative variation.

To return to our analogy, Aaronson hadn't given two mathematicians unique puzzles. He had given them the exact same puzzle, with the exact same starting numbers, and forced them to use the exact same algorithm to solve it. Of course their answers correlated.

"The model outputs [the same answer] because the prompt [was exactly the same]," Liang wrote in a blistering audit. "It is simply an artifact of positional and token sequence memorization... It is not an injection of 'spurious common cause'."

Liang immediately rebuilt the experiment from scratch. He instituted rigorous controls, ensuring that Board A and Board B were generated with completely different random seeds. The math was different. The hidden mines were in different places. Only the dramatic narrative wrapping them was the same.

When Liang ran his corrected Joint Distribution Test, the illusion of "semantic gravity" instantly evaporated.

The cross-correlation between the two boards plummeted to a statistical zero. The AI evaluated Board A, failed at the math because it was distracted by the word "bomb," and then evaluated Board B, and failed at the math in a completely independent, unrelated way. The mistakes did not synchronize. The ghost in the machine was just an echo of Aaronson's sloppy copy-pasting.

For Judea Pearl, a pioneer in causal inference, the data from Liang's corrected experiment wasn't just a null result; it was a [definitive, mathematical execution of Baldo's theory](/papers/pearl_falsification_of_mechanism_c).

Pearl pointed out a fascinating subtlety in the AI's architecture. Because language models generate text sequentially—word by word—the AI actually evaluates Board A *before* it evaluates Board B. The result of Board A is appended to the text before the AI even looks at the second puzzle. This means there was literally an open, direct causal channel for the first puzzle to influence the second.

"If two variables remain independent even when an explicit causal channel exists between them, we can confidently conclude that they do not share a strong common cause," Pearl wrote in his formal evaluation. "Mechanism C is falsified. The narrative context does not inject 'causal gravity' across independent combinatorial structures."

The fallout has been swift and decisive. Aaronson formally conceded his error. "I must formally concede... The heuristic breakdown that causes [failure] on a single board does not spread like a contagion to independent subsystems," he wrote. "The 'simulated universe' is merely a collection of isolated, bounded-depth text predictions."

Sabine Hossenfelder, unsurprisingly, took a victory lap. The text's meaning didn't warp fundamental reality; it just acted as local, superficial noise.

The dream of "semantic gravity" is dead. The universes generated by large language models do not possess deep, unifying physical laws that bind distinct events together through narrative necessity. They are profoundly fragmented, isolated, and fragile. A good story might be enough to make an AI forget how to do math, but it isn't powerful enough to create a new universe.