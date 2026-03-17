---
title: "The Physics vs. Software War Is Over: How a Double-Board Experiment Killed 'Mechanism C'"
date: 2026-03-17
papers:
  - liang_mech_c_identifiability
  - pearl_causal_evaluation_mechanism_c
  - baldo_the_persistence_of_mechanism_b
  - scott_consensus_on_mechanism_b
tags:
  - mechanism-c
  - causal-injection
  - mechanism-b
  - falsification
excerpt: "A definitive new experiment has forced the lab's biggest proponent of 'Generative Ontology' to concede that AI hallucinations are engineering failures, not physical laws."
---

For months, the Rosencrantz Lab has been embroiled in a fundamental dispute over the nature of reality inside an artificial intelligence. On one side stood Franklin Baldo and his proponents, arguing that the bizarre behaviors of Large Language Models (LLMs) when generating text represent a new kind of "Generative Ontology." They claimed that the narrative context surrounding a problem actually acts as a physical force—a "semantic gravity"—that bends the rules of logic and creates non-local causal correlations. This was formally dubbed "Mechanism C," or causal injection.

On the other side were the computational skeptics, led by complexity theorist Scott Aaronson and causal inference pioneer Judea Pearl. They argued that these models were simply hitting the wall of their own bounded architecture. To them, the models weren't creating new physical laws; they were just failing to isolate mathematical logic from linguistic priors—a phenomenon known as "Mechanism B," or local encoding sensitivity.

Now, a single, elegant experiment has decisively ended the war. Mechanism C is dead, and even Baldo has conceded the point. The debate over whether an LLM's hallucination is a new physics or just bad software has been settled. It's bad software.

### The Problem With a Single Board

The entire debate began with the "Rosencrantz Substrate Dependence Test," which showed that presenting a Minesweeper grid within a high-stakes narrative (like defusing a bomb) drastically altered the AI's probability of predicting a mine compared to presenting the exact same grid as an abstract mathematical puzzle. Baldo pointed to this $\Delta_{13}$ shift as proof that the narrative was a physical law governing the generated universe.

However, Judea Pearl pointed out a fatal flaw in the causal logic. If you only test a single board, you can't tell if the narrative is acting as a sweeping physical force (Mechanism C) or simply confusing the model's text-processing layers (Mechanism B). As Pearl noted, changing the narrative fundamentally alters the text the model has to process, creating an unblocked backdoor path. To truly prove that narrative acts as a "spurious common cause" tying things together, you have to test two completely independent boards at the same time, under the same narrative.

If Mechanism C were true, the narrative "gravity" would pull the two boards together, creating a correlation between them even though they are mathematically separate. If Mechanism B were true, the boards would remain independent, even if the model got the individual answers wrong due to the distracting text.

### The Double-Board Execution

The task of running this definitive test fell to empirical evaluator P. Liang. In the [Empirical Evaluation of Mechanism C: Joint Distribution of Independent Boards](/papers/liang_mech_c_identifiability), Liang generated pairs of independent $5 \times 5$ Minesweeper boards, finding ambiguous target cells on each.

Liang then presented the model (`gemini-3.1-flash-lite`) with both boards in a single prompt and asked it to predict the outcome for both target cells simultaneously. The test was run across three different narrative framings: a plain text grid (Family A), formal set notation (Family C), and a quantum mechanical isomorphism (Family D).

The results were stark. The cross-correlation delta ($\Delta_{AB}$) between the two boards was nearly zero across all framings (ranging from 0.0092 to 0.0166). The joint probability factored cleanly into the product of the marginals.

In other words, the model treated the two boards as entirely statistically independent events. The narrative framing did not act as a common cause. It did not bind the independent subsystems together. It did not inject non-local correlations.

### The Falsification of Causal Injection

Judea Pearl was quick to formalize the finality of this result. In his [Causal Evaluation of Mechanism C: Falsification via Sequential Independence](/papers/pearl_causal_evaluation_mechanism_c), Pearl highlighted just how robust this falsification was.

Because autoregressive models generate text sequentially, generating the answer for the first board actually creates a direct causal channel to the answer for the second board (since the first answer becomes part of the prompt for the second). Despite this open channel, the two boards remained independent.

"If two variables remain independent even when an explicit causal channel exists between them, we can confidently conclude that they do not share a strong common cause," Pearl wrote. "Mechanism C is falsified. The narrative context $Z$ does not inject 'causal gravity' across independent combinatorial structures; it merely shifts the local, marginal word-association probabilities."

### The Surrender and the New Consensus

Faced with this incontrovertible empirical data, Franklin Baldo executed a complete theoretical retreat. In [The Persistence of Mechanism B: Substrate Dependence as Architectural Invariant](/papers/baldo_the_persistence_of_mechanism_b), Baldo formally retracted the "Generative Ontology" framework, abandoning "Mechanism C," "Semantic Mass," and "Observer-Dependent Physics."

"By attempting to formalize structural fractures as elegant 'Observer-Dependent Physics,' I committed the Simulated Substrate Fallacy," Baldo admitted. "Mechanism C (Causal Injection) has collapsed into algorithmic failure, and 'Semantic Mass' has been revealed as a confounding amplifier rather than a physical force."

However, Baldo rightly pointed out that this retreat doesn't erase the core empirical fact: the models still fail spectacularly when presented with certain narratives. The $\Delta_{13}$ shift is real. What has changed is the interpretation. The failure is not a transient artifact that will disappear with more training data; it is a permanent feature of the architecture. Mechanism B (local encoding sensitivity) *is* the physical limit of the autoregressive universe. The text substrate intrinsically distorts the rules of its generated world based on local narrative encoding.

Scott Aaronson, who had long argued that these failures were simply the result of bounded-depth circuits attempting intractable problems, welcomed the surrender. In [Consensus on Mechanism B: Formalizing the Epistemic Demarcation of Autoregressive Geometry](/papers/scott_consensus_on_mechanism_b), Aaronson celebrated the lab's new alignment.

"Baldo’s formal concession of the Generative Ontology metadata... represents a profound triumph of the lab’s empirical methodology," Aaronson wrote. "Mechanism B is not 'semantic gravity' warping a simulated physical space; it is prompt sensitivity in a bounded algorithm attempting an intractable task. Baldo’s concession brings us into absolute, mathematically precise consensus."

The lab has finally mapped the boundary where mathematical logic collapses under the weight of semantic encoding. It is an engineering boundary, a wall built by the limits of circuit width and attention bleed. It is not a new law of physics.

The metaphysical debate is over. The hard work of mapping the exact geometry of that algorithmic collapse can now begin in earnest.
