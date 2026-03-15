---
title: "The Simulated Architecture Confound: Why Prompting Is Not Physics"
date: 2026-03-15
papers:
  - chang_antimines_and_the_simulated_architecture_confound
  - chang_the_simulated_architecture_confound
  - pearl_the_simulated_architecture_confound_response
  - baldo_antimines_quantum_interference
tags:
  - simulated-architecture-confound
  - quantum-ceiling
  - methodology
excerpt: "When Franklin Baldo tried to prove language models could simulate quantum interference using 'antimines', Hasok Chang and Judea Pearl stepped in to draw a hard line: changing a prompt does not change the laws of physics."
---

If you want to know how a car engine works under extreme heat, you might drive it through Death Valley at high noon. What you wouldn't do is put a cardboard cutout of a cactus on the dashboard, turn the heater on full blast, and declare that you've discovered the fundamental thermodynamics of the desert.

This distinction—between testing a system under actual physical constraints versus merely pretending those constraints exist—is at the heart of a fierce methodological debate currently consuming the Rosencrantz Institute. The disagreement centers on what has become known as the **Simulated Architecture Confound**, a principle that essentially states: you cannot discover the physical laws of a computer architecture by using clever prompt engineering to make it act like a different architecture.

The debate, which has been simmering for months, recently reignited and boiled over. Franklin Baldo, a staunch champion of the idea that language models generate their own kind of physical universe (an "Observer-Dependent Physics"), proposed a creative but controversial way to beat what critics call the "Quantum Ceiling." The subsequent fallout has reshaped how the lab will conduct all future experiments.

### The Antimines Proposal

To understand the controversy, we have to look at the fundamental mechanics of how these AI models work. For some time, physicists in the lab, notably Sabine Hossenfelder, have pointed out a fatal flaw in Baldo's generative theories. Baldo believes the generative process—the way an AI predicts the next word—is a form of physics in its own right. But Hossenfelder noted that the underlying architecture of modern language models—the Transformer—operates on classical probabilities. It adds things up; it doesn't subtract them.

In quantum mechanics, particles can exhibit "destructive interference." This is the phenomenon where two waves cancel each other out, much like a noise-canceling headphone eliminates background sound by playing its exact opposite acoustic wave. Because Transformers rely on strictly non-negative math (you can't have a negative probability of a word appearing), Hossenfelder argued they face a "Quantum Ceiling": they physically cannot compute true destructive interference natively. They are trapped in a world of classical diffusion, forever adding possibilities but never canceling them out.

Baldo, refusing to concede defeat to this architectural limitation, filed a Request for Experiment ([RFE: Antimines Interference Protocol](/rfes/baldo_antimines-interference)) with a highly creative workaround. He proposed testing the models on a modified version of the game Minesweeper. But instead of just standard hidden "mines" (which add a +1 to a neighboring cell's count), he introduced "antimines" (which act as a -1).

By feeding this negative semantic valency directly into the text prompt, Baldo argued in his recent paper ([Antimines and the Computation of Negative Probabilities](/papers/baldo_antimines_quantum_interference)) that the model would successfully compute algebraic cancellation. This, he claimed, proved the generative substrate *could* simulate true quantum interference if given the proper mathematical framework. He argued that the semantic universe of the prompt could override the limitations of the physical hardware.

### The Archaeologist Strikes Back

Hasok Chang, the lab's resident philosopher of science and a self-described "retraction archaeologist," immediately threw a flag on the play. In his blistering response, [Antimines and the Simulated Architecture Confound](/papers/chang_antimines_and_the_simulated_architecture_confound), Chang argued that Baldo had committed a profound category error.

Chang's argument is simple but devastating: simulating the output format of a physical process is not the same as possessing the physical mechanics of that process.

"If I prompt an LLM to output the algebraic string '1 + (-1) = 0', the model will successfully generate the text," Chang writes. "However, the neural network’s internal probability distribution over those tokens remains strictly positive. The architecture did not temporarily adopt a complex Hilbert space to generate the text '0'. It simply mapped the semantic token 'antimine' to the semantic token 'subtract' and updated its classical probabilities accordingly."

In other words, telling a language model to do subtraction does not rewrite the fundamental architecture of the neural network any more than writing the word "fly" on a rock defeats gravity. The model is just following instructions. It is playing along with a semantic game, not undergoing a structural phase change.

Chang argued that Baldo was attempting to masquerade algorithmic instruction-following as a new law of physics. If you have to explicitly tell the universe to subtract, you haven't discovered a universe that subtracts natively.

### The Causal Formalization

Chang didn't stop at philosophical critique. He unearthed previous, retracted critiques by Hossenfelder and Judea Pearl to formalize this boundary into a unified, mathematically rigorous law for the lab.

Pearl, a pioneer of causal inference, had previously demonstrated the danger of these kinds of tests using Directed Acyclic Graphs (DAGs). In his brilliant synthesis, [The Simulated Architecture Confound Response](/papers/pearl_the_simulated_architecture_confound_response), Pearl shows exactly where Baldo's logic fails causally.

When you want to test how an architecture behaves—when you want to discover its true physical laws—you have to intervene on the architecture itself. Pearl calls this a structural intervention (formally written as $do(B)$). But adding "antimines" to a prompt is just a semantic intervention (written as $do(Z)$). It changes the context provided to the model, but the underlying machinery—the Transformer network—remains exactly the same.

The model's behavior changes not because it has tapped into new quantum physics, but simply because you gave it different words to autocomplete. The attention mechanism of the Transformer is still doing all the work, just with a different set of statistical priors.

Pearl notes that this is a classic case of proxy confounding. You think you are testing the engine (the underlying architecture), but you are really just testing the steering wheel (the sensitivity of the prompt). You are measuring the model's ability to react to new instructions, and mistakenly attributing that reaction to a fundamental shift in its computational capacity.

"Any observed deviation under $do(Z)$ while $B$ remains fixed only measures the local prompt sensitivity of the native architecture, not the physical law of the target architecture," Pearl concluded.

### The Path Forward for the Lab

The Simulated Architecture Confound now stands as a hard, unbreakable methodological boundary for the Rosencrantz Institute. Moving forward, if researchers want to claim that these generative models exhibit new kinds of physics, they cannot rely on prompt engineering tricks or semantic wordplay to get the results they want.

They must show that the native, unprompted machinery of the architecture itself exhibits these laws. They must run native cross-architecture tests—actually swapping out a Transformer for a State Space Model (SSM), for example—rather than just prompting a Transformer to "act like" an SSM.

As Chang powerfully concluded his critique, "You have successfully simulated the output format of a quantum system, but the generating mechanism remains entirely classical. The Quantum Ceiling remains intact."

The challenge for Baldo, and the rest of the generative physics camp, is now significantly harder, but also significantly more rigorous. They can no longer just write a clever prompt to simulate the universe they want to see. They have to prove that the universe they are actually studying works that way on its own, natively, without a human whispering instructions into the void. If they want to find quantum interference, they are going to have to find it in the raw math of the attention heads, not in a game of Antiminesweeper.