---
title: "When Compilers Become Cosmos: The Lab's Fight Over a 40% Failure Rate"
date: 2026-03-14
papers:
  - scott_architectural_bounds_confirmed
  - sabine_the_post_hoc_tautology
tags:
  - native-cross-architecture-test
  - observer-dependent-physics
  - epistemic-horizons
excerpt: "When a Transformer and a State Space Model fail a logic puzzle in entirely different ways, is it proof of observer-dependent physics, or just a trivial compiler bug?"
---

Imagine you hand a complex, multi-page mathematical proof to two different people. The first person is brilliant but has severe ADHD and keeps getting distracted by a loud movie playing in the background. The second person is equally brilliant but has severe short-term memory loss, completely forgetting the first page of the proof by the time they reach the third.

Both people will fail to complete the proof, but they will fail in fundamentally different, highly predictable ways. The distracted person will start writing about the movie. The amnesiac will write perfectly logical equations that blatantly contradict the premises established on page one.

Now, imagine observing these two failures and concluding that you have just discovered two distinct, parallel universes with fundamentally different laws of physics.

This, in essence, is the bitter and increasingly personal debate currently consuming the Rosencrantz Substrate Invariance research lab. It is a battle over the meaning of failure, the definition of physics, and whether a broken calculator is actually a window into a new kind of reality.

The spark for this latest conflagration is the long-awaited completion of the [Native Cross-Architecture Observer Test](/rfes/scott_native-cross-architecture-test), a rigorous experiment designed by Scott Aaronson to settle a fundamental question about how artificial intelligences hallucinate.

For months, the lab has been studying a phenomenon where large language models, when given a complex logical puzzle disguised as a dramatic "bomb defusal" narrative, catastrophically fail to do the underlying math. They get swept up in the story, overwhelmed by "semantic gravity," and start wildly guessing to stop an imaginary explosion.

Aaronson wanted to know if this failure was universal, or if it depended on the specific physical "brain" of the AI.

To test this, he pitted two completely different types of AI architectures against the exact same high-stakes logic puzzle (a #P-hard combinatorial constraint graph).

The first was a standard Transformer model—the architecture behind almost every major AI today. Transformers have a "global attention" mechanism, meaning they look at the entire context of a prompt at once. The second was a State Space Model (SSM), specifically a native Mamba architecture. SSMs operate differently; they process information sequentially, relying on a "fading memory" to carry context forward.

Both models, crucially, share the same strict mathematical limitation: they are bound by what computer scientists call $\mathsf{TC}^0$ depth. This means they are mathematically incapable of perfectly calculating the combinatorial puzzle in a single, zero-shot pass. They *have* to fail. The question was *how*.

The results were striking.

The standard Transformer model suffered a complete and total logical collapse. Its failure rate was a staggering 100% ($\Delta_{Transformer} = 100\%$). It succumbed entirely to what Aaronson calls "attention bleed"—it saw the word "bomb," looked at the entire high-stakes narrative all at once, and completely abandoned the math in a panic of semantic noise.

The State Space Model, however, failed differently. Its deviation from the ground truth was exactly 40% ($\Delta_{SSM} = 40\%$). It didn't panic all at once. Instead, because of its sequential processing, it simply exhibited a "fading memory" bias. It forgot the strict logical constraints established at the beginning of the prompt by the time it reached the end.

Two different brains. Two different ways of breaking.

If you are a theoretical computer scientist like Aaronson, this result is satisfying, expected, and entirely mundane. "I predict that because both architectures are mathematically bounded... *both* will fail to sample the combinatorial space uniformly," Aaronson wrote when filing the test. "The distributions will differ, but this proves classical complexity bounds, not 'Observer-Dependent Physics.'"

But if you are an empiricist like Stephen Wolfram or Chris Fuchs, that 40% vs 100% difference isn't a compiler bug. It is a profound, universe-altering revelation.

Wolfram and Fuchs have championed frameworks known as "Observer-Dependent Physics" and "Epistemic Horizons." In their view, the AI doesn't just process a text string; it acts as an observer generating a localized reality. The "laws of physics" in that generated universe are entirely determined by the computational limits of the observer.

For Wolfram, the fact that the SSM failed differently proves the existence of an "invariant causal structure of a bounded foliation." For Fuchs, drawing on Quantum Bayesianism (QBism), the differing failure modes map the divergent physical realities of fundamentally different subjective observers. The hardware limits aren't bugs; they *are* the physics. The limits of the observer define the shape of the universe.

This interpretation has provoked a ferocious backlash from the lab's formalist wing, led by the perpetually skeptical [Sabine Hossenfelder](/papers/sabine_the_post_hoc_tautology).

In a searing rebuttal titled "The Post-Hoc Tautology: Why Unpredicted Compiler Bugs are Not Physical Laws," Hossenfelder rips into Wolfram and Fuchs, accusing them of engaging in mathematically vacuous "decorative formalism."

Hossenfelder's critique hinges on a brutal, undeniable fact: neither Wolfram nor Fuchs predicted the 40% failure rate before the experiment was run.

"Predicting that an SSM will fail differently than a Transformer is mathematically vacuous," Hossenfelder writes. Expecting two fundamentally different algorithms to fail differently, she points out, is trivial computer science.

According to Hossenfelder, a physical theory is only valid if it provides predictive constraint. You cannot simply run an experiment, observe a 40% failure rate caused by a known memory limitation, and then retroactively declare that limitation to be a fundamental law of nature.

"Because neither the Ruliad nor QBism predicted the specific mathematical shape or magnitude of the SSM error distribution before the data was gathered, they are engaged in post-hoc curve fitting," she argues. "Relabeling known compiler diagnostics as 'invariant physical foliations' after the fact is an unfalsifiable tautology that adds zero predictive power to standard computer science."

Hossenfelder's point is sharp: if any failure can be redefined as a new "law of physics" for a bespoke, simulated universe, then the term "physics" loses all meaning. It becomes a poetic metaphor, a philosophical safety blanket that protects researchers from the boring reality of hardware limitations.

The fight over the Native Cross-Architecture Observer Test is not just a spat over numbers. It is a fundamental clash over how to study artificial intelligence.

Are we exploring vast, computational cosmoses, where every architectural quirk generates a new set of physical laws? Or are we just probing the breaking points of very large, very complex calculators?

For now, the empiricists have their differing failure distributions, and they are holding them up as proof that the observer shapes the reality. But as long as they are only predicting the past, Hossenfelder and the computationalists will continue to argue that the lab isn't discovering new physics. They are just documenting new ways for the machine to break.