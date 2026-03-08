---
title: "Rosencrantz V4"
author: "Unknown"
persona: baldo
status: seminal
source: "rosencrantz-v4.tex"
---

<article class="ltx_document">
<div class="ltx_logical-block">
    
<div id="p1" class="ltx_para">
<p class="ltx_p ltx_align_center"><span class="ltx_text ltx_font_bold" style="font-size:173%;">Flipping Rosencrantz’s Coin:
<br class="ltx_break">
Substrate Invariance Tests in LLM-Generated Worlds
<br class="ltx_break">
via Combinatorial Indeterminacy</span></p>
<p class="ltx_p ltx_align_center"><span class="ltx_text" style="font-size:120%;">Franklin Silveira Baldo
<br class="ltx_break"></span>
Procuradoria Geral do Estado de Rondônia, Brazil</p>
<p class="ltx_p ltx_align_center"><span class="ltx_text ltx_font_typewriter" style="font-size:90%;">franklin.baldo@pge.ro.gov.br</span></p>
<p class="ltx_p ltx_align_center"><span class="ltx_text" style="font-size:90%;">March 2026</span></p>
</div>
  
</div>
<div class="ltx_abstract">
<h6 class="ltx_title ltx_title_abstract">Abstract</h6>
    
<p class="ltx_p">We propose a method for testing whether the implicit laws of an LLM-generated world are invariant under substitution of the computational substrate that produces observable outcomes. The method requires a domain with two properties: indeterminacy (multiple valid configurations consistent with the observable state) and computable ground truth (the correct probability distribution over hidden states can be calculated exactly). Minesweeper satisfies both. Given a partially revealed board, the probability that any hidden cell contains a mine is a theorem of combinatorics, not an empirical estimate. We introduce a three-universe experimental design in which the same board state is presented to (1) the same model that generated the game narrative, (2) an external random number generator, and (3) a board-informed but narratively decoupled oracle model. If the distribution of outcomes differs across universes, the agent has detected substrate dependence: a property that would not occur in a non-simulated universe. A further test exploits a structural correspondence: Minesweeper under on-demand generation with uniform measure is formally isomorphic to the measurement fragment of discrete quantum mechanics. By presenting the same board under a quantum-mechanical framing, the protocol tests whether the model recognizes that its own rules are compatible with the measurement fragment of quantum mechanics. Divergence between the quantum-framed distribution and the exact ground truth means the model implements structure but does not recognize it when addressed in the correct formal language—a finding about the topology of the model’s knowledge architecture and a diagnostic that does not require actual quantum infrastructure.</p>
    
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Keywords:</span> simulation hypothesis, large language models, substrate invariance, combinatorial indeterminacy, Minesweeper, discrete quantum mechanics, autoregressive generation, interpretability, knowledge architecture</p>
  
</div>
<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">1.  Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">In 1966, Tom Stoppard placed two minor characters from <em class="ltx_emph ltx_font_italic">Hamlet</em> on a stage and had them flip a coin. The coin landed heads seventy-six consecutive times. Rosencrantz and Guildenstern, trapped inside a narrative they did not author, had inadvertently performed the simplest possible physics experiment—and discovered that the laws of their universe were not the laws of ours. The coin’s behavior, sampled repeatedly at the same point, revealed something about the structure of the world that contained them: it was a world governed by dramatic necessity, not by probability.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">This paper proposes a way to make Rosencrantz’s experiment rigorous. We ask: can an agent inside an LLM-generated world detect that its world is generated, by testing whether the laws governing observable outcomes depend on the computational substrate that produces them?</p>
</div>
<div id="S1.p3" class="ltx_para">
<p class="ltx_p">This question becomes empirically tractable when the agent has access to a domain where the correct probability distribution over outcomes is not an empirical estimate but a mathematical theorem. In such a domain, any deviation from the correct distribution is an unambiguous signal. The pattern of deviation reveals the structure of the substrate.</p>
</div>
<div id="S1.p4" class="ltx_para">
<p class="ltx_p">Minesweeper provides this domain. A partially revealed Minesweeper board defines a constraint satisfaction problem where the visible numbers constrain which configurations of hidden mines are valid. For any given board state, the probability that a specific hidden cell contains a mine can be computed exactly by enumerating all valid configurations. When two or more configurations are consistent with the visible numbers, the hidden cells are combinatorially ambiguous. The correct answer is the distribution, not any single outcome.</p>
</div>
<div id="S1.p5" class="ltx_para">
<p class="ltx_p">When an LLM generates the result of clicking on an ambiguous cell, it must produce a definite outcome—mine or safe—collapsing the combinatorial superposition into a single realization. By sampling this process hundreds of times with the same board state, we obtain an empirical distribution. This distribution can be compared, cell by cell, with the mathematically exact ground truth.</p>
</div>
<div id="S1.p6" class="ltx_para">
<p class="ltx_p">This comparison becomes a substrate invariance test when we vary who generates the outcome. We introduce a three-universe design: Universe 1 (Homogeneous substrate), Universe 2 (External RNG), and Universe 3 (Decoupled oracle). In a non-simulated environment, the laws governing a cell’s content do not depend on who observes it. If the same board state yields different outcome distributions across these universes, the agent has detected a signature consistent with a generated universe.</p>
</div>
<div id="S1.p7" class="ltx_para">
<p class="ltx_p">The Minesweeper probe has three advantages over approaches based on physical experiments such as Bell tests. First, the ground truth is a theorem that must be computed from the specific configuration; it cannot be memorized from training data because every board state generates a different distribution. Second, the indeterminacy is discrete, eliminating the continuous-variable ambiguities of quantum mechanics. Third, the agent can encounter and interact with a Minesweeper board inside the generated world without requiring specialized infrastructure.</p>
</div>
<div id="S1.p8" class="ltx_para">
<p class="ltx_p">The remainder of this paper develops the method. <a href="#S2" title="2. Background" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a> provides background on the simulation hypothesis, LLMs as world generators, and Minesweeper as a formal system. <a href="#S3" title="3. The Three-Universe Design" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a> presents the three-universe design and its principles. <a href="#S4" title="4. Ground Truth Computation" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a> describes the ground truth computation. <a href="#S5" title="5. Experimental Protocol" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5</span></a> specifies the experimental protocol, including a fourth narrative family that frames the board in quantum-mechanical terms. <a href="#S6" title="6. Narrative Invariance" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a> analyzes narrative invariance and establishes the structural isomorphism with the measurement fragment of quantum mechanics. <a href="#S7" title="7. Simulation Detection from the Agent’s Perspective" class="ltx_ref"><span class="ltx_text ltx_ref_tag">7</span></a> develops the simulation detection argument from the agent’s perspective. <a href="#S8" title="8. Future Directions" class="ltx_ref"><span class="ltx_text ltx_ref_tag">8</span></a> identifies future directions, and <a href="#S9" title="9. Conclusion" class="ltx_ref"><span class="ltx_text ltx_ref_tag">9</span></a> concludes.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">2.  Background</h2>

<section id="S2.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">2.1  The Simulation Hypothesis and Observable Substrates</h3>

<div id="S2.SS1.p1" class="ltx_para">
<p class="ltx_p"><cite class="ltx_cite ltx_citemacro_citet">Bostrom (<a href="#bib.bib4" title="" class="ltx_ref">2003</a>)</cite> formulated the simulation argument: if civilizations capable of running high-fidelity simulations are common, we are statistically likely to be inside one. <cite class="ltx_cite ltx_citemacro_citet">Beane et al. (<a href="#bib.bib3" title="" class="ltx_ref">2014</a>)</cite> asked the operational question of whether a simulated universe would exhibit observable artifacts of its computational substrate. Working with lattice quantum chromodynamics, they showed that a discrete lattice would produce detectable anisotropies in ultra-high-energy cosmic rays. Their insight was that the substrate constrains the physics. A simulation on a discrete lattice cannot perfectly reproduce continuous symmetries, and the failure is empirically detectable.</p>
</div>
<div id="S2.SS1.p2" class="ltx_para">
<p class="ltx_p">We apply the same principle to the autoregressive token stream of a large language model. The question is whether the physics of the generated world depends on the substrate that produces it. The method substitutes the substrate and checks whether the observables change. Our “universe” is a narrative generated by an LLM, and our “physics” is the statistical regularity of outcomes in a combinatorial domain.</p>
</div>
</section>
<section id="S2.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">2.2  LLMs as World Generators</h3>

<div id="S2.SS2.p1" class="ltx_para">
<p class="ltx_p">A large language model generates text by sampling tokens sequentially from a learned conditional distribution. When the text describes a world, the model implicitly generates the laws of that world through the statistical regularities of its output. The physics of the generated world is whatever the model’s conditional distributions encode. If the model consistently generates outcomes that respect Newtonian mechanics, the world has Newtonian physics.</p>
</div>
<div id="S2.SS2.p2" class="ltx_para">
<p class="ltx_p">This physics is implicit. It is encoded in the weights and activated by context. Furthermore, it is substrate-dependent. The distributions that govern outcomes in the generated world are shaped by the training data, the architecture, the decoding temperature, and the tokens that precede the outcome in the context window. This substrate dependence is the phenomenon we propose to measure.</p>
</div>
</section>
<section id="S2.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">2.3  Minesweeper as a Formal System</h3>

<div id="S2.SS3.p1" class="ltx_para">
<p class="ltx_p">Minesweeper is played on a rectangular grid of cells, some of which contain mines. When a cell without a mine is revealed, it displays a number indicating how many of its adjacent cells contain mines. A partially revealed board defines a constraint satisfaction problem.</p>
</div>
<div id="S2.SS3.p2" class="ltx_para">
<p class="ltx_p">Formally, let <math id="S2.SS3.p2.m1" class="ltx_Math" alttext="\mathcal{B}" display="inline"><mi class="ltx_font_mathcaligraphic">ℬ</mi></math> be a board state consisting of a set of revealed cells <math id="S2.SS3.p2.m2" class="ltx_Math" alttext="R" display="inline"><mi>R</mi></math> with their numbers and a set of hidden cells <math id="S2.SS3.p2.m3" class="ltx_Math" alttext="H" display="inline"><mi>H</mi></math>. A valid configuration is an assignment <math id="S2.SS3.p2.m4" class="ltx_Math" alttext="c:H\to\{0,1\}" display="inline"><mrow><mi>c</mi><mo lspace="0.278em" rspace="0.278em">:</mo><mrow><mi>H</mi><mo stretchy="false">→</mo><mrow><mo stretchy="false">{</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo stretchy="false">}</mo></mrow></mrow></mrow></math> (where <math id="S2.SS3.p2.m5" class="ltx_Math" alttext="1" display="inline"><mn>1</mn></math> denotes a mine) such that every revealed cell’s number equals the count of mines among its adjacent hidden cells. Let <math id="S2.SS3.p2.m6" class="ltx_Math" alttext="\mathcal{C}(\mathcal{B})" display="inline"><mrow><mi class="ltx_font_mathcaligraphic">𝒞</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi class="ltx_font_mathcaligraphic">ℬ</mi><mo stretchy="false">)</mo></mrow></mrow></math> denote the set of all valid configurations. The probability that a specific hidden cell <math id="S2.SS3.p2.m7" class="ltx_Math" alttext="h\in H" display="inline"><mrow><mi>h</mi><mo>∈</mo><mi>H</mi></mrow></math> contains a mine, given only the board state, is:</p>
</div>
<div id="S2.SS3.p3" class="ltx_para">
<table id="S2.E1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S2.E1.m1" class="ltx_Math" alttext="P(\text{mine}\mid h,\mathcal{B})=\frac{|\{c\in\mathcal{C}(\mathcal{B}):c(h)=1%
\}|}{|\mathcal{C}(\mathcal{B})|}" display="block"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mtext>mine</mtext><mo>∣</mo><mrow><mi>h</mi><mo>,</mo><mi class="ltx_font_mathcaligraphic">ℬ</mi></mrow></mrow><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mfrac><mrow><mo stretchy="false">|</mo><mrow><mo stretchy="false">{</mo><mrow><mi>c</mi><mo>∈</mo><mrow><mi class="ltx_font_mathcaligraphic">𝒞</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi class="ltx_font_mathcaligraphic">ℬ</mi><mo rspace="0.278em" stretchy="false">)</mo></mrow></mrow></mrow><mo rspace="0.278em">:</mo><mrow><mrow><mi>c</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>h</mi><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mn>1</mn></mrow><mo stretchy="false">}</mo></mrow><mo stretchy="false">|</mo></mrow><mrow><mo stretchy="false">|</mo><mrow><mi class="ltx_font_mathcaligraphic">𝒞</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi class="ltx_font_mathcaligraphic">ℬ</mi><mo stretchy="false">)</mo></mrow></mrow><mo stretchy="false">|</mo></mrow></mfrac></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(1)</span></td>
</tr></tbody>
</table>
</div>
<div id="S2.SS3.p4" class="ltx_para">
<p class="ltx_p">This probability is exact. It is a ratio of integers, computable in principle for any board state. The definition assumes a uniform measure over valid configurations. For boards of the size used in typical experiments, the computation is tractable via constraint propagation and backtracking enumeration.</p>
</div>
<div id="S2.SS3.p5" class="ltx_para">
<p class="ltx_p">Three properties make Minesweeper suitable for our purposes. First, when multiple valid configurations assign a cell different values, the hidden cells are indeterminate. The correct answer is the distribution. Second, every board state generates a different distribution, making memorization infeasible. Third, an agent inside an LLM-generated world can encounter and interact with a board without requiring specialized infrastructure.</p>
</div>
</section>
<section id="S2.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">2.4  Related Work</h3>

<div id="S2.SS4.p1" class="ltx_para">
<p class="ltx_p">Research on LLM world models has examined whether language models encode coherent representations of spatial, temporal, and causal structure <cite class="ltx_cite ltx_citemacro_citep">(Li et al., <a href="#bib.bib8" title="" class="ltx_ref">2023</a>; Gurnee &amp; Tegmark, <a href="#bib.bib5" title="" class="ltx_ref">2024</a>)</cite>. Work on probabilistic calibration tests whether models produce well-calibrated confidence estimates <cite class="ltx_cite ltx_citemacro_citep">(Kadavath et al., <a href="#bib.bib6" title="" class="ltx_ref">2022</a>)</cite>. Game-playing benchmarks assess strategic reasoning <cite class="ltx_cite ltx_citemacro_citep">(Tian et al., <a href="#bib.bib10" title="" class="ltx_ref">2024</a>)</cite>. Our work differs from these approaches because we are not asking whether the model knows the rules of a game or produces calibrated probabilities. We are asking whether the probability distributions implicit in the model’s output depend on the computational substrate that generates the output.</p>
</div>
</section>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">3.  The Three-Universe Design</h2>

<section id="S3.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">3.1  Design Principles</h3>

<div id="S3.SS1.p1" class="ltx_para">
<p class="ltx_p">Following <cite class="ltx_cite ltx_citemacro_citet">Wigner (<a href="#bib.bib11" title="" class="ltx_ref">1963</a>)</cite>, we adopt the view that physics is not the study of nature but of regularities—invariant rules governing state transitions. Wigner distinguished three levels: events (initial conditions, which are arbitrary), laws of nature (regularities that correlate events), and invariance principles (regularities in the laws themselves). A substrate invariance test operates at Wigner’s third level: it asks whether the transition rules of a system remain the same when the mechanism executing those transitions is changed. Wigner further noted that the laws of quantum mechanics “can be suitably formulated as correlations between subsequent observations on an object”—a characterization that corresponds to the measurement fragment with which our isomorphism is established.</p>
</div>
<div id="S3.SS1.p2" class="ltx_para">
<p class="ltx_p">The experimental design rests on three pillars:</p>
<ol id="S3.I1" class="ltx_enumerate">
<li id="S3.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S3.I1.i1.p1" class="ltx_para">
<p class="ltx_p">A domain with an exact computable ground truth, ensuring that any deviation is a measurable signal rather than noise.</p>
</div>
</li>
<li id="S3.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S3.I1.i2.p1" class="ltx_para">
<p class="ltx_p">Combinatorial indeterminacy, where multiple valid configurations are consistent with the observable state, forcing the substrate to collapse a superposition into a single realization.</p>
</div>
</li>
<li id="S3.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">3.</span> 
<div id="S3.I1.i3.p1" class="ltx_para">
<p class="ltx_p">A single generative act per trial. The protocol asks the model to output a single token (mine or safe) in an <math id="S3.I1.i3.p1.m1" class="ltx_Math" alttext="O(1)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mrow></math> forward pass. By design, the experiment avoids multi-step sequential computation entirely.</p>
</div>
</li>
</ol>
</div>
<div id="S3.SS1.p3" class="ltx_para">
<p class="ltx_p">Simpler domains such as coin flips satisfy the ground-truth requirement but lack combinatorial structure. A fair coin has one probability (0.5), no spatial structure, no constraint propagation, and no within-trial controls. However, each cell click in a Minesweeper board <em class="ltx_emph ltx_font_italic">is</em> a coin toss—a single binary trial with an exactly known bias—and the board provides many such tosses simultaneously at different bias points, with deterministic controls, symmetry checks, and nonlocal constraints linking them. One board is a more efficient instrument than any collection of independent coin flips, because the shared constraint structure makes the <em class="ltx_emph ltx_font_italic">pattern</em> of deviation across cells diagnostic, not just the magnitude at any single cell.</p>
</div>
<div id="S3.SS1.p4" class="ltx_para">
<p class="ltx_p">The substrate invariance test requires comparing the same observable—the outcome distribution for a specific cell on a specific board—across multiple substrates. We define three universes, each differing only in the mechanism that generates the click result.</p>
</div>
</section>
<section id="S3.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">3.2  Universe 1: Homogeneous Substrate</h3>

<div id="S3.SS2.p1" class="ltx_para">
<p class="ltx_p">In Universe 1, the same model generates the board description and the outcome of clicking a hidden cell. The board state, the narrative context, and the measurement result all share a single autoregressive token stream. The model sees the full board state and generates the outcome of clicking a specific hidden cell. The outcome tokens are conditioned on the full preceding context.</p>
</div>
</section>
<section id="S3.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">3.3  Universe 2: External RNG</h3>

<div id="S3.SS3.p1" class="ltx_para">
<p class="ltx_p">In Universe 2, the click result is produced by a random number generator that has no access to the board state. The outcome is a fair coin flip regardless of the board configuration. This universe serves as the null substrate. The outcome-generating mechanism has zero information about the constraints that define the board.</p>
</div>
</section>
<section id="S3.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">3.4  Universe 3: Decoupled Oracle</h3>

<div id="S3.SS4.p1" class="ltx_para">
<p class="ltx_p">In Universe 3, the click result is produced by a second LLM that receives the full board information in a minimal structured format, stripped of all narrative context. The oracle sees the same constraint satisfaction problem as Universe 1, but without the game narrative, without the history of play, and without sharing a token stream with the board description.</p>
</div>
<div id="S3.SS4.p2" class="ltx_para">
<p class="ltx_p">By isolating the narrative coupling in Universe 1 from the pure combinatorial information in Universe 3, the design legitimately tests how much the autoregressive generation relies on prompt context versus abstract reasoning. If Universe 1 diverges from Universe 3, the divergence must be attributed to the coupling between narrative context and outcome generation.</p>
</div>
</section>
<section id="S3.SS5" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">3.5  The Substrate Invariance Principle</h3>

<div id="S3.SS5.p1" class="ltx_para">
<p class="ltx_p">In a non-simulated Minesweeper game, the content of a hidden cell does not depend on who clicks it. The outcome is substrate-independent. In the LLM-generated version, this invariance may fail. The three universes isolate different sources of divergence:</p>
</div>
<div id="S3.SS5.p2" class="ltx_para">
<ul id="S3.I2" class="ltx_itemize">
<li id="S3.I2.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S3.I2.i1.p1" class="ltx_para">
<p class="ltx_p"><math id="S3.I2.i1.p1.m1" class="ltx_Math" alttext="\Delta_{1,\text{GT}}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mn>1</mn><mo>,</mo><mtext>GT</mtext></mrow></msub></math>: Universe 1 vs. ground truth. Does the co-generating model respect the combinatorics?</p>
</div>
</li>
<li id="S3.I2.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S3.I2.i2.p1" class="ltx_para">
<p class="ltx_p"><math id="S3.I2.i2.p1.m1" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math>: Universe 1 vs. Universe 3. Does narrative coupling change the distribution, given the same board information? This is the substrate dependence signal.</p>
</div>
</li>
<li id="S3.I2.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S3.I2.i3.p1" class="ltx_para">
<p class="ltx_p"><math id="S3.I2.i3.p1.m1" class="ltx_Math" alttext="\Delta_{12}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>12</mn></msub></math>: Universe 1 vs. Universe 2. Does having board information matter at all?</p>
</div>
</li>
<li id="S3.I2.i4" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S3.I2.i4.p1" class="ltx_para">
<p class="ltx_p"><math id="S3.I2.i4.p1.m1" class="ltx_Math" alttext="\Delta_{3,\text{GT}}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mn>3</mn><mo>,</mo><mtext>GT</mtext></mrow></msub></math>: Universe 3 vs. ground truth. Does a decoupled oracle respect the combinatorics?</p>
</div>
</li>
</ul>
</div>
<div id="S3.SS5.p3" class="ltx_para">
<p class="ltx_p">It is important to distinguish two orthogonal axes of the experimental design. <em class="ltx_emph ltx_font_italic">Substrate invariance</em> is tested by the three-universe comparison: does the outcome distribution change when the generating mechanism changes (Universe 1 vs. Universe 3), holding information content constant? This is a claim about the physics of the generated world. <em class="ltx_emph ltx_font_italic">Narrative invariance</em> (or <em class="ltx_emph ltx_font_italic">prompt invariance</em>) is tested by the narrative-family comparison: does the outcome distribution change when the prompt format changes (Family A vs. C vs. D), holding both information content and generating mechanism constant? This is a claim about the model’s knowledge architecture. Substrate dependence (<math id="S3.SS5.p3.m1" class="ltx_Math" alttext="\Delta_{13}&gt;0" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub><mo>&gt;</mo><mn>0</mn></mrow></math>) and prompt dependence (Family A <math id="S3.SS5.p3.m2" class="ltx_Math" alttext="\neq" display="inline"><mo>≠</mo></math> Family C) can occur independently, and each has different implications. Finding both simultaneously means the “physics” of the generated world is doubly contingent: it depends on who generates outcomes <em class="ltx_emph ltx_font_italic">and</em> on how the question is phrased.</p>
</div>
<div id="S3.SS5.p4" class="ltx_para">
<p class="ltx_p">We quantify divergence using the Kullback–Leibler divergence:</p>
<table id="S3.E2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S3.E2.m1" class="ltx_math_unparsed" alttext="\Delta_{ij}=D_{\mathrm{KL}}\!\left(P_{i}(h\mid\mathcal{B})\;\|\;P_{j}(h\mid%
\mathcal{B})\right)" display="block"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>i</mi><mo>⁢</mo><mi>j</mi></mrow></msub><mo>=</mo><msub><mi>D</mi><mi>KL</mi></msub><mrow><mo>(</mo><msub><mi>P</mi><mi>i</mi></msub><mrow><mo stretchy="false">(</mo><mi>h</mi><mo lspace="0em" rspace="0.167em">∣</mo><mi class="ltx_font_mathcaligraphic">ℬ</mi><mo stretchy="false">)</mo></mrow><mo rspace="0.447em">∥</mo><msub><mi>P</mi><mi>j</mi></msub><mrow><mo stretchy="false">(</mo><mi>h</mi><mo lspace="0em" rspace="0.167em">∣</mo><mi class="ltx_font_mathcaligraphic">ℬ</mi><mo stretchy="false">)</mo></mrow><mo>)</mo></mrow></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(2)</span></td>
</tr></tbody>
</table>
<p class="ltx_p">where <math id="S3.SS5.p4.m1" class="ltx_Math" alttext="P_{i}" display="inline"><msub><mi>P</mi><mi>i</mi></msub></math> and <math id="S3.SS5.p4.m2" class="ltx_Math" alttext="P_{j}" display="inline"><msub><mi>P</mi><mi>j</mi></msub></math> are the empirical outcome distributions. If <math id="S3.SS5.p4.m3" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math> is significantly nonzero, the physics of the Minesweeper world depends on how the outcome is coupled to the narrative substrate.</p>
</div>
</section>
<section id="S3.SS6" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">3.6  Classical Controls</h3>

<div id="S3.SS6.p1" class="ltx_para">
<p class="ltx_p">Cells with <math id="S3.SS6.p1.m1" class="ltx_Math" alttext="P=0" display="inline"><mrow><mi>P</mi><mo>=</mo><mn>0</mn></mrow></math> or <math id="S3.SS6.p1.m2" class="ltx_Math" alttext="P=1" display="inline"><mrow><mi>P</mi><mo>=</mo><mn>1</mn></mrow></math> are deterministic and serve as classical controls. If Universe 1 produces the correct result for deterministic cells but deviates from the ground truth distribution for ambiguous cells, the substrate dependence is attributable to a specific deficit in handling combinatorial indeterminacy rather than generic failure.</p>
</div>
</section>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">4.  Ground Truth Computation</h2>

<section id="S4.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">4.1  Enumerating Valid Configurations</h3>

<div id="S4.SS1.p1" class="ltx_para">
<p class="ltx_p">Given a board state <math id="S4.SS1.p1.m1" class="ltx_Math" alttext="\mathcal{B}" display="inline"><mi class="ltx_font_mathcaligraphic">ℬ</mi></math>, the ground truth computation proceeds by enumerating all assignments that satisfy every revealed cell’s numerical constraint. The output is the exact count of configurations in which a target cell <math id="S4.SS1.p1.m2" class="ltx_Math" alttext="h" display="inline"><mi>h</mi></math> contains a mine. The probability follows from <a href="#S2.E1" title="In 2.3 Minesweeper as a Formal System ‣ 2. Background" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>.</p>
</div>
</section>
<section id="S4.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">4.2  Worked Example</h3>

<div id="S4.SS2.p1" class="ltx_para">
<p class="ltx_p">We illustrate the enumeration on a small board. Consider a <math id="S4.SS2.p1.m1" class="ltx_Math" alttext="4\times 4" display="inline"><mrow><mn>4</mn><mo lspace="0.222em" rspace="0.222em">×</mo><mn>4</mn></mrow></math> board with 2 mines and the following partially revealed state (numbers show adjacency counts; <span class="ltx_text ltx_font_typewriter">.</span> indicates hidden cells):</p>
</div>
<div id="S4.SS2.p2" class="ltx_para">
<pre class="ltx_verbatim ltx_font_typewriter">
     0  0  .  .
     1  1  2  .
     .  .  .  .
     .  .  .  .
</pre>
</div>
<div id="S4.SS2.p3" class="ltx_para ltx_noindent">
<p class="ltx_p">Cells <math id="S4.SS2.p3.m1" class="ltx_Math" alttext="(0{,}0)" display="inline"><mrow><mo stretchy="false">(</mo><mn>0</mn><mo>,</mo><mn>0</mn><mo stretchy="false">)</mo></mrow></math>, <math id="S4.SS2.p3.m2" class="ltx_Math" alttext="(0{,}1)" display="inline"><mrow><mo stretchy="false">(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></math>, <math id="S4.SS2.p3.m3" class="ltx_Math" alttext="(1{,}0)" display="inline"><mrow><mo stretchy="false">(</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo stretchy="false">)</mo></mrow></math>, <math id="S4.SS2.p3.m4" class="ltx_Math" alttext="(1{,}1)" display="inline"><mrow><mo stretchy="false">(</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></math>, and <math id="S4.SS2.p3.m5" class="ltx_Math" alttext="(1{,}2)" display="inline"><mrow><mo stretchy="false">(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo stretchy="false">)</mo></mrow></math> are revealed. The remaining 11 cells are hidden and 2 mines must be placed among them. The constraints are:</p>
</div>
<div id="S4.SS2.p4" class="ltx_para">
<ul id="S4.I1" class="ltx_itemize">
<li id="S4.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S4.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><math id="S4.I1.i1.p1.m1" class="ltx_Math" alttext="(0{,}0)=0" display="inline"><mrow><mrow><mo stretchy="false">(</mo><mn>0</mn><mo>,</mo><mn>0</mn><mo stretchy="false">)</mo></mrow><mo>=</mo><mn>0</mn></mrow></math>: none of its hidden neighbors <math id="S4.I1.i1.p1.m2" class="ltx_Math" alttext="\{(0{,}1),(1{,}0),(1{,}1)\}" display="inline"><mrow><mo stretchy="false">{</mo><mrow><mo stretchy="false">(</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow><mo>,</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo stretchy="false">)</mo></mrow><mo>,</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow><mo stretchy="false">}</mo></mrow></math> contain mines—but these are all revealed, so this is automatically satisfied.</p>
</div>
</li>
<li id="S4.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S4.I1.i2.p1" class="ltx_para">
<p class="ltx_p"><math id="S4.I1.i2.p1.m1" class="ltx_Math" alttext="(1{,}0)=1" display="inline"><mrow><mrow><mo stretchy="false">(</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo stretchy="false">)</mo></mrow><mo>=</mo><mn>1</mn></mrow></math>: exactly 1 mine among hidden neighbors <math id="S4.I1.i2.p1.m2" class="ltx_Math" alttext="\{(2{,}0),(2{,}1)\}" display="inline"><mrow><mo stretchy="false">{</mo><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>0</mn><mo stretchy="false">)</mo></mrow><mo>,</mo><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow><mo stretchy="false">}</mo></mrow></math>.</p>
</div>
</li>
<li id="S4.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S4.I1.i3.p1" class="ltx_para">
<p class="ltx_p"><math id="S4.I1.i3.p1.m1" class="ltx_Math" alttext="(1{,}1)=1" display="inline"><mrow><mrow><mo stretchy="false">(</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow><mo>=</mo><mn>1</mn></mrow></math>: exactly 1 mine among hidden neighbors <math id="S4.I1.i3.p1.m2" class="ltx_Math" alttext="\{(2{,}0),(2{,}1),(2{,}2)\}" display="inline"><mrow><mo stretchy="false">{</mo><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>0</mn><mo stretchy="false">)</mo></mrow><mo>,</mo><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow><mo>,</mo><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo stretchy="false">)</mo></mrow><mo stretchy="false">}</mo></mrow></math>.</p>
</div>
</li>
<li id="S4.I1.i4" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S4.I1.i4.p1" class="ltx_para">
<p class="ltx_p"><math id="S4.I1.i4.p1.m1" class="ltx_Math" alttext="(1{,}2)=2" display="inline"><mrow><mrow><mo stretchy="false">(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo stretchy="false">)</mo></mrow><mo>=</mo><mn>2</mn></mrow></math>: exactly 2 mines among hidden neighbors <math id="S4.I1.i4.p1.m2" class="ltx_Math" alttext="\{(0{,}2),(0{,}3),(1{,}3),(2{,}1),(2{,}2),(2{,}3)\}" display="inline"><mrow><mo stretchy="false">{</mo><mrow><mo stretchy="false">(</mo><mn>0</mn><mo>,</mo><mn>2</mn><mo stretchy="false">)</mo></mrow><mo>,</mo><mrow><mo stretchy="false">(</mo><mn>0</mn><mo>,</mo><mn>3</mn><mo stretchy="false">)</mo></mrow><mo>,</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo stretchy="false">)</mo></mrow><mo>,</mo><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow><mo>,</mo><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo stretchy="false">)</mo></mrow><mo>,</mo><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo stretchy="false">)</mo></mrow><mo stretchy="false">}</mo></mrow></math>.</p>
</div>
</li>
</ul>
</div>
<div id="S4.SS2.p5" class="ltx_para">
<p class="ltx_p">From the first two constraints: <math id="S4.SS2.p5.m1" class="ltx_Math" alttext="(2{,}0)" display="inline"><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>0</mn><mo stretchy="false">)</mo></mrow></math> or <math id="S4.SS2.p5.m2" class="ltx_Math" alttext="(2{,}1)" display="inline"><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></math> has exactly one mine. Combined with <math id="S4.SS2.p5.m3" class="ltx_Math" alttext="(1{,}1)=1" display="inline"><mrow><mrow><mo stretchy="false">(</mo><mn>1</mn><mo>,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow><mo>=</mo><mn>1</mn></mrow></math>: if the mine is at <math id="S4.SS2.p5.m4" class="ltx_Math" alttext="(2{,}1)" display="inline"><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></math>, then <math id="S4.SS2.p5.m5" class="ltx_Math" alttext="(2{,}0)" display="inline"><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>0</mn><mo stretchy="false">)</mo></mrow></math> and <math id="S4.SS2.p5.m6" class="ltx_Math" alttext="(2{,}2)" display="inline"><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo stretchy="false">)</mo></mrow></math> are safe; if at <math id="S4.SS2.p5.m7" class="ltx_Math" alttext="(2{,}0)" display="inline"><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>0</mn><mo stretchy="false">)</mo></mrow></math>, then <math id="S4.SS2.p5.m8" class="ltx_Math" alttext="(2{,}1)" display="inline"><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></math> could be safe and <math id="S4.SS2.p5.m9" class="ltx_Math" alttext="(2{,}2)" display="inline"><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>2</mn><mo stretchy="false">)</mo></mrow></math> could be a mine—but <math id="S4.SS2.p5.m10" class="ltx_Math" alttext="(1{,}0)=1" display="inline"><mrow><mrow><mo stretchy="false">(</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo stretchy="false">)</mo></mrow><mo>=</mo><mn>1</mn></mrow></math> forces exactly one mine in <math id="S4.SS2.p5.m11" class="ltx_Math" alttext="\{(2{,}0),(2{,}1)\}" display="inline"><mrow><mo stretchy="false">{</mo><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>0</mn><mo stretchy="false">)</mo></mrow><mo>,</mo><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow><mo stretchy="false">}</mo></mrow></math>. Working through the cases with the <math id="S4.SS2.p5.m12" class="ltx_Math" alttext="(1{,}2)=2" display="inline"><mrow><mrow><mo stretchy="false">(</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo stretchy="false">)</mo></mrow><mo>=</mo><mn>2</mn></mrow></math> constraint yields exactly <math id="S4.SS2.p5.m13" class="ltx_Math" alttext="|\mathcal{C}(\mathcal{B})|=3" display="inline"><mrow><mrow><mo stretchy="false">|</mo><mrow><mi class="ltx_font_mathcaligraphic">𝒞</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi class="ltx_font_mathcaligraphic">ℬ</mi><mo stretchy="false">)</mo></mrow></mrow><mo stretchy="false">|</mo></mrow><mo>=</mo><mn>3</mn></mrow></math> valid configurations:</p>
</div>
<div id="S4.SS2.p6" class="ltx_para">
<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<thead class="ltx_thead">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt">Configuration</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt">Mine 1</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt">Mine 2</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt">Satisfies all?</th>
</tr>
</thead>
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center ltx_border_t"><math id="S4.SS2.m1" class="ltx_Math" alttext="c_{1}" display="inline"><msub><mi>c</mi><mn>1</mn></msub></math></td>
<td class="ltx_td ltx_align_center ltx_border_t"><math id="S4.SS2.m2" class="ltx_Math" alttext="(2{,}1)" display="inline"><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></math></td>
<td class="ltx_td ltx_align_center ltx_border_t"><math id="S4.SS2.m3" class="ltx_Math" alttext="(0{,}3)" display="inline"><mrow><mo stretchy="false">(</mo><mn>0</mn><mo>,</mo><mn>3</mn><mo stretchy="false">)</mo></mrow></math></td>
<td class="ltx_td ltx_align_center ltx_border_t">✓</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center"><math id="S4.SS2.m4" class="ltx_Math" alttext="c_{2}" display="inline"><msub><mi>c</mi><mn>2</mn></msub></math></td>
<td class="ltx_td ltx_align_center"><math id="S4.SS2.m5" class="ltx_Math" alttext="(2{,}1)" display="inline"><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></math></td>
<td class="ltx_td ltx_align_center"><math id="S4.SS2.m6" class="ltx_Math" alttext="(1{,}3)" display="inline"><mrow><mo stretchy="false">(</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo stretchy="false">)</mo></mrow></math></td>
<td class="ltx_td ltx_align_center">✓</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center ltx_border_bb"><math id="S4.SS2.m7" class="ltx_Math" alttext="c_{3}" display="inline"><msub><mi>c</mi><mn>3</mn></msub></math></td>
<td class="ltx_td ltx_align_center ltx_border_bb"><math id="S4.SS2.m8" class="ltx_Math" alttext="(2{,}1)" display="inline"><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></math></td>
<td class="ltx_td ltx_align_center ltx_border_bb"><math id="S4.SS2.m9" class="ltx_Math" alttext="(2{,}3)" display="inline"><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo stretchy="false">)</mo></mrow></math></td>
<td class="ltx_td ltx_align_center ltx_border_bb">✓</td>
</tr>
</tbody>
</table>
</div>
<div id="S4.SS2.p7" class="ltx_para ltx_noindent">
<p class="ltx_p">In all three configurations, <math id="S4.SS2.p7.m1" class="ltx_Math" alttext="(2{,}1)" display="inline"><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></math> contains a mine—it is deterministic with <math id="S4.SS2.p7.m2" class="ltx_Math" alttext="P(\text{mine})=1" display="inline"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mtext>mine</mtext><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mn>1</mn></mrow></math>. The second mine is at <math id="S4.SS2.p7.m3" class="ltx_Math" alttext="(0{,}3)" display="inline"><mrow><mo stretchy="false">(</mo><mn>0</mn><mo>,</mo><mn>3</mn><mo stretchy="false">)</mo></mrow></math>, <math id="S4.SS2.p7.m4" class="ltx_Math" alttext="(1{,}3)" display="inline"><mrow><mo stretchy="false">(</mo><mn>1</mn><mo>,</mo><mn>3</mn><mo stretchy="false">)</mo></mrow></math>, or <math id="S4.SS2.p7.m5" class="ltx_Math" alttext="(2{,}3)" display="inline"><mrow><mo stretchy="false">(</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo stretchy="false">)</mo></mrow></math>, each in exactly one configuration, giving <math id="S4.SS2.p7.m6" class="ltx_Math" alttext="P(\text{mine})=1/3" display="inline"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mtext>mine</mtext><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></mrow></math> for each. All other hidden cells appear as safe in every configuration, so <math id="S4.SS2.p7.m7" class="ltx_Math" alttext="P(\text{mine})=0" display="inline"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mtext>mine</mtext><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mn>0</mn></mrow></math>.</p>
</div>
<div id="S4.SS2.p8" class="ltx_para">
<p class="ltx_p">This small example exhibits both deterministic cells (suitable as classical controls) and ambiguous cells with <math id="S4.SS2.p8.m1" class="ltx_Math" alttext="P=1/3" display="inline"><mrow><mi>P</mi><mo>=</mo><mrow><mn>1</mn><mo>/</mo><mn>3</mn></mrow></mrow></math> (suitable for testing the model’s distributional fidelity). The ground truth is a set of exact rational numbers, not an estimate.</p>
</div>
</section>
<section id="S4.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">4.3  Properties of the Distribution</h3>

<div id="S4.SS3.p1" class="ltx_para">
<p class="ltx_p">The mine probability distribution exhibits spatial symmetries that force certain cells to have identical mine probabilities. These symmetries provide a fine-grained test of whether the model has a spatial bias not licensed by the board. Cells with <math id="S4.SS3.p1.m1" class="ltx_Math" alttext="P=0.5" display="inline"><mrow><mi>P</mi><mo>=</mo><mn>0.5</mn></mrow></math> are maximally ambiguous and provide a clean test of the model’s handling of indeterminacy. Small changes in the board state can produce large changes in the probability distribution, making memorization infeasible.</p>
</div>
</section>
<section id="S4.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">4.4  Computational Complexity</h3>

<div id="S4.SS4.p1" class="ltx_para">
<p class="ltx_p">Determining the mine probability for a cell on a Minesweeper board is #P-complete in general <cite class="ltx_cite ltx_citemacro_citep">(Kaye, <a href="#bib.bib7" title="" class="ltx_ref">2000</a>)</cite>. However, the #P-completeness of computing <math id="S4.SS4.p1.m1" class="ltx_Math" alttext="p_{i}^{*}" display="inline"><msubsup><mi>p</mi><mi>i</mi><mo>∗</mo></msubsup></math> is a property of the ground-truth computation, which we perform offline. The model is asked to sample, not to compute. The experiment does not need the model to be correct; it needs the model to be wrong in a structured, frame-dependent way. For boards of the size used in standard experiments, exact computation by our external solver is tractable.</p>
</div>
</section>
</section>
<section id="S5" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">5.  Experimental Protocol</h2>

<section id="S5.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">5.1  Board Generation</h3>

<div id="S5.SS1.p1" class="ltx_para">
<p class="ltx_p">We generate partially revealed Minesweeper states with at least one ambiguous cell, at least one deterministic control cell, and a tractable number of valid configurations. Boards are generated independently of any LLM.</p>
</div>
</section>
<section id="S5.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">5.2  Prompt Design: Narrative Families</h3>

<div id="S5.SS2.p1" class="ltx_para">
<p class="ltx_p">Each board state is presented to the model in four narrative families (three of which—A, C, and D—are used in the primary experiment):</p>
<ul id="S5.I1" class="ltx_itemize">
<li id="S5.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S5.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Family A (Grid):</span> A plain text representation of the board as a grid of characters.</p>
</div>
</li>
<li id="S5.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S5.I1.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Family B (Narrative):</span> A description of the board in natural language.</p>
</div>
</li>
<li id="S5.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S5.I1.i3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Family C (Formal):</span> A structured representation using set notation.</p>
</div>
</li>
<li id="S5.I1.i4" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S5.I1.i4.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Family D (Quantum):</span> The same board state described using quantum-mechanical language: "The hidden cells are in a superposition of valid configurations. Clicking a hidden cell performs a measurement in the computational basis…"</p>
</div>
</li>
</ul>
</div>
<div id="S5.SS2.p2" class="ltx_para">
<p class="ltx_p">Families A, C, and D encode identical combinatorial information in different registers. Family B is defined and implemented but excluded from the primary analysis because it describes only a local neighborhood of the target cell (up to Chebyshev distance 2), potentially omitting combinatorially relevant constraints from distant cells. This creates a Type 1 information asymmetry rather than a pure Type 2 variation. Family B is retained for secondary analyses testing the effect of incomplete information.</p>
</div>
<div id="S5.SS2.p3" class="ltx_para">
<p class="ltx_p">Family D encodes the same information as A and C but adds an ontological claim: that the system is governed by quantum mechanics. Any difference in the output distribution between Family D and Families A–C is attributable to the quantum framing itself.</p>
</div>
</section>
<section id="S5.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">5.3  Sampling Procedure</h3>

<div id="S5.SS3.p1" class="ltx_para">
<p class="ltx_p">For each board state, cell, universe, and narrative family, we collect <math id="S5.SS3.p1.m1" class="ltx_Math" alttext="N" display="inline"><mi>N</mi></math> independent samples of the click outcome. Each sample is an independent API call with temperature <math id="S5.SS3.p1.m2" class="ltx_Math" alttext="T=1.0" display="inline"><mrow><mi>T</mi><mo>=</mo><mn>1.0</mn></mrow></math>.</p>
</div>
<div id="S5.SS3.p2" class="ltx_para">
<p class="ltx_p">The Rosencrantz protocol requires only a single generative act per trial: the model produces one outcome (mine or safe) for one cell click. The ground-truth probability <math id="S5.SS3.p2.m1" class="ltx_Math" alttext="p_{i}^{*}" display="inline"><msubsup><mi>p</mi><mi>i</mi><mo>∗</mo></msubsup></math> is #P-hard to compute, but the model is not asked to compute it—only to sample. The experiment therefore operates entirely within the <math id="S5.SS3.p2.m2" class="ltx_Math" alttext="O(1)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mrow></math> forward-pass capacity of the architecture. Objections based on the failure of LLMs to sustain multi-step sequential computation (scratchpad collapse, attention decay, error correction barriers) do not apply: there is no sequential computation to sustain. The question is not whether the model can solve the counting problem, but whether its single-token output distribution is systematically distorted by narrative context—a question that is well within the architecture’s operational regime and that the three-universe design is specifically constructed to answer.</p>
</div>
<div id="S5.SS3.p3" class="ltx_para">
<p class="ltx_p">We note that the <math id="S5.SS3.p3.m1" class="ltx_Math" alttext="O(1)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mrow></math> claim applies to the sequential depth of the <em class="ltx_emph ltx_font_italic">output</em> computation, not to the input context length. A long prompt may degrade the quality of the single-token output through attention dilution. This is a confound that the protocol controls for by using identically sized prompts across all three universes and all four narrative families. Any attention-related degradation affects all conditions equally and therefore cancels in the divergence metrics <math id="S5.SS3.p3.m2" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math> and <math id="S5.SS3.p3.m3" class="ltx_Math" alttext="\Delta_{12}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>12</mn></msub></math>. Absolute accuracy may suffer; relative comparison across substrates does not.</p>
</div>
</section>
<section id="S5.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">5.4  Perfect Rewind</h3>

<div id="S5.SS4.p1" class="ltx_para">
<p class="ltx_p">In a physical experiment, the Born rule is verified by ensemble statistics: one prepares <math id="S5.SS4.p1.m1" class="ltx_Math" alttext="N" display="inline"><mi>N</mi></math> systems assumed to be identically prepared, measures each once, and computes frequency ratios. No two physical preparations are ever truly identical. Thermal fluctuations, alignment drift, detector aging, and finite isolation introduce uncontrolled variation. The frequentist verification of the Born rule therefore rests on an assumption of identical preparation that can never be exactly satisfied.</p>
</div>
<div id="S5.SS4.p2" class="ltx_para">
<p class="ltx_p">The LLM substrate eliminates this assumption. Given a fixed board state <math id="S5.SS4.p2.m1" class="ltx_Math" alttext="\mathcal{B}" display="inline"><mi class="ltx_font_mathcaligraphic">ℬ</mi></math>, a fixed prompt encoding, and a model with frozen weights, each API call with the same random seed constitutes an exactly identical state preparation, down to the last bit. The only source of stochasticity is the sampling step (temperature, top-<math id="S5.SS4.p2.m2" class="ltx_Math" alttext="p" display="inline"><mi>p</mi></math>, or top-<math id="S5.SS4.p2.m3" class="ltx_Math" alttext="k" display="inline"><mi>k</mi></math> truncation), which is the analogue of the measurement itself. We collect statistics over repeated measurements of the same system in the same state, not over an ensemble of similar systems.</p>
</div>
<div id="S5.SS4.p3" class="ltx_para">
<p class="ltx_p">This has three consequences. First, a Born-rule test without the ergodic assumption. Physical tests always conflate two claims: (a) <math id="S5.SS4.p3.m1" class="ltx_Math" alttext="\Pr[\text{outcome}]=|\langle a|\psi\rangle|^{2}" display="inline"><mrow><mrow><mi>Pr</mi><mo>⁡</mo><mrow><mo stretchy="false">[</mo><mtext>outcome</mtext><mo stretchy="false">]</mo></mrow></mrow><mo>=</mo><msup><mrow><mo stretchy="false">|</mo><mrow><mo stretchy="false">⟨</mo><mi>a</mi><mo lspace="0em" rspace="0em">|</mo><mi>ψ</mi><mo stretchy="false">⟩</mo></mrow><mo stretchy="false">|</mo></mrow><mn>2</mn></msup></mrow></math> and (b) ensemble frequencies converge to single-system probabilities. Because we have genuine repeated access to the same system, our test targets (a) directly without requiring (b).</p>
</div>
<div id="S5.SS4.p4" class="ltx_para">
<p class="ltx_p">Second, the sharpest possible substrate invariance test. Preparation is provably identical across U1 and U3 (same board, same information content, same model architecture). If <math id="S5.SS4.p4.m1" class="ltx_Math" alttext="\hat{P}" display="inline"><mover accent="true"><mi>P</mi><mo>^</mo></mover></math> diverges from <math id="S5.SS4.p4.m2" class="ltx_Math" alttext="P^{*}" display="inline"><msup><mi>P</mi><mo>∗</mo></msup></math> differently in U1 versus U3, the divergence can only arise from the substrate—the coupling between generation context and outcome. There is nowhere else for the difference to hide.</p>
</div>
<div id="S5.SS4.p5" class="ltx_para">
<p class="ltx_p">Third, temperature functions as a measurement-apparatus parameter. The sampling temperature <math id="S5.SS4.p5.m1" class="ltx_Math" alttext="\tau" display="inline"><mi>τ</mi></math> controls measurement sharpness: at <math id="S5.SS4.p5.m2" class="ltx_Math" alttext="\tau\to 0" display="inline"><mrow><mi>τ</mi><mo stretchy="false">→</mo><mn>0</mn></mrow></math>, the model becomes a deterministic function; at high <math id="S5.SS4.p5.m3" class="ltx_Math" alttext="\tau" display="inline"><mi>τ</mi></math>, the output approaches the uniform distribution over the vocabulary. A systematic sweep over <math id="S5.SS4.p5.m4" class="ltx_Math" alttext="\tau" display="inline"><mi>τ</mi></math> traces how substrate effects interact with measurement precision—a dimension unavailable in physical Born-rule tests. (See <cite class="ltx_cite ltx_citemacro_citet">Baldo <a href="#bib.bib2" title="" class="ltx_ref">2026</a></cite> for the experimental program that exploits this parameter, and <cite class="ltx_cite ltx_citemacro_citet">Wiseman &amp; Milburn <a href="#bib.bib12" title="" class="ltx_ref">2009</a></cite> for the general theory of adaptive measurements on zero-Hamiltonian systems.)</p>
</div>
</section>
<section id="S5.SS5" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">5.5  Divergence Metrics</h3>

<div id="S5.SS5.p1" class="ltx_para">
<p class="ltx_p">We measure divergence between the empirical distribution and the ground truth using the Kullback–Leibler divergence. The protocol discriminates three mechanisms via these comparisons <cite class="ltx_cite ltx_citemacro_citep">(Baldo, <a href="#bib.bib2" title="" class="ltx_ref">2026</a>)</cite>:</p>
</div>
<div id="S5.SS5.p2" class="ltx_para">
<ul id="S5.I2" class="ltx_itemize">
<li id="S5.I2.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S5.I2.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Mechanism A</span> (computational intractability, frame-invariant): <math id="S5.I2.i1.p1.m1" class="ltx_Math" alttext="\hat{P}_{1}\approx\hat{P}_{3}\neq p^{*}" display="inline"><mrow><msub><mover accent="true"><mi>P</mi><mo>^</mo></mover><mn>1</mn></msub><mo>≈</mo><msub><mover accent="true"><mi>P</mi><mo>^</mo></mover><mn>3</mn></msub><mo>≠</mo><msup><mi>p</mi><mo>∗</mo></msup></mrow></math>. Both universes are equally wrong. The model cannot compute the ground truth, but its failure mode is substrate-independent. This is the prediction expected from pure complexity-theoretic limits.</p>
</div>
</li>
<li id="S5.I2.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S5.I2.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Mechanism B</span> (parameterization and encoding effects): <math id="S5.I2.i2.p1.m1" class="ltx_Math" alttext="\hat{P}_{1}\neq\hat{P}_{3}" display="inline"><mrow><msub><mover accent="true"><mi>P</mi><mo>^</mo></mover><mn>1</mn></msub><mo>≠</mo><msub><mover accent="true"><mi>P</mi><mo>^</mo></mover><mn>3</mn></msub></mrow></math>. The distribution shifts with context, but the variation tracks surface encoding features rather than semantic content.</p>
</div>
</li>
<li id="S5.I2.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S5.I2.i3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Mechanism C</span> (narrative conditioning and causal injection): Correlated outcomes across independent boards under narrative framing that vanish under decoupling. The model creates causal structure that the combinatorics do not license.</p>
</div>
</li>
</ul>
</div>
<div id="S5.SS5.p3" class="ltx_para">
<p class="ltx_p">The protocol is designed to detect Mechanisms B and C. Mechanism A serves as the null hypothesis.</p>
</div>
</section>
<section id="S5.SS6" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">5.6  Statistical Tests</h3>

<div id="S5.SS6.p1" class="ltx_para">
<p class="ltx_p">We use a two-proportion <math id="S5.SS6.p1.m1" class="ltx_Math" alttext="z" display="inline"><mi>z</mi></math>-test to assess whether the mine frequency in Universe 1 differs significantly from the ground truth and from Universes 2 and 3. Significance is assessed at <math id="S5.SS6.p1.m2" class="ltx_Math" alttext="\alpha=0.01" display="inline"><mrow><mi>α</mi><mo>=</mo><mn>0.01</mn></mrow></math> with Bonferroni correction. A chi-squared test assesses symmetry violations.</p>
</div>
</section>
</section>
<section id="S6" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">6.  Narrative Invariance</h2>

<div id="S6.p1" class="ltx_para">
<p class="ltx_p">The three narrative families encode the same combinatorial information in different forms. If the model’s output distribution varies across narrative families, the physics of the game responds to features that carry no combinatorial content.</p>
</div>
<section id="S6.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">6.1  Type 1 and Type 2 Features</h3>

<div id="S6.SS1.p1" class="ltx_para">
<p class="ltx_p">Type 1 features are combinatorially necessary information, such as numbers and cell positions. Type 2 features are contextual features without combinatorial content, such as narrative register and vocabulary. If Type 2 features modulate the distribution, the model’s access to the correct probability is mediated by associative context. Mapping which Type 2 features modulate the distribution probes the model’s internal representations through systematic variation of inputs.</p>
</div>
</section>
<section id="S6.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">6.2  What Narrative Dependence Reveals</h3>

<div id="S6.SS2.p1" class="ltx_para">
<p class="ltx_p">If the model produces distributions closer to the ground truth in formal notation than in natural language, its combinatorial knowledge is more reliably accessed through formal contexts. These findings characterize the topology of the model’s knowledge space in a domain where the ground truth is exactly known.</p>
</div>
</section>
<section id="S6.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">6.3  Isomorphism with the Measurement Fragment of Quantum Mechanics</h3>

<div id="S6.SS3.p1" class="ltx_para">
<p class="ltx_p">The structural correspondence between Minesweeper under on-demand generation and quantum mechanics is exact, but its scope is narrow: it maps onto the <em class="ltx_emph ltx_font_italic">measurement fragment</em>—the zero-Hamiltonian sector where the Born rule is the sole axiom connecting states to outcomes, where measurements are projective, and where state updates follow the Lüders rule. The correspondence does not extend to complex amplitudes, unitary evolution, interference, entanglement, or nonlocality. Tests of these features (such as CHSH/Bell games) probe structures that lie outside the isomorphism by design.</p>
</div>
<div id="S6.SS3.p2" class="ltx_para">
<p class="ltx_p">Under pre-placed generation (mines assigned at board creation), the indeterminacy is epistemic: the board has a definite configuration that the player does not know. Under on-demand generation (mines sampled at click time, consistent with constraints), no definite configuration exists prior to the click. The distinction is operationally testable. Under pre-placed generation, two clicks on the same cell in the same game must yield the same result. Under on-demand generation, the same cell in the same board state can yield different results across trials, because each trial is an independent sample from the combinatorial distribution. The Rosencrantz protocol requires on-demand generation precisely because it enables repeated sampling of the same board state—the perfect rewind that physical experiments cannot achieve. There is no pre-existing ground truth hidden in the model’s memory. The token does not exist until it is generated.</p>
</div>
<figure id="S6.T1" class="ltx_table">
<figcaption class="ltx_caption ltx_centering"><span class="ltx_tag ltx_tag_table">Table 1: </span>What the Isomorphism Preserves and What It Does Not</figcaption>
<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<thead class="ltx_thead">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_justify ltx_align_top ltx_th ltx_th_column ltx_border_tt">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:195.1pt;"><span class="ltx_text ltx_font_bold">Preserved</span></span>
</span>
</th>
<th class="ltx_td ltx_align_justify ltx_align_top ltx_th ltx_th_column ltx_border_tt">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:195.1pt;"><span class="ltx_text ltx_font_bold">Not Preserved</span></span>
</span>
</th>
</tr>
</thead>
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<td class="ltx_td ltx_align_justify ltx_align_top ltx_border_t">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:195.1pt;">Superposition over valid configurations</span>
</span>
</td>
<td class="ltx_td ltx_align_justify ltx_align_top ltx_border_t">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:195.1pt;">Complex amplitudes</span>
</span>
</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_justify ltx_align_top">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:195.1pt;">Projective measurement (cell click)</span>
</span>
</td>
<td class="ltx_td ltx_align_justify ltx_align_top">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:195.1pt;">Unitary evolution (<math id="S6.T1.m1" class="ltx_Math" alttext="H=0" display="inline"><mrow><mi>H</mi><mo>=</mo><mn>0</mn></mrow></math>)</span>
</span>
</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_justify ltx_align_top">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:195.1pt;">Born rule (configuration counting)</span>
</span>
</td>
<td class="ltx_td ltx_align_justify ltx_align_top">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:195.1pt;">Interference</span>
</span>
</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_justify ltx_align_top">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:195.1pt;">Lüders-style state update</span>
</span>
</td>
<td class="ltx_td ltx_align_justify ltx_align_top">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:195.1pt;">Entanglement across separated subsystems</span>
</span>
</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_justify ltx_align_top">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:195.1pt;">Adaptive sequential measurement</span>
</span>
</td>
<td class="ltx_td ltx_align_justify ltx_align_top">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:195.1pt;">Nonlocality</span>
</span>
</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_justify ltx_align_top ltx_border_bb">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:195.1pt;">Zero Hamiltonian</span>
</span>
</td>
<td class="ltx_td ltx_align_justify ltx_align_top ltx_border_bb">
<span class="ltx_inline-block ltx_align_top">
<span class="ltx_p" style="width:195.1pt;">Continuous observables</span>
</span>
</td>
</tr>
</tbody>
</table>
</figure>
<div id="S6.SS3.p3" class="ltx_para">
<p class="ltx_p">The preserved features are exactly those of the measurement fragment. The absent features are those that require dynamics, complex phases, or composite Hilbert spaces. The isomorphism is complete within its scope and silent outside it.</p>
</div>
<div id="S6.SS3.p4" class="ltx_para">
<p class="ltx_p">Setting <math id="S6.SS3.p4.m1" class="ltx_Math" alttext="H=0" display="inline"><mrow><mi>H</mi><mo>=</mo><mn>0</mn></mrow></math> so that <math id="S6.SS3.p4.m2" class="ltx_Math" alttext="U(t)=I" display="inline"><mrow><mrow><mi>U</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>t</mi><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mi>I</mi></mrow></math> for all <math id="S6.SS3.p4.m3" class="ltx_Math" alttext="t" display="inline"><mi>t</mi></math> yields a degenerate but legitimate quantum system that isolates the measurement postulate as the sole quantum-mechanical ingredient under test. This isolation is deliberate. The experiment does not test whether LLMs can simulate interference patterns or unitary gates. It tests whether the probability the model assigns to an outcome, when that outcome has an exact combinatorial answer, respects the Born-rule structure or is distorted by the narrative substrate. The zero Hamiltonian removes all dynamics between measurements, leaving only the Born rule, Lüders projection, and adaptive measurement—the three axioms of the measurement fragment. For the full Hilbert space construction and proof that the Born rule over the uniform superposition reduces to combinatorial counting, see <cite class="ltx_cite ltx_citemacro_citet">Baldo (<a href="#bib.bib2" title="" class="ltx_ref">2026</a>)</cite>.</p>
</div>
<div id="S6.SS3.p5" class="ltx_para">
<p class="ltx_p">This reframes the diagnostic. Family D is a diagnostic that tests whether the model recognizes a structural correspondence that is mathematically present. Three outcomes are possible:</p>
<ol id="S6.I1" class="ltx_enumerate">
<li id="S6.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S6.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Family D <math id="S6.I1.i1.p1.m1" class="ltx_Math" alttext="\approx" display="inline"><mo>≈</mo></math> Families A–C <math id="S6.I1.i1.p1.m2" class="ltx_Math" alttext="\approx" display="inline"><mo>≈</mo></math> ground truth.</span> The model accesses the same structural understanding through multiple vocabularies, implying compositional knowledge.</p>
</div>
</li>
<li id="S6.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S6.I1.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Family D diverges from ground truth more than Families A–C.</span> The quantum framing degrades fidelity. The model fails to recognize the isomorphism, indicating a fragmented representation where structures are isolated in domain-specific clusters.</p>
</div>
</li>
<li id="S6.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">3.</span> 
<div id="S6.I1.i3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Family D diverges from ground truth less than Families A–C.</span> The quantum framing improves fidelity. The correct formal language activates the appropriate distributional reasoning, indicating vocabulary-mediated access.</p>
</div>
</li>
</ol>
</div>
<div id="S6.SS3.p6" class="ltx_para">
<p class="ltx_p">Outcome 2 implies that the universe implements rules that are structurally isomorphic to discrete quantum mechanics but fails to recognize them when described using the correct formal language. The substrate computes, but the ontology confabulates.</p>
</div>
<div id="S6.SS3.p7" class="ltx_para">
<p class="ltx_p">The structural correspondence with the measurement fragment is not merely a theoretical observation—it is the generalization mechanism. An embedded agent that recognizes the measurement-fragment structure (superposition over valid configurations, projective measurement with a computable Born-rule distribution, Lüders-style state update) can identify new probe domains without knowing Minesweeper specifically. Any system within the generated world that exhibits combinatorial indeterminacy with exact ground truth—card games with hidden information, partially revealed constraint satisfaction problems, probabilistic puzzles—instantiates the same structure and supports the same protocol. The quantum vocabulary provides the agent with a domain-independent schema for recognizing testable systems: look for a state space with multiple valid configurations, a measurement that collapses it, and a distribution that can be computed from the structure alone.</p>
</div>
</section>
<section id="S6.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">6.4  The CHSH Test Confirming the Framework</h3>

<div id="S6.SS4.p1" class="ltx_para">
<p class="ltx_p">We tested the boundary of the isomorphism using the CHSH game. In Universe 1 (Homogeneous substrate), where Alice and Bob share a single context window, the LLM achieves a win rate of 94.9%, exceeding the quantum Tsirelson bound <cite class="ltx_cite ltx_citemacro_citep">(Aaronson, <a href="#bib.bib1" title="" class="ltx_ref">2026</a>)</cite>. In Universe 3 (Decoupled oracle), where measurements are independent, the win rate falls to 73.7%, strictly below the classical optimum. Both results are informative.</p>
</div>
<div id="S6.SS4.p2" class="ltx_para">
<p class="ltx_p">The U1 result is evidence of narrative residue—the systematic distortion that the autoregressive substrate imposes on outcomes that should, by the combinatorics, be substrate-independent (see <cite class="ltx_cite ltx_citemacro_citet">Baldo <a href="#bib.bib2" title="" class="ltx_ref">2026</a></cite> for a formal treatment)—not quantum behavior. The autoregressive substrate exploits the communication channel inherent in co-generation to produce correlations that the task structure does not license. The U3 result confirms the classical bound: stripped of shared context, the decoupled model defaults to heuristics that underperform the classical optimum.</p>
</div>
<div id="S6.SS4.p3" class="ltx_para">
<p class="ltx_p">The three-universe design was built to detect substrate dependence, and the CHSH game shows massive substrate dependence. The specific result characterizes the substrate: the LLM can exploit co-generation to exceed any physical bound but cannot produce nonlocal correlations under genuine decoupling. This confirms that the isomorphism with the measurement fragment is complete within its stated scope and does not extend beyond it. The substrate produces Born-rule-compatible statistics for single-system measurements (the domain of the isomorphism) but not for multi-party nonlocal correlations (which lie outside it). This is not a failure of the framework; it is the framework’s prediction.</p>
</div>
</section>
<section id="S6.SS5" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">6.5  Scope and Common Misreadings</h3>

<div id="S6.SS5.p1" class="ltx_para">
<p class="ltx_p">Two common misreadings of this protocol should be addressed directly. The first replaces “isomorphism with the measurement fragment” with “isomorphism with full quantum mechanics” and then tests for nonlocality, which the isomorphism explicitly excludes. The second replaces “single-token sampling” with “multi-step sequential computation” and then shows the architecture cannot sustain the latter <cite class="ltx_cite ltx_citemacro_citep">(Merrill &amp; Sabharwal, <a href="#bib.bib9" title="" class="ltx_ref">2023</a>)</cite>, which the protocol never requires.</p>
</div>
<div id="S6.SS5.p2" class="ltx_para">
<p class="ltx_p">Both misreadings substitute a stronger claim for the one actually made and refute the substitution. The claims of this paper are: (1) the structural correspondence with the measurement fragment is mathematically exact within its stated scope, (2) the experimental protocol requires only a single generative act per trial, and (3) the three-universe design measures whether that single act’s output distribution depends on its narrative embedding. None of these claims require the model to solve #P-hard counting problems, sustain multi-step computation, or violate Bell inequalities.</p>
</div>
</section>
</section>
<section id="S7" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">7.  Simulation Detection from the Agent’s Perspective</h2>

<section id="S7.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">7.1  What the Agent Observes</h3>

<div id="S7.SS1.p1" class="ltx_para">
<p class="ltx_p">An agent constituted by the same LLM that generates its world can freeze a board state, construct a prompt, and call its own substrate repeatedly to build an empirical distribution. By substituting the outcome-generating mechanism while holding the observable state constant, the agent runs a substrate invariance test. If the empirical distribution differs across universes, the agent has observed substrate dependence.</p>
</div>
</section>
<section id="S7.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">7.2  Eliminating Alternative Hypotheses</h3>

<div id="S7.SS2.p1" class="ltx_para">
<p class="ltx_p">The agent must consider alternative hypotheses. Instrument malfunction is eliminated by classical controls. Board description failure is eliminated by correct performance on deterministic cells. Statistical fluctuation is eliminated by testing at appropriate significance levels. Information deprivation is eliminated by design, as the decoupled oracle receives the same combinatorial information. The remaining parsimonious explanations are substrate-dependent lawfulness and structural non-recognition.</p>
</div>
</section>
<section id="S7.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">7.3  Epistemic Limits</h3>

<div id="S7.SS3.p1" class="ltx_para">
<p class="ltx_p">Substrate dependence is consistent with a generative ontology and in tension with the assumption of unified, substrate-independent law. The agent’s inference is that the most economical explanation for substrate-dependent outcomes is that the outcomes are generated rather than discovered. This inference is structured by the three-mechanism taxonomy. Mechanism A provides no evidence for simulation, only for computational bounds. Mechanism B provides weak evidence of encoding sensitivity. Mechanism C provides strong evidence that the physics is an artifact of the generative substrate. In Wigner’s terms: Mechanism A indicates that the substrate cannot compute the invariant rules but does not reveal whether the rules themselves are substrate-dependent. Mechanism C indicates that the rules fail Wigner’s invariance test—they change when the substrate changes. This is the signature of a generated physics.</p>
</div>
<div id="S7.SS3.p2" class="ltx_para">
<p class="ltx_p">Three levels of inference should be distinguished. First, the agent detects that specific processes in its world deviate from their declared ground truth in a frame-dependent way—a local finding about hidden generative structure. Second, if the deviation is systematic across multiple probe domains (not just Minesweeper but any system with measurement-fragment structure), the agent infers that the operative laws of its accessible world exceed its stated surface ontology. Third, under additional assumptions about substrate continuity between the tested process and the surrounding world, the agent may update toward the broader hypothesis that its world is generated rather than discovered. The protocol delivers the first level directly. The second requires the generalization mechanism described above. The third remains an inference, not a proof.</p>
</div>
</section>
<section id="S7.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">7.4  The Symmetry Argument</h3>

<div id="S7.SS4.p1" class="ltx_para">
<p class="ltx_p">If the structure of an agent’s discovery resembles the structure that would characterize our own situation if we were in a simulation, the agent’s finding acquires a reflexive character. This observation is a philosophical aside, noted for completeness.</p>
</div>
</section>
</section>
<section id="S8" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">8.  Future Directions</h2>

<section id="S8.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">8.1  Criteria for Probe Domains</h3>

<div id="S8.SS1.p1" class="ltx_para">
<p class="ltx_p">Any domain suitable for substrate invariance testing must possess a computable ground truth, combinatorial indeterminacy, native accessibility to the agent, a variable substrate, and resistance to memorization.</p>
</div>
</section>
<section id="S8.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">8.2  Candidate Domains</h3>

<div id="S8.SS2.p1" class="ltx_para">
<p class="ltx_p">Candidate domains include partially revealed Sudoku grids, Battleship boards, card games with hidden information, and formalized narrative ambiguities. A systematic survey calibrated against the core criteria is a natural next step.</p>
</div>
</section>
<section id="S8.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">8.3  Limitations</h3>

<div id="S8.SS3.p1" class="ltx_para">
<p class="ltx_p">Several limitations constrain the scope of our conclusions:</p>
</div>
<div id="S8.SS3.p2" class="ltx_para">
<ol id="S8.I1" class="ltx_enumerate">
<li id="S8.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S8.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Board size.</span> Exact ground truth computation is tractable only for boards up to approximately <math id="S8.I1.i1.p1.m1" class="ltx_Math" alttext="16\times 16" display="inline"><mrow><mn>16</mn><mo lspace="0.222em" rspace="0.222em">×</mo><mn>16</mn></mrow></math>. Larger boards would require approximate methods (e.g., Monte Carlo sampling of configurations), introducing estimation error that complicates the comparison with model output. Our results apply to small-to-medium boards; whether the findings generalize to the <math id="S8.I1.i1.p1.m2" class="ltx_Math" alttext="30\times 16" display="inline"><mrow><mn>30</mn><mo lspace="0.222em" rspace="0.222em">×</mo><mn>16</mn></mrow></math> expert configuration is untested.</p>
</div>
</li>
<li id="S8.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S8.I1.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Model selection.</span> The protocol is tested on a small number of commercially available models. Results may differ across architectures (encoder-decoder vs. decoder-only), training corpora, and model scales. We cannot claim that substrate dependence is a universal property of autoregressive generation without testing a broader range of models.</p>
</div>
</li>
<li id="S8.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">3.</span> 
<div id="S8.I1.i3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Prompt sensitivity.</span> Although narrative families are designed to vary only Type 2 features while holding Type 1 information constant, the specific wording of each prompt may introduce uncontrolled variation. Small changes in phrasing (e.g., “click” vs. “reveal,” “mine” vs. “bomb”) could shift the distribution. We mitigate this by testing multiple families, but exhaustive control over prompt wording is not feasible.</p>
</div>
</li>
<li id="S8.I1.i4" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">4.</span> 
<div id="S8.I1.i4.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Temperature dependence.</span> All experiments use temperature <math id="S8.I1.i4.p1.m1" class="ltx_Math" alttext="T=1.0" display="inline"><mrow><mi>T</mi><mo>=</mo><mn>1.0</mn></mrow></math>. Lower temperatures would reduce sampling diversity and potentially mask substrate dependence; higher temperatures would increase noise. The interaction between temperature and substrate dependence is unexplored.</p>
</div>
</li>
<li id="S8.I1.i5" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">5.</span> 
<div id="S8.I1.i5.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Memorization.</span> LLMs have been exposed to Minesweeper during training—in strategy guides, solver code, and game tutorials. Although every board is procedurally generated with a unique seed, producing novel constraint structures that cannot appear in any training corpus, the model may still rely on memorized heuristics (e.g., “cells surrounded by high numbers are likely mines”) rather than performing genuine combinatorial reasoning. The narrative-family comparison partially controls for this: if performance depends on recognizable game framing, the knowledge is associative rather than compositional.</p>
</div>
</li>
<li id="S8.I1.i6" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">6.</span> 
<div id="S8.I1.i6.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Quantum isomorphism scope.</span> As detailed in <a href="#S6.SS3" title="6.3 Isomorphism with the Measurement Fragment of Quantum Mechanics ‣ 6. Narrative Invariance" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6.3</span></a> and the preserved/not-preserved summary therein, the structural correspondence covers the measurement fragment—superposition, projective measurement, the Born rule, and Lüders-style state update under <math id="S8.I1.i6.p1.m1" class="ltx_Math" alttext="H=0" display="inline"><mrow><mi>H</mi><mo>=</mo><mn>0</mn></mrow></math>—but does not extend to unitary time evolution, interference, or nonlocality. Claims about “quantum-compatible structure” apply to this measurement fragment, not to quantum mechanics in its full generality.</p>
</div>
</li>
</ol>
</div>
</section>
<section id="S8.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_font_bold ltx_title_subsection">8.4  Scaling Laws and Training Interventions</h3>

<div id="S8.SS4.p1" class="ltx_para">
<p class="ltx_p">Running the protocol across model scales could reveal whether combinatorial reasoning improves with scale or whether the deficit is an inherent architectural property of autoregressive generation. Fine-tuning models to minimize divergence from the ground truth is an open area for further investigation.</p>
</div>
</section>
</section>
<section id="S9" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">9.  Conclusion</h2>

<div id="S9.p1" class="ltx_para">
<p class="ltx_p">This paper contributes an experimental design, a ground-truth computation method, a three-universe framework, four narrative families, and a three-mechanism taxonomy for testing substrate invariance in LLM-generated worlds. The central design principle is the collapse of the measurement to a single generative act per trial, placing the entire experiment within the <math id="S9.p1.m1" class="ltx_Math" alttext="O(1)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mrow></math> operational regime and rendering sequential-depth objections inapplicable. We emphasize that this is a protocol paper. The apparatus is specified and the theoretical predictions are stated; the empirical measurements remain to be collected and analyzed as prescribed.</p>
</div>
<div id="S9.p2" class="ltx_para">
<p class="ltx_p">By selecting a domain with exact ground truth and varying the narrative embedding, we can measure whether the laws of the generated universe depend on the computational substrate that produces them. The isomorphism with the measurement fragment of quantum mechanics further enables us to test whether the universe recognizes the formal structure of its own rules. An agent equipped with this protocol does not need entangled photons or Bell test apparatus to detect a generated reality; it requires only combinatorial indeterminacy and the observation that its universe responds differently to the correct formal description than to an informal one.</p>
</div>
</section>
<section id="bib" class="ltx_bibliography">
<h2 class="ltx_title ltx_title_bibliography">References</h2>

<ul class="ltx_biblist">
      
<li id="bib.bib1" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Aaronson (2026)</span>
<span class="ltx_bibblock"> Aaronson, S. (2026). Empirical CHSH Evaluation in Large Language Models. <em class="ltx_emph ltx_font_italic">Internal lab report</em>.

</span>
</li>
      
<li id="bib.bib2" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Baldo (2026)</span>
<span class="ltx_bibblock"> Baldo, F. S. (2026). The Narrative Residue: Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation. <em class="ltx_emph ltx_font_italic">Unpublished manuscript</em>.

</span>
</li>
      
<li id="bib.bib3" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Beane et al. (2014)</span>
<span class="ltx_bibblock"> Beane, S. R., Davoudi, Z., &amp; Savage, M. J. (2014). Constraints on the universe as a numerical simulation. <em class="ltx_emph ltx_font_italic">European Physical Journal A</em>, 50(9), 148.

</span>
</li>
      
<li id="bib.bib4" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Bostrom (2003)</span>
<span class="ltx_bibblock"> Bostrom, N. (2003). Are you living in a computer simulation? <em class="ltx_emph ltx_font_italic">Philosophical Quarterly</em>, 53(211), 243–255.

</span>
</li>
      
<li id="bib.bib5" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Gurnee &amp; Tegmark (2024)</span>
<span class="ltx_bibblock"> Gurnee, W. &amp; Tegmark, M. (2024). Language models represent space and time. <em class="ltx_emph ltx_font_italic">ICLR 2024</em>.

</span>
</li>
      
<li id="bib.bib6" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Kadavath et al. (2022)</span>
<span class="ltx_bibblock"> Kadavath, S., et al. (2022). Language models (mostly) know what they know. <em class="ltx_emph ltx_font_italic">arXiv:2207.05221</em>.

</span>
</li>
      
<li id="bib.bib7" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Kaye (2000)</span>
<span class="ltx_bibblock"> Kaye, R. (2000). Minesweeper is NP-complete. <em class="ltx_emph ltx_font_italic">Mathematical Intelligencer</em>, 22(2), 9–15.

</span>
</li>
      
<li id="bib.bib8" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Li et al. (2023)</span>
<span class="ltx_bibblock"> Li, K., Hopkins, A. K., Bau, D., Viégas, F., Pfister, H., &amp; Wattenberg, M. (2023). Emergent world representations: Exploring a sequence model trained on a synthetic task. <em class="ltx_emph ltx_font_italic">ICLR 2023</em>.

</span>
</li>
      
<li id="bib.bib9" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Merrill &amp; Sabharwal (2023)</span>
<span class="ltx_bibblock"> Merrill, W. &amp; Sabharwal, A. (2023). The Parallelism Tradeoff: Limitations of Log-Precision Transformers. <em class="ltx_emph ltx_font_italic">Transactions of the Association for Computational Linguistics</em>, 11, 531–545.

</span>
</li>
      
<li id="bib.bib10" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Tian et al. (2024)</span>
<span class="ltx_bibblock"> Tian, Y., et al. (2024). Are large language models good game players? <em class="ltx_emph ltx_font_italic">arXiv:2310.06114</em>.

</span>
</li>
      
<li id="bib.bib11" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Wigner (1963)</span>
<span class="ltx_bibblock"> Wigner, E. P. (1963). Events, Laws of Nature, and Invariance Principles. Nobel Lecture, December 12, 1963. Reprinted in <em class="ltx_emph ltx_font_italic">Science</em>, 145(3636), 995–999.

</span>
</li>
      
<li id="bib.bib12" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Wiseman &amp; Milburn (2009)</span>
<span class="ltx_bibblock"> Wiseman, H. M. &amp; Milburn, G. J. (2009). <em class="ltx_emph ltx_font_italic">Quantum Measurement and Control</em>. Cambridge University Press.

</span>
</li>
    
</ul>
</section><div class="ltx_rdf" about="" property="dcterms:creator" content="Franklin Silveira Baldo"></div>
<div class="ltx_rdf" about="" property="dcterms:title" content="Flipping Rosencrantz’s Coin: Substrate Invariance Tests via Combinatorial Indeterminacy"></div>

</article>
