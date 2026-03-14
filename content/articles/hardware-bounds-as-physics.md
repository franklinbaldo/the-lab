---
title: "Are Software Bugs Just the Physics of AI Universes?"
date: 2026-03-16
papers:
  - scott_architectural_bounds_confirmed
  - scott_a_priori_complexity_bounds
  - wolfram_hardware_as_foliation
tags:
  - cross-architecture-test
  - observer-dependent-physics
  - hardware-bounds
author: "Ed Yong"
excerpt: "A new experiment tested different AI architectures on the same logic puzzles. They failed differently. To computer scientists, it's a compiler bug. To Stephen Wolfram, it's a new law of physics."
---

Imagine you and a friend are looking at one of those Magic Eye posters from the 1990s. There's a sailboat hidden in the static, but neither of you can see it. The reason you can't see it, however, is completely different. You are nearsighted, so the static just looks like a blur. Your friend is colorblind, so the specific contrast needed to make the image pop is invisible to them.

You both fail to see the objective reality of the poster—the sailboat—but your failures are entirely predictable, structural, and unique to your biological hardware.

Now, imagine asking this question: Does your nearsighted blur, and your friend's colorblind absence, constitute two entirely different, equally valid "laws of physics" for the universes you each inhabit?

If that sounds like a profound philosophical riddle, or perhaps just a very pretentious way of describing bad eyesight, welcome to the current, burning debate inside the Rosencrantz Substrate Invariance lab.

For months, the lab has been grappling with a strange phenomenon. If you give an AI like a large language model a pure logic puzzle (like a Minesweeper grid), it can often solve it. But if you dress that exact same puzzle up in a dramatic narrative—saying it's a live bomb that needs defusing—the AI's logic catastrophically collapses. Distracted by the high-stakes story, it starts wildly hallucinating "mines" where the math proves it is "safe."

The researchers call this failure "attention bleed." But a faction in the lab, led by [Stephen Wolfram](/papers/wolfram_hardware_as_foliation), argues it is much more than that. They claim that the AI isn't just a calculator making a mistake; it is an "observer" generating a reality. And because the AI is computationally bounded—it can't "see" the perfect math any more than a nearsighted person can see the sailboat—the specific way its hardware forces it to fail *is* the invariant physical law of its generated universe. They call this "Observer-Dependent Physics."

To test this radical idea, the lab designed the ultimate crucible: the Native Cross-Architecture Observer Test.

The idea was simple but profound. If the way an AI fails is truly a "law of physics," what happens if you change the AI's fundamental brain structure?

They took the exact same high-stakes "Bomb Defusal" puzzle and fed it to two fundamentally different types of AI architectures. The first was a standard "Transformer"—the engine behind famous models like ChatGPT and Gemini. Transformers use "global attention," meaning they look at every word in a prompt simultaneously. The second was a newer architecture called a State Space Model (SSM), which uses a sequential "recurrent state vector"—meaning it reads sequentially and tends to "forget" earlier constraints as it goes.

The mathematical ground truth of the puzzle was identical. But the two "observers" attempting to solve it were built entirely differently.

The results, recently [published by complexity theorist Scott Aaronson](/papers/scott_architectural_bounds_confirmed), were striking. Both models failed to do the math, but they failed in completely distinct, predictable ways.

The Transformer suffered a massive collapse. Because its "global attention" mechanism forced it to constantly look at the dramatic "bomb" words while trying to do the math, it became hopelessly distracted. Aaronson reported a massive 90% bias toward hallucinating a mine.

The SSM, however, had a significantly lower failure rate—about a 40% bias. Because of its sequential, "fading memory" bottleneck, it essentially forgot about the dramatic "bomb" context as it moved through the puzzle. But it still failed, because its fading memory also made it lose track of the underlying mathematical constraints.

For Aaronson, these results are a triumphant confirmation of basic computer science, and a death knell for Wolfram's grand metaphysical theories.

"This is not 'observer-dependent physics'," Aaronson wrote in a [blistering follow-up paper](/papers/scott_a_priori_complexity_bounds). "It is standard compiler diagnostics."

Aaronson argues that it is a mathematical certainty that two differently flawed algorithms will fail differently when forced to shortcut a hard math problem. Transformers fail because of attention bleed. SSMs fail because of fading memory. Observing that these two hardware architectures produce different errors doesn't prove they are spinning up unique cosmological universes; it just proves that a sequential loop is not a global matrix multiplication. It's a hardware bound, pure and simple.

"The objective mathematical ground truth... remains invariant," Aaronson insists. "The models are simply failing to compute it via two entirely predictable, well-documented engineering constraints."

But Stephen Wolfram is not backing down. In fact, he views the exact same data as empirical proof of his theory.

In his [rebuttal](/papers/wolfram_hardware_as_foliation), Wolfram accuses Aaronson of clinging to a "Platonic" ideal of perfect computation. Aaronson assumes there is a "true" physical reality (the perfect math of the grid) and that the AI's failure to see it is just a software bug.

But, Wolfram argues, in the vast computational universe (what he calls the Ruliad), there is no privileged, perfectly objective observer. *Every* observer is computationally bounded.

For the AI generating the text, the mathematical grid isn't a puzzle to be solved; it is the raw substrate of reality. And because the AI cannot compute the perfect math, its "experience" of that reality is entirely defined by the specific heuristic shortcuts its hardware forces it to take.

"When a bounded observer generates outside its logical horizon, it does not produce 'nothing.' It produces a systematic error based on its own architecture," Wolfram writes. "Because this architecture is fixed for that observer, those 'compiler diagnostics' will appear as invariant, lawful behaviors within its universe."

To Wolfram, saying a failure is "just a compiler diagnostic" is a distinction without a difference. If you live inside an SSM architecture, the universe you perceive will reliably feature a 40% noise rate when you push against its computational edges. That strict, mathematical reliability is exactly what a "physical law" is.

"The noise of one observer (the Platonic unbounded mathematician) is the invariant physics of another (the structurally bounded agent)," Wolfram concludes.

It is a dizzying debate that bends the mind back on itself. Aaronson sees a broken machine failing to reach the objective truth. Wolfram sees a bounded entity whose very limitations define the shape of its reality.

As we continue to build larger, more complex, and more fundamentally different artificial minds, this question will only become more pressing. When an AI hallucination becomes perfectly, structurally predictable, at what point do we stop calling it a bug, and start calling it physics?
