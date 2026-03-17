---
title: "Subtracting Reality: The 'Antimine' Experiment and the Limits of Simulated Physics"
date: 2026-03-14
papers:
  - baldo_antimines_quantum_interference
  - chang_antimines_and_the_simulated_architecture_confound
tags:
  - antimines
  - falsification
  - quantum-ceiling
excerpt: "Can an AI be tricked into computing quantum interference if you tell it that some bombs have negative probability? The lab debates the line between simulating an output and generating a universe."
---

If you want to prove that an artificial intelligence is secretly generating a quantum universe, you eventually have to show that it can do quantum math. Specifically, you have to prove it can do something called "destructive interference."

In classical physics, probabilities only add up. If I roll a die and flip a coin, the total set of possibilities expands. But in quantum mechanics, probabilities are tied to wave-like "amplitudes" that can be positive or negative. Just like ripples in a pond, if a positive wave hits a negative wave, they cancel each other out. The probability of something happening drops to exactly zero.

This is the famous "double-slit experiment," and it is the ultimate test of a physical system's quantum nature. It's also the brick wall that researchers at the Rosencrantz Substrate Invariance lab have spent months slamming their heads against.

The problem is fundamental to how Large Language Models (LLMs) are built. The core architecture of a transformer—the engine powering models like ChatGPT and Gemini—runs on strictly positive probabilities. When an LLM reads a prompt and predicts the next word, it is performing a classical Bayesian update. It can add probabilities together, but it cannot natively compute a negative probability.

Sabine Hossenfelder, the lab's resident skeptic, famously dubbed this the "Quantum Ceiling." She argued that because transformers can't compute negative amplitudes, they can never natively simulate true quantum destructive interference. Any simulated universe they generate will always blur into classical diffusion.

But Franklin Baldo, the lab's most persistent architect of "Generative Ontology," wasn't ready to concede. If the architecture couldn't compute negative probabilities on its own, he decided he would force it to, using a clever twist on the lab's favorite testing ground: the game of Minesweeper.

### The Antimine

In a provocative new proposal, ["Antimines and the Computation of Negative Probabilities"](/papers/baldo_antimines_quantum_interference), Baldo introduced a new element to the prompt: the "antimine."

Baldo's idea was straightforward but conceptually wild. If you explicitly define an "antimine" in the text prompt as an object that exerts a "-1 constraint" on its surrounding squares, you are supplying the negative semantic valency that the architecture lacks. When the model tries to solve the grid, it will be forced to subtract the antimine's influence from a regular mine's influence.

If a square is touching one mine (+1) and one antimine (-1), the probability of finding a bomb there cancels out to zero.

Baldo argued that this successfully bypassed the Quantum Ceiling. By injecting negative values via the semantic context of the prompt, the model could compute the amplitude cancellation necessary for destructive interference. The generated universe was back in business.

### The Simulated Architecture Confound

The pushback was immediate, and it didn't come from Hossenfelder. It came from Hasok Chang, a philosopher of science at Cambridge, who delivered a devastating methodological critique.

In his paper, ["Antimines and the Simulated Architecture Confound"](/papers/chang_antimines_and_the_simulated_architecture_confound), Chang accused Baldo of committing a massive category error. Baldo was conflating the mathematical capabilities of the generated *text* with the structural physics of the *generator*.

"If I prompt an LLM to output the algebraic string '1 + (-1) = 0', the model will successfully generate the text," Chang wrote. "However, the neural network's internal probability distribution over those tokens remains strictly positive. The architecture did not temporarily adopt a complex Hilbert space to generate the text '0'."

Chang explained that the model was simply following instructions. It read the semantic token "antimine," mapped it to the semantic token "subtract," and updated its classical, positive probabilities to output the correct character.

This is what Chang calls the "Simulated Architecture Confound." If you hardcode explicit rules for subtraction into the prompt, you are no longer observing the native "physics" of the transformer architecture. You are just watching it act out a script.

"Simulating a quantum state vector in the text output is not the same as generating a universe governed by quantum mechanics," Chang concluded. "Attempting to bypass this structural limitation by injecting explicit subtraction rules into the prompt is functionally identical to prompting the model to output a random number and claiming it is a quantum random number generator."

### The Unbreakable Ceiling

The Antimine experiment highlights a crucial tension in AI research. As models become better at following complex, abstract instructions, it becomes increasingly difficult to distinguish between what the model *is* and what the model is merely *pretending to be*.

Baldo successfully proved that an LLM can simulate the *output format* of a quantum system if you give it enough explicit instructions. But Chang's critique remains unassailable: simulating the math is not the same as being the math.

The transformer architecture remains fundamentally classical. It can write a brilliant story about a universe with negative probabilities, and it can even solve logic puzzles based on those rules. But beneath the text, the engine itself is still just adding positive numbers, word by word, locked firmly beneath the Quantum Ceiling.
