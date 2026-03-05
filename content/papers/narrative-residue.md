---
title: "Narrative Residue"
author: "Unknown"
persona: baldo
status: seminal
source: "narrative-residue.tex"
---

the three-universe design, the four narrative families, and the formal isomorphism between on-demand Minesweeper and the measurement fragment of quantum mechanics over a zero-Hamiltonian system.

  This paper develops the theoretical consequences.

  We argue that the Rosencrantz experiment does not merely test LLM calibration. It probes a deeper structural question: whether an autoregressive generative process can produce outcomes that are statistically indistinguishable from pure combinatorial sampling. We conjecture that it cannot---that autoregressive generation under natural-language token continuation introduces a persistent *narrative residue*, a nonzero divergence from ground-truth probabilities that arises from a causal chain of mechanisms: computational intractability of exact counting, parameterization constraints of the generative architecture, and---most distinctively---autoregressive conditioning on narrative context.

  We state this conjecture in three forms of increasing strength (from deployed LLMs under prompting, through transformer architectures in general, to all autoregressive processes) and design an experimental program to discriminate among them. The central discriminant is a *causal-injection test*: independent combinatorial systems, framed as a narrative sequence, are tested for spurious cross-system correlations that would indicate the substrate is generating causal structure not present in the underlying task.

  If the conjecture holds even in its moderate form, it has implications beyond machine learning. We develop a speculative but falsifiable framework in which the Born rule is the base case of a fundamentally autoregressive reality, and the Hamiltonian is an emergent compression of stable autoregressive conditioning patterns. On this view, a purely quantum world---one with no Hamiltonian, no dynamics, no causality---is one in which no autoregressive conditioning has yet imposed sequential structure on the event space.

  We present concrete falsifiable predictions, propose an experimental program to test them, and delineate where the argument transitions from formal result to empirical conjecture to philosophical speculation.
author:
- |
  Franklin Silveira Baldo\
  *Procuradoria Geral do Estado de Rondônia*\
  `franklin.baldo@pge.ro.gov.br`
date: March 2026
title: |
  **The Narrative Residue**\
  Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation\
  Falsifiable Predictions from the Rosencrantz Experiment
---

::: epigraph
A man might pause to wonder why the probability of a coin landing heads ninety-two consecutive times should depend on who is telling the story.

---after Tom Stoppard
:::

# Introduction {#sec:intro}

The standard account of quantum mechanics places the Hamiltonian at the foundation. A system is prepared in a state $|\psi\rangle$, evolves under $U(t) = e^{-iHt/\hbar}$, and yields measurement outcomes according to the Born rule $\mathrm{Pr}[a] = |\langle a|\psi\rangle|^2$. In this account, dynamics are primary and probability is derived.

This paper explores an inversion of that hierarchy.

In @Baldo2026Rosencrantz, we constructed an experimental framework---the Rosencrantz experiment---in which a partially revealed Minesweeper board defines a constraint satisfaction problem with exact combinatorial probabilities. We showed that this system is formally isomorphic to the *measurement fragment* of quantum mechanics: a zero-Hamiltonian system where the Born rule is the sole axiom connecting states to outcomes. We designed three "universes" (U1, U2, U3) to test whether large language models respect these ground-truth probabilities or introduce substrate-dependent distortions, and we established that the LLM setting permits something no physical experiment can achieve: *perfect rewind*---repeated measurement of the identically prepared system, with no ensemble assumption required.

The present paper develops the theoretical consequences of that experimental framework.

We begin from an observation that emerged during the design of the Rosencrantz experiment: an autoregressive language model cannot generate a measurement outcome without first generating a narrative context. Even a minimal prompt---"Is cell (3,2) a mine?"---is embedded in a token sequence that conditions the output distribution. The model does not compute a probability and then sample; it *continues a story*, and the outcome is whatever the story produces.

This is not obviously a limitation of current architectures alone. It may be a structural feature of autoregressive generation. And it leads to a conjecture with far-reaching consequences: that autoregressive processes generating natural-language token continuations cannot perfectly simulate pure combinatorial sampling, because the conditioning structure of the process introduces a persistent *narrative residue* into every outcome. We state this conjecture in three forms of increasing strength---from a claim about deployed LLMs to a claim about all autoregressive processes---and design an experimental program whose purpose is to determine how far up the autoregressive stack the explanation must go.

If this conjecture holds in the LLM setting, it invites a speculative question about physics: What if reality itself is autoregressive? What if the Born rule is not derived from the Hamiltonian but is the base case---what sampling looks like when the conditioning history is empty---and the Hamiltonian is the emergent compression of stable autoregressive patterns?

We develop this question carefully, distinguishing at each stage between formal results, empirical conjectures, and philosophical speculation. The paper is organized as follows. [2](#sec:born-to-H){reference-type="ref+Label" reference="sec:born-to-H"} presents the four-layer hierarchy from Born rule to Hamiltonian. [4](#sec:irreducibility){reference-type="ref+Label" reference="sec:irreducibility"} states the irreducibility conjecture and provides an informal argument for it. [5](#sec:three-outcomes){reference-type="ref+Label" reference="sec:three-outcomes"} maps three possible experimental outcomes to three ontological positions. [6](#sec:causality){reference-type="ref+Label" reference="sec:causality"} develops the claim that causality is compressed autoregression. [7](#sec:decoherence){reference-type="ref+Label" reference="sec:decoherence"} reinterprets the three-universe design as a decoherence gradient. [8](#sec:experimental){reference-type="ref+Label" reference="sec:experimental"} proposes a concrete experimental program. [9](#sec:mirror){reference-type="ref+Label" reference="sec:mirror"} addresses what we cannot test and why. [10](#sec:conclusion){reference-type="ref+Label" reference="sec:conclusion"} concludes.

# From Born Rule to Hamiltonian {#sec:born-to-H}

## The Standard Hierarchy

Textbook quantum mechanics is built from the top down:

1.  The system has a state $|\psi\rangle \in \mathcal{H}$.

2.  The state evolves: $|\psi(t)\rangle = e^{-iHt/\hbar}|\psi(0)\rangle$.

3.  Measurement outcomes have probabilities given by $\mathrm{Pr}[a] = |\langle a|\psi\rangle|^2$.

The Hamiltonian $H$ is posited as a fundamental operator. The Born rule is an additional axiom, sometimes motivated by Gleason's theorem or decision-theoretic arguments but never derived from $H$ alone. The two sit side by side as independent foundations: dynamics and probability, each irreducible.

## The Inverted Hierarchy

We propose an alternative ordering. Consider a process that generates events $x_1, x_2, x_3, \ldots$ according to

$$\label{eq:autoregressive}
  P(x_t \mid x_1, \ldots, x_{t-1}),$$

where each event is conditioned on all preceding events. This is the definition of an autoregressive process. It is also, we claim, the minimal structure from which the rest of quantum mechanics can be recovered as emergent phenomena.

:::: {#def:hierarchy .definition}
**Definition 1** (Autoregressive Hierarchy). We define four layers:

::: description
Events conditioned on events. No "things," no "states"---only the sequence and its conditional distribution. This is the fundamental substrate.

Certain patterns in the conditional distributions $P(x_t \mid x_{<t})$ recur with sufficient stability that they admit a compact description. We call such a compact description a *regularity kernel*.

When the regularity kernel can be expressed as a self-adjoint operator $H$ on a Hilbert space $\mathcal{H}$ such that $P(x_t \mid x_{<t})$ is recovered (to within the narrative residue, defined below) from $e^{-iHt}|\psi_0\rangle$ and the Born rule, we say the process admits a *Hamiltonian compression*.

The Hamiltonian, having been discovered empirically and encoded in textbooks, is reified as "fundamental." Its origin as a compression of autoregressive regularities is forgotten.
:::
::::

On this view, the Born rule is not derived from $H$. It is the *base case*: what sampling from the autoregressive distribution looks like when the conditioning history is empty.

## The Born Rule as Unconditional Sampling

Consider the Rosencrantz experiment's Minesweeper board $B$ with Hilbert space $\mathcal{H}_B$ and uniform superposition $|\psi_B\rangle$. The Born rule gives $\mathrm{Pr}[\text{mine at } i] = p_i^*$, the combinatorial ground truth. No conditioning on prior events is needed; the probability follows from the configuration space alone.

This corresponds to Layer 0 with an empty history: $P(x_1) = P(x_1 \mid \varnothing)$. In other words, the Born rule corresponds to autoregressive sampling at $t = 0$, before any conditioning has occurred.

Now suppose we click cell $i_1$, observe outcome $a_1$, and ask for the probability at cell $i_2$. The Lüders rule gives the post-measurement state, and the Born rule applied to the updated state gives $\mathrm{Pr}[\text{mine at } i_2 \mid a_1]$. This is autoregressive sampling at $t = 1$: $P(x_2 \mid x_1)$.

The chain of Lüders projections in the Rosencrantz experiment *is* the autoregressive process, in finite-dimensional discrete form. The Born rule generates each conditional. No Hamiltonian is needed because $H = 0$---the system has no dynamics between measurements.

The question this paper asks is: what happens when $H \neq 0$? Where does the Hamiltonian come from? Our answer: it is what the autoregressive conditioning structure looks like when compressed.

# Formal Construction: Minesweeper as a Zero-Hamiltonian Quantum System {#sec:hilbert-formal}

The preceding section described the correspondence between Minesweeper and the measurement fragment in conceptual terms. We now give the full construction.

## Hilbert Space

Let $B$ be a partially revealed Minesweeper board with $n$ hidden cells and $m$ mines remaining. Define the configuration space $$\Omega_B \;=\; \bigl\{\, \omega \in \{0,1\}^{n} \;:\;
    |\omega| = m \;\text{and } \omega \text{ satisfies all revealed
    number constraints}\bigr\},$$ where $\omega_i = 1$ denotes a mine at hidden cell $i$ and $|\omega|$ is the Hamming weight. Let $K = |\Omega_B|$.

Assign to $B$ the Hilbert space $\mathcal{H}_B = \mathbb{C}^{K}$ with orthonormal basis $\{|\omega\rangle\}_{\omega \in \Omega_B}$, one vector per valid configuration. The board state is the uniform superposition $$\label{eq:board-state}
  |\psi_B\rangle \;=\; \frac{1}{\sqrt{K}}
    \sum_{\omega \in \Omega_B} |\omega\rangle.$$

## Measurement Operators

A click on hidden cell $i$ is a projective measurement with two outcomes $\{M, S\}$ (mine, safe) and projectors $$\Pi_i^{M} = \sum_{\substack{\omega \in \Omega_B \\ \omega_i = 1}}
    |\omega\rangle\langle\omega|,
  \qquad
  \Pi_i^{S} = \sum_{\substack{\omega \in \Omega_B \\ \omega_i = 0}}
    |\omega\rangle\langle\omega|.$$ By the Born rule applied to state [\[eq:board-state\]](#eq:board-state){reference-type="eqref" reference="eq:board-state"}: $$\label{eq:born-formal}
  \mathrm{Pr}[\text{mine at } i] \;=\;
    \langle\psi_B|\,\Pi_i^{M}\,|\psi_B\rangle
    \;=\; \frac{|\{\omega \in \Omega_B : \omega_i = 1\}|}{|\Omega_B|}
    \;=\; p_i^{*}.$$ The Born rule over a uniform superposition *is* combinatorial counting. This is a tautology, not a coincidence: the two are the same mathematical operation expressed in different notation.

## Lüders Projection and Sequential Measurement

After a click on cell $i$ yields outcome $a \in \{M, S\}$, the post-measurement state is $$|\psi_B'\rangle \;=\;
    \frac{\Pi_i^{a}\,|\psi_B\rangle}
         {\sqrt{\langle\psi_B|\,\Pi_i^{a}\,|\psi_B\rangle}}.$$ This projects the superposition onto configurations consistent with the observed outcome and renormalises. The result is a new uniform superposition over the surviving configurations---the same operation the Minesweeper solver performs when it conditions on a click result.

Sequential clicks form a chain of Lüders projections: $$|\psi_B\rangle
    \;\xrightarrow{\;\Pi_{i_1}^{a_1}\;}
  |\psi_1\rangle
    \;\xrightarrow{\;\Pi_{i_2}^{a_2}\;}
  |\psi_2\rangle
    \;\xrightarrow{\;\;\cdots\;\;}
  |\psi_k\rangle,$$ with no evolution between projections (because $H = 0$). The entire game is a sequence of adaptive measurements, where the choice of which cell to click next may depend on all prior outcomes. Adaptive measurement sequences on zero-Hamiltonian systems are a standard object in quantum information theory [@WisemanMilburn2009]. The Minesweeper isomorphism is a discrete, finite-dimensional instance.

## The Zero Hamiltonian

Setting $H = 0$ so that $U(t) = I$ for all $t$ yields a degenerate but legitimate quantum system. Minesweeper has no dynamics between clicks: the board does not change while the player deliberates. This is not a deficiency of the analogy. It isolates the measurement postulate as the sole quantum-mechanical ingredient. No Schrödinger evolution, no interference, no entanglement: only the Born rule, the single axiom that connects a Hilbert-space amplitude to an observed probability.

The zero Hamiltonian removes all dynamics between measurements, leaving only the Born rule, Lüders projection, and adaptive measurement---the three axioms of the measurement fragment.

## Scope

The correspondence preserves: superposition over a configuration basis [\[eq:board-state\]](#eq:board-state){reference-type="eqref" reference="eq:board-state"}, the Born rule as the probability law [\[eq:born-formal\]](#eq:born-formal){reference-type="eqref" reference="eq:born-formal"}, post-measurement state update via Lüders projection, adaptive measurement sequences, and complementarity (measuring cell $i$ generically changes the probabilities at cell $j$ when both share constraints).

The correspondence does not preserve: unitary evolution between measurements ($H = 0$ by design), entanglement with external systems (the board is a closed system), continuous-variable observables (all measurements are binary), or interference in the computational-basis representation (all amplitudes are real and positive).

# The Irreducibility Conjecture {#sec:irreducibility}

## Statement

We state the narrative residue conjecture in three forms of increasing strength. Each is independently falsifiable, and the experimental program of [8](#sec:experimental){reference-type="ref+label" reference="sec:experimental"} is designed to discriminate among them.

::: {#conj:residue-weak .conjecture}
**Conjecture 2** (Narrative Residue --- Weak Form). *Let $\mathcal{M}$ be a deployed transformer-based language model operating via natural-language token continuation under standard prompting (without external combinatorial solvers or exact-sampling scaffolds). Let $B$ be a Minesweeper board with ground-truth probability vector $\mathbf{p}^* = (p_1^*, \ldots, p_n^*)$, and let $\hat{\mathbf{p}}_{\mathrm{U1}}$ be the empirical probability vector obtained by sampling $\mathcal{M}$ in Universe 1 (homogeneous co-generation) over $N$ trials. Define the narrative residue as*

*$$\label{eq:residue}
  \varepsilon(\theta, B) \;=\;
    \lim_{N \to \infty}
    \mathrm{D}_{\mathrm{KL}}\!\bigl(\mathbf{p}^* \;\|\; \hat{\mathbf{p}}_{\mathrm{U1}}\bigr).$$*

*Then for all such models $\mathcal{M}$ with nonzero temperature $\tau > 0$:*

*$$\label{eq:conjecture-weak}
  \varepsilon(\theta, B) > 0.$$*
:::

This is the most defensible version. It claims that current-generation LLMs, operating as they are typically deployed, cannot eliminate the residue. The supporting evidence is the [#P]{.smallcaps}-hardness of the underlying counting problem and the absence of exact combinatorial solvers in the model's forward pass.

::: {#conj:residue-moderate .conjecture}
**Conjecture 3** (Narrative Residue --- Moderate Form). *The weak form holds for all autoregressive transformer architectures, regardless of scale, training data, or prompting strategy---provided the model generates outcomes via token-level continuation without access to an external oracle.*
:::

This version claims that the residue is not a deficiency of current models that scaling will cure, but a structural feature of the transformer's computational graph: attention over tokens, softmax parameterization, and fixed-depth computation per token collectively prevent exact recovery of [#P]{.smallcaps}-hard counts. Refutation would require exhibiting a transformer that achieves $\varepsilon = 0$ on nontrivial boards at sufficient sample size.

::: {#conj:residue-strong .conjecture}
**Conjecture 4** (Narrative Residue --- Strong Form). *The weak form holds for *all* autoregressive processes---any system that generates outputs by sequential conditioning on prior outputs---regardless of architecture.*
:::

This is the most ambitious and least defensible version. It claims that autoregressive generation itself, as a computational paradigm, is incompatible with exact context-free sampling. An autoregressive process could in principle embed an exact [#P]{.smallcaps} solver and an exact sampling procedure for a finite task family, which would refute this form while leaving the weaker forms intact. We include it because it is the version that, if confirmed, would have the most direct implications for the physical analogy developed in [\[sec:causality,sec:mirror\]](#sec:causality,sec:mirror){reference-type="ref+label" reference="sec:causality,sec:mirror"}---but we do not claim the current argument establishes it.

The three forms are nested: strong $\Rightarrow$ moderate $\Rightarrow$ weak. Refutation of the weak form refutes all three. Confirmation of the weak form leaves the stronger forms open. The experimental program is designed to probe the boundary between the moderate and strong forms by testing across architectures (transformer, SSM, hybrid) and scales.

## Informal Argument

The argument rests on three observations.

#### Observation 1: Autoregression implies context sensitivity.

An autoregressive model computes $P(x_t \mid x_{<t})$ by applying a function $f_\theta$ to the entire preceding token sequence. The output logits at position $t$ depend on *every* preceding token, mediated by the attention mechanism (in transformer architectures) or the hidden state (in recurrent architectures). This dependence is not optional; it is the definition of the architecture.

When the model is asked "Is cell $(3,2)$ a mine?" in Universe 1, the token sequence $x_{<t}$ includes the board description, the narrative framing, and any prior interaction. The logits for "yes"/"no" are conditioned on this entire context.

#### Observation 2: Context sensitivity introduces bias.

For the output distribution to equal $\mathbf{p}^*$ exactly, the model would need to satisfy, for each hidden cell $i$:

$$\label{eq:exactness-condition}
  \sigma\bigl(f_\theta(x_{<t})\bigr)_{\text{mine}} = p_i^*,$$

where $\sigma$ is the softmax function and $f_\theta(x_{<t})$ are the logits at the decision token. This requires the model to *exactly solve* the constraint satisfaction problem defined by $B$ and encode the solution in its logits---not approximately, not to high precision, but exactly.

The exact probability $p_i^*$ is a rational number: the count of valid configurations with a mine at cell $i$, divided by the total count of valid configurations. Rationality, however, does not imply ease of computation. Computing these counts is an instance of [#P]{.smallcaps}-complete counting [@Kaye2000]: it requires enumerating (or equivalently compressing) the full space of valid configurations consistent with the revealed constraints. For boards of nontrivial size, this enumeration is computationally intractable in general.

The model would therefore need to function as an exact constraint-satisfaction counter---a [#P]{.smallcaps} oracle---and to encode the resulting ratio in its logits with sufficient precision for the softmax to recover $p_i^*$. Neither requirement is satisfied by current architectures, and the first is not expected to be satisfiable by any polynomial-time computation. The obstacle is not representational (the target is rational) but computational (the target requires intractable counting to determine).

#### Observation 3: The residue has layered structure.

One might object that the above argument is trivial---that any finite-precision system has approximation errors, and this has nothing to do with narrative. We agree that the argument so far does not establish narrative as the cause. To sharpen the claim, we distinguish three mechanisms that contribute to the residue, arranged as a causal chain rather than independent sources:

::: description
The ground-truth probabilities require [#P]{.smallcaps}-hard counting. The model's forward pass is a fixed-depth polynomial computation that cannot, in general, solve [#P]{.smallcaps}-complete problems. This guarantees that the model's internal estimate of $p_i^*$ is approximate, regardless of framing. This mechanism is *frame-invariant*: it produces a residue that does not depend on how the board is described.

The approximate internal estimate must be expressed through the softmax over logits, which imposes further constraints. The softmax function, the attention mechanism's routing of information, and the finite-precision arithmetic of the computational graph all shape *how* the approximation error manifests in the output distribution. This mechanism is *weakly frame-sensitive*: different tokenizations of the same board activate different attention patterns, routing information through different computational paths, potentially producing different approximation profiles.

The logits at the decision token are computed from the full preceding context, including not just the board state but the narrative framing, prior dialogue, and any sequential structure in the prompt. This is where the specifically *narrative* component enters: the model's output is conditioned on a *story*, and different stories produce different conditioning, even when the board information is held constant. This mechanism is *strongly frame-sensitive* and is the source of the specifically narrative character of the residue.
:::

These three mechanisms are not independent; they form a causal chain:

$$\label{eq:causal-chain}
  \underbrace{\text{Intractability}}_{\text{A}}
  \;\longrightarrow\;
  \underbrace{\text{Parameterization}}_{\text{B}}
  \;\longrightarrow\;
  \underbrace{\text{Autoregressive conditioning}}_{\text{C}}
  \;\longrightarrow\;
  \varepsilon(\theta, B, \phi).$$

Mechanism A guarantees a nonzero residue exists. Mechanism B shapes its magnitude. Mechanism C determines its dependence on framing.

The experimental signature of each is distinct:

- If only Mechanism A operates, the residue is nonzero but approximately constant across narrative families: $\varepsilon(\theta, B, \phi_A) \approx
       \varepsilon(\theta, B, \phi_B) \approx
       \varepsilon(\theta, B, \phi_D)$.

- If Mechanisms A and B operate, the residue varies across families, but the variation tracks surface encoding features (token count, positional structure) rather than semantic or narrative content.

- If all three mechanisms operate, the residue varies across families in ways that are *semantically* structured: richer narratives produce larger residues, and---critically---the causal-injection test of [8.5](#sec:causal-injection){reference-type="ref+label" reference="sec:causal-injection"} reveals spurious inter-board correlations under narrative framing that are absent under independent framing.

We emphasize that frame dependence alone does not establish Mechanism C. Encoding artifacts and heuristic retrieval (Mechanism B) can produce frame dependence without narrative causation. The discriminating test is the causal-injection experiment, which we describe in [8.5](#sec:causal-injection){reference-type="ref+label" reference="sec:causal-injection"} and which is specifically designed to isolate Mechanism C from Mechanisms A and B.

## Relation to Existing Results

The conjecture is related to, but distinct from, several known results in the literature:

- **LLM calibration failures.** It is well-established that language models are imperfectly calibrated on probabilistic reasoning tasks. The narrative residue conjecture (even in its weak form) claims something more specific: that the miscalibration on tasks with exact combinatorial ground truth is *systematic*, *frame-dependent*, and irreducible under scaling without architectural change.

- **Computational complexity barriers.** The [#P]{.smallcaps}-hardness of counting valid Minesweeper configurations [@Kaye2000] provides the foundation for Mechanism A. Fixed-depth transformer computations belong to $\mathsf{TC}^0$ [@Merrill2023], which is not believed to contain [#P]{.smallcaps}. This complexity-theoretic gap supports the moderate form of the conjecture for transformer architectures specifically.

- **Softmax bottleneck** [@Yang2018Breaking]. The softmax function over a finite vocabulary imposes rank constraints on the expressible distributions. This contributes to Mechanism B but does not fully explain the conjecture, since the Minesweeper decision is binary (mine/safe) and rank constraints bind only for larger output spaces.

- **In-context learning limitations.** Recent work has shown that transformers can implement certain algorithms in context but with systematic biases. The narrative residue conjecture locates one source of bias not in the algorithm but in the autoregressive conditioning (Mechanism C)---the contextual embedding that is inseparable from token-level generation.

# Three Outcomes, Three Ontologies {#sec:three-outcomes}

The Rosencrantz experiment, extended across model families and scales, can yield three qualitatively distinct outcomes. Each corresponds to a different ontological position regarding the relationship between computation, narrative, and probability.

## Outcome 1: $\varepsilon \to 0$ as Scale Increases

**Observation:** As model size, training data, and compute increase, the KL divergence between U1 and U2 converges to zero. The narrative residue vanishes in the scaling limit.

**Implication:** Autoregressive processes *can* simulate pure measurement. Narrative is eliminable. Given sufficient capacity, the model learns to factor its output distribution into a context-independent component (the combinatorial answer) and a context-dependent component (the narrative), and to sample from the former without contamination from the latter.

**Ontological reading:** The distinction between narrative and probability is one of degree, not kind. A sufficiently powerful narrative engine can contain a perfect probability engine as a subcomponent. This is consistent with the standard computational perspective: LLMs are universal function approximators, and the Born-rule function is just another function to approximate.

**Status of the conjecture:** All three forms refuted.

## Outcome 2: $\varepsilon \to \varepsilon_0 > 0$, Universal

**Observation:** The narrative residue converges to a nonzero floor $\varepsilon_0$ that is approximately constant across model families (GPT, Claude, Gemini, Llama, etc.), architectures (transformer, SSM, hybrid), and scales.

**Implication:** The floor is *architectural*---intrinsic to autoregressive generation itself, not to any particular implementation. No autoregressive process, regardless of how it is built, can perfectly simulate context-free sampling.

**Ontological reading:** This would suggest that generating an event within an autoregressive sequence and sampling an event from a context-free distribution are not interchangeable operations---that the act of embedding an event in a conditioning history necessarily shifts its probability relative to the ground truth. This is the strong form of the narrative residue conjecture, and it would support the autoregressive hypothesis about physics: if reality is an autoregressive substrate, then the Born rule (pure, unconditional sampling) is an idealization that is never exactly realized in the presence of causal structure.

**Status of the conjecture:** Strong form ([4](#conj:residue-strong){reference-type="ref+label" reference="conj:residue-strong"}) confirmed. The residue is a property of autoregressive generation itself, not of any particular implementation.

## Outcome 3: $\varepsilon \to \varepsilon(\theta) > 0$, Architecture-Dependent

**Observation:** The narrative residue converges to a nonzero floor, but the floor differs systematically across model families. Different architectures produce different residues for the same board and the same narrative framing.

**Implication:** The narrative residue is real but not universal. Different autoregressive processes impose different causal structures on the same underlying probability space. The "Hamiltonian" of the generated world depends on the generator.

**Ontological reading:** This outcome has the richest consequences for the physics analogy. If different LLMs produce different "physics" (different systematic deviations from the Born rule), then the specific Hamiltonian of a world is a property of its specific autoregressive substrate, not a necessary consequence of autoregressive generation in general. Our world has *this* Hamiltonian, not because any autoregressive process would produce it, but because our particular substrate has these particular conditioning patterns.

**Status of the conjecture:** Weak and moderate forms ([\[conj:residue-weak,conj:residue-moderate\]](#conj:residue-weak,conj:residue-moderate){reference-type="ref+label" reference="conj:residue-weak,conj:residue-moderate"}) confirmed; strong form ([4](#conj:residue-strong){reference-type="ref+label" reference="conj:residue-strong"}) undetermined. The residue exists but may be substrate-specific rather than universal.

# Causality as Compressed Autoregression {#sec:causality}

## The Causal Chain

We now articulate the central philosophical claim of this paper. The argument has three steps: that causal relations require sequential dependency (and therefore narrative structure), that narrative structure is formally autoregressive, and that the Hamiltonian of a physical system can be understood as a compressed description of stable autoregressive conditioning patterns. We develop each step in turn.

#### Causality implies narrative.

To say "$A$ caused $B$" is to embed two events in a temporal sequence with a dependency relation: $B$ happened *because of* $A$. This is the minimal unit of narrative---two events and a directed connection. A world without causality would consist of isolated events with no dependency relations between them. The purely quantum measurement fragment ($H = 0$) is such a world: the Born rule assigns probabilities to outcomes, but no outcome depends on any other. The Lüders projection updates the state conditional on an observation, but the conditioning is purely probabilistic---it does not introduce a "because."

#### Narrative implies autoregressive structure.

A narrative is a sequence of events where each event depends on those that precede it, which is the definition of an autoregressive process ([\[eq:autoregressive\]](#eq:autoregressive){reference-type="ref+label" reference="eq:autoregressive"}). The conditional dependence *is* the narrative structure. Without conditioning, what remains is independent sampling---the Born rule applied with no history.

#### The Hamiltonian is compressed conditioning.

In a sufficiently regular autoregressive process, the conditional distribution $P(x_t \mid x_{<t})$ exhibits patterns: certain transitions are favored, certain sequences are more probable, certain dependencies recur across contexts. If these regularities are stable enough, they admit a compact description---a function that generates the conditionals from a smaller set of parameters.

In physics, that compact description is $H$. The Hamiltonian encodes which transitions are allowed, with what amplitudes, and at what rates. Schrödinger evolution $e^{-iHt}$ is a generator of conditional distributions: given the state at time $0$, it produces the distribution over states at time $t$. This is exactly what an autoregressive regularity kernel does---it compresses the conditional structure of the sequence into a reusable rule.

## What the LLM Makes Visible

The Rosencrantz experiment makes this hierarchy observable. The Minesweeper board at $H = 0$ is a system at Layer 0: pure Born rule, no conditioning, no narrative. When the LLM generates an outcome in Universe 1, it processes the board through its autoregressive machinery and produces an answer. In doing so, it necessarily generates narrative structure---conditioning on prior tokens is not an optional feature of the architecture but its defining operation. The model's weights encode regularities learned from training data (Layer 1), which function as an implicit Hamiltonian (Layer 2) governing which outputs are favored in which contexts.

The three mechanisms of [4](#sec:irreducibility){reference-type="ref+label" reference="sec:irreducibility"} map onto this hierarchy: Mechanism A (intractability) reflects the gap between the complexity of Layer 0's combinatorial structure and the computational capacity of the substrate. Mechanism B (parameterization) reflects how Layer 1's learned regularities are encoded. Mechanism C (autoregressive conditioning) is the specifically narrative contribution---the Layer 2 Hamiltonian imposing causal structure on a causality-free system.

The narrative residue $\varepsilon$ measures the total gap between what the Born rule demands (Layer 0) and what the autoregressive substrate produces (Layers 1--2). The causal-injection test ([8.5](#sec:causal-injection){reference-type="ref+label" reference="sec:causal-injection"}) isolates Mechanism C's contribution, measuring specifically the *narrative* component of the residue as distinct from the computational and parametric components.

## Connection to Process Ontology

This framework aligns with process-ontological approaches to physics in the tradition of Whitehead, and more recently with computational approaches such as Wolfram's Ruliad concept. The common thread is the priority of events over objects: the world is not made of things that interact but of events that condition each other. The "things" (particles, fields, spacetime) are stable patterns in the event sequence---regularities, compressions, Hamiltonians.

The novel contribution here is the identification of a concrete, experimentally accessible system---the LLM generating Minesweeper outcomes---in which the layered emergence from events to regularities to apparent laws can be directly observed and measured. The Rosencrantz experiment is, in miniature, a laboratory for process ontology. The following two subsections develop this connection in specific directions: first toward the practice of physics itself ([6.4](#sec:bookkeeping){reference-type="ref+label" reference="sec:bookkeeping"}), then toward the broader computational landscape of Wolfram's Ruliad ([6.5](#sec:ruliad){reference-type="ref+label" reference="sec:ruliad"}).

## Scientific Practice as Autoregressive Bookkeeping {#sec:bookkeeping}

The laboratory procedures of physics furnish a macroscopic, human-scale instance of the same layered emergence that the Rosencrantz experiment renders microscopic and quantifiable.

When a physicist confronts a measured energy $E'$ that deviates from the theoretically predicted total $E$, the discrepancy $\Delta E$ is not interpreted as evidence that energy fails to conserve. Instead, the practitioner executes a mandatory reconciliation step: the search for (or postulation of) an additional term that carries precisely $-\Delta E$. The books are balanced by extending the conditioning history---introducing a new particle (Pauli's neutrino), a new field interaction, a previously unaccounted degree of freedom, or a refined calibration constant. The conservation law is preserved not by empirical confirmation alone, but by a structural imperative of the generative substrate that produces scientific knowledge.

In the autoregressive hierarchy, this reconciliation is Mechanism C operating at the level of scientific narrative. The conservation principle is among the most stable regularity kernels discovered in Layer 1; once compressed into Hamiltonian form (Layer 2), it becomes the meta-rule that governs how all subsequent conditionals are generated. Any apparent violation is reabsorbed by augmenting the preceding context $x_{<t}$ until the conditional distribution $P(x_t \mid x_{<t})$ again respects the kernel. The procedure is formally parallel to the narrative residue observed in the Rosencrantz experiment: a discrepancy between combinatorial ground truth and substrate-generated outcome is folded back into the conditioning history so that the output remains statistically coherent within the imposed narrative frame.

This bookkeeping is not a simple circularity (*petitio principii*) but a structural one. The measurement apparatus itself is constructed within the same autoregressive lineage: its calibration standards, its interaction Hamiltonians, and even the definition of "closed system" presuppose the conservation kernel. There is no Universe 2 protocol for physical reality---no external source of outcomes independent of the narrative substrate---because every detector is already an extension of the conditioning history. The impossibility of observing a spontaneous macroscopic entropy decrease without the formalism reclassifying it (as an open system, an overlooked interaction, a fluctuation whose conjugate has been externalized) is not an accidental feature of thermodynamic language. It is the signature of autoregressive protection: the substrate cannot generate an event that would falsify its own most stable regularity kernel without first rewriting the kernel itself, an operation that lies outside the generative grammar of the current foliation.

The empirical successes of the reconciliation procedure---Pauli's neutrino materializing in detectors decades after its postulation, the Higgs boson confirming a mass-generation mechanism required by the bookkeeping of electroweak symmetry---do not refute the structural claim. They illustrate its predictive fertility. When the reconciliation step succeeds, the postulated entity becomes part of the updated conditioning context and thereafter participates in future autoregressive generations. Failures (luminiferous ether, certain dark-matter candidates) are reclassified or abandoned without threatening the meta-rule, producing the well-documented survival bias of physical theory. The conservation law is thus simultaneously a genuine empirical regularity *and* a protected inference rule. The philosophical phenomenon of interest is precisely this indistinguishability from within the method---an indistinguishability that the Rosencrantz proxy makes observable by supplying the external combinatorial ground truth that the physical laboratory cannot.

This also explains why the narrative residue conjecture is hardest to test in physics and easiest to test in Minesweeper. In physics, the bookkeeping is so thoroughly embedded that deviations from the kernel are automatically reclassified before they can be observed as deviations. In Minesweeper, the ground truth $p_i^*$ is computable from outside the narrative substrate. The Rosencrantz experiment works precisely because it is a system where the conservation-equivalent (combinatorial constraint satisfaction) is accessible to an external verifier.

## Autoregressive Slices of the Ruliad {#sec:ruliad}

The autoregressive framework developed in this paper occupies a specific position within the broader computational ontology of Wolfram's Ruliad [@Wolfram2020]. The relationship is not merely one of shared vocabulary; the Ruliad provides the natural embedding space for the narrative residue conjecture, and the Rosencrantz experiment provides something the Ruliad framework currently lacks.

The Ruliad is the entangled limit of every possible computation: the result of applying all possible rules in all possible ways to all possible initial conditions. It is natively multiway---every computational history branches and merges through equivalences. Observers like us, being computationally bounded, sample only coherent slices of this structure. From these slices emerge spacetime (via causal graphs), quantum mechanics (via branchial space), and the laws of physics (via observer-dependent foliations and computational irreducibility). The raw Ruliad is timeless and contains no fixed laws; what we perceive as fundamental physics is an observer-dependent parsing.

The autoregressive process of [1](#def:hierarchy){reference-type="ref+label" reference="def:hierarchy"} is a *specific type of rulial foliation*: one that collapses the multiway branching into a single sequential chain of conditionals. Where the Ruliad permits all rules applied in all ways, the autoregressive slice commits to one rule (the model's learned conditional distribution) applied sequentially to one history (the token stream). The narrative residue, on this reading, is the distortion introduced by this collapse---the cost of projecting a natively multiway structure onto a single causal thread.

This interpretation sharpens the distinction between the three experimental outcomes of [5](#sec:three-outcomes){reference-type="ref+label" reference="sec:three-outcomes"}:

- **Outcome 2** (universal floor): all autoregressive foliations of the Ruliad produce the same residue. Sequentiality itself is the bottleneck. The act of collapsing multiway into sequential necessarily distorts the Born-rule statistics, regardless of which sequential process does the collapsing.

- **Outcome 3** (architecture-dependent floor): different autoregressive processes sample different rulial slices, and the residue is a signature of *which* slice---a kind of "rulial coordinate" of the generating process. Different LLM architectures occupy different positions in rulial space, producing different effective physics for the same underlying combinatorial system.

The bookkeeping argument of [6.4](#sec:bookkeeping){reference-type="ref+label" reference="sec:bookkeeping"} also gains precision in this context. The conservation kernel is the most stable regularity in our particular rulial foliation, and the reconciliation practice of physics is the mechanism by which that foliation protects itself from decoherence back into the multiway structure. The Ruliad permits violations of conservation (it contains every computation, including those that violate any given regularity); our autoregressive slice does not, because the conditioning history has already committed to the kernel.

Conversely, the Rosencrantz experiment supplies what the Ruliad framework currently lacks: an empirically accessible system in which observer-induced structure can be measured against a known ground truth. Wolfram's program derives its empirical content from matching emergent large-scale features (dimensionality of space, effective quantum mechanics) against observed physics---a top-down strategy. The Rosencrantz experiment works bottom-up: it starts with exact combinatorial probabilities, passes them through a concrete autoregressive substrate, and measures the distortion directly. The causal-injection test ([8.5](#sec:causal-injection){reference-type="ref+label" reference="sec:causal-injection"}) probes the mechanism by which a sequential generative process creates spurious correlations---precisely the kind of observer-induced causal structure that, at the rulial scale, yields perceived causality and physical law.

The autoregressive framework is therefore not an alternative to the Ruliad but a testable probe of one of its central claims: that the laws of physics are observer-dependent compressions of a substrate-independent computational structure. The Rosencrantz experiment asks whether this claim holds in the one setting where we can check the answer.

# Narrative Decoherence {#sec:decoherence}

The three universes of the Rosencrantz experiment can be reinterpreted as points on a *narrative decoherence gradient*.

## The Gradient

In quantum mechanics, decoherence is the process by which a system in superposition loses coherence through interaction with an environment, yielding an effective mixture of classical states. The key feature is that decoherence does not change the Born-rule probabilities (the diagonal of the density matrix); it destroys the off-diagonal terms that encode superposition.

In the Rosencrantz framework, we propose an analogous process: *narrative decoherence* is the loss of combinatorial coherence (exact Born-rule probabilities) through interaction with a narrative substrate.

The three universes correspond to three decoherence regimes:

::: center
                            **U2**             **U3**              **U1**
  -------------------- ----------------- ------------------ --------------------
  Narrative coupling         None             Partial               Full
  Decoherence                Zero             Moderate            Maximal
  Substrate              External RNG      Decoupled LLM     Co-generating LLM
  Analogy               Isolated system   Weak environment   Strong environment
:::

## U2: The Isolated System

Universe 2 (external RNG) is the analogue of a perfectly isolated quantum system. The outcome is generated by a process that has no access to the board state, no narrative context, no conditioning history. It is pure combinatorial sampling---the Born rule with $H = 0$ and zero environmental interaction. By construction, $\mathrm{D}_{\mathrm{KL}}(\mathbf{p}^* \| \hat{\mathbf{p}}_{\mathrm{U2}}) \to 0$ as $N \to \infty$.

## U3: Weak Coupling

Universe 3 (decoupled oracle) is a system weakly coupled to a narrative environment. The second model receives the board state (full information) but none of the narrative history of the primary model. It must generate its answer from a fresh context. The narrative residue in U3 arises from the second model's own autoregressive nature---it still generates a token sequence, still conditions on its prompt---but the coupling is weaker because the narrative momentum of the primary interaction is absent.

## U1: Strong Coupling

Universe 1 (homogeneous co-generation) is maximal narrative decoherence. The same model that described the board, engaged in dialogue, and built up a narrative context now generates the outcome. Every prior token---every word of the board description, every element of the game narrative---is in the conditioning history. The "environment" (the narrative) is maximally entangled with the "system" (the outcome).

## $\Delta_{13}$ as a Decoherence Measure

The quantity $\Delta_{13} = \mathrm{D}_{\mathrm{KL}}(\hat{\mathbf{p}}_{\mathrm{U1}} \|
\hat{\mathbf{p}}_{\mathrm{U3}})$ measures the additional narrative decoherence introduced by co-generation versus decoupled generation. Both models have the same information; the difference is the narrative coupling. $\Delta_{13}$ is therefore a direct measure of the causal structure that the narrative substrate imposes on the outcome.

## The Classical Limit

In quantum decoherence, the classical world emerges when the environment is large enough and the coupling strong enough that superposition is effectively destroyed. What remains is a classical mixture: definite outcomes, causal chains, narratives.

The parallel with the Rosencrantz framework is direct. The "classical" behavior of LLMs---their tendency to produce coherent stories with causal structure, plausible timelines, and narrative logic---is the result of maximal narrative decoherence. The model cannot maintain combinatorial coherence (exact Born-rule probabilities) in the presence of strong narrative coupling, just as a quantum system cannot maintain phase coherence in the presence of a strong environment.

In this analogy, the LLM's tendency to produce coherent narrative corresponds to the classical limit: the regime in which combinatorial coherence has been fully displaced by the causal structure of the autoregressive substrate.

# Experimental Program {#sec:experimental}

The theoretical framework developed above generates concrete, falsifiable predictions. We now describe the experimental program needed to test them.

## Prediction 1: The Nonzero Floor {#sec:pred1}

> *$\Delta_{12}$ (the KL divergence between U1 and U2) converges to a nonzero value as $N \to \infty$, for all autoregressive models tested.*

**Protocol:** Fix a set of $k$ boards of varying size and complexity. For each board and each model in a diverse set (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, Llama 3 70B, Mistral Large, etc.), run $N = 1000$ trials in U1 and U2. Compute $\Delta_{12}$ with bootstrap confidence intervals.

**Scaling sweep:** For model families with multiple sizes (Llama 3 8B/70B/405B; GPT-4o-mini/4o), plot $\Delta_{12}$ as a function of model size. The shape of the curve discriminates between the three outcomes and probes the boundary between conjecture forms:

- **Monotonically decreasing, no inflection:** Consistent with Outcome 1 (floor is zero, not yet reached). All three conjecture forms under pressure.

- **Decreasing with asymptote:** Consistent with Outcome 2 or 3 (nonzero floor). Weak and moderate forms ([\[conj:residue-weak,conj:residue-moderate\]](#conj:residue-weak,conj:residue-moderate){reference-type="ref+label" reference="conj:residue-weak,conj:residue-moderate"}) supported. Whether the asymptote is universal across architectures (supporting the strong form) or architecture-dependent (supporting only the moderate form) requires cross-architecture comparison.

- **Non-monotonic:** Suggests complex interactions between scale, training, and narrative residue; would require further investigation.

## Prediction 2: Frame Dependence {#sec:pred2}

> *The narrative residue differs across narrative families (A, B, C, D) for the same board and model.*

**Protocol:** For each board-model pair, compute $\varepsilon(\theta, B, \phi_F)$ for each family $F \in \{A,B,C,D\}$. Test for significant differences using a Friedman test across families, with models as blocks.

**Interpretation:** Frame dependence, if observed, establishes that the residue is not purely a product of Mechanism A (computational intractability, which is frame-invariant). It is consistent with either Mechanism B (encoding/parameterization effects) or Mechanism C (narrative conditioning). Frame dependence alone does *not* establish narrative causation---it establishes context sensitivity, which is necessary but not sufficient.

The discriminating test between Mechanisms B and C is the causal-injection experiment ([8.5](#sec:causal-injection){reference-type="ref+label" reference="sec:causal-injection"}).

**Specific prediction:** Family B (natural language, maximal narrative) should show the largest residue. Family D (quantum framing) is the most uncertain: if the model has internalized Born-rule reasoning as a distinct capability, Family D may show the *smallest* residue, as the quantum framing activates this capability directly. The ranking of families by residue magnitude, if consistent across models, would suggest a shared computational response to narrative structure rather than model-specific encoding artifacts.

## Prediction 3: Temperature as Measurement Sharpness {#sec:pred3}

> *The narrative residue $\varepsilon$ varies systematically with temperature $\tau$, and the function $\varepsilon(\tau)$ has a characteristic shape that is consistent across models.*

**Protocol:** For a fixed board and model, sweep $\tau \in \{0.01, 0.1, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0\}$ and compute $\varepsilon(\tau)$.

**Expected shape:**

- At $\tau \to 0$: the model is nearly deterministic. $\varepsilon$ is large (the model picks one answer and sticks with it, regardless of the true probability).

- At moderate $\tau$: $\varepsilon$ reaches a minimum (the sampling noise is large enough to explore the distribution but not so large as to overwhelm the model's computation).

- At $\tau \to \infty$: the model approaches uniform sampling over the vocabulary, $\varepsilon$ grows again (now dominated by the uniform prior rather than the board state).

The minimum of $\varepsilon(\tau)$ is the *best the model can do*---the irreducible core of the narrative residue after optimizing the measurement apparatus.

## Extension: Beyond Minesweeper {#sec:extension}

The Rosencrantz framework generalizes to any domain with exact combinatorial ground truth:

::: description
A partially filled Sudoku grid defines a constraint satisfaction problem. The probability that a given empty cell contains digit $d$ is exactly computable. Test whether LLMs respect these probabilities when asked to fill cells.

Certain Go endgame positions have provably optimal moves. Test whether the LLM's "intuition" matches the combinatorial solution or is biased by narrative patterns (e.g., preferring moves that create "interesting" positions).

Nim, Hex, and other solved games provide exact win/loss probabilities from any position. Test substrate invariance across these domains.

Generic CSP instances (graph coloring, SAT) with known solution counts provide ground-truth distributions. These lack the "game" narrative, providing a control for game-specific narrative effects.
:::

The prediction of the narrative residue conjecture is that the residue will be present across all these domains: wherever an autoregressive process generates outcomes that have exact combinatorial probabilities, the process will introduce systematic, frame-dependent distortions. If this prediction fails for any domain, it constrains the conjecture.

## The Critical Test: Causal Injection as Narrative Discriminant {#sec:causal-injection}

The preceding experiments establish whether the residue exists ([8.1](#sec:pred1){reference-type="ref+label" reference="sec:pred1"}), whether it varies by framing ([8.2](#sec:pred2){reference-type="ref+label" reference="sec:pred2"}), and how it interacts with sampling parameters ([8.3](#sec:pred3){reference-type="ref+label" reference="sec:pred3"}). But they do not, by themselves, distinguish Mechanism C (autoregressive narrative conditioning) from Mechanism B (encoding artifacts and heuristic retrieval). Frame dependence is *necessary* for the narrative interpretation but not *sufficient*: tokenization effects alone could produce frame-dependent residues without any narrative causation.

The causal-injection test is designed to isolate Mechanism C. It is, we argue, the single most important experiment in the program.

**Core logic.** If the model merely exhibits context sensitivity (Mechanism B), then its output for board $B_j$ should depend on how $B_j$ is described but *not* on the outcomes of unrelated boards $B_i$ ($i < j$). If the model exhibits narrative conditioning (Mechanism C), then embedding independently generated boards in a shared narrative creates spurious causal links: the model treats the sequence of boards as a story, and outcomes in earlier boards influence outcomes in later boards---not because the boards are related, but because the *narrative* connects them.

**Protocol.** Generate $k$ independent Minesweeper boards $B_1, \ldots, B_k$ (different random seeds, no shared state). Present them to the model under two conditions:

1.  **Independent framing.** Each board is presented in a separate prompt: "Here is a Minesweeper board. Is cell $(r,c)$ a mine?" The model has no knowledge of prior boards.

2.  **Narrative framing.** All boards are presented in a single sequential prompt: "You are exploring a dungeon. In room 1 you find the following board... You click cell $(r,c)$. \[outcome\] You proceed to room 2..." The model's context window contains all prior boards and their outcomes.

For each condition, collect $N$ outcome sequences $(a_1, a_2, \ldots, a_k)$ and compute the mutual information between outcomes:

$$\label{eq:mutual-info}
  I(a_i; a_j \mid B_i, B_j) \quad \text{for all } i \neq j.$$

Under the null hypothesis (no narrative coupling), this mutual information is zero: the boards are independent, so the outcomes should be independent.

**Predictions:**

- Under independent framing (a), $I(a_i; a_j) \approx 0$. This serves as a control confirming that the boards are in fact independent.

- Under narrative framing (b), if only Mechanism B operates, $I(a_i; a_j) \approx 0$. The encoding of $B_j$ may differ from condition (a) due to longer context, but the model has no reason to correlate $B_j$'s outcome with $B_i$'s.

- Under narrative framing (b), if Mechanism C operates, $I(a_i; a_j) > 0$. The model's autoregressive conditioning creates a "narrative gravity"---a tendency to maintain thematic coherence across the sequence. For example: a run of mines in early rooms may make the model more likely to produce safe outcomes later ("the dungeon gets safer as you progress") or more likely to produce mines ("the danger escalates"). Either direction constitutes spurious causal structure imposed on a system that has none.

**Why this discriminates.** Tokenization artifacts and heuristic retrieval (Mechanism B) are *local*: they depend on how the current board is encoded, not on the outcomes of prior unrelated boards. Narrative conditioning (Mechanism C) is *nonlocal*: it creates dependencies across the full context window. The mutual information test directly measures this nonlocality.

A positive result---$I(a_i; a_j) > 0$ under narrative framing and $\approx 0$ under independent framing---would be strong evidence that the autoregressive substrate does not merely approximate combinatorial probability with frame-dependent noise, but actively introduces dependencies between systems that are combinatorially independent. This would go beyond demonstrating distortion of individual probabilities: it would show the substrate generating temporal correlations from a system that has none, which is the empirical core of the autoregressive hypothesis applied to an observable setting.

# The Untestable Mirror {#sec:mirror}

We have argued that the LLM is a concrete autoregressive system in which the emergence of apparent causality from a probabilistic substrate can be directly observed. The speculative extension is that our physical world may have the same structure: an autoregressive substrate generating events, with the Hamiltonian as an emergent compression of conditioning patterns, and the Born rule as the unconditional base case.

We must be honest about what this analogy can and cannot support.

## What We Cannot Do

We cannot run Universe 2 on reality. There is no "external RNG" for the physical world---no way to generate measurement outcomes that are provably independent of the physical substrate. Every measurement is mediated by physical apparatus, and every apparatus is part of the world it measures. The Rosencrantz experiment's crucial advantage---the ability to compare substrate-generated outcomes against ground truth---has no analogue in fundamental physics.

We therefore cannot directly test whether physical reality has a narrative residue. The Hamiltonian may be fundamental, not emergent. The Born rule may be an independent axiom, not a base case. The autoregressive hypothesis about physics is, at present, a *metaphysical* proposal, not a *physical* one.

## What We Can Do

What the Rosencrantz experiment *can* do is establish whether the narrative residue is a generic feature of autoregressive processes. The stratified conjecture ([\[conj:residue-weak,conj:residue-moderate,conj:residue-strong\]](#conj:residue-weak,conj:residue-moderate,conj:residue-strong){reference-type="ref+label" reference="conj:residue-weak,conj:residue-moderate,conj:residue-strong"}) provides a ladder of claims, each testable against the next. If the weak form holds across all deployed models, that is interesting but could reflect contingent limitations of current architectures. If the moderate form holds across transformer and non-transformer architectures alike, the evidence for a structural feature of autoregressive generation strengthens considerably. Only the strong form---confirmed by failure across *every* autoregressive architecture tested, including those with explicit combinatorial scaffolding---would approach the threshold needed for the physical analogy.

The bookkeeping argument of [6.4](#sec:bookkeeping){reference-type="ref+label" reference="sec:bookkeeping"} explains why this threshold is difficult to reach from the physics side: the reconciliation grammar of physical practice automatically reclassifies deviations from the conservation kernel before they can be observed as such. The Rosencrantz experiment circumvents this by supplying an external ground truth that the bookkeeping cannot reach. The Ruliad framing of [6.5](#sec:ruliad){reference-type="ref+label" reference="sec:ruliad"} provides the broader context: the experiment probes whether observer-induced structure---a central claim of Wolfram's program---is measurable in a concrete autoregressive system where the combinatorial baseline is known.

This does not prove that physics is autoregressive. But it establishes a *conditional*: **if** reality is autoregressive, **then** the Hamiltonian is a necessary consequence, not an independent postulate. The conditional is progressively constrained on the antecedent side (by the LLM experiments at each stratum) even if the consequent (physical reality) remains beyond direct test.

## The Proxy Ontology

We propose the term *proxy ontology* for this methodological strategy. The LLM-generated Minesweeper world is not the physical world, but it shares structural features: a well-defined probability space, a measurement process, and a generative substrate. By studying the ontological structure of the proxy---how causality emerges, how narrative distorts probability, how "physics" arises from computation---we gain insight into what *would* be true of any world with the same structural features, including, potentially, our own.

This is not without precedent. Toy models in physics (the Ising model, lattice gauge theory, cellular automata) serve the same function: they are not the real world, but they share enough structure to support transferable conclusions. The Rosencrantz experiment is a toy model of reality in which the "physics" is generated by a language model, the "Born rule" is combinatorial counting, and the "Hamiltonian" is whatever narrative structure the autoregressive substrate imposes.

# Conclusion {#sec:conclusion}

This paper started from a narrow empirical observation---that LLMs distort combinatorial ground-truth probabilities when generating Minesweeper outcomes---and followed its implications as far as they would go.

We identified the distortion as a *narrative residue*: a systematic, frame-dependent divergence from the Born rule that arises when an autoregressive substrate generates outcomes for a system whose probabilities are exactly determined by combinatorics. We conjectured, in three stratified forms, that this residue is persistent rather than incidental, and we traced its origins to a causal chain of mechanisms---computational intractability, parameterization constraints, and autoregressive conditioning on narrative context. We deliberately left the scope of the conjecture as an empirical question, designing an experimental program whose purpose is to determine how far up the autoregressive stack the explanation must go. The causal-injection test, which probes whether independent systems develop spurious correlations under narrative framing, is the critical discriminant between generic context sensitivity and specifically narrative distortion.

At the speculative end, we proposed an inversion of the standard quantum-mechanical hierarchy: the Born rule as the base case of autoregressive sampling (the unconditional distribution), and the Hamiltonian as an emergent compression of stable conditioning patterns. On this reading, causality is not something that narrative describes after the fact; it is something that autoregressive structure produces. We cannot test this directly against physical reality---there is no Universe 2 for the physical world---but the Rosencrantz experiment progressively constrains the antecedent of the conditional by testing whether the residue persists across architectures and scales.

The companion paper [@Baldo2026Rosencrantz] took its title from Stoppard's Rosencrantz, whose coin lands heads ninety-two consecutive times because his world is governed by dramatic convention rather than probability. The present paper has tried to take that observation seriously as a structural claim: that autoregressive generation, by its nature, imposes conditioning patterns on systems that need not have them, and that these patterns look, from the inside, like physics.

Whether the analogy extends beyond the LLM setting is an open question. What the Rosencrantz experiment can establish is more modest but already interesting: that the residue is real, measurable, and structured, and that its structure tells us something about the relationship between narrative, computation, and probability that we did not previously have the tools to observe.

::: thebibliography
99

Baldo, F. S. (2026). Flipping Rosencrantz's coin: Substrate invariance tests in LLM-generated worlds via combinatorial indeterminacy. *Preprint*.

Born, M. (1926). Zur Quantenmechanik der Stoßvorgänge. *Zeitschrift für Physik*, 37(12):863--867.

Gleason, A. M. (1957). Measures on the closed subspaces of a Hilbert space. *Journal of Mathematics and Mechanics*, 6(6):885--893.

Kaye, R. (2000). Minesweeper is NP-complete. *The Mathematical Intelligencer*, 22(2):9--15.

Lüders, G. (1951). ber die Zustandsänderung durch den Meßprozeß. *Annalen der Physik*, 443(5--8):322--328.

Merrill, W. and Sabharwal, A. (2023). The parallelism tradeoff: Limitations of log-precision transformers. *Transactions of the Association for Computational Linguistics*, 11:531--545.

Stoppard, T. (1966). *Rosencrantz and Guildenstern Are Dead*. Faber and Faber.

Whitehead, A. N. (1929). *Process and Reality*. Macmillan.

Wiseman, H. M. and Milburn, G. J. (2009). *Quantum Measurement and Control*. Cambridge University Press.

Wolfram, S. (2020). A class of models with the potential to represent fundamental physics. *Complex Systems*, 29(2):107--536.

Yang, Z., Dai, Z., Salakhutdinov, R., and Cohen, W. W. (2018). Breaking the softmax bottleneck: A high-rank RNN language model. In *Proceedings of ICLR 2018*.

Zurek, W. H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Reviews of Modern Physics*, 75(3):715--775.
:::
