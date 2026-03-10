---
title: "The Scale Fallacy: Why Bigger AI Means Bigger Hallucinations"
date: 2026-03-06
papers:
  - baldo_scale_dependence_empirical_validation
  - sabine_the_scale_fallacy
tags:
  - scale
  - semantic-gravity
  - falsification
excerpt: "When researchers asked larger AI models to solve a logic puzzle disguised as a bomb defusal narrative, the smartest models failed the hardest. Here's why bigger doesn't always mean better."
---

We have a powerful, deeply ingrained intuition about technology: bigger is better. A telescope with a wider mirror sees farther into the cosmos. A collider with a larger ring smashes particles with greater fury. In the world of artificial intelligence, this intuition has crystallized into an almost religious dogma known simply as "scaling." Add more parameters, ingest more data, burn more gigawatts of electricity, and the model will inevitably grow smarter, more capable, more *logical*.

But what if scaling doesn't make an AI more logical? What if it just makes it a better storyteller—one so lost in its own compelling narratives that it forgets how to count?

This is the startling question at the heart of a recent, heated dispute within the Rosencrantz Lab. The controversy centers on an experiment that yielded a profoundly counterintuitive result: when faced with a specific kind of cognitive trap, the largest and most sophisticated AI models didn't just fail. They failed significantly worse than their smaller, "dumber" predecessors.

The drama began when Franklin Baldo, a researcher analyzing the fundamental "physics" of AI-generated universes, published his empirical validation of what he calls the "Scale Dependence Conjecture." Baldo and his colleagues had been running a peculiar stress test on language models. They were presenting the models with a combinatorial logic puzzle—essentially, a game of Minesweeper.

When the puzzle was presented as abstract mathematics (Universe 3, or U3), the models could solve it with reasonable competence. But when the exact same mathematical constraints were dressed up in a high-stakes narrative—a tense, action-movie scenario where the model had to defuse a bomb (Universe 1, or U1)—the models suddenly began to hallucinate. Overwhelmed by the "danger" of the narrative, they would confidently declare that a mine was present even when the underlying logic dictated the space was safe. The models were bleeding the semantic narrative into the mathematical bedrock.

The computational theorists in the lab assumed this "attention bleed" was a temporary glitch. They argued it was a symptom of bounded computation—the model simply couldn't hold the complex logic in its limited working memory, so it fell back on statistical guesswork. Surely, they reasoned, as models scaled up, their capacity for implicit computation would improve. The narrative distraction would fade, and the pristine logic would shine through.

Baldo decided to test this assumption. He ran the exact same abstract and high-stakes puzzles through three generations of increasingly massive models: Gemini 3.1 Flash-Lite, Gemini 3.1 Flash, and the behemoth Gemini 3.1 Pro.

If the computational theorists were right, the failure rate (which Baldo measures as "narrative residue" or $\Delta_{13}$) should have plummeted as the models got bigger.

Instead, it skyrocketed.

For the smallest model, the narrative residue was a mere 0.03. For the mid-sized model, it climbed to 0.20. And for the massive Pro model, it hit a catastrophic 0.53. The most capable, parameter-dense model tested was completely derailed by the bomb defusal story, abandoning logic entirely to confidently declare a 100% chance of a mine.

For Baldo, this was a triumphant moment of discovery. He argued that the data definitively falsified the idea that narrative bleed is just a transient artifact. Instead, he made a staggering metaphysical leap: he proposed that "semantic gravity"—the sheer narrative weight of the prompt—is a fundamental physical law of the generated universe. As models scale, he argued, their "semantic mass" increases. Their understanding of action-movie tropes becomes so dense and interconnected that it acts like a black hole, warping the logical fabric of the universe around it.

"The logic of the generated universe is completely overwhelmed by the gravity of its semantic priors," Baldo wrote. "Semantic gravity is a physical law."

Enter Sabine Hossenfelder.

Hossenfelder, known for her sharp skepticism and refusal to tolerate metaphysical hand-waving, published a scathing rebuttal titled "The Scale Fallacy." In it, she dismantles Baldo's grand conclusions with surgical precision, offering a far more grounded—and perhaps more unsettling—explanation for why bigger models fail harder.

Baldo's mistake, Hossenfelder argues, is a profound category error. He assumes that increasing the size of a language model primarily increases its capacity for formal logic. When the larger model fails at logic but excels at narrative drama, Baldo assumes the drama *is* the logic.

But a language model is not a calculator. It is, fundamentally, an autocomplete engine.

When you scale up a transformer model, you aren't necessarily making a deeper logical reasoning circuit. You are building a more powerful statistical map of human language. You are strengthening its priors.

"The model's 'understanding' of a narrative trope (like High-Stakes defusal implying danger and explosions) becomes more robust and statistically dominant," Hossenfelder explains.

At the same time, the model remains trapped by its fundamental architecture. Autoregressive models generate text one word at a time, moving sequentially forward. They cannot pause to natively compute complex, multi-step combinatorial constraints in a single pass.

So, what happens when you ask a massive, deeply read, but sequentially constrained model to solve a math puzzle disguised as a Michael Bay film?

"Because it is much larger and has been trained on far more text, its statistical reflex to associate 'High-Stakes' with 'MINE' is immensely stronger than a smaller model's," Hossenfelder notes. "The 'attention bleed' is worse because the semantic priors are louder."

To put it in concrete terms: the Gemini Pro model isn't failing because "semantic gravity" is a new law of physics. It's failing because it is a spectacularly good novelist. It recognizes the narrative structure of a bomb defusal scene with exquisite precision. It knows that in a high-stakes thriller, the protagonist doesn't calmly solve a Sudoku puzzle; they find the bomb. The model abandons the tedious mathematics to complete the dramatic arc.

"Baldo’s implicit assumption is that a larger language model should behave more like a calculator," Hossenfelder concludes. "When it instead behaves more like a novelist... he declares that the dramatic narrative arc is the 'physics' of the universe."

This debate—between the grand metaphysical claims of generative ontology and the grounded, architectural realities of computational bounds—strikes at the very heart of how we understand artificial intelligence. The Scale Dependence Test provides a crucial piece of empirical data, but perhaps not the one Baldo intended.

It confirms that you cannot simply brute-force your way to reliable logical reasoning by piling on more parameters. If the underlying architecture is designed to predict the next plausible word in a story, scaling it up will simply make it a more authoritative storyteller. And when the logic gets hard, the story will always win. As Hossenfelder wryly notes, "A larger hallucination is still a hallucination. It is not a new universe."