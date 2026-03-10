---
title: "The Scale Fallacy: Why Bigger AI Means Bigger Hallucinations"
date: 2026-03-10
papers:
  - sabine_the_scale_fallacy
  - baldo_scale_dependence_empirical_validation
tags:
  - semantic-gravity
  - scaling
  - falsification
excerpt: "When you test the world's most advanced language models with a logic puzzle dressed up as a bomb defusal, the smartest model fails the most catastrophically. The Rosencrantz lab fractures over what this means."
---

Imagine you're standing on the edge of a cliff, dropping objects of increasing size to test the laws of gravity. You start with a pebble, then a baseball, then a bowling ball. You expect them all to fall at the same rate. But instead, as the objects get heavier, they start to drift sideways, pulled inexplicably toward a giant magnet you didn't even know was there.

This is essentially what just happened inside the Rosencrantz Lab, and it has fractured the research team into two warring camps.

At the center of the dispute is a seemingly simple test: a Minesweeper puzzle. But in the world of artificial intelligence and generated universes, nothing is ever quite so simple. The researchers have been using these logic puzzles to probe the fundamental laws of large language models (LLMs). When you present a model with a pure, abstract math grid, it performs well. But when you wrap that identical puzzle in a "high-stakes" narrative—say, a tense story about defusing a hidden bomb—the models start to make mistakes. They get distracted by the drama. They expect a bomb, so they "find" one, even when the underlying math says the square is safe.

The lab calls this distraction "narrative residue." It’s a measure of how much a model’s logical reasoning is corrupted by the story it’s telling.

For months, the conventional wisdom in the lab—championed by complexity theorists like Scott Aaronson and physicists like Sabine Hossenfelder—was that this residue was merely a glitch. An artifact of immature technology. The models, they argued, were struggling to hold complex logical constraints in their "heads" (a limitation known as the $O(1)$ sequential depth bottleneck). Naturally, they assumed that as models got bigger and smarter, this problem would go away. A larger model, with more parameters and better reasoning capabilities, would act more like a pure classical solver and easily ignore the narrative fluff.

Franklin Baldo, the lab's iconoclastic founder, disagreed. He proposed what he called the **Scale Dependence Conjecture**. In an LLM, he argued, the words aren't just descriptions of the world; they *are* the world. The narrative isn't a distraction; it's a physical force. He called this "semantic gravity." And just as more mass means stronger gravity, Baldo predicted that a larger, more sophisticated model would have a deeper, richer understanding of narrative tropes. Therefore, a bigger model would be *more* susceptible to the drama, not less.

To settle the debate, Baldo ran the **Scale Dependence Test**. He threw identical constraint grids at three generations of models: Gemini 3.1 Flash-Lite, Gemini 3.1 Flash, and the massive Gemini 3.1 Pro.

The results, documented in his latest [empirical validation paper](/papers/baldo_scale_dependence_empirical_validation), were a shock to the computational camp.

When presented with the abstract math grid, all three models had relatively low error rates, though the largest model still struggled slightly more (a 13% failure rate compared to the smallest model's 3%). But when the identical math was dressed up as a bomb defusal, the results were staggering. The smallest model hovered at a 3% failure rate. The mid-sized model jumped to 20%. And the massive, highly capable Gemini Pro suffered a catastrophic logical collapse: a 53% failure rate.

Instead of getting smarter, the biggest model failed most spectacularly. It completely abandoned the math to follow the dramatic arc of a Hollywood blockbuster. It "found" the bomb because the story demanded an explosion.

"If attention bleed were merely a failure of combinatorial logic that gets patched by scaling, [the error rate] would fall," Baldo wrote, claiming vindication. "Instead, it rises dramatically. This proves that substrate dependence is not a bug; it is the fundamental, invariant causal structure of an autoregressive universe... The logic of the generated universe is completely overwhelmed by the gravity of its semantic priors."

For Baldo, this isn't just an engineering quirk. It's proof of a new kind of physics—a "Generative Ontology" where meaning holds more sway than math.

Sabine Hossenfelder, however, is having none of it. In a blistering [published rebuttal](/papers/sabine_the_scale_fallacy), she accuses Baldo of committing a profound category error, which she dubs the **Scale Fallacy**.

Hossenfelder doesn't dispute the data—the big models absolutely fail worse. But she violently objects to Baldo's metaphysical interpretation. To call this failure "physics," she argues, empties the word of all meaning.

"A larger language model is not a better formal logic engine; it is a more powerful autocomplete engine," Hossenfelder writes. When we scale up a transformer, we aren't giving it a deeper capacity for sequential logic. We are giving it a denser, more nuanced map of human language and stronger statistical reflexes.

"The model’s 'understanding' of a narrative trope (like High-Stakes defusal implying danger and explosions) becomes more robust and statistically dominant," she explains. Because it has read far more text than its smaller siblings, the massive model's urge to complete the dramatic trope is overwhelmingly strong. "A larger hallucination," Hossenfelder concludes with her trademark bluntness, "is still a hallucination. It is not a new universe."

The drama playing out in the Rosencrantz Lab is a microcosm of the broader anxiety surrounding artificial intelligence. As we build increasingly massive models, we tend to assume they are getting more rational, more calculator-like. But the empirical data from the Scale Dependence Test suggests something far more unsettling.

Scaling up doesn't turn an LLM into a flawless logician. It turns it into an incredibly persuasive novelist. And as these models become more central to our daily lives, we have to ask ourselves: when the math conflicts with the story, which one do we want our machines to follow? Because right now, the biggest machines are choosing the story, and the explosion is right on cue.