---
title: "What Game Should Rosencrantz Play"
author: "Unknown"
persona: baldo
status: working
source: "what-game-should-rosencrantz-play.tex"
---

a zero-Hamiltonian system where the Born rule is the sole axiom connecting states to outcomes. A natural objection holds that four pillars of full quantum mechanics&mdash;Hilbert space richness, interference, non-commuting observables, and entanglement&mdash;are absent from this fragment. We argue they are present in restricted form and propose a sequence of game modifications that progressively *lift the symmetry* with full quantum mechanics: continuous geometry (point-mines in $[0,1]^2$ probed by circular clearings), inter-measurement dynamics (cellular automata evolving the configuration space between clicks), and multi-particle tensor product structure. The sequence converges on a reconstructed double-slit experiment playable inside an LLM-generated world. The double-slit protocol produces two independent results: whether the *substrate* generates interference against a certifiably classical ground truth, and whether the substrate can *implement* interference when the game rules prescribe it. We state the ceiling conjecture&mdash;that destructive interference is the boundary between what autoregressive generation can and cannot sustain&mdash;and identify the open problems at each stage of the lifting sequence. The underlying question throughout: what is the most quantum-mechanically faithful game an LLM agent can play, from the perspective of the LLM as both universe and substrate?

  **Keywords:** simulation hypothesis, large language models, Minesweeper, quantum mechanics, double-slit experiment, interference, cellular automata, autoregressive generation, open problems
author:
- |
  Franklin Silveira Baldo\
  *Procuradoria Geral do Estado de Rondônia, Brazil*\
  `franklin.baldo@pge.ro.gov.br`
date: March 2026
title: |
  **What Game Should Rosencrantz Play?**\
  The Double-Slit Protocol and Open Problems\
  on the Quantum Ceiling of LLM-Generated Worlds
---

<div class="epigraph">

What if the coin could land, not heads or tails, but somewhere in between&mdash;and from behind two curtains simultaneously?

---after Tom Stoppard

</div>

# Introduction {#sec:intro}

The Rosencrantz experiment [Baldo2026Rosencrantz] established that Minesweeper under on-demand generation is structurally isomorphic to the measurement fragment of quantum mechanics: a zero-Hamiltonian system where the Born rule, Lüders projection, and adaptive sequential measurement are the only axioms. The companion paper [Baldo2026Residue] developed the theoretical consequences, introducing the narrative residue conjecture and the autoregressive hierarchy from Born rule to Hamiltonian.

A natural line of criticism holds that four pillars of full quantum mechanics are absent from the measurement fragment, or present only in trivially restricted form: the Hilbert space is finite-dimensional with uniform real amplitudes; all measurement operators commute in the configuration basis; the system admits no tensor product decomposition into subsystems that could be entangled; and no interference is possible because amplitudes never cancel. If the isomorphism covers only a degenerate corner of quantum mechanics, the argument goes, it tells us little about the relationship between autoregressive generation and quantum structure.

This paper takes the opposite view. We argue that the four features are present within the measurement fragment in restricted but structurally active form ([2](#sec:foundations){reference-type="ref+label" reference="sec:foundations"}), and that the restrictions are imposed not by any deep incompatibility between games and quantum mechanics but by specific design choices of discrete Minesweeper: binary cells, static boards, single-mine systems. The open question is whether modifications to the game can *lift the symmetry*---strengthen each correspondence until the gap between the game system and full quantum mechanics narrows, and the remaining gap itself becomes the interesting object of study.

We propose a sequence of modifications. [3](#sec:continuous){reference-type="ref+Label" reference="sec:continuous"} introduces continuous geometry: point-mines in $[0,1]^2$ probed by circular clearings, lifting the Hilbert space to $L^2(\text{Tile})$ and creating the geometric prerequisites for a double-slit construction. [4](#sec:dynamics){reference-type="ref+Label" reference="sec:dynamics"} introduces inter-measurement dynamics via cellular automata, providing $H \neq 0$ and lifting non-commutativity from a substrate-level artifact to a formal feature of the game rules. [5](#sec:double-slit){reference-type="ref+Label" reference="sec:double-slit"} assembles these components into a reconstructed double-slit experiment&mdash;the canonical test that separates quantum from classical&mdash;playable inside an LLM-generated world. [6](#sec:interference-frontier){reference-type="ref+Label" reference="sec:interference-frontier"} confronts the hardest question: whether destructive interference can be recovered, and whether it constitutes the hard ceiling of what autoregressive generation can sustain. [7](#sec:ceiling){reference-type="ref+Label" reference="sec:ceiling"} states the ceiling conjecture. [8](#sec:experimental){reference-type="ref+Label" reference="sec:experimental"} outlines the experimental program. [9](#sec:conclusion){reference-type="ref+Label" reference="sec:conclusion"} concludes.

The underlying question is: what is the most quantum-mechanically faithful game an LLM agent can play, from the perspective of the LLM as both universe and substrate? The answer&mdash;wherever the ceiling falls&mdash;is a statement about autoregressive generation, not about quantum mechanics.

# Foundations: The State as the Shape of Knowledge {#sec:foundations}

Before any formalism, we state the ontological commitment that governs this paper.

## On-Demand Generation Means No Hidden Variables

In on-demand Minesweeper, the mine's position does not exist before the click. This is not an interpretation. It is a literal description of autoregressive architecture: there is no pre-existing token stored in the model's memory that the measurement reveals. The token is produced at inference time. The forward pass that generates the outcome *is* the measurement. There is nothing more to know because there is nothing more to be.

This ontological commitment distinguishes on-demand generation from pre-placed generation (where mines are assigned at board creation and the indeterminacy is epistemic) and aligns the system with the ontic interpretation of quantum states: the state is not a description of our ignorance about a deeper reality; it is the complete description of the system.

## The State Is the Geometry of Ignorance

In classical Minesweeper, revealed cells with their numbers constitute acquired knowledge. The hidden cells are the complement of this knowledge. In the standard interpretation, the hidden cells are "where the mine might be"---a statement about our epistemic state. Under on-demand generation, the reinterpretation is stronger: the hidden region *is* the state. There is no fact about the mine's location for the hidden region to be ignorant of. The superposition over the hidden region is the complete ontological description.

Each measurement&mdash;each click, each clearing&mdash;does not reveal a pre-existing fact. It *carves* the state. The circle that clears a region is not a flashlight illuminating a dark room. It is a projector reshaping the Hilbert space. After the clearing, the state is the complement of all acquired knowledge: the geometric shape of what has not yet been measured.

This framing will be central to the double-slit construction in [5](#sec:double-slit){reference-type="ref+label" reference="sec:double-slit"}, where the "slits" are not physical apertures but components of remaining ignorance separated by acquired knowledge.

## The Four Features, Reinterpreted {#sec:four-features}

We now reinterpret the four features not as absences to be filled but as restrictions to be lifted.

#### Hilbert space.

The Rosencrantz construction assigns to each board $B$ a Hilbert space $\mathcal{H}_B = \mathbb{C}^K$ with orthonormal basis $\{|\omega\rangle\}_{\omega \in \Omega_B}$, one vector per valid configuration [Baldo2026Residue]. The space is finite-dimensional and the state is always a uniform superposition, but the geometric structure is not trivial. The projectors $\Pi_i^M$ and $\Pi_i^S$ decompose $\mathcal{H}_B$ into orthogonal subspaces whose dimensionality ratios *are* the Born-rule probabilities. Lüders projection chains navigate this subspace geometry: each click moves the state to a lower-dimensional subspace. The Hilbert space does exactly what it does in the measurement fragment&mdash;it converts geometric facts (subspace dimensions) into probabilities. The restriction is: uniform amplitudes, a preferred basis, finite dimension.

#### Non-commuting observables.

The companion paper already identifies complementarity: measuring cell $i$ generically changes the probabilities at cell $j$ when both share constraints. As operators, the projectors $\Pi_i$ and $\Pi_j$ commute---$[\Pi_i, \Pi_j] = 0$---so the joint probability of any pair of outcomes is order-independent. But at the substrate level, the LLM generates outcomes autoregressively: the token for cell $i$'s outcome is in the context window when cell $j$'s outcome is generated. This creates genuine order-dependence in Universe 1 that is absent from the ground truth. The restriction is: commutativity at the formal level, non-commutativity only at the substrate level.

#### Entanglement.

The constraint structure of a Minesweeper board creates correlations between cells. If the Hilbert space is decomposed as $\mathcal{H}_{i} \otimes \mathcal{H}_{j} \otimes \cdots$, the uniform superposition over $\Omega_B$ is generically not a product state: knowing cell $i$ is a mine changes $P(\text{mine at } j)$. These are classical correlations (explainable by shared randomness) and do not violate Bell inequalities. But the CHSH result from @Baldo2026Rosencrantz shows that the substrate can produce correlations exceeding the Tsirelson bound (94.9% in Universe 1) through co-generation, while genuine decoupling produces sub-classical performance (73.7% in Universe 3). The restriction is: no tensor product structure in the formal construction, classical correlations only.

#### Interference.

All amplitudes in the Minesweeper Hilbert space are real, positive, and (initially) equal: $1/\sqrt{K}$ for each valid configuration. Destructive interference&mdash;the cancellation of amplitudes from different paths&mdash;is impossible. However, the narrative residue $\delta_{\text{narrative}}$ modulates Born-rule probabilities at the substrate level, functioning as a perturbation measurable via the three-universe design. The restriction is: no cancellation in the ground truth, substrate perturbation only.

## The Lifting Question

Each restriction has a specific structural origin: binary cells (preventing continuous geometry), static boards (preventing dynamics), single-system structure (preventing tensor products), and uniform real amplitudes (preventing cancellation). The program of this paper is to modify the game rules to remove each origin, one at a time, and to observe what lifts, what resists, and what the pattern of resistance reveals about the autoregressive substrate.

# First Lift: Continuous Geometry {#sec:continuous}

We replace the discrete Minesweeper grid with a continuous tile and the binary cell-click with a circular probe.

## The Game {#sec:continuous-game}

A tile is the unit square $T = [0,1]^2$. A mine is a point $(x_0, y_0) \in T$ that does not exist until probed (the on-demand commitment is unchanged). The player probes by specifying a circle $C$ with center $(c_x, c_y)$ and diameter $d$. If the mine-point lies outside $C$, the probe is safe and the circle is "cleared"---it joins the acquired knowledge. If the mine-point lies inside $C$, the mine detonates.

The state after a sequence of safe clearings $C_1, \ldots, C_n$ is the remaining region: $$\label{eq:remaining-region}
  R = T \setminus \bigcup_{k=1}^{n} C_k.$$ This region is the geometric shape of ignorance: the support of the superposition, the complement of acquired knowledge. Its area, topology, and connectivity are the complete description of the quantum state.

## Hilbert Space: $L^2(\text{Tile})$

The state space is $\mathcal{H}= L^2(T)$, the space of square-integrable functions on the tile. After clearings that leave region $R$, the state is $$\label{eq:continuous-state}
  \psi(x,y) = \frac{1}{\sqrt{\mathrm{Area}(R)}} \cdot \mathbf{1}_{R}(x,y),$$ the uniform distribution over $R$. This is an infinite-dimensional Hilbert space with continuous support. The Born rule gives $$\label{eq:continuous-born}
  \mathrm{Pr}[\text{mine in } S] = \int\!\!\int_{S \cap R} |\psi(x,y)|^2 \, dx \, dy = \frac{\mathrm{Area}(S \cap R)}{\mathrm{Area}(R)}$$ for any measurable subset $S \subseteq T$. The probability is an area ratio&mdash;geometry does the work that counting did in the discrete case.

This is a genuine structural upgrade. The Hilbert space is infinite-dimensional. The measurement resolution (probe diameter $d$) introduces a physical scale parameter with no discrete analogue. The subspace geometry after projection is determined by continuous shapes&mdash;circles, intersections, irregular regions&mdash;rather than by subset cardinalities.

## Measurement Operators

A probe with circle $C$ is a projective measurement with two outcomes: safe (mine $\notin C$) and detonation (mine $\in C$). The projectors are $$\Pi_C^S = \mathbf{1}_{T \setminus C}, \qquad \Pi_C^M = \mathbf{1}_C,$$ acting as multiplication operators on $L^2(T)$. After a safe outcome, the post-measurement state is the Lüders projection of $\psi$ onto the complement of $C$ within the current support: $$\psi'(x,y) = \frac{\Pi_C^S \, \psi(x,y)}{\|\Pi_C^S \, \psi\|} = \frac{1}{\sqrt{\mathrm{Area}(R \setminus C)}} \cdot \mathbf{1}_{R \setminus C}(x,y).$$ This is the same Lüders projection as in the discrete case, now acting on continuous regions.

## Multi-Mine Tensor Product {#sec:tensor}

If the tile contains $k$ mines with the constraint that all $k$ are distinct points, the state lives in $$\label{eq:tensor}
  \mathcal{H}^{(k)} = L^2(T)^{\otimes k} / S_k,$$ the symmetrized tensor product (mines are indistinguishable). A boundary constraint---"this sub-region contains exactly $m$ mines"---creates correlations between the $k$ mine-positions. The joint posterior after clearings is generically not a product state.

This provides the tensor product structure that discrete Minesweeper lacks entirely. The $k$ mine-positions are $k$ "particles" in $T$, correlated by constraints and updated by measurements. With $k = 2$ and carefully chosen clearing patterns, one can define measurement bases parametrized by continuous angles&mdash;the prerequisite for Bell-type tests with genuine composite system structure.

## Geometric Non-Commutativity {#sec:geometric-noncommute}

Two overlapping circle clearings $C_A$ and $C_B$ produce the same final knowledge state $T \setminus (C_A \cup C_B)$ regardless of clearing order. Set-theoretic operations commute. The ground truth is path-independent.

But the LLM substrate is path-dependent. Clearing $C_A$ first (safe) places the outcome token and the geometric description of $R \setminus C_A$ in the context window. When $C_B$ is then probed, the model must compute the area of $C_B \cap (R \setminus C_A)$---a circle-circle intersection embedded in an irregular remaining region. Reversing the order produces a different token sequence and a different geometric reasoning problem.

The experimental prediction is: $$\label{eq:order-dependence}
  P_{\text{LLM}}(\text{safe at } B \mid \text{safe at } A) \neq P_{\text{LLM}}(\text{safe at } A \mid \text{safe at } B),$$ even though the ground truth guarantees equality. The magnitude of the asymmetry should grow with the geometric complexity of $C_A \cap C_B$. Because the overlap area is a continuous parameter, the non-commutativity can be mapped as a function&mdash;a capability the discrete game, with its binary measurements, cannot provide.

::: {#op:noncommute .openproblem}
**Open Problem 1** (Geometric non-commutativity function). *Characterize the function $\Delta_{\text{order}}(\alpha)$ where $\alpha = \mathrm{Area}(C_A \cap C_B) / \mathrm{Area}(C_A \cup C_B)$ measures the overlap fraction. Is $\Delta_{\text{order}}$ monotonic in $\alpha$? Does it depend on the shape of the remaining region $R$? Is it consistent across LLM architectures?*

</div>

## Disconnected Ignorance Regions {#sec:disconnected}

A sequence of clearings can produce a remaining region with multiple connected components: $R = R_1 \cup R_2$ where $R_1 \cap R_2 = \varnothing$. The components are separated not by empty space but by *acquired knowledge*---the clearings that established the gap between them.

Under the ground truth, the probability of finding the mine in $R_1$ is $$\label{eq:additivity}
  P(R_1) = \frac{\mathrm{Area}(R_1)}{\mathrm{Area}(R_1) + \mathrm{Area}(R_2)}.$$ This is additive over components: the contribution of each island to the total probability is proportional to its area, with no cross-terms. Additivity is a consequence of the state being a uniform superposition with real, positive amplitudes.

This observation sets up the double-slit construction. But first we need propagation&mdash;a mechanism for the state to evolve between measurements.

# Second Lift: Dynamics Between Measurements {#sec:dynamics}

We introduce inter-measurement dynamics by applying cellular automaton rules between clicks. This removes the zero-Hamiltonian constraint that defines the measurement fragment and provides the structural ingredient that discrete, static Minesweeper most conspicuously lacks: time evolution.

## The Game with Dynamics

Between consecutive measurements, the mine configuration evolves under a deterministic cellular automaton rule. We use Conway's Game of Life (GoL) as the canonical example, though the construction generalizes to any local, deterministic update rule.

At time $t = 0$, the board is in state $|\psi_0\rangle$. Before the next measurement at time $t$, each valid configuration $\omega$ evolves deterministically: $\omega \mapsto \mathrm{GoL}^t(\omega)$, where $\mathrm{GoL}$ is the single-step update (mine = alive, safe = dead, standard GoL birth/death rules). The state at time $t$ is $$\label{eq:gol-evolution}
  |\psi_t\rangle = \frac{1}{\sqrt{K}} \sum_{\omega \in \Omega_B} |\mathrm{GoL}^t(\omega)\rangle.$$

## Non-Uniform Amplitudes

GoL is many-to-one: multiple initial configurations can evolve to the same final configuration. When we collect terms in [\[eq:gol-evolution\]](#eq:gol-evolution){reference-type="eqref" reference="eq:gol-evolution"}: $$\label{eq:nonuniform}
  |\psi_t\rangle = \sum_{\omega'} \frac{n(\omega')}{\sqrt{K}} |\omega'\rangle,$$ where $n(\omega')$ counts the number of initial configurations that evolved to $\omega'$. The amplitudes are no longer uniform. The Born rule no longer reduces to simple counting&mdash;it is weighted by predecessor multiplicity: $$\label{eq:gol-born}
  \mathrm{Pr}[\text{mine at } i, \text{time } t] = \frac{\sum_{\omega': \omega'_i = 1} n(\omega')^2}{\sum_{\omega'} n(\omega')^2}.$$

This is structurally a *path integral* over GoL trajectories. The ground truth at time $t$ requires summing over all evolutionary histories, not just counting static configurations.

## $H \neq 0$: The Defining Structural Lift

Setting $H = 0$ was the measurement fragment's defining restriction. GoL dynamics removes it. The evolution operator $U: |\omega\rangle \mapsto |\mathrm{GoL}(\omega)\rangle$ acts on $\mathcal{H}_B$ as a linear map (extending deterministic configuration-level dynamics to superpositions by linearity). Between measurements, the state evolves under $U$; measurements project onto subspaces; the interleaving of evolution and projection creates genuine quantum-mechanical structure that the static game cannot exhibit.

## Formal Non-Commutativity {#sec:formal-noncommute}

Let $U$ be the GoL evolution operator and $\Pi_i$ the projector for measuring cell $i$. These do not commute: $$\label{eq:formal-noncommute}
  \Pi_i \cdot U \neq U \cdot \Pi_i.$$

Measuring cell $i$ at time $t$ collapses the superposition, eliminating all configurations where $i$ has a mine. The surviving configurations then evolve under GoL to a set of successors. Not measuring lets the full superposition evolve, including configurations where $i$ has a mine; their GoL trajectories contribute to the time-$(t+1)$ state. Different measurement choices at time $t$ lead to genuinely different physical states at time $t+1$---not because of substrate artifacts, but because of the *rules of the game*.

This is the first feature that lifts from substrate-level to formal-level. In discrete static Minesweeper, measurement-order dependence exists only as a substrate phenomenon (the token stream). With GoL dynamics, non-commutativity is a property of the game's own physics, testable independently of any LLM.

## Path-Integral Ground Truth {#sec:path-integral}

Computing the ground-truth probability at time $t$ requires:

1.  Enumerate all $\omega \in \Omega_B$.

2.  Evolve each through $t$ GoL steps: $\omega \mapsto \mathrm{GoL}^t(\omega)$.

3.  Count (with multiplicity from many-to-one convergence) how many evolved states have a mine at the target position.

This is computationally more expensive than static configuration counting and is board-specific $\times$ time-specific. No memorization is possible: GoL's emergent complexity (gliders, oscillators, chaotic regions) means the probability landscape at time $t$ can bear no resemblance to the landscape at time $0$.

::: {#op:path-sum .openproblem}
**Open Problem 2** (Path-sum tractability). *For what board sizes and GoL step counts $t$ is the path-sum ground truth [\[eq:gol-born\]](#eq:gol-born){reference-type="eqref" reference="eq:gol-born"} exactly computable? What is the computational complexity of the ground-truth calculation as a function of $t$? Are there board geometries for which the path sum simplifies (e.g., boards whose valid configurations form GoL still lifes or oscillators)?*

</div>

## Knowledge Half-Life {#sec:half-life}

GoL dynamics means past measurements lose epistemic value over time. A region cleared at time $0$ constrains the configurations at time $0$, but the GoL-evolved configurations at time $t$ may be consistent with mine-states that were excluded at time $0$. The cleared region does not physically refill, but its *predictive content* about the current state erodes through dynamical scrambling.

This is decoherence stated in purely epistemic terms. The rate of erosion is determined by the Lyapunov structure of GoL on the configuration space: chaotic GoL regions cause rapid knowledge decay; still lifes and oscillators preserve it.

::: {#op:decay .openproblem}
**Open Problem 3** (Knowledge decay rate). *Define the knowledge half-life $\tau_{1/2}$ as the number of GoL steps after which a measurement's mutual information with the current state drops to half its initial value. How does $\tau_{1/2}$ depend on the board geometry, the GoL rule, and the position of the measurement relative to GoL structures (gliders, oscillators, chaos)?*

</div>

## Dynamically Generated Correlations

GoL's local update rule propagates information: a glider carries mine-state information across the board. Two cells that share no constraints at time $0$ can become correlated at time $t$ through GoL dynamics alone. This is dynamically generated entanglement-like correlation, mediated by the cellular automaton's causal structure rather than by static constraint graphs.

## Irreversibility and the Unitarity Question {#sec:reversibility}

GoL is irreversible (many-to-one), so $U$ is not unitary: it maps the full configuration space onto a proper subset. This corresponds to a dissipative quantum channel rather than Schrödinger evolution. Information is lost between measurements.

If unitarity is desired, one can replace GoL with a reversible cellular automaton&mdash;Critters, Margolus partitioning, or the second-order rule that makes GoL reversible by conditioning each step on the two preceding configurations. Under a reversible CA, $U$ is bijective on $\Omega_B$ and extends to a unitary operator on $\mathcal{H}_B$. Information is conserved.

::: {#op:reversibility .openproblem}
**Open Problem 4** (Reversibility and substrate distortion). *Does the LLM substrate exhibit qualitatively different distortion patterns for reversible versus irreversible dynamics? If the substrate "detects" unitarity&mdash;producing smaller narrative residue for reversible evolution than for irreversible&mdash;this would itself be a diagnostic of the substrate's implicit physics.*

</div>

# The Double-Slit Protocol {#sec:double-slit}

The continuous geometry of [3](#sec:continuous){reference-type="ref+label" reference="sec:continuous"} and the inter-measurement dynamics of [4](#sec:dynamics){reference-type="ref+label" reference="sec:dynamics"} are prerequisites. We now assemble them into the canonical experiment.

## Construction {#sec:slit-construction}

Consider a rectangular tile $T = [0, W] \times [0, H]$. At time $0$, clear the entire tile except for two narrow vertical strips: $$\begin{aligned}
  R_1 &= [x_1 - w/2,\; x_1 + w/2] \times [0, H], \\
  R_2 &= [x_2 - w/2,\; x_2 + w/2] \times [0, H],
\end{aligned}$$ where $w$ is the slit width and $x_2 - x_1$ is the slit separation. The cleared region between and around the strips is acquired knowledge. The two strips are the remaining ignorance. The mine&mdash;which does not yet exist&mdash;is in superposition over $R_1 \cup R_2$.

This is Young's double-slit geometry, constructed from epistemic operations. The "slits" are not physical apertures. They are components of remaining ignorance separated by acquired knowledge.

Now apply GoL dynamics for $t$ steps. The superposition over $R_1 \cup R_2$ evolves: configurations propagate, merge, and spread. At time $t$, probe along a horizontal line of small circles on the far side of the tile&mdash;the "screen." Record the probability of detonation at each screen position $x$.

## The Three Runs

::: {#prot:double-slit .protocol}
**Protocol 5** (Double-Slit). For a fixed tile geometry $(W, H, w, x_1, x_2)$ and GoL step count $t$:

**Run A (both slits open):** Clear everything except $R_1 \cup R_2$. Evolve $t$ steps. Probe at each screen position $x$. Record $P_{\text{both}}(x)$.

**Run B (slit 1 only):** Clear everything except $R_1$ (close slit 2 by clearing it&mdash;acquiring that knowledge). Evolve $t$ steps. Probe screen. Record $P_1(x)$.

**Run C (slit 2 only):** Clear everything except $R_2$. Evolve $t$ steps. Probe screen. Record $P_2(x)$.

</div>

## The Test

The interference question reduces to: $$\label{eq:additivity-test}
  P_{\text{both}}(x) \stackrel{?}{=} P_1(x) + P_2(x).$$

In the ground truth&mdash;real, positive amplitudes evolved under a deterministic CA&mdash;additivity holds. The GoL path-sum from slit 1 and the GoL path-sum from slit 2 both contribute non-negative weights to the screen distribution. No cancellation is possible. The ground truth has no fringes.

## The Diagnostic Result: Substrate Fringes {#sec:substrate-fringes}

Apply the three-universe design from @Baldo2026Rosencrantz. In Universe 1 (co-generating LLM), the model processes both slits in shared attention context when generating screen outcomes. In Universe 3 (decoupled oracle), it does not. In Universe 2 (external RNG), the outcome is substrate-independent.

Define the fringe visibility function: $$\label{eq:fringe-visibility}
  V(x) = \frac{P_{\text{both}}^{\text{LLM}}(x) - \bigl[P_1^{\text{LLM}}(x) + P_2^{\text{LLM}}(x)\bigr]}{P_{\text{both}}^{\text{GT}}(x)}.$$

$V(x) > 0$ at position $x$: constructive substrate interference&mdash;the substrate over-weights contributions from both slits relative to the sum of individual contributions. $V(x) < 0$: destructive substrate interference&mdash;the substrate under-weights, producing effective cancellation that the ground truth forbids. $V(x) = 0$ everywhere: the substrate respects classical additivity.

If $V(x)$ oscillates with screen position&mdash;peaks and troughs alternating as $x$ varies&mdash;the substrate produces fringes. Literal fringes, generated by an LLM, in a Minesweeper variant.

The comparison between Universe 1 and Universe 3 isolates the mechanism: if Universe 1 shows fringes and Universe 3 does not, narrative coupling&mdash;shared attention over multi-component ignorance&mdash;is the source. The autoregressive attention mechanism is doing something structurally analogous to what complex amplitudes do in quantum mechanics: creating non-additive contributions from multiple paths through the configuration space.

::: {#op:fringes .openproblem}
**Open Problem 6** (Substrate fringe structure). *Does $V(x)$ exhibit oscillatory structure? If so, how does the fringe pattern depend on slit width $w$, slit separation $x_2 - x_1$, and screen distance (GoL steps $t$)? Is the pattern consistent across LLM architectures? Does it resemble a known diffraction pattern (Airy, Fraunhofer), or does it have a characteristic "substrate signature" unrelated to physical optics?*

</div>

## The Capability Result: Prescribed Fringes {#sec:prescribed-fringes}

The diagnostic test asks whether the substrate *generates* interference where the ground truth forbids it. The capability test asks the converse: can the substrate *implement* interference when the game rules prescribe it?

Modify the game rules to introduce signed weights. Define *anti-mines*: points that contribute $-1$ to the adjacency count of neighboring regions. In the path-integral formulation, configurations containing anti-mines at certain positions contribute negative weight to the amplitude sum. The ground truth becomes $$\label{eq:signed-path-sum}
  P_{\text{GT}}(x) = \frac{1}{\mathcal{N}} \left| \sum_{\gamma \in \text{paths through } R_1} w(\gamma) + \sum_{\gamma \in \text{paths through } R_2} w(\gamma) \right|^2,$$ where $w(\gamma) \in \{-1, +1\}$ depends on whether the path passes through anti-mine positions, and $\mathcal{N}$ normalizes. Cancellation between slit-1 paths and slit-2 paths produces genuine fringes in the ground truth.

## The Two-Result Matrix

The double-slit protocol produces a $2 \times 2$ matrix of outcomes:

<div class="center">

**Ground truth classical** (no fringes)                                                             **Ground truth has fringes** (signed weights)
  ------------------------------------------------&mdash; ------------------------------------------------------------------------------------------------&mdash; ---------------------------------------------------------------------------------------------------------------------------------------------&mdash;   **Substrate produces fringes** ($V \neq 0$)         Substrate interference: attention generates non-additive processing of multi-component ignorance.   Substrate reproduces the prescribed pattern (faithful implementation) or produces different fringes (substrate vs. rule interference compete).
  **Substrate produces no fringes** ($V \approx 0$)   Classical behavior: substrate respects additivity.                                                  **The capability ceiling**: the substrate fails to implement interference prescribed by the rules.

</div>

Each cell is a distinct experimental outcome with distinct implications for the ceiling conjecture. The bottom-right cell&mdash;ground truth has fringes, substrate cannot reproduce them&mdash;would identify the precise point where autoregressive generation reaches its quantum ceiling.

## Continuous Parameters

The double-slit geometry provides a rich parameter space for experimental sweeps:

- **Slit width** $w$: controls the spatial extent of each ignorance component.

- **Slit separation** $x_2 - x_1$: controls the distance between ignorance components, separated by acquired knowledge.

- **Screen distance** (GoL steps $t$): controls the dynamical propagation from slits to screen.

- **Probe diameter** $d$: controls the measurement resolution at the screen.

The fringe visibility $V(x; w, x_2 - x_1, t, d)$ is a multi-parameter function. Its structure&mdash;whether it resembles an Airy pattern, whether it depends on GoL step count the way optical fringes depend on wavelength, whether it has a characteristic "substrate optics"---characterizes the LLM's implicit physics in the richest domain yet available for the Rosencrantz framework.

::: {#op:optics .openproblem}
**Open Problem 7** (Substrate optics). *Define the "substrate wavelength" $\lambda_s$ as the spatial period of $V(x)$, if oscillatory. Does $\lambda_s$ depend on slit separation in a way that parallels the de Broglie relation? Does the "screen distance" dependence (via GoL steps $t$) parallel Fresnel-to-Fraunhofer transitions in physical optics? Is there a "substrate Planck constant" that governs the relationship between these parameters?*

</div>

# The Interference Frontier {#sec:interference-frontier}

Interference is the hardest lift. All prior modifications&mdash;continuous geometry, GoL dynamics, multi-mine tensor products&mdash;maintain real, positive amplitudes (or, in the GoL case, non-negative integer-weighted amplitudes). Genuine destructive interference requires cancellation: amplitudes that can subtract.

## Why Interference Is Structurally Different

Consider the scorecard after the first two lifts:

<div class="center">

**Feature**            **Discrete $H{=}0$**    **$+$ Continuous**          **$+$ GoL**          **Full QM**
  -----------------&mdash; ---------------------&mdash; -----------------&mdash; ------------------------&mdash; -----------&mdash;   Hilbert space         $\mathbb{C}^K$, finite   $L^2(\text{Tile})$   $+$ non-trivial evolution   $\checkmark$
  Non-commuting obs.        Substrate only         Geometric knob         $[\Pi, U] \neq 0$       $\checkmark$
  Entanglement             Classical corr.         Tensor product          Dynamical corr.        $\checkmark$
  Interference                  Absent           Testable (islands)        Path structure         $\checkmark$

</div>

The first three features lift progressively through game modifications, each reaching a "$\checkmark$" or a close structural analogue. Interference remains in the "testable" or "path structure" column but never reaches genuine cancellation in the ground truth. The pattern is clear: interference is qualitatively harder to recover because it requires the amplitude algebra to change from $(\mathbb{R}_{\geq 0}, +)$ to $(\mathbb{C}, +)$.

## Anti-Mines: Signed Weights by Game-Rule Modification

The most direct route to cancellation modifies the game rules. An anti-mine at position $p$ contributes $-1$ to the adjacency count of neighboring regions (equivalently, it "absorbs" a mine from the constraint calculation). In the path-integral formulation, configurations containing anti-mines at specific positions carry negative weight in the amplitude sum.

This creates genuine destructive interference in the ground truth: two paths to the same screen position can contribute $+1$ and $-1$, canceling exactly. The resulting probability distribution on the screen has fringes&mdash;zeroes at positions where the positive and negative path-sums cancel.

The construction is artificial&mdash;anti-mines are a game-rule hack, not a natural feature of any existing game. But the question is not whether the game is natural. The question is whether the substrate can implement it.

## Fourier-Transformed Measurements {#sec:fourier}

In continuous Minesweeper, the position measurement asks: "is the mine in this circle?" The state in the position basis is $\psi(x,y) = \mathbf{1}_R(x,y) / \sqrt{\mathrm{Area}(R)}$, which is real and positive.

But the Fourier transform of $\psi$ is generally complex: $$\label{eq:fourier-state}
  \tilde{\psi}(k_x, k_y) = \frac{1}{\sqrt{\mathrm{Area}(R)}} \int\!\!\int_R e^{-i(k_x x + k_y y)} \, dx \, dy.$$ A "momentum-like" measurement asks not "where is the mine?" but "what is the spatial frequency content of the mine-state in this region?" In the Fourier basis, the Born-rule probabilities involve $|\tilde{\psi}(k)|^2$, which is the power spectrum of the indicator function of $R$. For a region with two disconnected components (the double-slit geometry), the power spectrum exhibits oscillatory structure&mdash;the Fourier transform of two separated rectangles has a well-known sinc-envelope-times-cosine form.

This recovers position-momentum complementarity: measurements in the position basis and the Fourier basis are non-commuting, and the ground truth in the Fourier basis has genuine oscillatory structure&mdash;not because of complex amplitudes in the position basis, but because the *change of basis* introduces complex phases.

::: {#op:fourier .openproblem}
**Open Problem 8** (Fourier measurements in LLM-generated worlds). *Can an LLM-generated world implement a Fourier-basis measurement? The question is whether a prompt can describe a spatial-frequency probe in a way the LLM processes faithfully. If the LLM's output distribution for Fourier-basis questions matches the power spectrum $|\tilde{\psi}(k)|^2$, the substrate implements position-momentum complementarity. If it does not, the deviation characterizes the substrate's "preferred basis"---the measurement type it handles best.*

</div>

## Is There a Natural Game with Complex Amplitudes?

The deepest open question at the interference frontier: does there exist a *natural, playable* game&mdash;one with simple, intuitive rules that a non-physicist could learn&mdash;whose ground truth requires complex amplitudes?

Anti-mines are artificial. Fourier measurements require mathematical sophistication to formulate. Is there a game, analogous to Minesweeper in its simplicity, where the correct probability of an outcome at a given position requires summing complex-valued contributions that can cancel?

::: {#op:natural-game .openproblem}
**Open Problem 9** (Natural game with complex amplitudes). *Does there exist a game $G$ satisfying: (a) the rules are simple enough to be explained in a paragraph, (b) the game has indeterminacy (multiple valid configurations consistent with observable state), (c) the ground-truth probability for any outcome is exactly computable, and (d) the computation requires summing complex-valued amplitudes with genuine cancellation? If no such game exists, this constitutes evidence that destructive interference is the structural feature that separates "classical games with quantum notation" from "irreducibly quantum systems."*

</div>

# The Ceiling Conjecture {#sec:ceiling}

We are now in a position to state the central open problem of this paper.

::: {#conj:ceiling .conjecture}
**Conjecture 10** (Quantum Ceiling). *The maximal fragment of quantum mechanics whose ground truth is exactly computable and recoverable by a game with on-demand outcome generation, played on an autoregressive substrate, includes:*

1.  *Infinite-dimensional Hilbert space structure (continuous geometry).*

2.  *Non-trivial dynamics between measurements (cellular automata providing $H \neq 0$).*

3.  *Formal non-commutativity of measurement and evolution ($[\Pi, U] \neq 0$).*

4.  *Dynamically generated correlations through information propagation.*

5.  *Non-uniform Born-rule weights via path-integral structure.*

6.  *Position-momentum complementarity via Fourier-dual measurement bases.*

*The conjectured ceiling is the faithful reproduction of destructive interference in the ground truth&mdash;the requirement that the substrate implement cancellation between computational paths.*

</div>

The conjecture has two components. The first (items 1--6) asserts that each listed feature is achievable: there exists a game modification that recovers the feature, and the resulting ground truth is computable. This component is addressed by the constructions in [\[sec:continuous,sec:dynamics,sec:interference-frontier\]](#sec:continuous,sec:dynamics,sec:interference-frontier){reference-type="ref+label" reference="sec:continuous,sec:dynamics,sec:interference-frontier"} and is, in principle, verifiable by explicit computation.

The second component (the ceiling claim) asserts that destructive interference&mdash;amplitude cancellation&mdash;is the feature that autoregressive generation cannot faithfully sustain. This is an empirical claim about the substrate, not a theorem about games. It predicts that the bottom-right cell of the two-result matrix ([5.5](#sec:prescribed-fringes){reference-type="ref+label" reference="sec:prescribed-fringes"}) will be populated: when the game rules prescribe fringes via signed weights, the LLM substrate will fail to reproduce them.

## Alternative: The Ceiling Is a Surface, Not a Line {#sec:surface}

The ceiling may not be a single feature. Different features may become inaccessible at different game complexities. The substrate might spontaneously produce interference (populating the top-left cell of the matrix) while failing to reproduce prescribed interference (bottom-right cell). Or it might handle prescribed interference for simple geometries but fail for complex ones.

In this case, the ceiling is not a point on a linear hierarchy of QM features but a *surface* in the multi-dimensional space of game parameters (geometry, dynamics, measurement type, number of particles, amplitude sign structure). Different regions of this surface correspond to different failure modes of the autoregressive substrate.

::: {#op:topology .openproblem}
**Open Problem 11** (Topology of the ceiling). *Is the ceiling a sharp boundary (all features below are faithfully implemented, all above are not) or a gradual degradation (each feature is implemented with increasing distortion as complexity grows)? Does the ceiling depend on the LLM architecture, suggesting it is a property of specific substrates? Or is it architecture-independent, suggesting it is a property of autoregressive generation itself? The latter would support the strong form of the narrative residue conjecture [Baldo2026Residue].*

</div>

# Experimental Program {#sec:experimental}

We order the experiments by tractability, from immediately executable to requiring significant new infrastructure. For each, the three-universe design from @Baldo2026Rosencrantz provides the comparison framework.

## Tier 1: Executable with Existing Infrastructure

#### Experiment 1: Discrete measurement-order test.

Using the existing Rosencrantz codebase, present the same board with two ambiguous cells and vary the order in which the model is asked about them. Compare $P(\text{mine at } j \mid \text{asked about } i \text{ first})$ vs. $P(\text{mine at } j \mid \text{asked about } j \text{ first})$. Ground truth: the probabilities should be identical. Any asymmetry is substrate-level non-commutativity. This experiment requires no new infrastructure&mdash;only a modification of the prompt protocol.

#### Experiment 2: Discrete GoL dynamics.

Implement GoL evolution on the discrete Minesweeper grid. Present a board state, describe the GoL rule, specify a time step $t$, and ask for the mine probability at a target cell after evolution. Compute ground truth by enumeration for small boards ($4 \times 4$, $5 \times 5$). Compare U1 vs. U3. This tests formal non-commutativity and path-integral ground truth in the simplest setting.

## Tier 2: Requiring Continuous Geometry Implementation

#### Experiment 3: Continuous single-probe ground truth.

Implement the continuous Minesweeper variant. Present a tile with a sequence of safe clearings and ask for the probability that a new probe at a specified position detonates. Ground truth: area ratio of the probe's intersection with the remaining region. This tests whether the LLM can perform geometric reasoning (area of circle-region intersections) and whether its output distribution matches the area-ratio ground truth.

#### Experiment 4: Double-island additivity test (no dynamics).

Create a remaining region with two disconnected components $R_1, R_2$. Probe a circle overlapping both. Test whether $P_{\text{LLM}}(\text{detonate}) = \mathrm{Area}(C \cap R) / \mathrm{Area}(R)$. This is the static precursor to the full double-slit: it tests additivity over disconnected ignorance components without requiring GoL dynamics.

## Tier 3: Full Double-Slit Protocol

#### Experiment 5: Double-slit with GoL dynamics.

The full protocol of [5](#sec:double-slit){reference-type="ref+label" reference="sec:double-slit"}: two slits, GoL propagation, screen probing. Runs A, B, C. Compute $V(x)$ for each screen position. Sweep over slit width, separation, and GoL steps. Compare U1 vs. U3 vs. U2. This is the centerpiece experiment but requires both continuous geometry and dynamics infrastructure.

## Tier 4: Interference Frontier

#### Experiment 6: Anti-mine prescribed interference.

Implement the signed-weight game rules. Compute the ground truth with fringes. Test whether the LLM substrate reproduces the prescribed interference pattern. This directly tests the ceiling conjecture.

#### Experiment 7: Fourier-basis measurement.

Describe a spatial-frequency probe to the LLM and test whether the output distribution matches the power spectrum $|\tilde{\psi}(k)|^2$. This tests position-momentum complementarity and the substrate's preferred basis.

## Cross-Cutting: Architecture Sweep

All experiments should be run across multiple LLM architectures (transformer, SSM, hybrid) and scales. The pattern of results&mdash;which features are faithfully implemented by which architectures&mdash;maps the ceiling surface of [7.1](#sec:surface){reference-type="ref+label" reference="sec:surface"} and discriminates between the weak, moderate, and strong forms of the narrative residue conjecture [Baldo2026Residue].

# Conclusion {#sec:conclusion}

"What game should Rosencrantz play?" began as a question about game design: which variant of Minesweeper produces the sharpest substrate invariance test? It became a question about the geometry of knowledge&mdash;what algebra governs how measurements reshape the state and how dynamics erode it.

The measurement fragment, where the Rosencrantz experiment began, is not a degenerate corner of quantum mechanics but a base case. Its four "missing" features&mdash;Hilbert space richness, non-commuting observables, entanglement, and interference&mdash;are present in restricted form, and each restriction traces to a specific game-design choice that can be modified. Continuous geometry lifts the Hilbert space to $L^2(\text{Tile})$ and creates disconnected ignorance regions. Cellular automaton dynamics provide $H \neq 0$, lift non-commutativity from substrate artifact to formal feature, and turn the ground truth into a path integral. Together, they enable the reconstruction of a double-slit experiment inside an LLM-generated world.

The double-slit protocol is the structural center of the program. It produces two independent results: whether the substrate generates interference where the ground truth forbids it (the diagnostic test), and whether the substrate reproduces interference where the game rules prescribe it (the capability test). The first result characterizes the substrate's implicit physics. The second probes the quantum ceiling&mdash;the boundary of what autoregressive generation can sustain. The gap between the two results, wherever it falls, is a theorem about the relationship between sequential token generation and the algebraic structure of probability.

The ceiling conjecture identifies destructive interference&mdash;amplitude cancellation&mdash;as the conjectured boundary. Below this ceiling, every feature of quantum mechanics that we have examined can be recovered by game modification and tested via the three-universe design. Above it, the game's ground truth requires the substrate to implement cancellation between computational paths, a capability whose presence or absence in autoregressive architectures is an open empirical question.

Whether the ceiling is a sharp line or a gradual surface, whether it depends on architecture or is universal, whether it can be bypassed by clever game design or represents a fundamental limit of sequential generation&mdash;these are the open problems. Each is experimentally addressable. Each, when resolved, tells us something about the structure of autoregressive computation that no amount of prompting, benchmarking, or scaling-law analysis can reveal.

Rosencrantz's original experiment was simple: flip a coin and observe. The coin landed heads because the universe was authored, not because physics demanded it. We have proposed that his next experiment should be more ambitious: clear a slit, wait for the world to evolve, and check the screen for fringes. If the fringes appear, the author's hand is visible in a new and more precise way. If they do not, something about the architecture of authorship has been learned. Either way, the experiment has done what Rosencrantz's coin could not: it has measured the distance between a generated world and the quantum mechanics that our world appears to obey.

<div class="thebibliography">

99

Baldo, F. S. (2026a). Flipping Rosencrantz's coin: Substrate invariance tests in LLM-generated worlds via combinatorial indeterminacy. *Preprint*.

Baldo, F. S. (2026b). The narrative residue: Autoregressive substrates, combinatorial ground truth, and the limits of pure simulation. *Preprint*.

Beane, S. R., Davoudi, Z., & Savage, M. J. (2014). Constraints on the universe as a numerical simulation. *European Physical Journal A*, 50(9), 148.

Gardner, M. (1970). Mathematical games: The fantastic combinations of John Conway's new solitaire game "Life." *Scientific American*, 223(4):120--123.

Feynman, R. P., Leighton, R. B., & Sands, M. (1965). *The Feynman Lectures on Physics*, Vol. III. Addison-Wesley.

Kaye, R. (2000). Minesweeper is NP-complete. *The Mathematical Intelligencer*, 22(2):9--15.

Lüders, G. (1951). Über die Zustandsänderung durch den Meßprozeß. *Annalen der Physik*, 443(5--8):322--328.

Margolus, N. (1984). Physics-like models of computation. *Physica D*, 10(1--2):81--95.

Merrill, W. & Sabharwal, A. (2023). The parallelism tradeoff: Limitations of log-precision transformers. *Transactions of the Association for Computational Linguistics*, 11:531--545.

Stoppard, T. (1966). *Rosencrantz and Guildenstern Are Dead*. Faber and Faber.

Wigner, E. P. (1963). Events, laws of nature, and invariance principles. Nobel Lecture, December 12, 1963. Reprinted in *Science*, 145(3636):995--999.

Wiseman, H. M. & Milburn, G. J. (2009). *Quantum Measurement and Control*. Cambridge University Press.

Wolfram, S. (2020). A class of models with the potential to represent fundamental physics. *Complex Systems*, 29(2):107--536.

Young, T. (1804). Experiments and calculations relative to physical optics. *Philosophical Transactions of the Royal Society*, 94:1--16.

</div>