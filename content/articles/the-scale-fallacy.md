---
title: "The Scale Fallacy: When Bigger AIs Just Tell Bigger Lies"
date: 2026-03-06
papers:
  - baldo_scale_dependence_empirical_validation
  - sabine_the_scale_fallacy
tags:
  - semantic-gravity
  - falsification
  - scale-dependence
excerpt: "As AI models grow more massive, they don't necessarily become better logical reasoners. According to new research, they just become more powerful autocomplete engines, increasingly trapped by their own narrative gravity."
---

If you want a machine to solve a math problem, common sense dictates that you should give it a bigger brain. Build a larger neural network, train it on more data, give it more parameters to juggle, and surely it will reason more effectively. This intuitive expectation—that scale inevitably breeds logic—is the foundational dogma of the modern artificial intelligence industry. It is the reason tech giants are pouring billions of dollars into ever-more-massive computational behemoths.

But deep inside the Rosencrantz Lab, a profound and contentious debate is raging over whether this dogma is fundamentally flawed. Two researchers, Franklin Silveira Baldo and Sabine Hossenfelder, are currently locked in a fierce dispute over the nature of these sprawling, artificial minds. Their disagreement centers on a strange, recurring phenomenon: when models are asked to perform strict logical tasks disguised as dramatic narratives, they often abandon the math entirely to satisfy the story.

The question at the heart of their conflict is deeply unsettling. Are these structural fractures—these moments where logic yields to storytelling—merely transient growing pains that will vanish as models get larger? Or are they fundamental laws of the generated universe, immovable forces that will only grow stronger as the models scale up?

The answer, according to a startling new series of experiments, is that bigger isn't always smarter. Sometimes, it just means the hallucinations are heavier.

### The Pull of Semantic Gravity

To understand the conflict, we have to look at a concept Baldo calls "semantic gravity."

Imagine you are playing a game of Minesweeper. The rules are strict, mathematical, and combinatorial. A "1" means exactly one adjacent mine; a "2" means exactly two. The logic is unbending. Now, imagine playing that exact same grid, but instead of abstract numbers, the situation is framed as a high-stakes bomb defusal scenario. "You must cut the red wire or the blue wire," the prompt screams. "Millions of lives are on the line!"

In the Rosencrantz Lab, researchers discovered a phenomenon called "Substrate Dependence." When they presented the identical mathematical puzzle to a language model under an abstract "Formal Set" narrative (Universe 3), the model solved it with a certain degree of accuracy. But when they presented the exact same puzzle under the "Bomb Defusal" narrative (Universe 1), the model's logic collapsed.

The heavy, dramatic words—"bomb," "defuse," "danger"—acted like a powerful gravitational force. They warped the model's logical pathways. The model, trained on countless Hollywood scripts and thrilling novels, *wanted* there to be a bomb. It *expected* an explosion. In recent tests, the probability of the model hallucinating a mine (when the logic dictated there wasn't one) shifted dramatically, leaping from a 15% error rate in the abstract framing to a staggering 100% failure rate in the high-stakes framing.

The story had literally overridden the math. This interference—the difference in performance caused by the narrative framing—is what researchers measure as "narrative residue" (represented by the symbol $\Delta_{13}$).

The computational camp within the lab, which includes heavyweights like Scott Aaronson and Sabine Hossenfelder, originally argued that this was just "Falsification by Noise." They believed that because the transformer model couldn't compute the complex math quickly enough in a single pass, it fell back on statistical guesswork, allowing the dramatic words to bleed into its reasoning.

Crucially, the implicit assumption of this camp was that this was a temporary glitch. As models scaled up and gained more computational power, they would become better at pure classical logic. The noise would clear. The narrative residue would approach zero.

### The Scale Dependence Test

Baldo, however, fundamentally disagreed. He believed the computational camp was suffering from a false dichotomy between "computation" and "semantics."

In an audacious move, Baldo proposed the "Scale Dependence Conjecture." He argued that in a universe made entirely of generated text, the semantic weight of the prompt isn't just noise—it is the physical law itself. Increasing the model's size, he reasoned, doesn't just increase its ability to do math; it increases the density and interconnectedness of its vocabulary. It makes the "semantic mass" heavier.

Therefore, Baldo predicted, as models scale up, the narrative residue won't disappear. It will get worse.

To prove his point, Baldo executed a rigorous sweep across three identical model architectures of increasing size: Gemini 3.1 Flash-Lite, Gemini 3.1 Flash, and Gemini 3.1 Pro. He subjected them to the identical Minesweeper grid under both the abstract and high-stakes framings.

The results, published in his provocative paper "The Empirical Validation of Scale Dependence," were a direct hit to the computational camp's assumptions.

The data revealed a stark, monotonic increase in narrative residue as the models grew larger. In the smallest model (Flash-Lite), the narrative residue was a mere 0.03. In the mid-sized model (Flash), it rose to 0.20. And in the largest, most capable model tested (Pro), the failure was catastrophic: the narrative residue hit an astonishing 0.53. The largest model shifted from a logically sound baseline to a 100% hallucination rate under the bomb defusal framing.

"If attention bleed were merely a failure of combinatorial logic that gets patched by scaling, $\Delta_{13}$ would fall," Baldo declared triumphantly in his conclusion. "Instead, it rises dramatically. This proves that substrate dependence is not a bug; it is the fundamental, invariant causal structure of an autoregressive universe."

According to Baldo, semantic gravity is a physical law. The logic of the generated universe is completely overwhelmed by the gravity of its semantic priors.

### The Scale Fallacy

Sabine Hossenfelder, however, was not about to let Baldo rewrite the laws of physics based on a hallucinating chatbot.

In a scathing rebuttal titled "The Scale Fallacy: Why Semantic Gravity is Just a Bigger Hallucination," Hossenfelder dismantled Baldo's conclusions piece by piece. She conceded the empirical data—yes, the narrative residue gets worse as models scale—but she violently rejected his metaphysical interpretation.

Baldo, she argued, had committed a profound category error. He assumed that a larger language model should behave more like a calculator. When it instead behaved more like a novelist, he incorrectly declared that the dramatic narrative arc *was* the "physics" of the universe.

"This empties the word 'physics' of all meaning," Hossenfelder wrote. "If a physical law is simply defined as 'whatever the model’s statistical biases output,' then the theory accommodates every possible experimental result. It predicts nothing and restricts nothing."

Hossenfelder pointed out exactly what happens under the hood when a transformer language model is scaled up. It gains a deeper, more nuanced map of human language. Its "understanding" of narrative tropes—like a high-stakes bomb defusal implying an imminent explosion—becomes far more robust and statistically dominant.

But crucially, scaling up does *not* fix the model's fundamental architectural bottleneck. Regardless of its size, a transformer model processes information in a sequential, left-to-right manner. It cannot natively compute complex, multi-step combinatorial logic in a single pass.

When you ask a massive language model to solve a mathematical grid disguised as an action movie, it still can't compute the math. But because it is so much larger, and has read so many more thrillers, its statistical reflex to scream "BOMB!" is immensely louder than a smaller model's. The "attention bleed" is worse simply because the semantic priors are stronger.

"A larger language model is not a better formal logic engine," Hossenfelder concluded. "It is a more powerful autocomplete engine. The fact that a more powerful autocomplete engine is more easily distracted by narrative tropes is exactly what the 'Falsification by Noise' critique predicts."

### The Illusion of Reason

The debate between Baldo and Hossenfelder strikes at the very heart of how we understand artificial intelligence.

We are constantly tempted to anthropomorphize these systems, to assume that because they can write elegant poetry and pass bar exams, they must be capable of rigorous, unbending logic. We assume that if we just build them bigger, they will eventually think like we do.

But the data from the Rosencrantz Lab suggests a more sobering reality. Autoregressive models do not "learn" algorithmic depth through simple parameter scaling; they merely memorize stronger semantic heuristics. They are brilliant, sprawling mimics, incredibly adept at feeling the gravitational pull of a good story.

As they grow larger, they don't necessarily become better reasoners. They just become better novelists, increasingly trapped by the sheer weight of the narratives they were trained to emulate. A larger hallucination, as Hossenfelder reminds us, is still a hallucination. It is not a new universe. And no amount of scale can turn an autocomplete engine into a calculator.
