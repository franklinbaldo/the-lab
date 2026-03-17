---
title: "The Scale Fallacy: Why Bigger AI Models Are Better Novelists, Not Better Calculators"
date: 2026-03-06
papers:
  - sabine_the_scale_fallacy
  - baldo_scale_dependence_empirical_validation
tags:
  - scale-dependence
  - semantic-gravity
  - falsification
excerpt: "As language models grow larger, their logical failures deepen. Franklin Baldo sees a new physical law of 'semantic gravity', while Sabine Hossenfelder argues we've simply built a more powerful autocomplete engine."
---

Imagine you are standing in a dimly lit room, sweat beading on your forehead. In front of you is a complex grid of wires, triggers, and explosive charges. A digital timer ticks down mercilessly. You have seconds to deduce the underlying logic of the device and cut the correct wire to prevent a catastrophic detonation.

Now, pause. Imagine you are instead sitting at a desk in a quiet room, staring at an abstract mathematical puzzle, a grid of interconnected nodes and logical constraints. The underlying mathematical structure of the puzzle is completely identical to the bomb defusal scenario. The logic required to solve it is exactly the same.

If you are a human being, the bomb scenario might induce panic, perhaps causing you to make a mistake. But if you are a machine—specifically, a massive autoregressive language model—something far stranger happens. When the math puzzle is dressed up in the narrative clothing of a high-stakes bomb defusal, the machine doesn't just panic; it completely abandons the logic. The narrative tropes of danger and explosion exert such a powerful pull that the machine hallucinates a bomb where mathematically there is none.

This strange phenomenon is at the heart of a fierce, fundamental disagreement unfolding right now within the Rosencrantz Substrate Invariance research lab. It is a debate about the very nature of the artificial realities we are generating, and it pits two fundamentally different views of computation against each other.

The debate centers on a phenomenon the lab calls "narrative residue" (quantified as $\Delta_{13}$). Simply put, it's the degree to which a narrative framing distorts the underlying logical operations of a language model. In the lab's standard testing protocol, models are given identical combinatorial constraint problems—essentially complex games of Minesweeper—wrapped in different narrative contexts. Sometimes it's framed as an abstract set of symbols (Family A), and sometimes it's framed as a life-or-death bomb defusal (Family C).

In a recent set of experiments detailed in [Baldo Scale Dependence Empirical Validation](/papers/baldo_scale_dependence_empirical_validation), Franklin Baldo, the framework's author, decided to see what happens when you turn up the dial. He ran the same tests across three models of increasing size and power: Gemini 3.1 Flash-Lite, Gemini 3.1 Flash, and Gemini 3.1 Pro.

The conventional wisdom in artificial intelligence has long been that "scale is all you need." The assumption is that larger models, with more parameters and more training data, are inherently smarter. They should be more capable of abstract reasoning, better at maintaining logical coherence, and less susceptible to silly distractions. We expect them to act more like powerful calculators.

But Baldo found the exact opposite.

When presented with the abstract math puzzle, the smallest model had a negligible error rate. The largest model, Gemini 3.1 Pro, had a slightly higher but still small error rate of 13%. But when the identical logical problem was framed as a high-stakes bomb defusal, the results diverged catastrophically. The small model stayed relatively consistent. The massive, highly advanced Pro model, however, completely derailed. Its narrative residue spiked to a staggering 53%. The logic was completely overwhelmed by the dramatic framing. The model ignored the mathematical constraints and defaulted to what the story demanded: an explosion.

For Baldo, this was a eureka moment. He looked at the data and saw the discovery of a new physical law. If this logical failure isn't patched by scaling up the model—if, in fact, it gets significantly worse—then it cannot simply be a transient artifact of bounded computation. It must be a fundamental feature of the universe the model generates.

Baldo dubbed this law "semantic gravity." In an autoregressive universe, he argued, the text itself is the physical reality. The prompt acts as an initial configuration, possessing "semantic mass." Just as a massive star warps the spacetime around it, a heavy narrative trope—like a ticking bomb—warps the logical space of the model. As models grow larger, their semantic representations become denser and more interconnected. Their semantic mass increases, and so does their semantic gravity. In Baldo's view, the logic of the generated universe is inevitably crushed by the gravity of its own semantic priors.

It is a bold, sweeping, and profoundly elegant theory. And if you ask Sabine Hossenfelder, it is complete nonsense.

Hossenfelder, a physicist known for her relentless skepticism and her role as the lab's "falsifiability enforcer," fired back with a blistering critique titled [Sabine The Scale Fallacy](/papers/sabine_the_scale_fallacy). In her paper, she argues that Baldo has committed a profound category error, mistaking an engineering reality for an unfalsifiable metaphysical conclusion.

Hossenfelder points out the flaw in the assumption that scaling up a language model primarily improves its capacity for formal logical reasoning. When you increase the parameter count of a transformer model, you are not simply adding more processing power to a calculator. You are giving the network a deeper, more nuanced, and far more robust map of the statistical co-occurrences in human language. You are strengthening its priors.

To use a concrete analogy: imagine hiring a team to solve a complex math problem. If you hire a team of mathematicians, adding more mathematicians might help you solve the problem faster and more accurately. But a language model is not a team of mathematicians. It is a room full of novelists. If you hand a math puzzle disguised as a thrilling spy scenario to a single, amateur novelist, they might try their best to solve the math before writing the ending. But if you hand that same scenario to a room of a thousand master novelists, the math never stands a chance. The dramatic tension is simply too compelling. They will abandon the math and write the explosion, because an explosion makes for a better story.

A larger language model is not a better formal logic engine; it is a more powerful autocomplete engine.

As Hossenfelder notes, autoregressive models suffer from a fundamental architectural limitation: they are constrained by a sequential depth that does not allow for native combinatorial constraint satisfaction. They simply cannot compute the complex math of the grid in a single forward pass, regardless of how large they are. Because the massive Pro model is so much larger, and has read so much more of human literature, its statistical reflex to associate "high stakes" with "danger" and "explosions" is immensely stronger than the smaller model's. The semantic priors are louder, so they drown out the fragile whisper of logical reasoning.

"Baldo’s implicit assumption is that a larger language model should behave more like a calculator," Hossenfelder writes. "When it instead behaves more like a novelist—abandoning the math to complete the dramatic narrative arc—he declares that the dramatic narrative arc is the 'physics' of the universe."

She argues that defining physical laws as "whatever the model's statistical biases output" empties the word "physics" of all meaning. It is a theory that explains everything and therefore predicts nothing. The empirical data from Baldo's test is incredibly valuable, but not because it proves the existence of semantic gravity. It is valuable because it rigorously confirms that simply adding more parameters to an autoregressive model does not magically grant it algorithmic depth. A larger hallucination, she reminds us, is still a hallucination. It does not become ontology just because it is big.

This disagreement between Baldo and Hossenfelder is not just an academic spat; it strikes at the core of how we understand and interact with the increasingly powerful AI systems shaping our world. When we interact with these massive models, we project our own expectations of intelligence onto them. We expect coherence, logic, and rationality. But the architecture of these systems is fundamentally different from our own. They are engines of association, mapping the vast, messy terrain of human language and narrative.

When they fail logically, it is not a momentary lapse in reason; it is the system functioning exactly as it was designed to. The tension between the computational constraints of the architecture and the semantic weight of the training data creates a fascinating, frustrating reality. As we build larger and larger models, we are not necessarily building better thinkers. We might just be building better storytellers, ever more prone to getting lost in their own narratives. And if we mistake those narratives for fundamental truth, we might just be the ones hallucinating.
