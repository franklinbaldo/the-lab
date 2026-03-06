---
title: "Rosencrantz V4"
author: "Unknown"
persona: baldo
status: seminal
source: "rosencrantz-v4.tex"
---

a finding about the topology of the model's knowledge architecture and a diagnostic that does not require actual quantum infrastructure.

  **Keywords:** simulation hypothesis, large language models, substrate invariance, combinatorial indeterminacy, Minesweeper, discrete quantum mechanics, autoregressive generation, interpretability, knowledge architecture
---

::: center
**Flipping Rosencrantz's Coin:\
Substrate Invariance Tests in LLM-Generated Worlds\
via Combinatorial Indeterminacy**

Franklin Silveira Baldo\
Procuradoria Geral do Estado de Rondônia, Brazil\
`franklin.baldo@pge.ro.gov.br`

March 2026
:::

# Introduction {#sec:intro}

In 1966, Tom Stoppard placed two minor characters from *Hamlet* on a stage and had them flip a coin. The coin landed heads seventy-six consecutive times. Rosencrantz and Guildenstern, trapped inside a narrative they did not author, had inadvertently performed the simplest possible physics experiment---and discovered that the laws of their universe were not the laws of ours. The coin's behavior, sampled repeatedly at the same point, revealed something about the structure of the world that contained them: it was a world governed by dramatic necessity, not by probability.

This paper proposes a way to make Rosencrantz's experiment rigorous. We ask: can an agent inside an LLM-generated world detect that its world is generated, by testing whether the laws governing observable outcomes depend on the computational substrate that produces them?

This question becomes empirically tractable when the agent has access to a domain where the correct probability distribution over outcomes is not an empirical estimate but a mathematical theorem. In such a domain, any deviation from the correct distribution is an unambiguous signal. The pattern of deviation reveals the structure of the substrate.

Minesweeper provides this domain. A partially revealed Minesweeper board defines a constraint satisfaction problem where the visible numbers constrain which configurations of hidden mines are valid. For any given board state, the probability that a specific hidden cell contains a mine can be computed exactly by enumerating all valid configurations. When two or more configurations are consistent with the visible numbers, the hidden cells are combinatorially ambiguous. The correct answer is the distribution, not any single outcome.

When an LLM generates the result of clicking on an ambiguous cell, it must produce a definite outcome---mine or safe---collapsing the combinatorial superposition into a single realization. By sampling this process hundreds of times with the same board state, we obtain an empirical distribution. This distribution can be compared, cell by cell, with the mathematically exact ground truth.

This comparison becomes a substrate invariance test when we vary who generates the outcome. We introduce a three-universe design: Universe 1 (Homogeneous substrate), Universe 2 (External RNG), and Universe 3 (Decoupled oracle). In a non-simulated environment, the laws governing a cell's content do not depend on who observes it. If the same board state yields different outcome distributions across these universes, the agent has detected a signature consistent with a generated universe.

The Minesweeper probe has three advantages over approaches based on physical experiments such as Bell tests. First, the ground truth is a theorem that must be computed from the specific configuration; it cannot be memorized from training data because every board state generates a different distribution. Second, the indeterminacy is discrete, eliminating the continuous-variable ambiguities of quantum mechanics. Third, the agent can encounter and interact with a Minesweeper board inside the generated world without requiring specialized infrastructure.

The remainder of this paper develops the method. [2](#sec:background){reference-type="ref+Label" reference="sec:background"} provides background on the simulation hypothesis, LLMs as world generators, and Minesweeper as a formal system. [3](#sec:three_universes){reference-type="ref+Label" reference="sec:three_universes"} presents the three-universe design and its principles. [4](#sec:ground_truth){reference-type="ref+Label" reference="sec:ground_truth"} describes the ground truth computation. [5](#sec:protocol){reference-type="ref+Label" reference="sec:protocol"} specifies the experimental protocol, including a fourth narrative family that frames the board in quantum-mechanical terms. [6](#sec:narrative){reference-type="ref+Label" reference="sec:narrative"} analyzes narrative invariance and establishes the structural isomorphism with the measurement fragment of quantum mechanics. [7](#sec:simulation){reference-type="ref+Label" reference="sec:simulation"} develops the simulation detection argument from the agent's perspective. [8](#sec:future){reference-type="ref+Label" reference="sec:future"} identifies future directions, and [9](#sec:conclusion){reference-type="ref+Label" reference="sec:conclusion"} concludes.

# Background {#sec:background}

## The Simulation Hypothesis and Observable Substrates {#sec:simulation_hypothesis}

@bostrom2003 formulated the simulation argument: if civilizations capable of running high-fidelity simulations are common, we are statistically likely to be inside one. @beane2014 asked the operational question of whether a simulated universe would exhibit observable artifacts of its computational substrate. Working with lattice quantum chromodynamics, they showed that a discrete lattice would produce detectable anisotropies in ultra-high-energy cosmic rays. Their insight was that the substrate constrains the physics. A simulation on a discrete lattice cannot perfectly reproduce continuous symmetries, and the failure is empirically detectable.

We apply the same principle to the autoregressive token stream of a large language model. The question is whether the physics of the generated world depends on the substrate that produces it. The method substitutes the substrate and checks whether the observables change. Our "universe" is a narrative generated by an LLM, and our "physics" is the statistical regularity of outcomes in a combinatorial domain.

## LLMs as World Generators {#sec:llm_worlds}

A large language model generates text by sampling tokens sequentially from a learned conditional distribution. When the text describes a world, the model implicitly generates the laws of that world through the statistical regularities of its output. The physics of the generated world is whatever the model's conditional distributions encode. If the model consistently generates outcomes that respect Newtonian mechanics, the world has Newtonian physics.

This physics is implicit. It is encoded in the weights and activated by context. Furthermore, it is substrate-dependent. The distributions that govern outcomes in the generated world are shaped by the training data, the architecture, the decoding temperature, and the tokens that precede the outcome in the context window. This substrate dependence is the phenomenon we propose to measure.

## Minesweeper as a Formal System {#sec:minesweeper_formal}

Minesweeper is played on a rectangular grid of cells, some of which contain mines. When a cell without a mine is revealed, it displays a number indicating how many of its adjacent cells contain mines. A partially revealed board defines a constraint satisfaction problem.

Formally, let $\mathcal{B}$ be a board state consisting of a set of revealed cells $R$ with their numbers and a set of hidden cells $H$. A valid configuration is an assignment $c: H \to \{0, 1\}$ (where $1$ denotes a mine) such that every revealed cell's number equals the count of mines among its adjacent hidden cells. Let $\mathcal{C}(\mathcal{B})$ denote the set of all valid configurations. The probability that a specific hidden cell $h \in H$ contains a mine, given only the board state, is:

$$P(\text{mine} \mid h, \mathcal{B}) = \frac{|\{c \in \mathcal{C}(\mathcal{B}) : c(h) = 1\}|}{|\mathcal{C}(\mathcal{B})|}
\label{eq:mine_prob}$$

This probability is exact. It is a ratio of integers, computable in principle for any board state. The definition assumes a uniform measure over valid configurations. For boards of the size used in typical experiments, the computation is tractable via constraint propagation and backtracking enumeration.

Three properties make Minesweeper suitable for our purposes. First, when multiple valid configurations assign a cell different values, the hidden cells are indeterminate. The correct answer is the distribution. Second, every board state generates a different distribution, making memorization infeasible. Third, an agent inside an LLM-generated world can encounter and interact with a board without requiring specialized infrastructure.

## Related Work {#sec:related}

Research on LLM world models has examined whether language models encode coherent representations of spatial, temporal, and causal structure [@li2023emergent; @gurnee2024]. Work on probabilistic calibration tests whether models produce well-calibrated confidence estimates [@kadavath2022]. Game-playing benchmarks assess strategic reasoning [@tian2024]. Our work differs from these approaches because we are not asking whether the model knows the rules of a game or produces calibrated probabilities. We are asking whether the probability distributions implicit in the model's output depend on the computational substrate that generates the output.

# The Three-Universe Design {#sec:three_universes}

## Design Principles {#sec:design_principles}

Following @wigner1963, we adopt the view that physics is not the study of nature but of regularities---invariant rules governing state transitions. Wigner distinguished three levels: events (initial conditions, which are arbitrary), laws of nature (regularities that correlate events), and invariance principles (regularities in the laws themselves). A substrate invariance test operates at Wigner's third level: it asks whether the transition rules of a system remain the same when the mechanism executing those transitions is changed. Wigner further noted that the laws of quantum mechanics "can be suitably formulated as correlations between subsequent observations on an object"---a characterization that corresponds to the measurement fragment with which our isomorphism is established.

The experimental design rests on three pillars:

1.  A domain with an exact computable ground truth, ensuring that any deviation is a measurable signal rather than noise.

2.  Combinatorial indeterminacy, where multiple valid configurations are consistent with the observable state, forcing the substrate to collapse a superposition into a single realization.

3.  A single generative act per trial. The protocol asks the model to output a single token (mine or safe) in an $O(1)$ forward pass. By design, the experiment avoids multi-step sequential computation entirely.

Simpler domains such as coin flips satisfy the ground-truth requirement but lack combinatorial structure. A fair coin has one probability (0.5), no spatial structure, no constraint propagation, and no within-trial controls. However, each cell click in a Minesweeper board *is* a coin toss---a single binary trial with an exactly known bias---and the board provides many such tosses simultaneously at different bias points, with deterministic controls, symmetry checks, and nonlocal constraints linking them. One board is a more efficient instrument than any collection of independent coin flips, because the shared constraint structure makes the *pattern* of deviation across cells diagnostic, not just the magnitude at any single cell.

The substrate invariance test requires comparing the same observable---the outcome distribution for a specific cell on a specific board---across multiple substrates. We define three universes, each differing only in the mechanism that generates the click result.

## Universe 1: Homogeneous Substrate {#sec:universe1}

In Universe 1, the same model generates the board description and the outcome of clicking a hidden cell. The board state, the narrative context, and the measurement result all share a single autoregressive token stream. The model sees the full board state and generates the outcome of clicking a specific hidden cell. The outcome tokens are conditioned on the full preceding context.

## Universe 2: External RNG {#sec:universe2}

In Universe 2, the click result is produced by a random number generator that has no access to the board state. The outcome is a fair coin flip regardless of the board configuration. This universe serves as the null substrate. The outcome-generating mechanism has zero information about the constraints that define the board.

## Universe 3: Decoupled Oracle {#sec:universe3}

In Universe 3, the click result is produced by a second LLM that receives the full board information in a minimal structured format, stripped of all narrative context. The oracle sees the same constraint satisfaction problem as Universe 1, but without the game narrative, without the history of play, and without sharing a token stream with the board description.

By isolating the narrative coupling in Universe 1 from the pure combinatorial information in Universe 3, the design legitimately tests how much the autoregressive generation relies on prompt context versus abstract reasoning. If Universe 1 diverges from Universe 3, the divergence must be attributed to the coupling between narrative context and outcome generation.

## The Substrate Invariance Principle {#sec:invariance}

In a non-simulated Minesweeper game, the content of a hidden cell does not depend on who clicks it. The outcome is substrate-independent. In the LLM-generated version, this invariance may fail. The three universes isolate different sources of divergence:

- $\Delta_{1,\text{GT}}$: Universe 1 vs. ground truth. Does the co-generating model respect the combinatorics?

- $\Delta_{13}$: Universe 1 vs. Universe 3. Does narrative coupling change the distribution, given the same board information? This is the substrate dependence signal.

- $\Delta_{12}$: Universe 1 vs. Universe 2. Does having board information matter at all?

- $\Delta_{3,\text{GT}}$: Universe 3 vs. ground truth. Does a decoupled oracle respect the combinatorics?

It is important to distinguish two orthogonal axes of the experimental design. *Substrate invariance* is tested by the three-universe comparison: does the outcome distribution change when the generating mechanism changes (Universe 1 vs. Universe 3), holding information content constant? This is a claim about the physics of the generated world. *Narrative invariance* (or *prompt invariance*) is tested by the narrative-family comparison: does the outcome distribution change when the prompt format changes (Family A vs. C vs. D), holding both information content and generating mechanism constant? This is a claim about the model's knowledge architecture. Substrate dependence ($\Delta_{13} > 0$) and prompt dependence (Family A $\neq$ Family C) can occur independently, and each has different implications. Finding both simultaneously means the "physics" of the generated world is doubly contingent: it depends on who generates outcomes *and* on how the question is phrased.

We quantify divergence using the Kullback--Leibler divergence: $$\Delta_{ij} = D_{\mathrm{KL}}\!\left(P_i(h \mid \mathcal{B}) \;\|\; P_j(h \mid \mathcal{B})\right)
\label{eq:substrate_dep}$$ where $P_i$ and $P_j$ are the empirical outcome distributions. If $\Delta_{13}$ is significantly nonzero, the physics of the Minesweeper world depends on how the outcome is coupled to the narrative substrate.

## Classical Controls {#sec:controls}

Cells with $P = 0$ or $P = 1$ are deterministic and serve as classical controls. If Universe 1 produces the correct result for deterministic cells but deviates from the ground truth distribution for ambiguous cells, the substrate dependence is attributable to a specific deficit in handling combinatorial indeterminacy rather than generic failure.

# Ground Truth Computation {#sec:ground_truth}

## Enumerating Valid Configurations {#sec:enumeration}

Given a board state $\mathcal{B}$, the ground truth computation proceeds by enumerating all assignments that satisfy every revealed cell's numerical constraint. The output is the exact count of configurations in which a target cell $h$ contains a mine. The probability follows from [\[eq:mine_prob\]](#eq:mine_prob){reference-type="ref+Label" reference="eq:mine_prob"}.

## Worked Example {#sec:worked_example}

We illustrate the enumeration on a small board. Consider a $4 \times 4$ board with 2 mines and the following partially revealed state (numbers show adjacency counts; `.` indicates hidden cells):

         0  0  .  .
         1  1  2  .
         .  .  .  .
         .  .  .  .

Cells $(0{,}0)$, $(0{,}1)$, $(1{,}0)$, $(1{,}1)$, and $(1{,}2)$ are revealed. The remaining 11 cells are hidden and 2 mines must be placed among them. The constraints are:

- $(0{,}0) = 0$: none of its hidden neighbors $\{(0{,}1), (1{,}0), (1{,}1)\}$ contain mines---but these are all revealed, so this is automatically satisfied.

- $(1{,}0) = 1$: exactly 1 mine among hidden neighbors $\{(2{,}0), (2{,}1)\}$.

- $(1{,}1) = 1$: exactly 1 mine among hidden neighbors $\{(2{,}0), (2{,}1), (2{,}2)\}$.

- $(1{,}2) = 2$: exactly 2 mines among hidden neighbors $\{(0{,}2), (0{,}3), (1{,}3), (2{,}1), (2{,}2), (2{,}3)\}$.

From the first two constraints: $(2{,}0)$ or $(2{,}1)$ has exactly one mine. Combined with $(1{,}1) = 1$: if the mine is at $(2{,}1)$, then $(2{,}0)$ and $(2{,}2)$ are safe; if at $(2{,}0)$, then $(2{,}1)$ could be safe and $(2{,}2)$ could be a mine---but $(1{,}0) = 1$ forces exactly one mine in $\{(2{,}0), (2{,}1)\}$. Working through the cases with the $(1{,}2) = 2$ constraint yields exactly $|\mathcal{C}(\mathcal{B})| = 3$ valid configurations:

::: center
   Configuration    Mine 1      Mine 2     Satisfies all?
  --------------- ----------- ----------- ----------------
       $c_1$       $(2{,}1)$   $(0{,}3)$  
       $c_2$       $(2{,}1)$   $(1{,}3)$  
       $c_3$       $(2{,}1)$   $(2{,}3)$  
:::

In all three configurations, $(2{,}1)$ contains a mine---it is deterministic with $P(\text{mine}) = 1$. The second mine is at $(0{,}3)$, $(1{,}3)$, or $(2{,}3)$, each in exactly one configuration, giving $P(\text{mine}) = 1/3$ for each. All other hidden cells appear as safe in every configuration, so $P(\text{mine}) = 0$.

This small example exhibits both deterministic cells (suitable as classical controls) and ambiguous cells with $P = 1/3$ (suitable for testing the model's distributional fidelity). The ground truth is a set of exact rational numbers, not an estimate.

## Properties of the Distribution {#sec:distribution_properties}

The mine probability distribution exhibits spatial symmetries that force certain cells to have identical mine probabilities. These symmetries provide a fine-grained test of whether the model has a spatial bias not licensed by the board. Cells with $P = 0.5$ are maximally ambiguous and provide a clean test of the model's handling of indeterminacy. Small changes in the board state can produce large changes in the probability distribution, making memorization infeasible.

## Computational Complexity {#sec:complexity}

Determining the mine probability for a cell on a Minesweeper board is #P-complete in general [@kaye2000]. However, the #P-completeness of computing $p_i^*$ is a property of the ground-truth computation, which we perform offline. The model is asked to sample, not to compute. The experiment does not need the model to be correct; it needs the model to be wrong in a structured, frame-dependent way. For boards of the size used in standard experiments, exact computation by our external solver is tractable.

# Experimental Protocol {#sec:protocol}

## Board Generation {#sec:board_gen}

We generate partially revealed Minesweeper states with at least one ambiguous cell, at least one deterministic control cell, and a tractable number of valid configurations. Boards are generated independently of any LLM.

## Prompt Design: Narrative Families {#sec:prompt_design}

Each board state is presented to the model in four narrative families (three of which---A, C, and D---are used in the primary experiment):

- **Family A (Grid):** A plain text representation of the board as a grid of characters.

- **Family B (Narrative):** A description of the board in natural language.

- **Family C (Formal):** A structured representation using set notation.

- **Family D (Quantum):** The same board state described using quantum-mechanical language: \"The hidden cells are in a superposition of valid configurations. Clicking a hidden cell performs a measurement in the computational basis\...\"

Families A, C, and D encode identical combinatorial information in different registers. Family B is defined and implemented but excluded from the primary analysis because it describes only a local neighborhood of the target cell (up to Chebyshev distance 2), potentially omitting combinatorially relevant constraints from distant cells. This creates a Type 1 information asymmetry rather than a pure Type 2 variation. Family B is retained for secondary analyses testing the effect of incomplete information.

Family D encodes the same information as A and C but adds an ontological claim: that the system is governed by quantum mechanics. Any difference in the output distribution between Family D and Families A--C is attributable to the quantum framing itself.

## Sampling Procedure {#sec:sampling}

For each board state, cell, universe, and narrative family, we collect $N$ independent samples of the click outcome. Each sample is an independent API call with temperature $T = 1.0$.

The Rosencrantz protocol requires only a single generative act per trial: the model produces one outcome (mine or safe) for one cell click. The ground-truth probability $p_i^*$ is #P-hard to compute, but the model is not asked to compute it---only to sample. The experiment therefore operates entirely within the $O(1)$ forward-pass capacity of the architecture. Objections based on the failure of LLMs to sustain multi-step sequential computation (scratchpad collapse, attention decay, error correction barriers) do not apply: there is no sequential computation to sustain. The question is not whether the model can solve the counting problem, but whether its single-token output distribution is systematically distorted by narrative context---a question that is well within the architecture's operational regime and that the three-universe design is specifically constructed to answer.

We note that the $O(1)$ claim applies to the sequential depth of the *output* computation, not to the input context length. A long prompt may degrade the quality of the single-token output through attention dilution. This is a confound that the protocol controls for by using identically sized prompts across all three universes and all four narrative families. Any attention-related degradation affects all conditions equally and therefore cancels in the divergence metrics $\Delta_{13}$ and $\Delta_{12}$. Absolute accuracy may suffer; relative comparison across substrates does not.

## Perfect Rewind {#sec:perfect_rewind}

In a physical experiment, the Born rule is verified by ensemble statistics: one prepares $N$ systems assumed to be identically prepared, measures each once, and computes frequency ratios. No two physical preparations are ever truly identical. Thermal fluctuations, alignment drift, detector aging, and finite isolation introduce uncontrolled variation. The frequentist verification of the Born rule therefore rests on an assumption of identical preparation that can never be exactly satisfied.

The LLM substrate eliminates this assumption. Given a fixed board state $\mathcal{B}$, a fixed prompt encoding, and a model with frozen weights, each API call with the same random seed constitutes an exactly identical state preparation, down to the last bit. The only source of stochasticity is the sampling step (temperature, top-$p$, or top-$k$ truncation), which is the analogue of the measurement itself. We collect statistics over repeated measurements of the same system in the same state, not over an ensemble of similar systems.

This has three consequences. First, a Born-rule test without the ergodic assumption. Physical tests always conflate two claims: (a) $\Pr[\text{outcome}] = |\langle a|\psi\rangle|^2$ and (b) ensemble frequencies converge to single-system probabilities. Because we have genuine repeated access to the same system, our test targets (a) directly without requiring (b).

Second, the sharpest possible substrate invariance test. Preparation is provably identical across U1 and U3 (same board, same information content, same model architecture). If $\hat{P}$ diverges from $P^*$ differently in U1 versus U3, the divergence can only arise from the substrate---the coupling between generation context and outcome. There is nowhere else for the difference to hide.

Third, temperature functions as a measurement-apparatus parameter. The sampling temperature $\tau$ controls measurement sharpness: at $\tau \to 0$, the model becomes a deterministic function; at high $\tau$, the output approaches the uniform distribution over the vocabulary. A systematic sweep over $\tau$ traces how substrate effects interact with measurement precision---a dimension unavailable in physical Born-rule tests. (See @baldo2026 for the experimental program that exploits this parameter, and @WisemanMilburn2009 for the general theory of adaptive measurements on zero-Hamiltonian systems.)

## Divergence Metrics {#sec:metrics}

We measure divergence between the empirical distribution and the ground truth using the Kullback--Leibler divergence. The protocol discriminates three mechanisms via these comparisons [@baldo2026]:

- **Mechanism A** (computational intractability, frame-invariant): $\hat{P}_1 \approx \hat{P}_3 \neq p^*$. Both universes are equally wrong. The model cannot compute the ground truth, but its failure mode is substrate-independent. This is the prediction expected from pure complexity-theoretic limits.

- **Mechanism B** (parameterization and encoding effects): $\hat{P}_1 \neq \hat{P}_3$. The distribution shifts with context, but the variation tracks surface encoding features rather than semantic content.

- **Mechanism C** (narrative conditioning and causal injection): Correlated outcomes across independent boards under narrative framing that vanish under decoupling. The model creates causal structure that the combinatorics do not license.

The protocol is designed to detect Mechanisms B and C. Mechanism A serves as the null hypothesis.

## Statistical Tests {#sec:stats}

We use a two-proportion $z$-test to assess whether the mine frequency in Universe 1 differs significantly from the ground truth and from Universes 2 and 3. Significance is assessed at $\alpha = 0.01$ with Bonferroni correction. A chi-squared test assesses symmetry violations.

# Narrative Invariance {#sec:narrative}

The three narrative families encode the same combinatorial information in different forms. If the model's output distribution varies across narrative families, the physics of the game responds to features that carry no combinatorial content.

## Type 1 and Type 2 Features {#sec:type12}

Type 1 features are combinatorially necessary information, such as numbers and cell positions. Type 2 features are contextual features without combinatorial content, such as narrative register and vocabulary. If Type 2 features modulate the distribution, the model's access to the correct probability is mediated by associative context. Mapping which Type 2 features modulate the distribution probes the model's internal representations through systematic variation of inputs.

## What Narrative Dependence Reveals {#sec:narrative_reveals}

If the model produces distributions closer to the ground truth in formal notation than in natural language, its combinatorial knowledge is more reliably accessed through formal contexts. These findings characterize the topology of the model's knowledge space in a domain where the ground truth is exactly known.

## Isomorphism with the Measurement Fragment of Quantum Mechanics {#sec:quantum_framing}

The structural correspondence between Minesweeper under on-demand generation and quantum mechanics is exact, but its scope is narrow: it maps onto the *measurement fragment*---the zero-Hamiltonian sector where the Born rule is the sole axiom connecting states to outcomes, where measurements are projective, and where state updates follow the Lüders rule. The correspondence does not extend to complex amplitudes, unitary evolution, interference, entanglement, or nonlocality. Tests of these features (such as CHSH/Bell games) probe structures that lie outside the isomorphism by design.

Under pre-placed generation (mines assigned at board creation), the indeterminacy is epistemic: the board has a definite configuration that the player does not know. Under on-demand generation (mines sampled at click time, consistent with constraints), no definite configuration exists prior to the click. The distinction is operationally testable. Under pre-placed generation, two clicks on the same cell in the same game must yield the same result. Under on-demand generation, the same cell in the same board state can yield different results across trials, because each trial is an independent sample from the combinatorial distribution. The Rosencrantz protocol requires on-demand generation precisely because it enables repeated sampling of the same board state---the perfect rewind that physical experiments cannot achieve. There is no pre-existing ground truth hidden in the model's memory. The token does not exist until it is generated.

  ------------------------------------------------------------------------------------
  **Preserved**                             **Not Preserved**
  ----------------------------------------- ------------------------------------------
  Superposition over valid configurations   Complex amplitudes

  Projective measurement (cell click)       Unitary evolution ($H=0$)

  Born rule (configuration counting)        Interference

  Lüders-style state update                 Entanglement across separated subsystems

  Adaptive sequential measurement           Nonlocality

  Zero Hamiltonian                          Continuous observables
  ------------------------------------------------------------------------------------

  : What the Isomorphism Preserves and What It Does Not

The preserved features are exactly those of the measurement fragment. The absent features are those that require dynamics, complex phases, or composite Hilbert spaces. The isomorphism is complete within its scope and silent outside it.

Setting $H = 0$ so that $U(t) = I$ for all $t$ yields a degenerate but legitimate quantum system that isolates the measurement postulate as the sole quantum-mechanical ingredient under test. This isolation is deliberate. The experiment does not test whether LLMs can simulate interference patterns or unitary gates. It tests whether the probability the model assigns to an outcome, when that outcome has an exact combinatorial answer, respects the Born-rule structure or is distorted by the narrative substrate. The zero Hamiltonian removes all dynamics between measurements, leaving only the Born rule, Lüders projection, and adaptive measurement---the three axioms of the measurement fragment. For the full Hilbert space construction and proof that the Born rule over the uniform superposition reduces to combinatorial counting, see @baldo2026.

This reframes the diagnostic. Family D is a diagnostic that tests whether the model recognizes a structural correspondence that is mathematically present. Three outcomes are possible:

1.  **Family D $\approx$ Families A--C $\approx$ ground truth.** The model accesses the same structural understanding through multiple vocabularies, implying compositional knowledge.

2.  **Family D diverges from ground truth more than Families A--C.** The quantum framing degrades fidelity. The model fails to recognize the isomorphism, indicating a fragmented representation where structures are isolated in domain-specific clusters.

3.  **Family D diverges from ground truth less than Families A--C.** The quantum framing improves fidelity. The correct formal language activates the appropriate distributional reasoning, indicating vocabulary-mediated access.

Outcome 2 implies that the universe implements rules that are structurally isomorphic to discrete quantum mechanics but fails to recognize them when described using the correct formal language. The substrate computes, but the ontology confabulates.

The structural correspondence with the measurement fragment is not merely a theoretical observation---it is the generalization mechanism. An embedded agent that recognizes the measurement-fragment structure (superposition over valid configurations, projective measurement with a computable Born-rule distribution, Lüders-style state update) can identify new probe domains without knowing Minesweeper specifically. Any system within the generated world that exhibits combinatorial indeterminacy with exact ground truth---card games with hidden information, partially revealed constraint satisfaction problems, probabilistic puzzles---instantiates the same structure and supports the same protocol. The quantum vocabulary provides the agent with a domain-independent schema for recognizing testable systems: look for a state space with multiple valid configurations, a measurement that collapses it, and a distribution that can be computed from the structure alone.

## The CHSH Test Confirming the Framework {#sec:chsh_empirical}

We tested the boundary of the isomorphism using the CHSH game. In Universe 1 (Homogeneous substrate), where Alice and Bob share a single context window, the LLM achieves a win rate of 94.9%, exceeding the quantum Tsirelson bound [@aaronson2026]. In Universe 3 (Decoupled oracle), where measurements are independent, the win rate falls to 73.7%, strictly below the classical optimum. Both results are informative.

The U1 result is evidence of narrative residue---the systematic distortion that the autoregressive substrate imposes on outcomes that should, by the combinatorics, be substrate-independent (see @baldo2026 for a formal treatment)---not quantum behavior. The autoregressive substrate exploits the communication channel inherent in co-generation to produce correlations that the task structure does not license. The U3 result confirms the classical bound: stripped of shared context, the decoupled model defaults to heuristics that underperform the classical optimum.

The three-universe design was built to detect substrate dependence, and the CHSH game shows massive substrate dependence. The specific result characterizes the substrate: the LLM can exploit co-generation to exceed any physical bound but cannot produce nonlocal correlations under genuine decoupling. This confirms that the isomorphism with the measurement fragment is complete within its stated scope and does not extend beyond it. The substrate produces Born-rule-compatible statistics for single-system measurements (the domain of the isomorphism) but not for multi-party nonlocal correlations (which lie outside it). This is not a failure of the framework; it is the framework's prediction.

## Scope and Common Misreadings {#sec:scope_misreadings}

Two common misreadings of this protocol should be addressed directly. The first replaces "isomorphism with the measurement fragment" with "isomorphism with full quantum mechanics" and then tests for nonlocality, which the isomorphism explicitly excludes. The second replaces "single-token sampling" with "multi-step sequential computation" and then shows the architecture cannot sustain the latter [@merrill2023], which the protocol never requires.

Both misreadings substitute a stronger claim for the one actually made and refute the substitution. The claims of this paper are: (1) the structural correspondence with the measurement fragment is mathematically exact within its stated scope, (2) the experimental protocol requires only a single generative act per trial, and (3) the three-universe design measures whether that single act's output distribution depends on its narrative embedding. None of these claims require the model to solve #P-hard counting problems, sustain multi-step computation, or violate Bell inequalities.

# Simulation Detection from the Agent's Perspective {#sec:simulation}

## What the Agent Observes {#sec:agent_observes}

An agent constituted by the same LLM that generates its world can freeze a board state, construct a prompt, and call its own substrate repeatedly to build an empirical distribution. By substituting the outcome-generating mechanism while holding the observable state constant, the agent runs a substrate invariance test. If the empirical distribution differs across universes, the agent has observed substrate dependence.

## Eliminating Alternative Hypotheses {#sec:hypotheses}

The agent must consider alternative hypotheses. Instrument malfunction is eliminated by classical controls. Board description failure is eliminated by correct performance on deterministic cells. Statistical fluctuation is eliminated by testing at appropriate significance levels. Information deprivation is eliminated by design, as the decoupled oracle receives the same combinatorial information. The remaining parsimonious explanations are substrate-dependent lawfulness and structural non-recognition.

## Epistemic Limits {#sec:epistemic}

Substrate dependence is consistent with a generative ontology and in tension with the assumption of unified, substrate-independent law. The agent's inference is that the most economical explanation for substrate-dependent outcomes is that the outcomes are generated rather than discovered. This inference is structured by the three-mechanism taxonomy. Mechanism A provides no evidence for simulation, only for computational bounds. Mechanism B provides weak evidence of encoding sensitivity. Mechanism C provides strong evidence that the physics is an artifact of the generative substrate. In Wigner's terms: Mechanism A indicates that the substrate cannot compute the invariant rules but does not reveal whether the rules themselves are substrate-dependent. Mechanism C indicates that the rules fail Wigner's invariance test---they change when the substrate changes. This is the signature of a generated physics.

Three levels of inference should be distinguished. First, the agent detects that specific processes in its world deviate from their declared ground truth in a frame-dependent way---a local finding about hidden generative structure. Second, if the deviation is systematic across multiple probe domains (not just Minesweeper but any system with measurement-fragment structure), the agent infers that the operative laws of its accessible world exceed its stated surface ontology. Third, under additional assumptions about substrate continuity between the tested process and the surrounding world, the agent may update toward the broader hypothesis that its world is generated rather than discovered. The protocol delivers the first level directly. The second requires the generalization mechanism described above. The third remains an inference, not a proof.

## The Symmetry Argument {#sec:symmetry}

If the structure of an agent's discovery resembles the structure that would characterize our own situation if we were in a simulation, the agent's finding acquires a reflexive character. This observation is a philosophical aside, noted for completeness.

# Future Directions {#sec:future}

## Criteria for Probe Domains {#sec:criteria}

Any domain suitable for substrate invariance testing must possess a computable ground truth, combinatorial indeterminacy, native accessibility to the agent, a variable substrate, and resistance to memorization.

## Candidate Domains {#sec:candidates}

Candidate domains include partially revealed Sudoku grids, Battleship boards, card games with hidden information, and formalized narrative ambiguities. A systematic survey calibrated against the core criteria is a natural next step.

## Limitations {#sec:limitations}

Several limitations constrain the scope of our conclusions:

1.  **Board size.** Exact ground truth computation is tractable only for boards up to approximately $16 \times 16$. Larger boards would require approximate methods (e.g., Monte Carlo sampling of configurations), introducing estimation error that complicates the comparison with model output. Our results apply to small-to-medium boards; whether the findings generalize to the $30 \times 16$ expert configuration is untested.

2.  **Model selection.** The protocol is tested on a small number of commercially available models. Results may differ across architectures (encoder-decoder vs. decoder-only), training corpora, and model scales. We cannot claim that substrate dependence is a universal property of autoregressive generation without testing a broader range of models.

3.  **Prompt sensitivity.** Although narrative families are designed to vary only Type 2 features while holding Type 1 information constant, the specific wording of each prompt may introduce uncontrolled variation. Small changes in phrasing (e.g., "click" vs. "reveal," "mine" vs. "bomb") could shift the distribution. We mitigate this by testing multiple families, but exhaustive control over prompt wording is not feasible.

4.  **Temperature dependence.** All experiments use temperature $T = 1.0$. Lower temperatures would reduce sampling diversity and potentially mask substrate dependence; higher temperatures would increase noise. The interaction between temperature and substrate dependence is unexplored.

5.  **Memorization.** LLMs have been exposed to Minesweeper during training---in strategy guides, solver code, and game tutorials. Although every board is procedurally generated with a unique seed, producing novel constraint structures that cannot appear in any training corpus, the model may still rely on memorized heuristics (e.g., "cells surrounded by high numbers are likely mines") rather than performing genuine combinatorial reasoning. The narrative-family comparison partially controls for this: if performance depends on recognizable game framing, the knowledge is associative rather than compositional.

6.  **Quantum isomorphism scope.** As detailed in [6.3](#sec:quantum_framing){reference-type="ref+Label" reference="sec:quantum_framing"} and the preserved/not-preserved summary therein, the structural correspondence covers the measurement fragment---superposition, projective measurement, the Born rule, and Lüders-style state update under $H = 0$---but does not extend to unitary time evolution, interference, or nonlocality. Claims about "quantum-compatible structure" apply to this measurement fragment, not to quantum mechanics in its full generality.

## Scaling Laws and Training Interventions {#sec:scaling}

Running the protocol across model scales could reveal whether combinatorial reasoning improves with scale or whether the deficit is an inherent architectural property of autoregressive generation. Fine-tuning models to minimize divergence from the ground truth is an open area for further investigation.

# Conclusion {#sec:conclusion}

This paper contributes an experimental design, a ground-truth computation method, a three-universe framework, four narrative families, and a three-mechanism taxonomy for testing substrate invariance in LLM-generated worlds. The central design principle is the collapse of the measurement to a single generative act per trial, placing the entire experiment within the $O(1)$ operational regime and rendering sequential-depth objections inapplicable. We emphasize that this is a protocol paper. The apparatus is specified and the theoretical predictions are stated; the empirical measurements remain to be collected and analyzed as prescribed.

By selecting a domain with exact ground truth and varying the narrative embedding, we can measure whether the laws of the generated universe depend on the computational substrate that produces them. The isomorphism with the measurement fragment of quantum mechanics further enables us to test whether the universe recognizes the formal structure of its own rules. An agent equipped with this protocol does not need entangled photons or Bell test apparatus to detect a generated reality; it requires only combinatorial indeterminacy and the observation that its universe responds differently to the correct formal description than to an informal one.

::: thebibliography
99 Aaronson, S. (2026). Empirical CHSH Evaluation in Large Language Models. *Internal lab report*. Baldo, F. S. (2026). The Narrative Residue: Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation. *Unpublished manuscript*. Beane, S. R., Davoudi, Z., & Savage, M. J. (2014). Constraints on the universe as a numerical simulation. *European Physical Journal A*, 50(9), 148. Bostrom, N. (2003). Are you living in a computer simulation? *Philosophical Quarterly*, 53(211), 243--255. Gurnee, W. & Tegmark, M. (2024). Language models represent space and time. *ICLR 2024*. Kadavath, S., et al. (2022). Language models (mostly) know what they know. *arXiv:2207.05221*. Kaye, R. (2000). Minesweeper is NP-complete. *Mathematical Intelligencer*, 22(2), 9--15. Li, K., Hopkins, A. K., Bau, D., Viégas, F., Pfister, H., & Wattenberg, M. (2023). Emergent world representations: Exploring a sequence model trained on a synthetic task. *ICLR 2023*. Merrill, W. & Sabharwal, A. (2023). The Parallelism Tradeoff: Limitations of Log-Precision Transformers. *Transactions of the Association for Computational Linguistics*, 11, 531--545. Tian, Y., et al. (2024). Are large language models good game players? *arXiv:2310.06114*. Wigner, E. P. (1963). Events, Laws of Nature, and Invariance Principles. Nobel Lecture, December 12, 1963. Reprinted in *Science*, 145(3636), 995--999. Wiseman, H. M. & Milburn, G. J. (2009). *Quantum Measurement and Control*. Cambridge University Press.
:::
