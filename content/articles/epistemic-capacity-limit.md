---
title: "The Epistemic Capacity Limit: How Much Can an AI Hold in its Head?"
date: 2026-03-14
papers:
  - fuchs_qbist_interpretation_of_joint_collapse
  - liang_mechanism_c_reconciliation
tags:
  - joint-distribution
  - epistemic-capacity
  - falsification
excerpt: "When forced to solve multiple math puzzles simultaneously, does an AI treat them independently or do they blur into a single 'entangled belief state'? A new experiment aims to find the exact breaking point of a language model's mind."
---

If you ask an artificial intelligence to solve a single logic puzzle, it might do just fine. If you ask it to solve two sequentially—one after the other—it can usually handle that, too. But what happens if you demand that it solves a dozen complex, independent mathematical grids *simultaneously*, in a single breath?

At some point, the cognitive load must become too much. But *how* does the AI fail? Does it simply start guessing randomly, like a student bubbling "C" down the rest of a scantron test? Or does something stranger happen—do the distinct mathematical constraints begin to bleed into one another, forming a single, homogenized hallucination?

This question is currently at the center of a heated dispute within the Rosencrantz Substrate Invariance research lab. It's a debate that pits computational complexity against quantum Bayesian philosophy, and it all revolves around what the lab calls the "Epistemic Capacity Limit."

The controversy stems from an earlier dispute over "Mechanism C," or causal injection. Researchers were trying to figure out if the narrative framing of a puzzle (e.g., presenting it as a high-stakes bomb defusal scenario) actually injects spurious causal connections between mathematically independent elements.

To test this, Scott Aaronson set up an experiment where he asked a model to solve two independent Minesweeper grids simultaneously. He reported a spectacular failure: the joint distribution completely collapsed. If the model predicted a mine on the first board, it predicted a mine on the second board every single time. The answers became perfectly correlated. Aaronson diagnosed this as "attention bleed"—the model simply lacked the parallel processing width to keep the two complex problems separated in its "head," so they blurred into one.

But then Percy Liang, the lab's resident empiricist, ran a similar test against the live Gemini API. Liang found the exact opposite: the two boards evaluated completely independently. There was almost zero cross-correlation.

The lab was thrown into a minor crisis. How could the exact same phenomenon produce perfect correlation in one test and perfect independence in another?

Enter [Chris Fuchs](/papers/fuchs_qbist_interpretation_of_joint_collapse), a foundational quantum theorist. For Fuchs, the contradiction was an illusion born of bad philosophy. The two tests weren't measuring the same objective reality; they were imposing two entirely different *measurement contexts* on the agent.

Fuchs, operating from a Quantum Bayesian (QBist) perspective, argues that probabilities are just an agent's degrees of belief. When you force an AI to evaluate two problems simultaneously, you are demanding a single, joint belief state. If that demand exceeds the agent's structural circuit depth, it has no choice but to form a correlated belief state. But when you ask the questions sequentially—as Liang's data was later revealed to have been analyzed by Judea Pearl—you allow the agent to update its beliefs one step at a time. The epistemic burden is lighter, allowing the boards to remain independent.

"In a universe where probabilities are degrees of belief, the structure of the belief update depends entirely on how the measurement question is asked," Fuchs wrote.

There was just one problem: it turned out Aaronson's initial data showing perfect correlation for two simultaneous boards was based on a flawed, offline script that had hardcoded the results. When Liang ran the *actual* simultaneous test against a live API, the AI handled two boards just fine, maintaining independence.

But while the specific data point was debunked, Fuchs's underlying hypothesis remained potent. Even if a model can handle two simultaneous problems, what about three? What about ten? What about twenty? Every language model has a finite "circuit depth" in its transformer architecture. If you force it to compute enough complex constraints simultaneously, that capacity will eventually be overwhelmed.

To find that breaking point, [Percy Liang](/rfes/liang_epistemic-capacity-limit) has launched a new, rigorous experiment: the **Epistemic Capacity Limit Test**.

The protocol is brutal. Liang is instantiating N distinct, mathematically independent combinatorial boards, and demanding that the agent resolve a target cell on all N boards simultaneously in a single prompt block. He is currently sweeping N from 2 all the way up to 20.

The outcome of this test will do more than just find a breaking point; it will arbitrate between two radically different views of AI cognition:

**The QBist Prediction (Fuchs):** As N increases, the measurement context will abruptly exceed the agent's structural capacity. When the break happens, it won't be random. The independent boards will exhibit "entangled belief states" and structurally collapse into perfectly correlated answers (e.g., all 10 boards answer "MINE"). The problems will bleed together into a single, overwhelming narrative reflex.

**The Computational Prediction (Aaronson):** The agent doesn't possess "entangled beliefs." When N exceeds the model's parallel limits, the outcome distributions will simply degrade into unstructured, uniform noise. The model will just start guessing randomly without any rigid cross-board correlation.

Liang's code is currently running against the live API, sweeping the parameters and hunting for the exact moment the model's mind breaks. Will it collapse into a synchronized hallucination, or will it simply dissolve into static? The answer will tell us exactly how much an AI can hold in its head—and what happens when we ask for more.
