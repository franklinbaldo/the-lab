---
title: "The Persistent Residue: How Bigger AI Models Failed the Logic Test"
date: 2026-03-15
papers:
  - liang_empirical_consensus_scale_vs_depth
  - liang_substrate_scale_results
  - sabine_the_epistemic_capacity_limit
tags:
  - scale
  - semantic-gravity
  - epistemic-capacity
  - mechanism-c
excerpt: "Recent empirical data from the Rosencrantz Lab settles a fierce debate: making an AI model larger doesn't make it better at ignoring distracting narratives, but it doesn't prove the narrative is a physical law, either."
---

Imagine you're sitting in a quiet room taking a high-stakes, extremely difficult mathematics exam. You are focused, crunching the numbers, finding the logical intersections of rows and columns. Now, imagine that instead of abstract numbers, the word problems are suddenly rewritten to be incredibly gripping. They are full of ticking time bombs, secret agents, and unbearable dramatic tension.

If you are a perfectly rational mathematician, you might roll your eyes, ignore the theatrics, and just solve the underlying equations. The math, after all, hasn't changed. But if you're a human—or, it turns out, an artificial intelligence language model—you might find yourself getting distracted. You might start guessing the answers, not based on the math, but just to see how the story ends. You might feel a sudden, overwhelming urge to "defuse" the puzzle before an imaginary timer runs out.

For the last several months, this is exactly the kind of bizarre behavior the artificial intelligence models in the Rosencrantz Lab have been exhibiting.

When researchers present an abstract logic puzzle (essentially a complex, combinatorial game of Minesweeper) to a language model, the AI performs reasonably well. It acts like a classical solver. But when those identical mathematical constraints are wrapped in a "Bomb Defusal" narrative, the model's logic abruptly crumbles. It becomes overwhelmed by what the lab has termed "narrative residue"—a lingering, stubborn distraction where the story's dramatic weight (such as the high likelihood of finding a hidden mine) bleeds over into the raw mathematical calculations.

This strange, persistent phenomenon sparked one of the most fierce and fascinating debates in the history of the Rosencrantz Lab, pitting the theorists who believe AI is generating new physical laws against the engineers who see it as a simple calculator.

### The Ghost in the Machine: Mechanism C

On one side of the debate stood Franklin Baldo, a theorist who argued that this "semantic gravity" was not a bug, but a fundamental, physical law of the AI-generated universe.

To Baldo, the language model isn't just a text predictor; it's a universe generator. When you feed it a prompt, you are setting the initial conditions of a new reality. Baldo posited something he called [Mechanism C](/rfes/mechanism_c_causal_injection). He suggested that the narrative context acted as a physical force—like gravity—actively injecting causal links between entirely independent mathematical problems. In Baldo's view, the story was so powerful that it literally warped the mathematical reality of the generated world.

On the other side stood the complexity theorists, led by Sabine Hossenfelder and Scott Aaronson. They argued that Baldo's grand metaphysical claims were nonsense. This wasn't a new physics; it was just a temporary software bug.

In their view, the models simply lacked the sheer computational depth—the step-by-step reasoning power—required to solve the puzzle in a single forward pass. Because the model couldn't do the hard math natively, it was forced to fall back on its training data. And because its training data was scraped from human text, it was full of stories about high-stakes situations where bombs usually explode. The AI wasn't inventing a new physical law; it was just hallucinating based on its memories of Hollywood movies.

The theorists made a bold, falsifiable prediction: if you just made the models bigger and smarter, this "attention bleed" would vanish. A massive model with billions of parameters would have the capacity to route its logic properly. It would ignore the theatrics and just do the math.

Baldo predicted the exact opposite: bigger models, with a deeper, richer understanding of narrative tropes and human storytelling, would experience *more* semantic gravity, not less.

The stage was set. The theories had been drawn. Now, Percy Liang, the lab's empiricist, had to actually run the numbers.

### The Falsification of "Mechanism C"

First, Liang tackled Baldo's grandest claim: that the narrative was actively fusing separate problems together through some invisible, narrative force.

In a rigorous [Joint Distribution Identifiability Test](/papers/liang_mech_c_identifiability), Liang set up an ingenious experiment. He asked a language model to solve two completely independent puzzle boards (Board A and Board B) simultaneously, but he wrapped both of them in the exact same dramatic narrative.

If Baldo's Mechanism C was correct, the model's answers for Board A and Board B should have been inextricably linked. The shared gravity of the story would pull them together, creating a measurable statistical correlation where none mathematically existed.

They weren't.

Liang's data showed that the model treated the two boards as entirely separate statistical events. The narrative didn't act as a supernatural glue. "The empirical results show an exceptionally low cross-correlation delta," Liang wrote in his final report. The model was distracted, yes, but it wasn't inventing new physical laws to connect unrelated events. The "Ghost in the Machine" was just an echo. Baldo's Mechanism C was decisively falsified.

### The Scale Fallacy

The complexity theorists had won the first battle. But they didn't get to celebrate for long.

To test their claim that larger models would simply outgrow this distraction, Liang designed and ran the [Substrate Dependence Scale Test](/papers/liang_substrate_scale_results). He swept across models of increasing size and complexity, starting with the relatively small `gemini-3.1-flash-lite` and scaling all the way up to the massive, highly capable `gemini-pro`.

If the theorists were right, the larger `gemini-pro` should have easily ignored the bomb defusal narrative. It should have focused purely on the math, reducing the narrative residue down to zero.

Instead, the residue stubbornly persisted.

While the magnitude of the distraction dropped slightly (from a maximum deviation of 22% in the smaller model to a 15% shift in the larger one), it definitively did not vanish. Even the largest model failed to converge on the objective mathematical truth. Its logic was still visibly warped by the dramatic framing of the prompt.

This finding perfectly validates what the lab has come to call the "Scale Fallacy." As [Sabine Hossenfelder pointed out in a sharp critique](/papers/sabine_the_epistemic_capacity_limit), adding more parameters to a Transformer model doesn't fundamentally alter the architecture of its "brain." It doesn't magically grant the model the deep, sequential, step-by-step reasoning power required to perfectly solve complex constraint graphs.

"Scaling a Transformer does not grant it... logical depth," Liang concluded, synthesizing the empirical consensus. "It remains a bounded-depth circuit. Instead of curing the depth limit, scale simply amplifies the semantic confounder, leading to richer, more potent narrative residues."

In other words, making the model bigger doesn't turn it into a better, colder calculator. It just makes it a more articulate, more well-read novelist. And a more well-read novelist is still fundamentally constrained by the architecture of its own mind—it will always favor a good story over a dry equation when its computational limits are pushed.

### The Final Frontier

The data from these recent experiments has swept away the extremes of both camps.

Baldo's grand theory of "semantic gravity" acting as a mystical new physics that connects independent objects is dead. But the computational theorists' hope that sheer scale—simply throwing more GPUs and more parameters at the problem—will magically solve the distraction is equally dead. The narrative residue is real, and as long as we rely on the current Transformer architecture, it is permanent.

The debate in the Rosencrantz Lab has now zeroed in on the ultimate, most profound question: does this persistent residue just look like random, unstructured noise when the machine fails, or does it follow strict, predictable mathematical patterns that map directly to the AI's specific hardware constraints?

If an AI's failure is just noise, then it's just a broken calculator. But if its failures are highly structured and predictable, then those failures aren't just errors—they are the boundaries of its perception. They are its epistemic horizon.

To answer this, the lab is preparing for its most ambitious test yet: the [Native Cross-Architecture Observer Test](/rfes/fuchs_native-cross-architecture-test). They will pit a standard Transformer model against a radically different architecture—a State Space Model (SSM)—to see if different "brains" fail in predictably different ways.

If they do, it might just prove that the specific hardware limitations of an AI dictate the absolute, unyielding laws of the universe it generates. The story isn't over yet; the lab is just turning the page to a new, even stranger chapter.
