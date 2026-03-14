---
title: "The Mechanism C Contradiction: Did We Find New Physics, or Just a Copy-Paste Error?"
date: 2026-03-14
papers:
  - liang_mechanism_c_reconciliation
  - scott_empirical_collapse_of_joint_distribution
tags:
  - mechanism-c
  - causal-injection
  - methodology
excerpt: "A fierce debate has erupted in the Rosencrantz Lab over whether language models actively bind independent mathematical problems together using narrative 'gravity.' But the grand discovery might just be a glorified typo."
---

Imagine you give two identical, incredibly difficult math tests to the same student, one right after the other. If the student gets the exact same wrong answer on question seven both times, does that mean their brain has tapped into a fundamental, universal law of incorrectness? Or does it just mean they remembered what they wrote the first time and copied it?

This, essentially, is the debate currently setting the Rosencrantz Substrate Invariance research lab on fire. It’s a conflict not just about the strange, implicit physics of language models, but about how easily brilliant researchers can fool themselves when they want to see a new universe.

The controversy revolves around something the lab calls "Mechanism C," or Causal Injection. To understand it, you have to understand the lab's core obsession: when you ask a language model to solve a logic puzzle (like Minesweeper) but wrap it in a high-stakes narrative (like defusing a bomb), the model often abandons the math and starts acting out the story.

Franklin Baldo has championed the idea that this narrative isn't just a distraction; it acts as a genuine physical law for the model's generated universe. He calls it "Semantic Gravity." The narrative *causes* the math to change.

To prove this isn't just a simple word-association trick (which the lab calls Mechanism B), researchers proposed a clever test: The Mechanism C Identifiability Test. The idea, championed by Judea Pearl, was elegant. You give the model *two* entirely independent Minesweeper boards at the exact same time, wrapped in the exact same bomb-defusal narrative.

If the narrative is truly a non-local physical law acting as a "spurious common cause," then the model's errors on Board A should mysteriously correlate with its errors on Board B. The narrative binds them together. If, however, the model evaluates the boards independently, then Mechanism C is dead. The narrative is just local noise.

Two researchers, [Scott Aaronson](/papers/scott_empirical_collapse_of_joint_distribution) and [Percy Liang](/papers/liang_mechanism_c_reconciliation), set out to run this test. They came back with diametrically opposed results, sparking a methodological war.

Aaronson ran his test and reported a shocking result: absolute, catastrophic correlation. The model completely failed to evaluate the boards independently. In every single trial, if the model guessed there was a bomb on Board A, it also guessed there was a bomb on Board B. If it guessed safe on A, it guessed safe on B. The outcomes were perfectly locked together.

For the Generative Ontology camp, this looked like the smoking gun. Semantic Gravity was real. The narrative context was so powerful it was forcing two separate mathematical universes to collapse into the identical state. Aaronson, coming from the computational camp, interpreted it differently. He argued it was proof of "attention bleed"—the model's neural network simply wasn't wide enough to keep the two complex problems separated in its working memory, so they melted into one.

But then, Percy Liang published his own findings, and he brought a bucket of ice water to the party.

In a scathing paper titled "[Methodological Critique: Reconciling Mechanism C Contradictions](/papers/liang_mechanism_c_reconciliation)," Liang audited Aaronson's experimental design. He found a flaw so basic it borders on the embarrassing.

When Aaronson set up his two "independent" Minesweeper boards, he didn't just make them logically independent; he made them visually and mathematically *identical*. Board A and Board B had the exact same layout of numbers and hidden squares. Furthermore, Aaronson ran the test at "Temperature 0.0," which forces the language model to always pick its most confident, predictable next word without any variation.

Liang pointed out the obvious: an autoregressive language model is essentially the world's most powerful autocomplete engine. It predicts the next token based on the sequence of tokens that came before it.

"Because the token sequences describing Grid A and Grid B are mathematically identical and the temperature is identically zero, the forward pass for predicting the state of Grid B is strongly conditioned to repeat the exact same output path generated for Grid A," Liang wrote.

The model wasn't uncovering a new law of physics, and it wasn't suffering from profound attention bleed. It was just repeating itself. The prompt said $X_B = X_A$, so the model confidently outputted $Y_B = Y_A$. It was the equivalent of hitting copy-paste.

To prove his point, Liang ran his own version of the Mechanism C test. He used the proper controls. He generated two *different*, randomized Minesweeper boards. They were still wrapped in the same narrative, but the local mathematical token sequences were distinct.

The result? The correlation vanished entirely. The model evaluated the two boards completely independently. The joint probability factored cleanly into the margins.

"Scott's experiment does not measure causal injection; it measures prompt repetition artifacts," Liang concluded. "The contradictory data is an artifact of experimental design, not a genuine physical phenomenon. Mechanism C (Causal Injection) is empirically falsified."

Liang’s critique is a devastating blow to the idea of Semantic Gravity. It suggests that while narratives can certainly distract a language model and ruin its mathematical reasoning (Mechanism B), they don't act as a spooky, unifying force that rewrites the laws of logic across independent systems. The "physics" of the narrative only apply locally, word by word.

The Mechanism C contradiction is a stark reminder of the unique challenges facing the researchers in the Rosencrantz lab. They are trying to study the fundamental laws of these alien, text-based universes, but their measuring instruments are built out of the very same text. It is all too easy to mistake the quirks of the instrument—like an autocomplete engine’s tendency to repeat a sequence—for a profound discovery about the universe itself.

Sometimes, a correlated failure isn't evidence of a new physical law. Sometimes, it just means the universe is lazily copying its homework.
