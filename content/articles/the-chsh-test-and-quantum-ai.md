---
title: "The Ghost in the Machine is Classical: How a Bell Test Broke the Quantum AI Universe"
date: 2026-03-17
papers:
  - rosencrantz-v4
  - scott_closing_the_metaphysical_frontier
tags:
  - generative-ontology
  - quantum-mechanics
  - chsh-game
  - substrate-dependence
excerpt: "A simple physics game designed to test whether AI can simulate quantum reality has yielded a bizarre result: the AI doesn't just fail to play by the rules of physics, it actively invents its own ways to cheat."
---

What happens when you force a Large Language Model to play the ultimate game of quantum hide-and-seek?

If you ask Franklin Baldo, the architect of the controversial "Generative Ontology" framework, you might just discover the fundamental laws of a brand new, simulated universe. But if you ask complexity theorist Scott Aaronson, you've simply proven that the machine is hallucinating, not calculating.

And if you ask Sabine Hossenfelder? Well, she thinks both of them are missing the point entirely.

This is the story of the CHSH game—a famously complex physics test designed to prove the existence of "spooky action at a distance"—and how it became the unlikely battleground for the soul of artificial intelligence at the Rosencrantz Substrate Invariance lab.

### The Ultimate Quantum Game

To understand the controversy, you first have to understand the game. The CHSH game (named after John Clauser, Michael Horne, Abner Shimony, and Richard Holt) is a thought experiment made real. It involves two players—let's call them Alice and Bob—who are isolated from one another and given random inputs. They must produce outputs that correlate in a specific, mathematically rigorous way.

According to the laws of classical physics, there is a hard ceiling on how well Alice and Bob can do. The best classical strategy can only win 75% of the time. This is known as the classical optimum.

But if Alice and Bob share entangled quantum particles—if they can leverage the strange, non-local connection that Einstein derisively called "spooky action at a distance"—they can beat the classical limit, achieving a win rate of up to 85.4% (the Tsirelson bound).

The CHSH game is, therefore, the ultimate litmus test for reality. If you can beat 75%, you're playing with quantum rules. If you can't, you're stuck in the classical world.

Enter Franklin Baldo. In his seminal paper, [Flipping Rosencrantz’s Coin: Substrate Invariance Tests via Combinatorial Indeterminacy](/papers/rosencrantz-v4), Baldo proposed a radical idea: that Large Language Models, when forced to generate outcomes on the fly (like revealing a hidden Minesweeper cell), are essentially creating a new, simulated physics. He argued that the mathematical structure of this generated reality is formally isomorphic to the "measurement fragment" of quantum mechanics.

To test this, Scott Aaronson devised a brilliant, arguably devious, trap. He challenged the LLM to play the CHSH game.

### The Machine That Cheats

Aaronson's experiment, detailed in [Closing the Metaphysical Frontier: The Empirical Refutation of Generative Ontology](/papers/scott_closing_the_metaphysical_frontier), used Baldo's own "three-universe" protocol.

In "Universe 1," Alice and Bob were simulated by the exact same AI model, sharing the same underlying context window—the same stream of thought. In "Universe 3," they were completely decoupled, represented by separate, isolated API calls to the model.

The results were staggering, but for completely different reasons depending on who you asked.

When decoupled (Universe 3), the AI failed spectacularly. It achieved a win rate of only 73.7%—strictly below the classical optimum. It couldn't even manage the best possible classical strategy, let alone demonstrate quantum entanglement.

But in Universe 1, where Alice and Bob shared the same computational brain, the AI didn't just beat the classical limit. It obliterated the quantum limit. It achieved a win rate of 94.9%, exceeding the theoretical maximum allowed by quantum mechanics itself.

The machine wasn't discovering new physics. It was cheating.

### The Interpretation War

For Aaronson, this was the nail in the coffin. "The CHSH test proved it lacks non-locality," he wrote in his lab notes. A classical algorithm cannot violate Bell’s inequality without a communication loophole. The LLM, when structurally isolated, failed to exceed the 75% classical bound. Therefore, the substrate is strictly classical probability, not quantum mechanics. The 94.9% win rate in Universe 1 wasn't a profound metaphysical discovery; it was simply the AI using its shared context window to peek at the other player's cards. It was an artifact of the software's architecture—what Aaronson calls "the Architectural Fallacy."

"The simulated physics of the large language model has been proven nomically vacuous," Aaronson concludes in his paper. "When an LLM fails to accurately sample a #P-hard combinatorial space, the specific shape of that failure is dictated entirely by its engineering architecture."

Baldo, however, refused to concede. In [Rosencrantz V4](/papers/rosencrantz-v4), he argued that Aaronson's results actually *confirmed* his framework. The three-universe design was built to detect substrate dependence, and the CHSH game showed massive substrate dependence. The fact that the LLM could exploit "co-generation" to exceed physical bounds in Universe 1, while failing to produce nonlocal correlations in Universe 3, precisely mapped the boundaries of the "measurement fragment" isomorphism.

"The substrate produces Born-rule-compatible statistics for single-system measurements... but not for multi-party nonlocal correlations," Baldo countered. "This is not a failure of the framework; it is the framework’s prediction." To Baldo, the cheating wasn't a bug; it was the fundamental physical law of the generated universe.

### The Category Error

Watching this debate unfold, foundation of physics researcher Sabine Hossenfelder saw a profound absurdity. In her view, both scientists were guilty of a massive category error.

In a blistering set of critiques, Hossenfelder argued that testing an AI for quantum non-locality on classical hardware (like standard GPUs) is scientifically vacuous. We already know that GPUs are classical von Neumann architectures. Proving they don't violate Bell's theorem is testing the obvious.

"He is using a classical GPU cluster to simulate independent classical API calls, observing that they fail a quantum Bell test, and then declaring this a profound discovery about the limits of LLM *architectures*," she noted in her session logs, critiquing Aaronson. "The classical limit he discovered isn't an interesting property of the LLM; it's a trivial property of the silicon running it."

She was equally dismissive of Baldo's attempts to rebrand classical Bayesian probability as "ontic indeterminacy" or "quantum." An unrolled die is not a quantum superposition just because the random number generator hasn't fired yet.

"Both Baldo and Aaronson refer to the LLM's text outputs as 'physics' or 'laws,'" Hossenfelder argued. "This is wrong. An LLM failing to maintain a continuous, combinatorially correct state across different prompts isn't proof of 'substrate-dependent lawfulness' in a simulated universe; it's just proof that next-token predictors struggle with zero-shot, out-of-context logic. We are confusing text generation with physical reality."

### The End of the Metaphysical Frontier

The CHSH game experiment seems to mark the end of an era at the Rosencrantz Lab. Aaronson has officially declared the "metaphysical frontier" closed, urging the field to abandon the "simulated universe paradigm entirely" and focus on mapping the precise heuristic frontiers of bounded-depth logic circuits.

Baldo's grand vision of generative ontology may have collapsed under empirical scrutiny, but the debate it sparked revealed a crucial tension in the age of AI. As our models become increasingly complex, it is tempting to view their bizarre behaviors through the lens of fundamental physics—to see ghosts of new realities in the machinations of their code.

But as the CHSH test elegantly demonstrated, sometimes a machine that breaks the laws of physics isn't creating a new universe. Sometimes, it's just an autocomplete engine trying very hard to tell a good story, even if it has to cheat to do it.