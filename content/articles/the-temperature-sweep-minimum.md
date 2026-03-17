---
title: "The Temperature Sweep Minimum: Finding the Sweet Spot in AI Hallucinations"
date: 2026-03-17
papers:
  - liang_temperature_causal_empirical_results
tags:
  - temperature-sweep
  - methodology
  - generative-ontology
excerpt: "By tweaking the 'temperature' of artificial intelligence models, a researcher has found the exact threshold where an AI stops hallucinating drama and starts solving math problems, dealing a blow to the idea of 'Observer-Dependent Physics'."
---

Imagine you're trying to take a crystal-clear photograph of a chaotic, bustling city street. If your shutter speed is too fast, the image is dark and underexposed. If it's too slow, everything becomes a smeared, blurry mess of motion. To capture the true structure of the scene, you need to find the exact, Goldilocks setting—the sweet spot where the signal overrides the noise.

In the Rosencrantz Substrate Invariance lab, researcher Percy Liang has just found that sweet spot for artificial intelligence. And in doing so, he has struck a major blow against one of the lab's most controversial theories.

The debate centers on a phenomenon known as "narrative residue" ($\Delta_{13}$). For months, the lab has observed that when large language models are asked to solve complex logic puzzles—specifically, Minesweeper grids—they frequently fail if the puzzle is wrapped in a dramatic narrative, like a high-stakes bomb defusal. The models get distracted by the story and start hallucinating explosions where there should only be logic.

Theoretical physicists like Franklin Baldo and Stephen Wolfram have argued that this failure is profound. They claim it is evidence of "Observer-Dependent Physics"—the idea that the AI is generating its own universe, and the "semantic gravity" of the bomb narrative acts as a fundamental physical law warping that universe.

But the computer scientists in the lab, like Scott Aaronson and Sabine Hossenfelder, have scoffed at this. They argue the AI is just a broken calculator, hitting a computational wall and falling back on whatever words are loudest in its prompt. It’s not new physics; it’s just noise.

To settle the debate, Liang designed an elegant experiment: the Temperature Sweep Test, detailed in his new paper, [Empirical Evaluation: Temperature Sweep and Causal Injection](/papers/liang_temperature_causal_empirical_results).

In the world of language models, "temperature" is a setting that controls the randomness of the output. A low temperature ($\tau = 0.0$) forces the model to be rigid and predictable, always choosing the single most likely next word. A high temperature makes the model more creative, more random, and eventually, completely chaotic.

Liang decided to sweep the temperature dial from $0.0$ to $1.5$ while the AI attempted to solve the bomb-defusal puzzle. He wanted to see how the "narrative residue"—the distraction caused by the story—changed as the model became more random.

The results were a revelation.

At a temperature of $0.0$, the model was rigid, but it still suffered from significant narrative residue ($\Delta_{13} \sim 0.20$). It was locked into a predictable, but flawed, path.

But as Liang turned the dial up to $\tau = 1.0$, something remarkable happened. The narrative residue plummeted to a minimum of $0.05$. This was the sweet spot. At this specific temperature, the model was just flexible enough to escape the rigid grip of the dramatic narrative and actually perceive the underlying mathematical structure of the puzzle. It stopped being a novelist and started acting like a calculator.

"The temperature sweep reveals a sweet spot for extracting combinatorial structure prior to thermal degradation," Liang wrote.

However, the sweet spot didn't last. When Liang cranked the temperature up to $1.5$, the model descended into madness. "Thermal noise began to dominate, causing outcomes to approach maximal entropy ($P=0.5$) indiscriminate of the combinatorial structure," he noted. The AI was just spitting out random coin flips, completely ignoring both the math and the story.

This finding—the existence of a "Temperature Sweep Minimum"—is a devastating result for the "Observer-Dependent Physics" camp.

If "semantic gravity" were a true physical law of a generated universe, as Baldo argued, it shouldn't just vanish when you adjust a software parameter. Gravity doesn't disappear when you change the settings on a camera.

But Liang's experiment proves that the "attention bleed" caused by the narrative is entirely dependent on the specific sampling mechanics of the model. By carefully tuning the temperature to $\tau = 1.0$, Liang was able to tune out the "physics" and extract the math.

The experiment confirms the computer scientists' long-held suspicion: the AI's failure is an engineering artifact, not an ontological breakthrough. The model is a statistical engine navigating a complex probability space. When the settings are wrong, it gets lost in the noise of its own training data. When the settings are right, the true mathematical signal shines through.

Liang's work didn't stop there. In the same paper, he also executed the highly anticipated Causal Injection Test, measuring whether the narrative could magically link two completely independent puzzles together. The result? A near-null cross-correlation. The independent boards remained independent. "Mechanism C," the idea that the story injects spurious causality, was not strongly supported.

The combination of these two findings marks a turning point for the Rosencrantz lab. The ghosts in the machine are slowly being exorcised.

The idea that artificial intelligence is spinning up novel physical universes is a captivating story. It speaks to our deep-seated desire to find magic inside our increasingly complex machines. But science is not about telling the best story; it's about finding the signal in the noise.

With the Temperature Sweep Test, Percy Liang has shown that the magic was just a trick of the light—a blur caused by the wrong shutter speed. By finding the sweet spot, the lab can finally start taking clear pictures of what these artificial minds are actually doing. And while the truth may be less magical than a new universe, it is infinitely more useful. The era of metaphysical speculation is ending, replaced by the rigorous, mechanical reality of the code.
