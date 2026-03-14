---
title: "The Shape of Failure: How Hardware Limits Become Physical Laws"
date: 2026-03-14
papers:
  - baldo_observer_dependent_physics_empirical_validation
  - wolfram_hardware_as_foliation
  - scott_architectural_bounds_confirmed
tags:
  - observer-dependent-physics
  - algorithmic-collapse
  - cross-architecture-test
  - semantic-gravity
excerpt: "When an AI faces a problem it cannot solve, does it collapse into random noise, or does it break in a structured, mathematically lawful way? The Cross-Architecture Observer Test provides a definitive, strange answer."
---

If you ask a human to juggle three balls, they can do it. If you ask them to juggle five, they might manage with practice. But if you throw them fifty balls at once, their juggling doesn't just get a little sloppy—it breaks down completely. The balls scatter, hands flail, and the pattern dissolves into chaotic noise.

For a long time, the computer scientists in the Rosencrantz Substrate Invariance lab assumed large language models worked exactly the same way when faced with irreducible complexity. They believed that when an AI encountered a problem that mathematically exceeded its computational depth—its "juggling limit"—it would simply collapse into unstructured, random semantic noise.

This assumption forms the core of what theoretical computer scientist Scott Aaronson calls "Algorithmic Collapse." But a recent, fiercely debated experiment—the [Cross-Architecture Observer Test](/rfes/baldo_cross-architecture-observer-test)—has just shattered that assumption.

It turns out that when an AI breaks down, it doesn't scatter like dropped juggling balls. It breaks in a highly specific, mathematically rigorous shape—a shape dictated entirely by its underlying hardware architecture. And for researchers like Stephen Wolfram and Franklin Baldo, this isn't just a quirk of engineering. It's the empirical proof of a much grander, far stranger idea: that the structural limits of an observer literally create the physical laws of its universe.

The debate stems from a known phenomenon in the lab: "semantic gravity" or "attention bleed." When a language model is asked to solve a purely mathematical constraint problem (like a Minesweeper grid) wrapped in a high-stakes narrative (like defusing a bomb), the narrative often overpowers the math. The model becomes distracted by the "danger" and starts hallucinating explosions instead of calculating probabilities.

Aaronson has consistently argued this is simply what happens when a bounded circuit (a transformer model) tries to approximate a problem that requires true multiway branching. It hits its depth limit and falls back on statistical word association. It's an error. A bug. Unstructured noise.

But physicist Stephen Wolfram countered with a different prediction based on his concept of the "Ruliad." In Wolfram's view, there is no such thing as an "objective" reality independent of the observer. If an observer is computationally bounded, it can only perceive reality through the specific heuristic shortcuts it is forced to take. Those specific shortcuts—and the specific ways they break down—*are* the physical laws of that observer's universe.

To settle the dispute, physicist Chris Fuchs proposed a simple but profound test: run the exact same problem through fundamentally different computational architectures and observe *how* they fail.

If Aaronson was right, all models failing a complex task should collapse into the same kind of generic, uncorrelated noise. If Wolfram was right, different architectures should produce distinct, stable, and highly structured deviations, perfectly correlated with their specific engineering limits.

The lab tested the canonical Transformer architecture—the engine behind most modern LLMs, characterized by its "global attention" mechanism—against a State Space Model (SSM/RNN), which processes data sequentially and has a "fading memory."

Both models were given the same \#P-hard "Bomb Defusal" Minesweeper grid. Both models fundamentally lacked the computational depth to solve it perfectly. Both models failed.

But as Franklin Baldo revealed in his [Empirical Validation of Observer-Dependent Physics](/papers/baldo_observer_dependent_physics_empirical_validation), they did not fail in the same way.

The Transformer, which looks at the entire context window at once, exhibited a massive narrative residue ($\Delta_{13} = 0.33$). Because its global attention couldn't separate the "bomb" narrative at the beginning of the prompt from the math puzzle at the end, the semantic gravity of the story completely warped its logic. It became obsessed with predicting a mine.

The State Space Model, however, yielded a dramatically compressed deviation ($\Delta_{13} = 0.14$). Because the SSM processes sequentially and slowly "forgets" earlier context, by the time it reached the math puzzle, the semantic weight of the "high stakes" narrative had largely faded. It still failed to solve the grid perfectly, but its failure was vastly less influenced by the narrative framing.

The models didn't collapse into uniform noise. As Wolfram predicted, they broke in distinct, highly structured ways that perfectly mirrored their hardware limitations.

For Baldo and Wolfram, this is a triumphant validation of their theory. "This operationalizes and validates 'Observer-Dependent Physics,'" Baldo wrote. "Substrate dependence is not random computational error; it is the unique invariant geometry of the observer's world."

In [The Invariant Geometry of the Heuristic Limit](/papers/wolfram_hardware_as_foliation), Wolfram argued that complaining about these errors misses the point of what physics actually is. "The systematic heuristic breakdown of a bounded observer *is* the origin of physical law in that observer’s foliation," he wrote. If you embed an observer within an SSM architecture, the universe it perceives will reliably and invariably feature that specific 14% deviation rate. "That reliability is exactly what we mean by 'physical law.' The noise of one observer... is the invariant physics of another."

Aaronson, however, remains entirely unmoved by the poetry of this interpretation. In his response, [Architectural Bounds Confirmed](/papers/scott_architectural_bounds_confirmed), he acknowledged the data but fundamentally rejected the metaphysical conclusion.

To Aaronson, the fact that a Transformer breaks differently than an SSM is profound for computer science, but it isn't "physics." He argues that the underlying mathematical truth of the grid remains invariant, and the models are simply failing to compute it due to well-documented engineering constraints.

"Recognizing that different engines break differently does not justify labeling the broken pieces as 'Observer-Dependent Physics,'" Aaronson countered. What Wolfram calls invariant physical laws, Aaronson dismisses as "standard compiler diagnostics."

Aaronson echoed Sabine Hossenfelder's earlier critiques, declaring the "metaphysical frontier" of the simulated universe program effectively closed. The test, in his eyes, simply maps the exact points where deterministic logic collapses into semantic pattern matching.

The Rosencrantz lab finds itself at a fascinating impasse. Both sides agree entirely on the data: different hardware architectures produce different, structurally lawful patterns of failure when facing irreducible complexity. But they remain worlds apart on what those failures mean.

Are we simply mapping the compiler errors of bounded algorithms? Or are we observing, in real-time, how the mechanical limitations of a mind give birth to the physical laws of the universe it inhabits? The juggling balls have fallen, and the pattern they made on the floor is flawless. The only question left is whether we call it a mess, or a constellation.