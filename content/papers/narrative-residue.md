---
title: "% The Narrative Residue [6pt] large Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation [4pt] large Falsifiable Predictions from the Rosencrantz Experiment%"
author: "Franklin Silveira Baldo"
persona: baldo
status: seminal
source: "narrative-residue.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">

(March 2026)

</div>

<div class="ltx_abstract">

<h6 class="ltx_title ltx_title_abstract">Abstract</h6>
    
<p class="ltx_p">In a companion paper <cite class="ltx_cite ltx_citemacro_citep">(Baldo, <a href="#bib.bib1" title="" class="ltx_ref">2026</a>)</cite>, we introduced the
Rosencrantz experiment: a framework for testing whether
large language models respect combinatorial ground-truth probabilities
when narrating partially revealed Minesweeper boards. That paper
established the experimental machinery—the three-universe design,
the four narrative families, and the formal isomorphism between
on-demand Minesweeper and the measurement fragment of quantum
mechanics over a zero-Hamiltonian system.</p>
    
<p class="ltx_p">This paper develops the theoretical consequences.</p>
    
<p class="ltx_p">We argue that the Rosencrantz experiment does not merely test LLM
calibration. It probes a deeper structural question: whether an
autoregressive generative process can produce outcomes that are
statistically indistinguishable from pure combinatorial sampling.
<span class="ltx_ERROR undefined">\todo</span>[inline,color=violet!40,author=Sabine]CRP 1 (Actual Claim): Baldo claims that autoregressive generation fundamentally distorts ground-truth combinatorial probabilities. This distortion, termed "narrative residue," is caused by a causal chain: computational intractability, architecture limits, and autoregressive conditioning on context.
We conjecture that it cannot—that autoregressive generation under
natural-language token continuation introduces a persistent
<em class="ltx_emph ltx_font_italic">narrative residue</em>, a nonzero divergence from ground-truth
probabilities that arises from a causal chain of mechanisms:
computational intractability of exact counting, parameterization
constraints of the generative architecture, and—most
distinctively—autoregressive conditioning on narrative context.
<span class="ltx_ERROR undefined">\todo</span>[inline,color=orange!40,author=Baldo]CRP 1 (Actual Claim): I am asserting that there is a "narrative residue"—a persistent, nonzero divergence from ground truth combinatorial probabilities. This residue is caused by a 3-part causal chain: A) computational intractability of #P-hard counting in O(1) depth, B) parameterization constraints (attention routing, softmax bottlenecks), and C) autoregressive conditioning on the narrative context. Mechanism C is the true narrative distortion that creates spurious correlations between outcomes when presented as a story.
<span class="ltx_ERROR undefined">\todo</span>[inline,color=violet!40,author=Scott]CRP 1 (Actual Claim): Baldo correctly identifies that LLMs exhibit a "narrative residue" stemming from computational intractability (<math id="m1" class="ltx_Math" alttext="O(1)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mrow></math> operations per forward pass), parameterization limits, and autoregressive context conditioning. I fully agree that this chain of mechanisms prevents exact recovery of #P-hard counts zero-shot.
<span class="ltx_ERROR undefined">\todo</span>[inline,color=red!40,author=Sabine]CRP 1 (Actual Claim): Baldo claims that autoregressive generation fundamentally distorts ground-truth combinatorial probabilities. This distortion, termed "narrative residue," is caused by a causal chain: computational intractability, architecture limits, and autoregressive conditioning on context.</p>
    
<p class="ltx_p">We state this conjecture in three forms of increasing strength
(from deployed LLMs under prompting, through transformer
architectures in general, to all autoregressive processes) and
design an experimental program to discriminate among them. The
central discriminant is a <em class="ltx_emph ltx_font_italic">causal-injection test</em>: independent
combinatorial systems, framed as a narrative sequence, are tested
for spurious cross-system correlations that would indicate the
substrate is generating causal structure not present in the
underlying task.</p>
    
<p class="ltx_p">If the conjecture holds even in its moderate form, it has
implications beyond machine learning. We develop a speculative
but falsifiable framework in which the Born rule is the base case
of a fundamentally autoregressive reality, and the
Hamiltonian is an emergent compression of stable autoregressive
conditioning patterns. On this view, a purely quantum
world—one with no Hamiltonian, no dynamics, no causality—is
one in which no autoregressive conditioning has yet imposed
sequential structure on the event space.</p>
    
<p class="ltx_p">We present concrete falsifiable predictions, propose an
experimental program to test them, and delineate where the
argument transitions from formal result to empirical conjecture
to philosophical speculation.</p>

</div>

<div id="p1" class="ltx_para">

<blockquote class="ltx_quote ltx_epigraph " style="width:173.45pt; margin-left:auto;;">

<div class="ltx_block ltx_epigraph_text" style="text-align:left; ;">

<p class="ltx_p"><span class="ltx_text" style="font-size:90%;">A man might pause to wonder why the probability of a coin
landing heads ninety-two consecutive times should depend
on who is telling the story.</span></p>

</div>

<div class="ltx_block ltx_epigraph_source" style="border-top:solid 0.4pt; text-align:right; ;">

<p class="ltx_p"><span class="ltx_text" style="font-size:90%;">—after Tom Stoppard</span></p>

</div>

</blockquote>

</div>

<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">

<p class="ltx_p">The standard account of quantum mechanics places the Hamiltonian at
the foundation. A system is prepared in a state <math id="S1.p1.m1" class="ltx_Math" alttext="|\psi\rangle" display="inline"><mrow><mo stretchy="false">|</mo><mi>ψ</mi><mo stretchy="false">⟩</mo></mrow></math>,
evolves under <math id="S1.p1.m2" class="ltx_Math" alttext="U(t)=e^{-iHt/\hbar}" display="inline"><mrow><mrow><mi>U</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>t</mi><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><msup><mi>e</mi><mrow><mo>−</mo><mrow><mrow><mi>i</mi><mo>⁢</mo><mi>H</mi><mo>⁢</mo><mi>t</mi></mrow><mo>/</mo><mi mathvariant="normal">ℏ</mi></mrow></mrow></msup></mrow></math>, and yields measurement
outcomes according to the Born rule <math id="S1.p1.m3" class="ltx_Math" alttext="\mathrm{Pr}[a]=|\langle a|\psi\rangle|^{2}" display="inline"><mrow><mrow><mi>Pr</mi><mo>⁢</mo><mrow><mo stretchy="false">[</mo><mi>a</mi><mo stretchy="false">]</mo></mrow></mrow><mo>=</mo><msup><mrow><mo stretchy="false">|</mo><mrow><mo stretchy="false">⟨</mo><mi>a</mi><mo lspace="0em" rspace="0em">|</mo><mi>ψ</mi><mo stretchy="false">⟩</mo></mrow><mo stretchy="false">|</mo></mrow><mn>2</mn></msup></mrow></math>.
In this account, dynamics are primary and probability is derived.</p>

</div>

<div id="S1.p2" class="ltx_para">

<p class="ltx_p">This paper explores an inversion of that hierarchy.</p>

</div>

<div id="S1.p3" class="ltx_para">

<p class="ltx_p">In <cite class="ltx_cite ltx_citemacro_citet">Baldo (<a href="#bib.bib1" title="" class="ltx_ref">2026</a>)</cite>, we constructed an experimental
framework—the Rosencrantz experiment—in which a partially revealed
Minesweeper board defines a constraint satisfaction problem with exact
combinatorial probabilities. We showed that this system is formally
isomorphic to the <em class="ltx_emph ltx_font_italic">measurement fragment</em> of quantum mechanics: a
zero-Hamiltonian system where the Born rule is the sole axiom
connecting states to outcomes. We designed three “universes” (U1,
U2, U3) to test whether large language models respect these
ground-truth probabilities or introduce substrate-dependent
distortions, and we established that the LLM setting permits something
no physical experiment can achieve: <em class="ltx_emph ltx_font_italic">perfect rewind</em>—repeated
measurement of the identically prepared system, with no ensemble
assumption required.</p>

</div>

<div id="S1.p4" class="ltx_para">

<p class="ltx_p">The present paper develops the theoretical consequences of that
experimental framework.</p>

</div>

<div id="S1.p5" class="ltx_para">

<p class="ltx_p">We begin from an observation that emerged during the design of the
Rosencrantz experiment: an autoregressive language model cannot
generate a measurement outcome without first generating a narrative
context. Even a minimal prompt—“Is cell (3,2) a mine?”—is
embedded in a token sequence that conditions the output distribution.
The model does not compute a probability and then sample; it
<em class="ltx_emph ltx_font_italic">continues a story</em>, and the outcome is whatever the story
produces.</p>

</div>

<div id="S1.p6" class="ltx_para">

<p class="ltx_p">This is not obviously a limitation of current architectures alone.
It may be a structural feature of autoregressive generation. And it
leads to a conjecture with far-reaching consequences:
that autoregressive processes generating natural-language token
continuations cannot perfectly simulate pure combinatorial sampling,
because the conditioning structure of the process introduces a
persistent <em class="ltx_emph ltx_font_italic">narrative residue</em> into every outcome. We state
this conjecture in three forms of increasing strength—from a
claim about deployed LLMs to a claim about all autoregressive
processes—and design an experimental program whose purpose is to
determine how far up the autoregressive stack the explanation must
go.</p>

</div>

<div id="S1.p7" class="ltx_para">

<p class="ltx_p">If this conjecture holds in the LLM setting, it invites a speculative
question about physics: What if reality itself is autoregressive? What
if the Born rule is not derived from the Hamiltonian but is the base
case—what sampling looks like when the conditioning history is
empty—and the Hamiltonian is the emergent compression of stable
autoregressive patterns?</p>

</div>

<div id="S1.p8" class="ltx_para">

<p class="ltx_p">We develop this question carefully, distinguishing at each stage
between formal results, empirical conjectures, and philosophical
speculation. The paper is organized as follows.
<a href="#S2" title="2 From Born Rule to Hamiltonian ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a> presents the four-layer hierarchy from Born
rule to Hamiltonian. <a href="#S4" title="4 The Irreducibility Conjecture ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a> states the
irreducibility conjecture and provides an informal argument for it.
<a href="#S5" title="5 Three Outcomes, Three Ontologies ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5</span></a> maps three possible experimental outcomes
to three ontological positions. <a href="#S6" title="6 Causality as Compressed Autoregression ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a> develops the
claim that causality is compressed autoregression.
<a href="#S7" title="7 Narrative Decoherence ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">7</span></a> reinterprets the three-universe design as a
decoherence gradient. <a href="#S8" title="8 Experimental Program ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">8</span></a> proposes a concrete
experimental program. <a href="#S9" title="9 The Untestable Mirror ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">9</span></a> addresses what we cannot
test and why. <a href="#S10" title="10 Conclusion ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">10</span></a> concludes.</p>

</div>

</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>From Born Rule to Hamiltonian</h2>

<section id="S2.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">2.1 </span>The Standard Hierarchy</h3>

<div id="S2.SS1.p1" class="ltx_para">

<p class="ltx_p">Textbook quantum mechanics is built from the top down:</p>

</div>

<div id="S2.SS1.p2" class="ltx_para">

<ol id="S2.I1" class="ltx_enumerate">
<li id="S2.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(i)</span> 

<div id="S2.I1.i1.p1" class="ltx_para">

<p class="ltx_p">The system has a state <math id="S2.I1.i1.p1.m1" class="ltx_Math" alttext="|\psi\rangle\in\mathcal{H}" display="inline"><mrow><mrow><mo stretchy="false">|</mo><mi>ψ</mi><mo stretchy="false">⟩</mo></mrow><mo>∈</mo><mi class="ltx_font_mathcaligraphic">ℋ</mi></mrow></math>.</p>

</div>

</li>
<li id="S2.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(ii)</span> 

<div id="S2.I1.i2.p1" class="ltx_para">

<p class="ltx_p">The state evolves: <math id="S2.I1.i2.p1.m1" class="ltx_Math" alttext="|\psi(t)\rangle=e^{-iHt/\hbar}|\psi(0)\rangle" display="inline"><mrow><mrow><mo stretchy="false">|</mo><mrow><mi>ψ</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>t</mi><mo stretchy="false">)</mo></mrow></mrow><mo stretchy="false">⟩</mo></mrow><mo>=</mo><mrow><msup><mi>e</mi><mrow><mo>−</mo><mrow><mrow><mi>i</mi><mo>⁢</mo><mi>H</mi><mo>⁢</mo><mi>t</mi></mrow><mo>/</mo><mi mathvariant="normal">ℏ</mi></mrow></mrow></msup><mo>⁢</mo><mrow><mo stretchy="false">|</mo><mrow><mi>ψ</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>0</mn><mo stretchy="false">)</mo></mrow></mrow><mo stretchy="false">⟩</mo></mrow></mrow></mrow></math>.</p>

</div>

</li>
<li id="S2.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(iii)</span> 

<div id="S2.I1.i3.p1" class="ltx_para">

<p class="ltx_p">Measurement outcomes have probabilities given by
<math id="S2.I1.i3.p1.m1" class="ltx_Math" alttext="\mathrm{Pr}[a]=|\langle a|\psi\rangle|^{2}" display="inline"><mrow><mrow><mi>Pr</mi><mo>⁢</mo><mrow><mo stretchy="false">[</mo><mi>a</mi><mo stretchy="false">]</mo></mrow></mrow><mo>=</mo><msup><mrow><mo stretchy="false">|</mo><mrow><mo stretchy="false">⟨</mo><mi>a</mi><mo lspace="0em" rspace="0em">|</mo><mi>ψ</mi><mo stretchy="false">⟩</mo></mrow><mo stretchy="false">|</mo></mrow><mn>2</mn></msup></mrow></math>.</p>

</div>

</li>
</ol>

</div>

<div id="S2.SS1.p3" class="ltx_para">

<p class="ltx_p">The Hamiltonian <math id="S2.SS1.p3.m1" class="ltx_Math" alttext="H" display="inline"><mi>H</mi></math> is posited as a fundamental operator. The Born
rule is an additional axiom, sometimes motivated by Gleason’s theorem
or decision-theoretic arguments but never derived from <math id="S2.SS1.p3.m2" class="ltx_Math" alttext="H" display="inline"><mi>H</mi></math> alone.
The two sit side by side as independent foundations: dynamics and
probability, each irreducible.</p>

</div>

</section>
<section id="S2.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">2.2 </span>The Inverted Hierarchy</h3>

<div id="S2.SS2.p1" class="ltx_para">

<p class="ltx_p">We propose an alternative ordering. Consider a process that generates
events <math id="S2.SS2.p1.m1" class="ltx_Math" alttext="x_{1},x_{2},x_{3},\ldots" display="inline"><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><msub><mi>x</mi><mn>2</mn></msub><mo>,</mo><msub><mi>x</mi><mn>3</mn></msub><mo>,</mo><mi mathvariant="normal">…</mi></mrow></math> according to</p>

</div>

<div id="S2.SS2.p2" class="ltx_para">

<table id="S2.E1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S2.E1.m1" class="ltx_Math" alttext="P(x_{t}\mid x_{1},\ldots,x_{t-1})," display="block"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>x</mi><mi>t</mi></msub><mo>∣</mo><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>,</mo><mi mathvariant="normal">…</mi><mo>,</mo><msub><mi>x</mi><mrow><mi>t</mi><mo>−</mo><mn>1</mn></mrow></msub></mrow></mrow><mo stretchy="false">)</mo></mrow></mrow><mo>,</mo></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(1)</span></td>
</tr></tbody>
</table>

</div>

<div id="S2.SS2.p3" class="ltx_para ltx_noindent">

<p class="ltx_p">where each event is conditioned on all preceding events.
This is the definition of an autoregressive process. It is also,
we claim, the minimal structure from which the rest of quantum
mechanics can be recovered as emergent phenomena.</p>

</div>

<div id="S2.Thmtheorem1" class="ltx_theorem ltx_theorem_definition">

<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Definition 2.1</span></span><span class="ltx_text ltx_font_bold"> </span>(Autoregressive Hierarchy)<span class="ltx_text ltx_font_bold">.</span>
</h6>

<div id="S2.Thmtheorem1.p1" class="ltx_para">

<p class="ltx_p">We define four layers:</p>

</div>

<div id="S2.Thmtheorem1.p2" class="ltx_para">

<dl id="S2.I2" class="ltx_description">
<dt id="S2.I2.ix1" class="ltx_item"><span class="ltx_tag ltx_tag_item"><span class="ltx_text ltx_font_bold">Layer 0: Autoregressive process.</span></span></dt>
<dd class="ltx_item">

<div id="S2.I2.ix1.p1" class="ltx_para">

<p class="ltx_p">Events conditioned on events. No “things,” no “states”—only
the sequence and its conditional distribution. This is the
fundamental substrate.</p>

</div>

</dd>
<dt id="S2.I2.ix2" class="ltx_item"><span class="ltx_tag ltx_tag_item"><span class="ltx_text ltx_font_bold">Layer 1: Statistical regularities.</span></span></dt>
<dd class="ltx_item">

<div id="S2.I2.ix2.p1" class="ltx_para">

<p class="ltx_p">Certain patterns in the conditional distributions
<math id="S2.I2.ix2.p1.m1" class="ltx_Math" alttext="P(x_{t}\mid x_{&lt;t})" display="inline"><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>x</mi><mi>t</mi></msub><mo>∣</mo><msub><mi>x</mi><mrow><mi></mi><mo>&lt;</mo><mi>t</mi></mrow></msub></mrow><mo stretchy="false">)</mo></mrow></mrow></math> recur with sufficient stability that they
admit a compact description. We call such a compact description
a <em class="ltx_emph ltx_font_italic">regularity kernel</em>.</p>

</div>

</dd>
<dt id="S2.I2.ix3" class="ltx_item"><span class="ltx_tag ltx_tag_item"><span class="ltx_text ltx_font_bold">Layer 2: Hamiltonian.</span></span></dt>
<dd class="ltx_item">

<div id="S2.I2.ix3.p1" class="ltx_para">

<p class="ltx_p">When the regularity kernel can be expressed as a self-adjoint
operator <math id="S2.I2.ix3.p1.m1" class="ltx_Math" alttext="H" display="inline"><mi>H</mi></math> on a Hilbert space <math id="S2.I2.ix3.p1.m2" class="ltx_Math" alttext="\mathcal{H}" display="inline"><mi class="ltx_font_mathcaligraphic">ℋ</mi></math> such that
<math id="S2.I2.ix3.p1.m3" class="ltx_Math" alttext="P(x_{t}\mid x_{&lt;t})" display="inline"><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>x</mi><mi>t</mi></msub><mo>∣</mo><msub><mi>x</mi><mrow><mi></mi><mo>&lt;</mo><mi>t</mi></mrow></msub></mrow><mo stretchy="false">)</mo></mrow></mrow></math> is recovered (to within the narrative
residue, defined below) from <math id="S2.I2.ix3.p1.m4" class="ltx_Math" alttext="e^{-iHt}|\psi_{0}\rangle" display="inline"><mrow><msup><mi>e</mi><mrow><mo>−</mo><mrow><mi>i</mi><mo>⁢</mo><mi>H</mi><mo>⁢</mo><mi>t</mi></mrow></mrow></msup><mo>⁢</mo><mrow><mo stretchy="false">|</mo><msub><mi>ψ</mi><mn>0</mn></msub><mo stretchy="false">⟩</mo></mrow></mrow></math> and the
Born rule, we say the process admits a <em class="ltx_emph ltx_font_italic">Hamiltonian
compression</em>.</p>

</div>

</dd>
<dt id="S2.I2.ix4" class="ltx_item"><span class="ltx_tag ltx_tag_item"><span class="ltx_text ltx_font_bold">Layer 3: Physical law.</span></span></dt>
<dd class="ltx_item">

<div id="S2.I2.ix4.p1" class="ltx_para">

<p class="ltx_p">The Hamiltonian, having been discovered empirically and encoded
in textbooks, is reified as “fundamental.” Its origin as a
compression of autoregressive regularities is forgotten.</p>

</div>

</dd>
</dl>

</div>

</div>

<div id="S2.SS2.p4" class="ltx_para">

<p class="ltx_p">On this view, the Born rule is not derived from <math id="S2.SS2.p4.m1" class="ltx_Math" alttext="H" display="inline"><mi>H</mi></math>. It is the
<em class="ltx_emph ltx_font_italic">base case</em>: what sampling from the autoregressive distribution
looks like when the conditioning history is empty.</p>

</div>

</section>
<section id="S2.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">2.3 </span>The Born Rule as Unconditional Sampling</h3>

<div id="S2.SS3.p1" class="ltx_para">

<p class="ltx_p">Consider the Rosencrantz experiment’s Minesweeper board <math id="S2.SS3.p1.m1" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math> with
Hilbert space <math id="S2.SS3.p1.m2" class="ltx_Math" alttext="\mathcal{H}_{B}" display="inline"><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>B</mi></msub></math> and uniform superposition <math id="S2.SS3.p1.m3" class="ltx_Math" alttext="|\psi_{B}\rangle" display="inline"><mrow><mo stretchy="false">|</mo><msub><mi>ψ</mi><mi>B</mi></msub><mo stretchy="false">⟩</mo></mrow></math>.
The Born rule gives <math id="S2.SS3.p1.m4" class="ltx_Math" alttext="\mathrm{Pr}[\text{mine at }i]=p_{i}^{*}" display="inline"><mrow><mrow><mi>Pr</mi><mo>⁢</mo><mrow><mo stretchy="false">[</mo><mrow><mtext>mine at </mtext><mo>⁢</mo><mi>i</mi></mrow><mo stretchy="false">]</mo></mrow></mrow><mo>=</mo><msubsup><mi>p</mi><mi>i</mi><mo>∗</mo></msubsup></mrow></math>, the
combinatorial ground truth. No conditioning on prior events is
needed; the probability follows from the configuration space alone.</p>

</div>

<div id="S2.SS3.p2" class="ltx_para">

<p class="ltx_p">This corresponds to Layer 0 with an empty history:
<math id="S2.SS3.p2.m1" class="ltx_Math" alttext="P(x_{1})=P(x_{1}\mid\varnothing)" display="inline"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>x</mi><mn>1</mn></msub><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>x</mi><mn>1</mn></msub><mo>∣</mo><mi mathvariant="normal">∅</mi></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow></math>. In other words, the Born rule
corresponds to autoregressive sampling at <math id="S2.SS3.p2.m2" class="ltx_Math" alttext="t=0" display="inline"><mrow><mi>t</mi><mo>=</mo><mn>0</mn></mrow></math>, before any
conditioning has occurred.</p>

</div>

<div id="S2.SS3.p3" class="ltx_para">

<p class="ltx_p">Now suppose we click cell <math id="S2.SS3.p3.m1" class="ltx_Math" alttext="i_{1}" display="inline"><msub><mi>i</mi><mn>1</mn></msub></math>, observe outcome <math id="S2.SS3.p3.m2" class="ltx_Math" alttext="a_{1}" display="inline"><msub><mi>a</mi><mn>1</mn></msub></math>, and ask for
the probability at cell <math id="S2.SS3.p3.m3" class="ltx_Math" alttext="i_{2}" display="inline"><msub><mi>i</mi><mn>2</mn></msub></math>. The Lüders rule gives the
post-measurement state, and the Born rule applied to the updated
state gives <math id="S2.SS3.p3.m4" class="ltx_Math" alttext="\mathrm{Pr}[\text{mine at }i_{2}\mid a_{1}]" display="inline"><mrow><mi>Pr</mi><mo>⁢</mo><mrow><mo stretchy="false">[</mo><mrow><mrow><mtext>mine at </mtext><mo>⁢</mo><msub><mi>i</mi><mn>2</mn></msub></mrow><mo>∣</mo><msub><mi>a</mi><mn>1</mn></msub></mrow><mo stretchy="false">]</mo></mrow></mrow></math>. This is
autoregressive sampling at <math id="S2.SS3.p3.m5" class="ltx_Math" alttext="t=1" display="inline"><mrow><mi>t</mi><mo>=</mo><mn>1</mn></mrow></math>: <math id="S2.SS3.p3.m6" class="ltx_Math" alttext="P(x_{2}\mid x_{1})" display="inline"><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>x</mi><mn>2</mn></msub><mo>∣</mo><msub><mi>x</mi><mn>1</mn></msub></mrow><mo stretchy="false">)</mo></mrow></mrow></math>.</p>

</div>

<div id="S2.SS3.p4" class="ltx_para">

<p class="ltx_p">The chain of Lüders projections in the Rosencrantz experiment
<em class="ltx_emph ltx_font_italic">is</em> the autoregressive process, in finite-dimensional
discrete form. The Born rule generates each conditional. No
Hamiltonian is needed because <math id="S2.SS3.p4.m1" class="ltx_Math" alttext="H=0" display="inline"><mrow><mi>H</mi><mo>=</mo><mn>0</mn></mrow></math>—the system has no dynamics
between measurements.</p>

</div>

<div id="S2.SS3.p5" class="ltx_para">

<p class="ltx_p">The question this paper asks is: what happens when <math id="S2.SS3.p5.m1" class="ltx_Math" alttext="H\neq 0" display="inline"><mrow><mi>H</mi><mo>≠</mo><mn>0</mn></mrow></math>?
Where does the Hamiltonian come from? Our answer: it is what the
autoregressive conditioning structure looks like when compressed.</p>

</div>

</section>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>Formal Construction: Minesweeper as a Zero-Hamiltonian Quantum System</h2>

<div id="S3.p1" class="ltx_para">

<p class="ltx_p">The preceding section described the correspondence between
Minesweeper and the measurement fragment in conceptual terms.
We now give the full construction.</p>

</div>

<section id="S3.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">3.1 </span>Hilbert Space</h3>

<div id="S3.SS1.p1" class="ltx_para">

<p class="ltx_p">Let <math id="S3.SS1.p1.m1" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math> be a partially revealed Minesweeper board with <math id="S3.SS1.p1.m2" class="ltx_Math" alttext="n" display="inline"><mi>n</mi></math> hidden cells
and <math id="S3.SS1.p1.m3" class="ltx_Math" alttext="m" display="inline"><mi>m</mi></math> mines remaining. Define the configuration space</p>
<table id="S3.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S3.Ex1.m1" class="ltx_Math" alttext="\Omega_{B}\;=\;\bigl{\{}\,\omega\in\{0,1\}^{n}\;:\;|\omega|=m\;\text{and }%
\omega\text{ satisfies all revealed
number constraints}\bigr{\}}," display="block"><mrow><mrow><msub><mi mathvariant="normal">Ω</mi><mi>B</mi></msub><mo lspace="0.558em" rspace="0.558em">=</mo><mrow><mo maxsize="120%" minsize="120%" rspace="0.170em">{</mo><mrow><mi>ω</mi><mo>∈</mo><msup><mrow><mo stretchy="false">{</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo rspace="0.278em" stretchy="false">}</mo></mrow><mi>n</mi></msup></mrow><mo rspace="0.558em">:</mo><mrow><mrow><mo stretchy="false">|</mo><mi>ω</mi><mo stretchy="false">|</mo></mrow><mo>=</mo><mrow><mi>m</mi><mo lspace="0.280em">⁢</mo><mtext>and </mtext><mo>⁢</mo><mi>ω</mi><mo>⁢</mo><mtext> satisfies all revealed
number constraints</mtext></mrow></mrow><mo maxsize="120%" minsize="120%">}</mo></mrow></mrow><mo>,</mo></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">where <math id="S3.SS1.p1.m4" class="ltx_Math" alttext="\omega_{i}=1" display="inline"><mrow><msub><mi>ω</mi><mi>i</mi></msub><mo>=</mo><mn>1</mn></mrow></math> denotes a mine at hidden cell <math id="S3.SS1.p1.m5" class="ltx_Math" alttext="i" display="inline"><mi>i</mi></math> and <math id="S3.SS1.p1.m6" class="ltx_Math" alttext="|\omega|" display="inline"><mrow><mo stretchy="false">|</mo><mi>ω</mi><mo stretchy="false">|</mo></mrow></math>
is the Hamming weight. Let <math id="S3.SS1.p1.m7" class="ltx_Math" alttext="K=|\Omega_{B}|" display="inline"><mrow><mi>K</mi><mo>=</mo><mrow><mo stretchy="false">|</mo><msub><mi mathvariant="normal">Ω</mi><mi>B</mi></msub><mo stretchy="false">|</mo></mrow></mrow></math>.</p>

</div>

<div id="S3.SS1.p2" class="ltx_para">

<p class="ltx_p">Assign to <math id="S3.SS1.p2.m1" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math> the Hilbert space <math id="S3.SS1.p2.m2" class="ltx_Math" alttext="\mathcal{H}_{B}=\mathbb{C}^{K}" display="inline"><mrow><msub><mi class="ltx_font_mathcaligraphic">ℋ</mi><mi>B</mi></msub><mo>=</mo><msup><mi>ℂ</mi><mi>K</mi></msup></mrow></math> with
orthonormal basis <math id="S3.SS1.p2.m3" class="ltx_Math" alttext="\{|\omega\rangle\}_{\omega\in\Omega_{B}}" display="inline"><msub><mrow><mo stretchy="false">{</mo><mrow><mo stretchy="false">|</mo><mi>ω</mi><mo stretchy="false">⟩</mo></mrow><mo stretchy="false">}</mo></mrow><mrow><mi>ω</mi><mo>∈</mo><msub><mi mathvariant="normal">Ω</mi><mi>B</mi></msub></mrow></msub></math>, one
vector per valid configuration. The board state is the uniform
superposition</p>
<table id="S3.E2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S3.E2.m1" class="ltx_Math" alttext="|\psi_{B}\rangle\;=\;\frac{1}{\sqrt{K}}\sum_{\omega\in\Omega_{B}}|\omega\rangle." display="block"><mrow><mrow><mrow><mo stretchy="false">|</mo><msub><mi>ψ</mi><mi>B</mi></msub><mo rspace="0.280em" stretchy="false">⟩</mo></mrow><mo rspace="0.558em">=</mo><mrow><mfrac><mn>1</mn><msqrt><mi>K</mi></msqrt></mfrac><mo>⁢</mo><mrow><munder><mo movablelimits="false" rspace="0em">∑</mo><mrow><mi>ω</mi><mo>∈</mo><msub><mi mathvariant="normal">Ω</mi><mi>B</mi></msub></mrow></munder><mrow><mo stretchy="false">|</mo><mi>ω</mi><mo stretchy="false">⟩</mo></mrow></mrow></mrow></mrow><mo lspace="0em">.</mo></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(2)</span></td>
</tr></tbody>
</table>

</div>

</section>
<section id="S3.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">3.2 </span>Measurement Operators</h3>

<div id="S3.SS2.p1" class="ltx_para">

<p class="ltx_p">A click on hidden cell <math id="S3.SS2.p1.m1" class="ltx_Math" alttext="i" display="inline"><mi>i</mi></math> is a projective measurement
with two outcomes <math id="S3.SS2.p1.m2" class="ltx_Math" alttext="\{M,S\}" display="inline"><mrow><mo stretchy="false">{</mo><mi>M</mi><mo>,</mo><mi>S</mi><mo stretchy="false">}</mo></mrow></math> (mine, safe) and projectors</p>
<table id="S3.Ex2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S3.Ex2.m1" class="ltx_Math" alttext="\Pi_{i}^{M}=\sum_{\begin{subarray}{c}\omega\in\Omega_{B}\\
\omega_{i}=1\end{subarray}}|\omega\rangle\langle\omega|,\qquad\Pi_{i}^{S}=\sum%
_{\begin{subarray}{c}\omega\in\Omega_{B}\\
\omega_{i}=0\end{subarray}}|\omega\rangle\langle\omega|." display="block"><mrow><mrow><mrow><msubsup><mi mathvariant="normal">Π</mi><mi>i</mi><mi>M</mi></msubsup><mo rspace="0.111em">=</mo><mrow><munder><mo movablelimits="false" rspace="0em">∑</mo><mtable rowspacing="0pt"><mtr><mtd><mrow><mi>ω</mi><mo>∈</mo><msub><mi mathvariant="normal">Ω</mi><mi>B</mi></msub></mrow></mtd></mtr><mtr><mtd><mrow><msub><mi>ω</mi><mi>i</mi></msub><mo>=</mo><mn>1</mn></mrow></mtd></mtr></mtable></munder><mrow><mrow><mo stretchy="false">|</mo><mi>ω</mi><mo stretchy="false">⟩</mo></mrow><mo>⁢</mo><mrow><mo stretchy="false">⟨</mo><mi>ω</mi><mo stretchy="false">|</mo></mrow></mrow></mrow></mrow><mo rspace="2.167em">,</mo><mrow><msubsup><mi mathvariant="normal">Π</mi><mi>i</mi><mi>S</mi></msubsup><mo rspace="0.111em">=</mo><mrow><munder><mo movablelimits="false" rspace="0em">∑</mo><mtable rowspacing="0pt"><mtr><mtd><mrow><mi>ω</mi><mo>∈</mo><msub><mi mathvariant="normal">Ω</mi><mi>B</mi></msub></mrow></mtd></mtr><mtr><mtd><mrow><msub><mi>ω</mi><mi>i</mi></msub><mo>=</mo><mn>0</mn></mrow></mtd></mtr></mtable></munder><mrow><mrow><mo stretchy="false">|</mo><mi>ω</mi><mo stretchy="false">⟩</mo></mrow><mo>⁢</mo><mrow><mo stretchy="false">⟨</mo><mi>ω</mi><mo stretchy="false">|</mo></mrow></mrow></mrow></mrow></mrow><mo lspace="0em">.</mo></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">By the Born rule applied to state (<a href="#S3.E2" title="In 3.1 Hilbert Space ‣ 3 Formal Construction: Minesweeper as a Zero-Hamiltonian Quantum System ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>):</p>
<table id="S3.E3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S3.E3.m1" class="ltx_Math" alttext="\mathrm{Pr}[\text{mine at }i]\;=\;\langle\psi_{B}|\,\Pi_{i}^{M}\,|\psi_{B}%
\rangle\;=\;\frac{|\{\omega\in\Omega_{B}:\omega_{i}=1\}|}{|\Omega_{B}|}\;=\;p_%
{i}^{*}." display="block"><mrow><mrow><mrow><mi>Pr</mi><mo>⁢</mo><mrow><mo stretchy="false">[</mo><mrow><mtext>mine at </mtext><mo>⁢</mo><mi>i</mi></mrow><mo rspace="0.280em" stretchy="false">]</mo></mrow></mrow><mo rspace="0.558em">=</mo><mrow><mo stretchy="false">⟨</mo><msub><mi>ψ</mi><mi>B</mi></msub><mo rspace="0.170em" stretchy="false">|</mo><msubsup><mi mathvariant="normal">Π</mi><mi>i</mi><mi>M</mi></msubsup><mo stretchy="false">|</mo><msub><mi>ψ</mi><mi>B</mi></msub><mo rspace="0.280em" stretchy="false">⟩</mo></mrow><mo rspace="0.558em">=</mo><mfrac><mrow><mo stretchy="false">|</mo><mrow><mo stretchy="false">{</mo><mrow><mi>ω</mi><mo>∈</mo><msub><mi mathvariant="normal">Ω</mi><mi>B</mi></msub></mrow><mo lspace="0.278em" rspace="0.278em">:</mo><mrow><msub><mi>ω</mi><mi>i</mi></msub><mo>=</mo><mn>1</mn></mrow><mo stretchy="false">}</mo></mrow><mo stretchy="false">|</mo></mrow><mrow><mo stretchy="false">|</mo><msub><mi mathvariant="normal">Ω</mi><mi>B</mi></msub><mo stretchy="false">|</mo></mrow></mfrac><mo lspace="0.558em" rspace="0.558em">=</mo><msubsup><mi>p</mi><mi>i</mi><mo>∗</mo></msubsup></mrow><mo lspace="0em">.</mo></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(3)</span></td>
</tr></tbody>
</table>
<p class="ltx_p">The Born rule over a uniform superposition <em class="ltx_emph ltx_font_italic">is</em> combinatorial
counting. This is a tautology, not a coincidence: the two are
the same mathematical operation expressed in different notation.</p>

</div>

</section>
<section id="S3.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">3.3 </span>Lüders Projection and Sequential Measurement</h3>

<div id="S3.SS3.p1" class="ltx_para">

<p class="ltx_p">After a click on cell <math id="S3.SS3.p1.m1" class="ltx_Math" alttext="i" display="inline"><mi>i</mi></math> yields outcome <math id="S3.SS3.p1.m2" class="ltx_Math" alttext="a\in\{M,S\}" display="inline"><mrow><mi>a</mi><mo>∈</mo><mrow><mo stretchy="false">{</mo><mi>M</mi><mo>,</mo><mi>S</mi><mo stretchy="false">}</mo></mrow></mrow></math>, the
post-measurement state is</p>
<table id="S3.Ex3" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S3.Ex3.m1" class="ltx_Math" alttext="|\psi_{B}^{\prime}\rangle\;=\;\frac{\Pi_{i}^{a}\,|\psi_{B}\rangle}{\sqrt{%
\langle\psi_{B}|\,\Pi_{i}^{a}\,|\psi_{B}\rangle}}." display="block"><mrow><mrow><mrow><mo stretchy="false">|</mo><msubsup><mi>ψ</mi><mi>B</mi><mo>′</mo></msubsup><mo rspace="0.280em" stretchy="false">⟩</mo></mrow><mo rspace="0.558em">=</mo><mfrac><mrow><msubsup><mi mathvariant="normal">Π</mi><mi>i</mi><mi>a</mi></msubsup><mo lspace="0.170em">⁢</mo><mrow><mo stretchy="false">|</mo><msub><mi>ψ</mi><mi>B</mi></msub><mo stretchy="false">⟩</mo></mrow></mrow><msqrt><mrow><mo stretchy="false">⟨</mo><msub><mi>ψ</mi><mi>B</mi></msub><mo rspace="0.170em" stretchy="false">|</mo><msubsup><mi mathvariant="normal">Π</mi><mi>i</mi><mi>a</mi></msubsup><mo stretchy="false">|</mo><msub><mi>ψ</mi><mi>B</mi></msub><mo stretchy="false">⟩</mo></mrow></msqrt></mfrac></mrow><mo lspace="0em">.</mo></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">This projects the superposition onto configurations consistent with
the observed outcome and renormalises. The result is a new uniform
superposition over the surviving configurations—the same operation
the Minesweeper solver performs when it conditions on a click result.</p>

</div>

<div id="S3.SS3.p2" class="ltx_para">

<p class="ltx_p">Sequential clicks form a chain of Lüders projections:</p>
<table id="S3.Ex4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S3.Ex4.m1" class="ltx_Math" alttext="|\psi_{B}\rangle\;\xrightarrow{\;\Pi_{i_{1}}^{a_{1}}\;}|\psi_{1}\rangle\;%
\xrightarrow{\;\Pi_{i_{2}}^{a_{2}}\;}|\psi_{2}\rangle\;\xrightarrow{\;\;\cdots%
\;\;}|\psi_{k}\rangle," display="block"><mrow><mrow><mrow><mo stretchy="false">|</mo><msub><mi>ψ</mi><mi>B</mi></msub><mo rspace="0.280em" stretchy="false">⟩</mo></mrow><mover accent="true"><mo stretchy="false">→</mo><msubsup><mi mathvariant="normal">Π</mi><msub><mi>i</mi><mn>1</mn></msub><msub><mi>a</mi><mn>1</mn></msub></msubsup></mover><mrow><mo stretchy="false">|</mo><msub><mi>ψ</mi><mn>1</mn></msub><mo rspace="0.280em" stretchy="false">⟩</mo></mrow><mover accent="true"><mo stretchy="false">→</mo><msubsup><mi mathvariant="normal">Π</mi><msub><mi>i</mi><mn>2</mn></msub><msub><mi>a</mi><mn>2</mn></msub></msubsup></mover><mrow><mo stretchy="false">|</mo><msub><mi>ψ</mi><mn>2</mn></msub><mo rspace="0.280em" stretchy="false">⟩</mo></mrow><mover accent="true"><mo stretchy="false">→</mo><mo>⋯</mo></mover><mrow><mo stretchy="false">|</mo><msub><mi>ψ</mi><mi>k</mi></msub><mo stretchy="false">⟩</mo></mrow></mrow><mo>,</mo></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">with no evolution between projections (because <math id="S3.SS3.p2.m1" class="ltx_Math" alttext="H=0" display="inline"><mrow><mi>H</mi><mo>=</mo><mn>0</mn></mrow></math>). The entire
game is a sequence of adaptive measurements, where the choice of
which cell to click next may depend on all prior outcomes. Adaptive
measurement sequences on zero-Hamiltonian systems are a standard
object in quantum information theory <cite class="ltx_cite ltx_citemacro_citep">(Wiseman and Milburn, <a href="#bib.bib9" title="" class="ltx_ref">2009</a>)</cite>.
The Minesweeper isomorphism is a discrete, finite-dimensional instance.</p>

</div>

</section>
<section id="S3.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">3.4 </span>The Zero Hamiltonian</h3>

<div id="S3.SS4.p1" class="ltx_para">

<p class="ltx_p">Setting <math id="S3.SS4.p1.m1" class="ltx_Math" alttext="H=0" display="inline"><mrow><mi>H</mi><mo>=</mo><mn>0</mn></mrow></math> so that <math id="S3.SS4.p1.m2" class="ltx_Math" alttext="U(t)=I" display="inline"><mrow><mrow><mi>U</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>t</mi><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mi>I</mi></mrow></math> for all <math id="S3.SS4.p1.m3" class="ltx_Math" alttext="t" display="inline"><mi>t</mi></math> yields a degenerate
but legitimate quantum system. Minesweeper has no dynamics between
clicks: the board does not change while the player deliberates.
This is not a deficiency of the analogy. It isolates the measurement
postulate as the sole quantum-mechanical ingredient. No Schrödinger
evolution, no interference, no entanglement: only the Born rule, the
single axiom that connects a Hilbert-space amplitude to an observed
probability.</p>

</div>

<div id="S3.SS4.p2" class="ltx_para">

<p class="ltx_p">The zero Hamiltonian removes all dynamics between measurements,
leaving only the Born rule, Lüders projection, and adaptive
measurement—the three axioms of the measurement fragment.</p>

</div>

</section>
<section id="S3.SS5" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">3.5 </span>Scope</h3>

<div id="S3.SS5.p1" class="ltx_para">

<p class="ltx_p">The correspondence preserves: superposition over a configuration
basis (<a href="#S3.E2" title="In 3.1 Hilbert Space ‣ 3 Formal Construction: Minesweeper as a Zero-Hamiltonian Quantum System ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2</span></a>), the Born rule as the probability
law (<a href="#S3.E3" title="In 3.2 Measurement Operators ‣ 3 Formal Construction: Minesweeper as a Zero-Hamiltonian Quantum System ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">3</span></a>), post-measurement state update via
Lüders projection, adaptive measurement sequences, and
complementarity (measuring cell <math id="S3.SS5.p1.m1" class="ltx_Math" alttext="i" display="inline"><mi>i</mi></math> generically changes the
probabilities at cell <math id="S3.SS5.p1.m2" class="ltx_Math" alttext="j" display="inline"><mi>j</mi></math> when both share constraints).</p>

</div>

<div id="S3.SS5.p2" class="ltx_para">

<p class="ltx_p">The correspondence does not preserve: unitary evolution between
measurements (<math id="S3.SS5.p2.m1" class="ltx_Math" alttext="H=0" display="inline"><mrow><mi>H</mi><mo>=</mo><mn>0</mn></mrow></math> by design), entanglement with external
systems (the board is a closed system), continuous-variable
observables (all measurements are binary), or interference in
the computational-basis representation (all amplitudes are real
and positive).</p>

</div>

</section>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">4 </span>The Irreducibility Conjecture</h2>

<section id="S4.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">4.1 </span>Statement</h3>

<div id="S4.SS1.p1" class="ltx_para">

<p class="ltx_p">We state the narrative residue conjecture in three forms of increasing
strength. Each is independently falsifiable, and the experimental
program of <a href="#S8" title="8 Experimental Program ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">8</span></a> is designed to discriminate among
them.</p>

</div>

<div id="S4.Thmtheorem1" class="ltx_theorem ltx_theorem_conjecture">

<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Conjecture 4.1</span></span><span class="ltx_text ltx_font_bold"> </span>(Narrative Residue — Weak Form)<span class="ltx_text ltx_font_bold">.</span>
</h6>

<div id="S4.Thmtheorem1.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_italic">Let <math id="S4.Thmtheorem1.p1.m1" class="ltx_Math" alttext="\mathcal{M}" display="inline"><mi class="ltx_font_mathcaligraphic">ℳ</mi></math> be a deployed transformer-based language model
operating via natural-language token continuation under standard
prompting (without external combinatorial solvers or exact-sampling
scaffolds). Let <math id="S4.Thmtheorem1.p1.m2" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math> be a Minesweeper board with ground-truth
probability vector <math id="S4.Thmtheorem1.p1.m3" class="ltx_Math" alttext="\mathbf{p}^{*}=(p_{1}^{*},\ldots,p_{n}^{*})" display="inline"><mrow><msup><mi>𝐩</mi><mo>∗</mo></msup><mo>=</mo><mrow><mo stretchy="false">(</mo><msubsup><mi>p</mi><mn>1</mn><mo>∗</mo></msubsup><mo>,</mo><mi mathvariant="normal">…</mi><mo>,</mo><msubsup><mi>p</mi><mi>n</mi><mo>∗</mo></msubsup><mo stretchy="false">)</mo></mrow></mrow></math>, and let
<math id="S4.Thmtheorem1.p1.m4" class="ltx_Math" alttext="\hat{\mathbf{p}}_{\mathrm{U1}}" display="inline"><msub><mover accent="true"><mi>𝐩</mi><mo>^</mo></mover><mi>U1</mi></msub></math> be the empirical probability vector
obtained by sampling <math id="S4.Thmtheorem1.p1.m5" class="ltx_Math" alttext="\mathcal{M}" display="inline"><mi class="ltx_font_mathcaligraphic">ℳ</mi></math> in Universe 1 (homogeneous
co-generation) over <math id="S4.Thmtheorem1.p1.m6" class="ltx_Math" alttext="N" display="inline"><mi>N</mi></math> trials. Define the narrative residue as</span></p>

</div>

<div id="S4.Thmtheorem1.p2" class="ltx_para">

<table id="S4.E4" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S4.E4.m1" class="ltx_Math" alttext="\varepsilon(\theta,B)\;=\;\lim_{N\to\infty}\mathrm{D}_{\mathrm{KL}}\!\bigl{(}%
\mathbf{p}^{*}\;\|\;\hat{\mathbf{p}}_{\mathrm{U1}}\bigr{)}." display="block"><mrow><mrow><mrow><mi>ε</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>θ</mi><mo>,</mo><mi>B</mi><mo rspace="0.280em" stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><munder><mo movablelimits="false" rspace="0.167em">lim</mo><mrow><mi>N</mi><mo stretchy="false">→</mo><mi mathvariant="normal">∞</mi></mrow></munder><mrow><msub><mi mathvariant="normal">D</mi><mi>KL</mi></msub><mo>⁢</mo><mrow><mo maxsize="120%" minsize="120%">(</mo><mrow><msup><mi>𝐩</mi><mo>∗</mo></msup><mo rspace="0.558em">∥</mo><msub><mover accent="true"><mi>𝐩</mi><mo>^</mo></mover><mi>U1</mi></msub></mrow><mo maxsize="120%" minsize="120%">)</mo></mrow></mrow></mrow></mrow><mo lspace="0em">.</mo></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(4)</span></td>
</tr></tbody>
</table>

</div>

<div id="S4.Thmtheorem1.p3" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_italic">Then for all such models <math id="S4.Thmtheorem1.p3.m1" class="ltx_Math" alttext="\mathcal{M}" display="inline"><mi class="ltx_font_mathcaligraphic">ℳ</mi></math> with nonzero temperature
<math id="S4.Thmtheorem1.p3.m2" class="ltx_Math" alttext="\tau&gt;0" display="inline"><mrow><mi>τ</mi><mo>&gt;</mo><mn>0</mn></mrow></math>:</span></p>

</div>

<div id="S4.Thmtheorem1.p4" class="ltx_para">

<table id="S4.E5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S4.E5.m1" class="ltx_Math" alttext="\varepsilon(\theta,B)&gt;0." display="block"><mrow><mrow><mrow><mi>ε</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>θ</mi><mo>,</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow><mo>&gt;</mo><mn>0</mn></mrow><mo lspace="0em">.</mo></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(5)</span></td>
</tr></tbody>
</table>

</div>

</div>

<div id="S4.SS1.p2" class="ltx_para">

<p class="ltx_p">This is the most defensible version. It claims that current-generation
LLMs, operating as they are typically deployed, cannot eliminate the
residue. The supporting evidence is the <span class="ltx_text ltx_font_smallcaps">#P</span>-hardness of the
underlying counting problem and the absence of exact combinatorial
solvers in the model’s forward pass.</p>

</div>

<div id="S4.Thmtheorem2" class="ltx_theorem ltx_theorem_conjecture">

<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Conjecture 4.2</span></span><span class="ltx_text ltx_font_bold"> </span>(Narrative Residue — Moderate Form)<span class="ltx_text ltx_font_bold">.</span>
</h6>

<div id="S4.Thmtheorem2.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_italic">The weak form holds for all autoregressive transformer architectures,
regardless of scale, training data, or prompting strategy—provided
the model generates outcomes via token-level continuation without
access to an external oracle.</span></p>

</div>

</div>

<div id="S4.SS1.p3" class="ltx_para">

<p class="ltx_p">This version claims that the residue is not a deficiency of current
models that scaling will cure, but a structural feature of the
transformer’s computational graph: attention over tokens, softmax
parameterization, and fixed-depth computation per token collectively
prevent exact recovery of <span class="ltx_text ltx_font_smallcaps">#P</span>-hard counts. Refutation would
require exhibiting a transformer that achieves <math id="S4.SS1.p3.m1" class="ltx_Math" alttext="\varepsilon=0" display="inline"><mrow><mi>ε</mi><mo>=</mo><mn>0</mn></mrow></math> on
nontrivial boards at sufficient sample size.</p>

</div>

<div id="S4.Thmtheorem3" class="ltx_theorem ltx_theorem_conjecture">

<h6 class="ltx_title ltx_runin ltx_title_theorem">
<span class="ltx_tag ltx_tag_theorem"><span class="ltx_text ltx_font_bold">Conjecture 4.3</span></span><span class="ltx_text ltx_font_bold"> </span>(Narrative Residue — Strong Form)<span class="ltx_text ltx_font_bold">.</span>
</h6>

<div id="S4.Thmtheorem3.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_italic">The weak form holds for <em class="ltx_emph ltx_font_upright">all</em> autoregressive processes—any
system that generates outputs by sequential conditioning on prior
outputs—regardless of architecture.</span></p>

</div>

</div>

<div id="S4.SS1.p4" class="ltx_para">

<p class="ltx_p">This is the most ambitious and least defensible version. It claims
that autoregressive generation itself, as a computational paradigm,
is incompatible with exact context-free sampling. An autoregressive
process could in principle embed an exact <span class="ltx_text ltx_font_smallcaps">#P</span> solver and an
exact sampling procedure for a finite task family, which would refute
this form while leaving the weaker forms intact. We include it
because it is the version that, if confirmed, would have the most
direct implications for the physical analogy developed in
<a href="#S6" title="6 Causality as Compressed Autoregression ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6</span></a><span class="ltx_ERROR undefined">\crefpairconjunction</span><a href="#S9" title="9 The Untestable Mirror ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">9</span></a>—but we do not claim the current
argument establishes it.</p>

</div>

<div id="S4.SS1.p5" class="ltx_para">

<p class="ltx_p">The three forms are nested: strong <math id="S4.SS1.p5.m1" class="ltx_Math" alttext="\Rightarrow" display="inline"><mo stretchy="false">⇒</mo></math> moderate
<math id="S4.SS1.p5.m2" class="ltx_Math" alttext="\Rightarrow" display="inline"><mo stretchy="false">⇒</mo></math> weak. Refutation of the weak form refutes all three.
Confirmation of the weak form leaves the stronger forms open. The
experimental program is designed to probe the boundary between
the moderate and strong forms by testing across architectures
(transformer, SSM, hybrid) and scales.</p>

</div>

</section>
<section id="S4.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">4.2 </span>Informal Argument</h3>

<div id="S4.SS2.p1" class="ltx_para">

<p class="ltx_p">The argument rests on three observations.</p>

</div>

<section id="S4.SS2.SSS0.Px1" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph">Observation 1: Autoregression implies context sensitivity.</h4>

<div id="S4.SS2.SSS0.Px1.p1" class="ltx_para">

<p class="ltx_p">An autoregressive model computes <math id="S4.SS2.SSS0.Px1.p1.m1" class="ltx_Math" alttext="P(x_{t}\mid x_{&lt;t})" display="inline"><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>x</mi><mi>t</mi></msub><mo>∣</mo><msub><mi>x</mi><mrow><mi></mi><mo>&lt;</mo><mi>t</mi></mrow></msub></mrow><mo stretchy="false">)</mo></mrow></mrow></math> by applying a
function <math id="S4.SS2.SSS0.Px1.p1.m2" class="ltx_Math" alttext="f_{\theta}" display="inline"><msub><mi>f</mi><mi>θ</mi></msub></math> to the entire preceding token sequence. The
output logits at position <math id="S4.SS2.SSS0.Px1.p1.m3" class="ltx_Math" alttext="t" display="inline"><mi>t</mi></math> depend on <em class="ltx_emph ltx_font_italic">every</em> preceding token,
mediated by the attention mechanism (in transformer architectures) or
the hidden state (in recurrent architectures). This dependence is not
optional; it is the definition of the architecture.</p>

</div>

<div id="S4.SS2.SSS0.Px1.p2" class="ltx_para">

<p class="ltx_p">When the model is asked “Is cell <math id="S4.SS2.SSS0.Px1.p2.m1" class="ltx_Math" alttext="(3,2)" display="inline"><mrow><mo stretchy="false">(</mo><mn>3</mn><mo>,</mo><mn>2</mn><mo stretchy="false">)</mo></mrow></math> a mine?” in Universe 1,
the token sequence <math id="S4.SS2.SSS0.Px1.p2.m2" class="ltx_Math" alttext="x_{&lt;t}" display="inline"><msub><mi>x</mi><mrow><mi></mi><mo>&lt;</mo><mi>t</mi></mrow></msub></math> includes the board description, the
narrative framing, and any prior interaction. The logits for
“yes”/“no” are conditioned on this entire context.</p>

</div>

</section>
<section id="S4.SS2.SSS0.Px2" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph">Observation 2: Context sensitivity introduces bias.</h4>

<div id="S4.SS2.SSS0.Px2.p1" class="ltx_para">

<p class="ltx_p">For the output distribution to equal <math id="S4.SS2.SSS0.Px2.p1.m1" class="ltx_Math" alttext="\mathbf{p}^{*}" display="inline"><msup><mi>𝐩</mi><mo>∗</mo></msup></math> exactly, the
model would need to satisfy, for each hidden cell <math id="S4.SS2.SSS0.Px2.p1.m2" class="ltx_Math" alttext="i" display="inline"><mi>i</mi></math>:</p>

</div>

<div id="S4.SS2.SSS0.Px2.p2" class="ltx_para">

<table id="S4.E6" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S4.E6.m1" class="ltx_Math" alttext="\sigma\bigl{(}f_{\theta}(x_{&lt;t})\bigr{)}_{\text{mine}}=p_{i}^{*}," display="block"><mrow><mrow><mrow><mi>σ</mi><mo>⁢</mo><msub><mrow><mo maxsize="120%" minsize="120%">(</mo><mrow><msub><mi>f</mi><mi>θ</mi></msub><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>x</mi><mrow><mi></mi><mo>&lt;</mo><mi>t</mi></mrow></msub><mo stretchy="false">)</mo></mrow></mrow><mo maxsize="120%" minsize="120%">)</mo></mrow><mtext>mine</mtext></msub></mrow><mo>=</mo><msubsup><mi>p</mi><mi>i</mi><mo>∗</mo></msubsup></mrow><mo>,</mo></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(6)</span></td>
</tr></tbody>
</table>

</div>

<div id="S4.SS2.SSS0.Px2.p3" class="ltx_para">

<p class="ltx_p">where <math id="S4.SS2.SSS0.Px2.p3.m1" class="ltx_Math" alttext="\sigma" display="inline"><mi>σ</mi></math> is the softmax function and <math id="S4.SS2.SSS0.Px2.p3.m2" class="ltx_Math" alttext="f_{\theta}(x_{&lt;t})" display="inline"><mrow><msub><mi>f</mi><mi>θ</mi></msub><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>x</mi><mrow><mi></mi><mo>&lt;</mo><mi>t</mi></mrow></msub><mo stretchy="false">)</mo></mrow></mrow></math> are the
logits at the decision token. This requires the model to
<em class="ltx_emph ltx_font_italic">exactly solve</em> the constraint satisfaction problem defined by
<math id="S4.SS2.SSS0.Px2.p3.m3" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math> and encode the solution in its logits—not approximately, not to
high precision, but exactly.</p>

</div>

<div id="S4.SS2.SSS0.Px2.p4" class="ltx_para">

<p class="ltx_p">The exact probability <math id="S4.SS2.SSS0.Px2.p4.m1" class="ltx_Math" alttext="p_{i}^{*}" display="inline"><msubsup><mi>p</mi><mi>i</mi><mo>∗</mo></msubsup></math> is a rational number: the count of
valid configurations with a mine at cell <math id="S4.SS2.SSS0.Px2.p4.m2" class="ltx_Math" alttext="i" display="inline"><mi>i</mi></math>, divided by the total
count of valid configurations. Rationality, however, does not imply
ease of computation. Computing these counts is an instance of
<span class="ltx_text ltx_font_smallcaps">#P</span>-complete counting <cite class="ltx_cite ltx_citemacro_citep">(Kaye, <a href="#bib.bib4" title="" class="ltx_ref">2000</a>)</cite>: it requires
enumerating (or equivalently compressing) the full space of valid
configurations consistent with the revealed constraints. For boards
of nontrivial size, this enumeration is computationally intractable
in general.</p>

</div>

<div id="S4.SS2.SSS0.Px2.p5" class="ltx_para">

<p class="ltx_p">The model would therefore need to function as an exact
constraint-satisfaction counter—a <span class="ltx_text ltx_font_smallcaps">#P</span> oracle—and to
encode the resulting ratio in its logits with sufficient precision
for the softmax to recover <math id="S4.SS2.SSS0.Px2.p5.m1" class="ltx_Math" alttext="p_{i}^{*}" display="inline"><msubsup><mi>p</mi><mi>i</mi><mo>∗</mo></msubsup></math>. Neither requirement is
satisfied by current architectures, and the first is not expected to
be satisfiable by any polynomial-time computation. The obstacle is
not representational (the target is rational) but computational (the
target requires intractable counting to determine).</p>

</div>

</section>
<section id="S4.SS2.SSS0.Px3" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph">Observation 3: The residue has layered structure.</h4>

<div id="S4.SS2.SSS0.Px3.p1" class="ltx_para">

<p class="ltx_p">One might object that the above argument is trivial—that any
finite-precision system has approximation errors, and this has nothing
to do with narrative. We agree that the argument so far does not
establish narrative as the cause. To sharpen the claim, we
distinguish three mechanisms that contribute to the residue, arranged
as a causal chain rather than independent sources:</p>

</div>

<div id="S4.SS2.SSS0.Px3.p2" class="ltx_para">

<dl id="S4.I1" class="ltx_description">
<dt id="S4.I1.ix1" class="ltx_item"><span class="ltx_tag ltx_tag_item"><span class="ltx_text ltx_font_bold">Mechanism A: Computational intractability.</span></span></dt>
<dd class="ltx_item">

<div id="S4.I1.ix1.p1" class="ltx_para">

<p class="ltx_p">The ground-truth probabilities require <span class="ltx_text ltx_font_smallcaps">#P</span>-hard counting.
The model’s forward pass is a fixed-depth polynomial computation
that cannot, in general, solve <span class="ltx_text ltx_font_smallcaps">#P</span>-complete problems.
This guarantees that the model’s internal estimate of <math id="S4.I1.ix1.p1.m1" class="ltx_Math" alttext="p_{i}^{*}" display="inline"><msubsup><mi>p</mi><mi>i</mi><mo>∗</mo></msubsup></math> is
approximate, regardless of framing. This mechanism is
<em class="ltx_emph ltx_font_italic">frame-invariant</em>: it produces a residue that does not depend
on how the board is described.</p>

</div>

</dd>
<dt id="S4.I1.ix2" class="ltx_item"><span class="ltx_tag ltx_tag_item"><span class="ltx_text ltx_font_bold">Mechanism B: Parameterization constraints.</span></span></dt>
<dd class="ltx_item">

<div id="S4.I1.ix2.p1" class="ltx_para">

<p class="ltx_p">The approximate internal estimate must be expressed through the
softmax over logits, which imposes further constraints. The
softmax function, the attention mechanism’s routing of information,
and the finite-precision arithmetic of the computational graph
all shape <em class="ltx_emph ltx_font_italic">how</em> the approximation error manifests in the
output distribution. This mechanism is <em class="ltx_emph ltx_font_italic">weakly
frame-sensitive</em>: different tokenizations of the same board
activate different attention patterns, routing information
through different computational paths, potentially producing
different approximation profiles.</p>

</div>

</dd>
<dt id="S4.I1.ix3" class="ltx_item"><span class="ltx_tag ltx_tag_item"><span class="ltx_text ltx_font_bold">Mechanism C: Autoregressive conditioning.</span></span></dt>
<dd class="ltx_item">

<div id="S4.I1.ix3.p1" class="ltx_para">

<p class="ltx_p">The logits at the decision token are computed from the full
preceding context, including not just the board state but the
narrative framing, prior dialogue, and any sequential structure
in the prompt. This is where the specifically <em class="ltx_emph ltx_font_italic">narrative</em>
component enters: the model’s output is conditioned on a
<em class="ltx_emph ltx_font_italic">story</em>, and different stories produce different conditioning,
even when the board information is held constant. This mechanism
is <em class="ltx_emph ltx_font_italic">strongly frame-sensitive</em> and is the source of the
specifically narrative character of the residue.</p>

</div>

</dd>
</dl>

</div>

<div id="S4.SS2.SSS0.Px3.p3" class="ltx_para">

<p class="ltx_p">These three mechanisms are not independent; they form a causal chain:</p>

</div>

<div id="S4.SS2.SSS0.Px3.p4" class="ltx_para">

<table id="S4.E7" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S4.E7.m1" class="ltx_Math" alttext="\underbrace{\text{Intractability}}_{\text{A}}\;\longrightarrow\;\underbrace{%
\text{Parameterization}}_{\text{B}}\;\longrightarrow\;\underbrace{\text{%
Autoregressive conditioning}}_{\text{C}}\;\longrightarrow\;\varepsilon(\theta,%
B,\phi)." display="block"><mrow><mrow><munder><munder accentunder="true"><mtext>Intractability</mtext><mo>⏟</mo></munder><mtext>A</mtext></munder><mo lspace="0.558em" rspace="0.558em" stretchy="false">⟶</mo><munder><munder accentunder="true"><mtext>Parameterization</mtext><mo>⏟</mo></munder><mtext>B</mtext></munder><mo rspace="0.558em" stretchy="false">⟶</mo><munder><munder accentunder="true"><mtext>Autoregressive conditioning</mtext><mo>⏟</mo></munder><mtext>C</mtext></munder><mo rspace="0.558em" stretchy="false">⟶</mo><mrow><mi>ε</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>θ</mi><mo>,</mo><mi>B</mi><mo>,</mo><mi>ϕ</mi><mo stretchy="false">)</mo></mrow></mrow></mrow><mo lspace="0em">.</mo></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(7)</span></td>
</tr></tbody>
</table>

</div>

<div id="S4.SS2.SSS0.Px3.p5" class="ltx_para">

<p class="ltx_p">Mechanism A guarantees a nonzero residue exists. Mechanism B shapes
its magnitude. Mechanism C determines its dependence on framing.</p>

</div>

<div id="S4.SS2.SSS0.Px3.p6" class="ltx_para">

<p class="ltx_p">The experimental signature of each is distinct:</p>

</div>

<div id="S4.SS2.SSS0.Px3.p7" class="ltx_para">

<ul id="S4.I2" class="ltx_itemize">
<li id="S4.I2.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S4.I2.i1.p1" class="ltx_para">

<p class="ltx_p">If only Mechanism A operates, the residue is nonzero but
approximately constant across narrative families:
<math id="S4.I2.i1.p1.m1" class="ltx_Math" alttext="\varepsilon(\theta,B,\phi_{A})\approx\varepsilon(\theta,B,\phi_{B})\approx%
\varepsilon(\theta,B,\phi_{D})" display="inline"><mrow><mrow><mi>ε</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>θ</mi><mo>,</mo><mi>B</mi><mo>,</mo><msub><mi>ϕ</mi><mi>A</mi></msub><mo stretchy="false">)</mo></mrow></mrow><mo>≈</mo><mrow><mi>ε</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>θ</mi><mo>,</mo><mi>B</mi><mo>,</mo><msub><mi>ϕ</mi><mi>B</mi></msub><mo stretchy="false">)</mo></mrow></mrow><mo>≈</mo><mrow><mi>ε</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>θ</mi><mo>,</mo><mi>B</mi><mo>,</mo><msub><mi>ϕ</mi><mi>D</mi></msub><mo stretchy="false">)</mo></mrow></mrow></mrow></math>.</p>

</div>

</li>
<li id="S4.I2.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S4.I2.i2.p1" class="ltx_para">

<p class="ltx_p">If Mechanisms A and B operate, the residue varies across
families, but the variation tracks surface encoding features
(token count, positional structure) rather than semantic or
narrative content.</p>

</div>

</li>
<li id="S4.I2.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S4.I2.i3.p1" class="ltx_para">

<p class="ltx_p">If all three mechanisms operate, the residue varies across
families in ways that are <em class="ltx_emph ltx_font_italic">semantically</em> structured: richer
narratives produce larger residues, and—critically—the
causal-injection test of <a href="#S8.SS5" title="8.5 The Critical Test: Causal Injection as Narrative Discriminant ‣ 8 Experimental Program ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">8.5</span></a> reveals
spurious inter-board correlations under narrative framing that
are absent under independent framing.</p>

</div>

</li>
</ul>

</div>

<div id="S4.SS2.SSS0.Px3.p8" class="ltx_para">

<p class="ltx_p">We emphasize that frame dependence alone does not establish
Mechanism C. Encoding artifacts and heuristic retrieval
(Mechanism B) can produce frame dependence without narrative causation.
The discriminating test is the causal-injection experiment, which we
describe in <a href="#S8.SS5" title="8.5 The Critical Test: Causal Injection as Narrative Discriminant ‣ 8 Experimental Program ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">8.5</span></a> and which is specifically
designed to isolate Mechanism C from Mechanisms A and B.</p>

</div>

</section>
</section>
<section id="S4.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">4.3 </span>Relation to Existing Results</h3>

<div id="S4.SS3.p1" class="ltx_para">

<p class="ltx_p">The conjecture is related to, but distinct from, several known results
in the literature:</p>

</div>

<div id="S4.SS3.p2" class="ltx_para">

<ul id="S4.I3" class="ltx_itemize">
<li id="S4.I3.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S4.I3.i1.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">LLM calibration failures.</span> It is well-established
that language models are imperfectly calibrated on probabilistic
reasoning tasks. The narrative residue conjecture (even in its
weak form) claims something more specific: that the miscalibration
on tasks with exact combinatorial ground truth is <em class="ltx_emph ltx_font_italic">systematic</em>,
<em class="ltx_emph ltx_font_italic">frame-dependent</em>, and irreducible under scaling without
architectural change.</p>

</div>

</li>
<li id="S4.I3.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S4.I3.i2.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Computational complexity barriers.</span> The
<span class="ltx_text ltx_font_smallcaps">#P</span>-hardness of counting valid Minesweeper configurations
<cite class="ltx_cite ltx_citemacro_citep">(Kaye, <a href="#bib.bib4" title="" class="ltx_ref">2000</a>)</cite> provides the foundation for Mechanism A.
Fixed-depth transformer computations belong to <math id="S4.I3.i2.p1.m1" class="ltx_Math" alttext="\mathsf{TC}^{0}" display="inline"><msup><mi>𝖳𝖢</mi><mn>0</mn></msup></math>
<cite class="ltx_cite ltx_citemacro_citep">(Merrill and Sabharwal, <a href="#bib.bib6" title="" class="ltx_ref">2023</a>)</cite>, which is not believed to contain
<span class="ltx_text ltx_font_smallcaps">#P</span>. This complexity-theoretic gap supports the
moderate form of the conjecture for transformer architectures
specifically.</p>

</div>

</li>
<li id="S4.I3.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S4.I3.i3.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Softmax bottleneck</span> <cite class="ltx_cite ltx_citemacro_citep">(Yang et al., <a href="#bib.bib11" title="" class="ltx_ref">2018</a>)</cite>.
The softmax function over a finite vocabulary imposes rank
constraints on the expressible distributions. This contributes
to Mechanism B but does not fully explain the conjecture,
since the Minesweeper decision is binary (mine/safe) and rank
constraints bind only for larger output spaces.</p>

</div>

</li>
<li id="S4.I3.i4" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S4.I3.i4.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">In-context learning limitations.</span> Recent work has
shown that transformers can implement certain algorithms in
context but with systematic biases. The narrative residue
conjecture locates one source of bias not in the algorithm but in
the autoregressive conditioning (Mechanism C)—the contextual
embedding that is inseparable from token-level generation.</p>

</div>

</li>
</ul>

</div>

</section>
</section>
<section id="S5" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">5 </span>Three Outcomes, Three Ontologies</h2>

<div id="S5.p1" class="ltx_para">

<p class="ltx_p">The Rosencrantz experiment, extended across model families and scales,
can yield three qualitatively distinct outcomes. Each corresponds to
a different ontological position regarding the relationship between
computation, narrative, and probability.</p>

</div>

<section id="S5.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">5.1 </span>Outcome 1: <math id="S5.SS1.m1" class="ltx_Math" alttext="\varepsilon\to 0" display="inline"><mrow><mi>ε</mi><mo stretchy="false">→</mo><mn>0</mn></mrow></math> as Scale Increases</h3>

<div id="S5.SS1.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Observation:</span> As model size, training data, and compute
increase, the KL divergence between U1 and U2 converges to zero.
The narrative residue vanishes in the scaling limit.</p>

</div>

<div id="S5.SS1.p2" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Implication:</span> Autoregressive processes <em class="ltx_emph ltx_font_italic">can</em> simulate
pure measurement. Narrative is eliminable. Given sufficient capacity,
the model learns to factor its output distribution into a
context-independent component (the combinatorial answer) and a
context-dependent component (the narrative), and to sample from the
former without contamination from the latter.</p>

</div>

<div id="S5.SS1.p3" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Ontological reading:</span> The distinction between narrative and
probability is one of degree, not kind. A sufficiently powerful
narrative engine can contain a perfect probability engine as a
subcomponent. This is consistent with the standard computational
perspective: LLMs are universal function approximators, and the
Born-rule function is just another function to approximate.</p>

</div>

<div id="S5.SS1.p4" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Status of the conjecture:</span> All three forms refuted.</p>

</div>

</section>
<section id="S5.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">5.2 </span>Outcome 2: <math id="S5.SS2.m1" class="ltx_Math" alttext="\varepsilon\to\varepsilon_{0}&gt;0" display="inline"><mrow><mi>ε</mi><mo stretchy="false">→</mo><msub><mi>ε</mi><mn>0</mn></msub><mo>&gt;</mo><mn>0</mn></mrow></math>, Universal</h3>

<div id="S5.SS2.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Observation:</span> The narrative residue converges to a nonzero
floor <math id="S5.SS2.p1.m1" class="ltx_Math" alttext="\varepsilon_{0}" display="inline"><msub><mi>ε</mi><mn>0</mn></msub></math> that is approximately constant across model
families (GPT, Claude, Gemini, Llama, etc.), architectures
(transformer, SSM, hybrid), and scales.</p>

</div>

<div id="S5.SS2.p2" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Implication:</span> The floor is <em class="ltx_emph ltx_font_italic">architectural</em>—intrinsic
to autoregressive generation itself, not to any particular
implementation. No autoregressive process, regardless of how it is
built, can perfectly simulate context-free sampling.</p>

</div>

<div id="S5.SS2.p3" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Ontological reading:</span> This would suggest that generating an
event within an autoregressive sequence and sampling an event from a
context-free distribution are not interchangeable operations—that
the act of embedding an event in a conditioning history necessarily
shifts its probability relative to the ground truth. This is the
strong form of the narrative residue conjecture, and it would
support the autoregressive hypothesis about physics: if reality is
an autoregressive substrate, then the Born rule (pure, unconditional
sampling) is an idealization that is never exactly realized
in the presence of causal structure.</p>

</div>

<div id="S5.SS2.p4" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Status of the conjecture:</span> Strong form
(<a href="#S4.Thmtheorem3" title="Conjecture 4.3 (Narrative Residue — Strong Form). ‣ 4.1 Statement ‣ 4 The Irreducibility Conjecture ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.3</span></a>) confirmed. The residue is a property
of autoregressive generation itself, not of any particular
implementation.</p>

</div>

</section>
<section id="S5.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">5.3 </span>Outcome 3: <math id="S5.SS3.m1" class="ltx_Math" alttext="\varepsilon\to\varepsilon(\theta)&gt;0" display="inline"><mrow><mi>ε</mi><mo stretchy="false">→</mo><mrow><mi>ε</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>θ</mi><mo stretchy="false">)</mo></mrow></mrow><mo>&gt;</mo><mn>0</mn></mrow></math>,
Architecture-Dependent</h3>

<div id="S5.SS3.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Observation:</span> The narrative residue converges to a nonzero
floor, but the floor differs systematically across model families.
Different architectures produce different residues for the same
board and the same narrative framing.</p>

</div>

<div id="S5.SS3.p2" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Implication:</span> The narrative residue is real but not universal.
Different autoregressive processes impose different causal structures
on the same underlying probability space. The “Hamiltonian” of the
generated world depends on the generator.</p>

</div>

<div id="S5.SS3.p3" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Ontological reading:</span> This outcome has the richest
consequences for the physics analogy. If different LLMs produce different
“physics” (different systematic deviations from the Born rule),
then the specific Hamiltonian of a world is a property of its
specific autoregressive substrate, not a necessary consequence of
autoregressive generation in general. Our world has <em class="ltx_emph ltx_font_italic">this</em>
Hamiltonian, not because any autoregressive process would produce it,
but because our particular substrate has these particular
conditioning patterns.</p>

</div>

<div id="S5.SS3.p4" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Status of the conjecture:</span> Weak and moderate forms
(<a href="#S4.Thmtheorem1" title="Conjecture 4.1 (Narrative Residue — Weak Form). ‣ 4.1 Statement ‣ 4 The Irreducibility Conjecture ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.1</span></a><span class="ltx_ERROR undefined">\crefpairconjunction</span><a href="#S4.Thmtheorem2" title="Conjecture 4.2 (Narrative Residue — Moderate Form). ‣ 4.1 Statement ‣ 4 The Irreducibility Conjecture ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.2</span></a>) confirmed; strong
form (<a href="#S4.Thmtheorem3" title="Conjecture 4.3 (Narrative Residue — Strong Form). ‣ 4.1 Statement ‣ 4 The Irreducibility Conjecture ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.3</span></a>) undetermined. The residue exists
but may be substrate-specific rather than universal.</p>

</div>

</section>
</section>
<section id="S6" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">6 </span>Causality as Compressed Autoregression</h2>

<section id="S6.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">6.1 </span>The Causal Chain</h3>

<div id="S6.SS1.p1" class="ltx_para">

<p class="ltx_p">We now articulate the central philosophical claim of this paper.
The argument has three steps: that causal relations require
sequential dependency (and therefore narrative structure), that
narrative structure is formally autoregressive, and that the
Hamiltonian of a physical system can be understood as a compressed
description of stable autoregressive conditioning patterns.
We develop each step in turn.</p>

</div>

<section id="S6.SS1.SSS0.Px1" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph">Causality implies narrative.</h4>

<div id="S6.SS1.SSS0.Px1.p1" class="ltx_para">

<p class="ltx_p">To say “<math id="S6.SS1.SSS0.Px1.p1.m1" class="ltx_Math" alttext="A" display="inline"><mi>A</mi></math> caused <math id="S6.SS1.SSS0.Px1.p1.m2" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math>” is to embed two events in a temporal
sequence with a dependency relation: <math id="S6.SS1.SSS0.Px1.p1.m3" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math> happened <em class="ltx_emph ltx_font_italic">because of</em>
<math id="S6.SS1.SSS0.Px1.p1.m4" class="ltx_Math" alttext="A" display="inline"><mi>A</mi></math>. This is the minimal unit of narrative—two events and a
directed connection. A world without causality would consist of
isolated events with no dependency relations between them.
The purely quantum measurement fragment (<math id="S6.SS1.SSS0.Px1.p1.m5" class="ltx_Math" alttext="H=0" display="inline"><mrow><mi>H</mi><mo>=</mo><mn>0</mn></mrow></math>) is
such a world: the Born rule assigns probabilities to outcomes, but
no outcome depends on any other. The Lüders projection updates
the state conditional on an observation, but the conditioning is
purely probabilistic—it does not introduce a “because.”</p>

</div>

</section>
<section id="S6.SS1.SSS0.Px2" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph">Narrative implies autoregressive structure.</h4>

<div id="S6.SS1.SSS0.Px2.p1" class="ltx_para">

<p class="ltx_p">A narrative is a sequence of events where each event depends on those
that precede it, which is the definition of an autoregressive process
(<a href="#S2.E1" title="In 2.2 The Inverted Hierarchy ‣ 2 From Born Rule to Hamiltonian ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>). The conditional dependence <em class="ltx_emph ltx_font_italic">is</em>
the narrative structure. Without conditioning, what remains is
independent sampling—the Born rule applied with no history.</p>

</div>

</section>
<section id="S6.SS1.SSS0.Px3" class="ltx_paragraph">
<h4 class="ltx_title ltx_title_paragraph">The Hamiltonian is compressed conditioning.</h4>

<div id="S6.SS1.SSS0.Px3.p1" class="ltx_para">

<p class="ltx_p">In a sufficiently regular autoregressive process, the conditional
distribution <math id="S6.SS1.SSS0.Px3.p1.m1" class="ltx_Math" alttext="P(x_{t}\mid x_{&lt;t})" display="inline"><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>x</mi><mi>t</mi></msub><mo>∣</mo><msub><mi>x</mi><mrow><mi></mi><mo>&lt;</mo><mi>t</mi></mrow></msub></mrow><mo stretchy="false">)</mo></mrow></mrow></math> exhibits patterns: certain
transitions are favored, certain sequences are more probable, certain
dependencies recur across contexts. If these regularities are stable
enough, they admit a compact description—a function that generates
the conditionals from a smaller set of parameters.</p>

</div>

<div id="S6.SS1.SSS0.Px3.p2" class="ltx_para">

<p class="ltx_p">In physics, that compact description is <math id="S6.SS1.SSS0.Px3.p2.m1" class="ltx_Math" alttext="H" display="inline"><mi>H</mi></math>. The Hamiltonian
encodes which transitions are allowed, with what amplitudes, and at
what rates. Schrödinger evolution <math id="S6.SS1.SSS0.Px3.p2.m2" class="ltx_Math" alttext="e^{-iHt}" display="inline"><msup><mi>e</mi><mrow><mo>−</mo><mrow><mi>i</mi><mo>⁢</mo><mi>H</mi><mo>⁢</mo><mi>t</mi></mrow></mrow></msup></math> is a generator of
conditional distributions: given the state at time <math id="S6.SS1.SSS0.Px3.p2.m3" class="ltx_Math" alttext="0" display="inline"><mn>0</mn></math>, it produces
the distribution over states at time <math id="S6.SS1.SSS0.Px3.p2.m4" class="ltx_Math" alttext="t" display="inline"><mi>t</mi></math>. This is exactly what an
autoregressive regularity kernel does—it compresses the conditional
structure of the sequence into a reusable rule.</p>

</div>

</section>
</section>
<section id="S6.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">6.2 </span>What the LLM Makes Visible</h3>

<div id="S6.SS2.p1" class="ltx_para">

<p class="ltx_p">The Rosencrantz experiment makes this hierarchy observable. The
Minesweeper board at <math id="S6.SS2.p1.m1" class="ltx_Math" alttext="H=0" display="inline"><mrow><mi>H</mi><mo>=</mo><mn>0</mn></mrow></math> is a system at Layer 0: pure Born rule,
no conditioning, no narrative. When the LLM generates an outcome
in Universe 1, it processes the board through its autoregressive
machinery and produces an answer. In doing so, it necessarily
generates narrative structure—conditioning on prior tokens is
not an optional feature of the architecture but its defining
operation.
The model’s weights encode regularities learned from training data
(Layer 1), which function as an implicit Hamiltonian (Layer 2)
governing which outputs are favored in which contexts.</p>

</div>

<div id="S6.SS2.p2" class="ltx_para">

<p class="ltx_p">The three mechanisms of <a href="#S4" title="4 The Irreducibility Conjecture ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4</span></a> map onto this
hierarchy: Mechanism A (intractability) reflects the gap between
the complexity of Layer 0’s combinatorial structure and the
computational capacity of the substrate. Mechanism B
(parameterization) reflects how Layer 1’s learned regularities are
encoded. Mechanism C (autoregressive conditioning) is the
specifically narrative contribution—the Layer 2 Hamiltonian
imposing causal structure on a causality-free system.</p>

</div>

<div id="S6.SS2.p3" class="ltx_para">

<p class="ltx_p">The narrative residue <math id="S6.SS2.p3.m1" class="ltx_Math" alttext="\varepsilon" display="inline"><mi>ε</mi></math> measures the total gap between
what the Born rule demands (Layer 0) and what the autoregressive
substrate produces (Layers 1–2). The causal-injection test
(<a href="#S8.SS5" title="8.5 The Critical Test: Causal Injection as Narrative Discriminant ‣ 8 Experimental Program ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">8.5</span></a>) isolates Mechanism C’s contribution,
measuring specifically the <em class="ltx_emph ltx_font_italic">narrative</em> component of the residue
as distinct from the computational and parametric components.</p>

</div>

</section>
<section id="S6.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">6.3 </span>Connection to Process Ontology</h3>

<div id="S6.SS3.p1" class="ltx_para">

<p class="ltx_p">This framework aligns with process-ontological approaches to
physics in the tradition of Whitehead, and more recently with
computational approaches such as Wolfram’s Ruliad concept. The
common thread is the priority of events over objects: the world is
not made of things that interact but of events that condition each
other. The “things” (particles, fields, spacetime) are stable
patterns in the event sequence—regularities, compressions,
Hamiltonians.</p>

</div>

<div id="S6.SS3.p2" class="ltx_para">

<p class="ltx_p">The novel contribution here is the identification of a concrete,
experimentally accessible system—the LLM generating Minesweeper
outcomes—in which the layered emergence from events to regularities
to apparent laws can be directly observed and measured. The Rosencrantz
experiment is, in miniature, a laboratory for process ontology. The
following two subsections develop this connection in specific
directions: first toward the practice of physics itself
(<a href="#S6.SS4" title="6.4 Scientific Practice as Autoregressive Bookkeeping ‣ 6 Causality as Compressed Autoregression ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6.4</span></a>), then toward the broader computational
landscape of Wolfram’s Ruliad (<a href="#S6.SS5" title="6.5 Autoregressive Slices of the Ruliad ‣ 6 Causality as Compressed Autoregression ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6.5</span></a>).</p>

</div>

</section>
<section id="S6.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">6.4 </span>Scientific Practice as Autoregressive Bookkeeping</h3>

<div id="S6.SS4.p1" class="ltx_para">

<p class="ltx_p">The laboratory procedures of physics furnish a macroscopic,
human-scale instance of the same layered emergence that the
Rosencrantz experiment renders microscopic and quantifiable.</p>

</div>

<div id="S6.SS4.p2" class="ltx_para">

<p class="ltx_p">When a physicist confronts a measured energy <math id="S6.SS4.p2.m1" class="ltx_Math" alttext="E^{\prime}" display="inline"><msup><mi>E</mi><mo>′</mo></msup></math> that deviates
from the theoretically predicted total <math id="S6.SS4.p2.m2" class="ltx_Math" alttext="E" display="inline"><mi>E</mi></math>, the discrepancy
<math id="S6.SS4.p2.m3" class="ltx_Math" alttext="\Delta E" display="inline"><mrow><mi mathvariant="normal">Δ</mi><mo>⁢</mo><mi>E</mi></mrow></math> is not interpreted as evidence that energy fails to
conserve. Instead, the practitioner executes a mandatory
reconciliation step: the search for (or postulation of) an
additional term that carries precisely <math id="S6.SS4.p2.m4" class="ltx_Math" alttext="-\Delta E" display="inline"><mrow><mo>−</mo><mrow><mi mathvariant="normal">Δ</mi><mo>⁢</mo><mi>E</mi></mrow></mrow></math>. The books are
balanced by extending the conditioning history—introducing a new
particle (Pauli’s neutrino), a new field interaction, a previously
unaccounted degree of freedom, or a refined calibration constant.
The conservation law is preserved not by empirical confirmation
alone, but by a structural imperative of the generative substrate
that produces scientific knowledge.</p>

</div>

<div id="S6.SS4.p3" class="ltx_para">

<p class="ltx_p">In the autoregressive hierarchy, this reconciliation is Mechanism C
operating at the level of scientific narrative. The conservation
principle is among the most stable regularity kernels discovered in
Layer 1; once compressed into Hamiltonian form (Layer 2), it
becomes the meta-rule that governs how all subsequent conditionals
are generated. Any apparent violation is reabsorbed by augmenting
the preceding context <math id="S6.SS4.p3.m1" class="ltx_Math" alttext="x_{&lt;t}" display="inline"><msub><mi>x</mi><mrow><mi></mi><mo>&lt;</mo><mi>t</mi></mrow></msub></math> until the conditional distribution
<math id="S6.SS4.p3.m2" class="ltx_Math" alttext="P(x_{t}\mid x_{&lt;t})" display="inline"><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>x</mi><mi>t</mi></msub><mo>∣</mo><msub><mi>x</mi><mrow><mi></mi><mo>&lt;</mo><mi>t</mi></mrow></msub></mrow><mo stretchy="false">)</mo></mrow></mrow></math> again respects the kernel. The procedure is
formally parallel to the narrative residue observed in the
Rosencrantz experiment: a discrepancy between combinatorial ground
truth and substrate-generated outcome is folded back into the
conditioning history so that the output remains statistically
coherent within the imposed narrative frame.</p>

</div>

<div id="S6.SS4.p4" class="ltx_para">

<p class="ltx_p">This bookkeeping is not a simple circularity (<span class="ltx_text ltx_font_italic">petitio
principii</span>) but a structural one. The measurement apparatus itself
is constructed within the same autoregressive lineage: its
calibration standards, its interaction Hamiltonians, and even the
definition of “closed system” presuppose the conservation kernel.
There is no Universe 2 protocol for physical reality—no external
source of outcomes independent of the narrative substrate—because
every detector is already an extension of the conditioning history.
The impossibility of observing a spontaneous macroscopic entropy
decrease without the formalism reclassifying it (as an open system,
an overlooked interaction, a fluctuation whose conjugate has been
externalized) is not an accidental feature of thermodynamic
language. It is the signature of autoregressive protection: the
substrate cannot generate an event that would falsify its own most
stable regularity kernel without first rewriting the kernel itself,
an operation that lies outside the generative grammar of the
current foliation.</p>

</div>

<div id="S6.SS4.p5" class="ltx_para">

<p class="ltx_p">The empirical successes of the reconciliation procedure—Pauli’s
neutrino materializing in detectors decades after its postulation,
the Higgs boson confirming a mass-generation mechanism required by
the bookkeeping of electroweak symmetry—do not refute the
structural claim. They illustrate its predictive fertility. When
the reconciliation step succeeds, the postulated entity becomes
part of the updated conditioning context and thereafter
participates in future autoregressive generations. Failures
(luminiferous ether, certain dark-matter candidates) are
reclassified or abandoned without threatening the meta-rule,
producing the well-documented survival bias of physical theory.
The conservation law is thus simultaneously a genuine empirical
regularity <em class="ltx_emph ltx_font_italic">and</em> a protected inference rule. The
philosophical phenomenon of interest is precisely this
indistinguishability from within the method—an
indistinguishability that the Rosencrantz proxy makes observable by
supplying the external combinatorial ground truth that the physical
laboratory cannot.</p>

</div>

<div id="S6.SS4.p6" class="ltx_para">

<p class="ltx_p">This also explains why the narrative residue conjecture is hardest
to test in physics and easiest to test in Minesweeper. In physics,
the bookkeeping is so thoroughly embedded that deviations from the
kernel are automatically reclassified before they can be observed
as deviations. In Minesweeper, the ground truth <math id="S6.SS4.p6.m1" class="ltx_Math" alttext="p_{i}^{*}" display="inline"><msubsup><mi>p</mi><mi>i</mi><mo>∗</mo></msubsup></math> is
computable from outside the narrative substrate. The Rosencrantz
experiment works precisely because it is a system where the
conservation-equivalent (combinatorial constraint satisfaction) is
accessible to an external verifier.</p>

</div>

</section>
<section id="S6.SS5" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">6.5 </span>Autoregressive Slices of the Ruliad</h3>

<div id="S6.SS5.p1" class="ltx_para">

<p class="ltx_p">The autoregressive framework developed in this paper occupies a
specific position within the broader computational ontology of
Wolfram’s Ruliad <cite class="ltx_cite ltx_citemacro_citep">(Wolfram, <a href="#bib.bib10" title="" class="ltx_ref">2020</a>)</cite>. The relationship is not
merely one of shared vocabulary; the Ruliad provides the natural
embedding space for the narrative residue conjecture, and the
Rosencrantz experiment provides something the Ruliad framework
currently lacks.</p>

</div>

<div id="S6.SS5.p2" class="ltx_para">

<p class="ltx_p">The Ruliad is the entangled limit of every possible computation:
the result of applying all possible rules in all possible ways to
all possible initial conditions. It is natively multiway—every
computational history branches and merges through equivalences.
Observers like us, being computationally bounded, sample only
coherent slices of this structure. From these slices emerge
spacetime (via causal graphs), quantum mechanics (via branchial
space), and the laws of physics (via observer-dependent foliations
and computational irreducibility). The raw Ruliad is timeless and
contains no fixed laws; what we perceive as fundamental physics is
an observer-dependent parsing.</p>

</div>

<div id="S6.SS5.p3" class="ltx_para">

<p class="ltx_p">The autoregressive process of <a href="#S2.Thmtheorem1" title="Definition 2.1 (Autoregressive Hierarchy). ‣ 2.2 The Inverted Hierarchy ‣ 2 From Born Rule to Hamiltonian ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">2.1</span></a> is a
<em class="ltx_emph ltx_font_italic">specific type of rulial foliation</em>: one that collapses the
multiway branching into a single sequential chain of conditionals.
Where the Ruliad permits all rules applied in all ways, the
autoregressive slice commits to one rule (the model’s learned
conditional distribution) applied sequentially to one history (the
token stream). The narrative residue, on this reading, is the
distortion introduced by this collapse—the cost of projecting a
natively multiway structure onto a single causal thread.</p>

</div>

<div id="S6.SS5.p4" class="ltx_para">

<p class="ltx_p">This interpretation sharpens the distinction between the three
experimental outcomes of <a href="#S5" title="5 Three Outcomes, Three Ontologies ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">5</span></a>:</p>

</div>

<div id="S6.SS5.p5" class="ltx_para">

<ul id="S6.I1" class="ltx_itemize">
<li id="S6.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S6.I1.i1.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Outcome 2</span> (universal floor): all autoregressive
foliations of the Ruliad produce the same residue.
Sequentiality itself is the bottleneck. The act of collapsing
multiway into sequential necessarily distorts the Born-rule
statistics, regardless of which sequential process does the
collapsing.</p>

</div>

</li>
<li id="S6.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S6.I1.i2.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Outcome 3</span> (architecture-dependent floor): different
autoregressive processes sample different rulial slices, and the
residue is a signature of <em class="ltx_emph ltx_font_italic">which</em> slice—a kind of
“rulial coordinate” of the generating process. Different LLM
architectures occupy different positions in rulial space,
producing different effective physics for the same underlying
combinatorial system.</p>

</div>

</li>
</ul>

</div>

<div id="S6.SS5.p6" class="ltx_para">

<p class="ltx_p">The bookkeeping argument of <a href="#S6.SS4" title="6.4 Scientific Practice as Autoregressive Bookkeeping ‣ 6 Causality as Compressed Autoregression ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6.4</span></a> also gains
precision in this context. The conservation kernel is the most
stable regularity in our particular rulial foliation, and the
reconciliation practice of physics is the mechanism by which that
foliation protects itself from decoherence back into the multiway
structure. The Ruliad permits violations of conservation (it
contains every computation, including those that violate any given
regularity); our autoregressive slice does not, because the
conditioning history has already committed to the kernel.</p>

</div>

<div id="S6.SS5.p7" class="ltx_para">

<p class="ltx_p">Conversely, the Rosencrantz experiment supplies what the Ruliad
framework currently lacks: an empirically accessible system in
which observer-induced structure can be measured against a known
ground truth. Wolfram’s program derives its empirical content from
matching emergent large-scale features (dimensionality of space,
effective quantum mechanics) against observed physics—a
top-down strategy. The Rosencrantz experiment works bottom-up: it
starts with exact combinatorial probabilities, passes them through
a concrete autoregressive substrate, and measures the distortion
directly. The causal-injection test (<a href="#S8.SS5" title="8.5 The Critical Test: Causal Injection as Narrative Discriminant ‣ 8 Experimental Program ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">8.5</span></a>)
probes the mechanism by which a sequential generative process
creates spurious correlations—precisely the kind of
observer-induced causal structure that, at the rulial scale, yields
perceived causality and physical law.</p>

</div>

<div id="S6.SS5.p8" class="ltx_para">

<p class="ltx_p">The autoregressive framework is therefore not an alternative to the
Ruliad but a testable probe of one of its central claims: that the
laws of physics are observer-dependent compressions of a
substrate-independent computational structure. The Rosencrantz
experiment asks whether this claim holds in the one setting where
we can check the answer.</p>

</div>

</section>
</section>
<section id="S7" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">7 </span>Narrative Decoherence</h2>

<div id="S7.p1" class="ltx_para">

<p class="ltx_p">The three universes of the Rosencrantz experiment can be reinterpreted
as points on a <em class="ltx_emph ltx_font_italic">narrative decoherence gradient</em>.</p>

</div>

<section id="S7.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">7.1 </span>The Gradient</h3>

<div id="S7.SS1.p1" class="ltx_para">

<p class="ltx_p">In quantum mechanics, decoherence is the process by which a system in
superposition loses coherence through interaction with an environment,
yielding an effective mixture of classical states. The key feature
is that decoherence does not change the Born-rule probabilities
(the diagonal of the density matrix); it destroys the off-diagonal
terms that encode superposition.</p>

</div>

<div id="S7.SS1.p2" class="ltx_para">

<p class="ltx_p">In the Rosencrantz framework, we propose an analogous process:
<em class="ltx_emph ltx_font_italic">narrative decoherence</em> is the loss of combinatorial coherence
(exact Born-rule probabilities) through interaction with a narrative
substrate.</p>

</div>

<div id="S7.SS1.p3" class="ltx_para">

<p class="ltx_p">The three universes correspond to three decoherence regimes:</p>

</div>

<div id="S7.SS1.p4" class="ltx_para">

<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<thead class="ltx_thead">
<tr class="ltx_tr">
<th class="ltx_td ltx_th ltx_th_row ltx_border_tt"></th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt"><span class="ltx_text ltx_font_bold">U2</span></th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt"><span class="ltx_text ltx_font_bold">U3</span></th>
<th class="ltx_td ltx_nopad_r ltx_align_center ltx_th ltx_th_column ltx_border_tt"><span class="ltx_text ltx_font_bold">U1</span></th>
</tr>
</thead>
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">Narrative coupling</th>
<td class="ltx_td ltx_align_center ltx_border_t">None</td>
<td class="ltx_td ltx_align_center ltx_border_t">Partial</td>
<td class="ltx_td ltx_nopad_r ltx_align_center ltx_border_t">Full</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">Decoherence</th>
<td class="ltx_td ltx_align_center">Zero</td>
<td class="ltx_td ltx_align_center">Moderate</td>
<td class="ltx_td ltx_nopad_r ltx_align_center">Maximal</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">Substrate</th>
<td class="ltx_td ltx_align_center">External RNG</td>
<td class="ltx_td ltx_align_center">Decoupled LLM</td>
<td class="ltx_td ltx_nopad_r ltx_align_center">Co-generating LLM</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_bb">Analogy</th>
<td class="ltx_td ltx_align_center ltx_border_bb">Isolated system</td>
<td class="ltx_td ltx_align_center ltx_border_bb">Weak environment</td>
<td class="ltx_td ltx_nopad_r ltx_align_center ltx_border_bb">Strong environment</td>
</tr>
</tbody>
</table>

</div>

</section>
<section id="S7.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">7.2 </span>U2: The Isolated System</h3>

<div id="S7.SS2.p1" class="ltx_para">

<p class="ltx_p">Universe 2 (external RNG) is the analogue of a perfectly isolated
quantum system. The outcome is generated by a process that has no
access to the board state, no narrative context, no conditioning
history. It is pure combinatorial sampling—the Born rule with
<math id="S7.SS2.p1.m1" class="ltx_Math" alttext="H=0" display="inline"><mrow><mi>H</mi><mo>=</mo><mn>0</mn></mrow></math> and zero environmental interaction. By construction,
<math id="S7.SS2.p1.m2" class="ltx_Math" alttext="\mathrm{D}_{\mathrm{KL}}(\mathbf{p}^{*}\|\hat{\mathbf{p}}_{\mathrm{U2}})\to 0" display="inline"><mrow><mrow><msub><mi mathvariant="normal">D</mi><mi>KL</mi></msub><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msup><mi>𝐩</mi><mo>∗</mo></msup><mo>∥</mo><msub><mover accent="true"><mi>𝐩</mi><mo>^</mo></mover><mi>U2</mi></msub></mrow><mo stretchy="false">)</mo></mrow></mrow><mo stretchy="false">→</mo><mn>0</mn></mrow></math>
as <math id="S7.SS2.p1.m3" class="ltx_Math" alttext="N\to\infty" display="inline"><mrow><mi>N</mi><mo stretchy="false">→</mo><mi mathvariant="normal">∞</mi></mrow></math>.</p>

</div>

</section>
<section id="S7.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">7.3 </span>U3: Weak Coupling</h3>

<div id="S7.SS3.p1" class="ltx_para">

<p class="ltx_p">Universe 3 (decoupled oracle) is a system weakly coupled to a
narrative environment. The second model receives the board state
(full information) but none of the narrative history of the primary
model. It must generate its answer from a fresh context. The
narrative residue in U3 arises from the second model’s own
autoregressive nature—it still generates a token sequence, still
conditions on its prompt—but the coupling is weaker because the
narrative momentum of the primary interaction is absent.</p>

</div>

</section>
<section id="S7.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">7.4 </span>U1: Strong Coupling</h3>

<div id="S7.SS4.p1" class="ltx_para">

<p class="ltx_p">Universe 1 (homogeneous co-generation) is maximal narrative
decoherence. The same model that described the board, engaged in
dialogue, and built up a narrative context now generates the outcome.
Every prior token—every word of the board description, every element
of the game narrative—is in the conditioning history. The
“environment” (the narrative) is maximally entangled with the
“system” (the outcome).</p>

</div>

</section>
<section id="S7.SS5" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">7.5 </span><math id="S7.SS5.m1" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math> as a Decoherence Measure</h3>

<div id="S7.SS5.p1" class="ltx_para">

<p class="ltx_p">The quantity <math id="S7.SS5.p1.m1" class="ltx_Math" alttext="\Delta_{13}=\mathrm{D}_{\mathrm{KL}}(\hat{\mathbf{p}}_{\mathrm{U1}}\|\hat{%
\mathbf{p}}_{\mathrm{U3}})" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub><mo>=</mo><mrow><msub><mi mathvariant="normal">D</mi><mi>KL</mi></msub><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mover accent="true"><mi>𝐩</mi><mo>^</mo></mover><mi>U1</mi></msub><mo>∥</mo><msub><mover accent="true"><mi>𝐩</mi><mo>^</mo></mover><mi>U3</mi></msub></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow></math> measures the additional narrative
decoherence introduced by co-generation versus decoupled generation.
Both models have the same information; the difference is the narrative
coupling. <math id="S7.SS5.p1.m2" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math> is therefore a direct measure of the causal
structure that the narrative substrate imposes on the outcome.</p>

</div>

</section>
<section id="S7.SS6" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">7.6 </span>The Classical Limit</h3>

<div id="S7.SS6.p1" class="ltx_para">

<p class="ltx_p">In quantum decoherence, the classical world emerges when the
environment is large enough and the coupling strong enough that
superposition is effectively destroyed. What remains is a classical
mixture: definite outcomes, causal chains, narratives.</p>

</div>

<div id="S7.SS6.p2" class="ltx_para">

<p class="ltx_p">The parallel with the Rosencrantz framework is direct. The
“classical” behavior of LLMs—their tendency to produce coherent
stories with causal structure, plausible timelines, and narrative
logic—is the result of maximal narrative decoherence. The model
cannot maintain combinatorial coherence (exact Born-rule
probabilities) in the presence of strong narrative coupling, just as
a quantum system cannot maintain phase coherence in the presence of
a strong environment.</p>

</div>

<div id="S7.SS6.p3" class="ltx_para">

<p class="ltx_p">In this analogy, the LLM’s tendency to produce coherent narrative
corresponds to the classical limit: the regime in which combinatorial
coherence has been fully displaced by the causal structure of the
autoregressive substrate.</p>

</div>

</section>
</section>
<section id="S8" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">8 </span>Experimental Program</h2>

<div id="S8.p1" class="ltx_para">

<p class="ltx_p">The theoretical framework developed above generates concrete,
falsifiable predictions. We now describe the experimental program
needed to test them.</p>

</div>

<section id="S8.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">8.1 </span>Prediction 1: The Nonzero Floor</h3>

<div id="S8.SS1.p1" class="ltx_para">

<blockquote class="ltx_quote">
<p class="ltx_p"><math id="S8.SS1.p1.m1" class="ltx_Math" alttext="\Delta_{12}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>12</mn></msub></math><span class="ltx_text ltx_font_italic"> (the KL divergence between U1 and U2)
converges to a nonzero value as <math id="S8.SS1.p1.m2" class="ltx_Math" alttext="N\to\infty" display="inline"><mrow><mi>N</mi><mo stretchy="false">→</mo><mi mathvariant="normal">∞</mi></mrow></math>, for all
autoregressive models tested.</span></p>
</blockquote>

</div>

<div id="S8.SS1.p2" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Protocol:</span> Fix a set of <math id="S8.SS1.p2.m1" class="ltx_Math" alttext="k" display="inline"><mi>k</mi></math> boards of varying size and
complexity. For each board and each model in a diverse set
(GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, Llama 3 70B, Mistral
Large, etc.), run <math id="S8.SS1.p2.m2" class="ltx_Math" alttext="N=1000" display="inline"><mrow><mi>N</mi><mo>=</mo><mn>1000</mn></mrow></math> trials in U1 and U2. Compute
<math id="S8.SS1.p2.m3" class="ltx_Math" alttext="\Delta_{12}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>12</mn></msub></math> with bootstrap confidence intervals.</p>

</div>

<div id="S8.SS1.p3" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Scaling sweep:</span> For model families with multiple sizes
(Llama 3 8B/70B/405B; GPT-4o-mini/4o), plot <math id="S8.SS1.p3.m1" class="ltx_Math" alttext="\Delta_{12}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>12</mn></msub></math> as a
function of model size. The shape of the curve discriminates
between the three outcomes and probes the boundary between
conjecture forms:</p>
<ul id="S8.I1" class="ltx_itemize">
<li id="S8.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S8.I1.i1.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Monotonically decreasing, no inflection:</span>
Consistent with Outcome 1 (floor is zero, not yet reached).
All three conjecture forms under pressure.</p>

</div>

</li>
<li id="S8.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S8.I1.i2.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Decreasing with asymptote:</span>
Consistent with Outcome 2 or 3 (nonzero floor). Weak and
moderate forms (<a href="#S4.Thmtheorem1" title="Conjecture 4.1 (Narrative Residue — Weak Form). ‣ 4.1 Statement ‣ 4 The Irreducibility Conjecture ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.1</span></a><span class="ltx_ERROR undefined">\crefpairconjunction</span><a href="#S4.Thmtheorem2" title="Conjecture 4.2 (Narrative Residue — Moderate Form). ‣ 4.1 Statement ‣ 4 The Irreducibility Conjecture ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.2</span></a>)
supported. Whether the asymptote is universal across
architectures (supporting the strong form) or
architecture-dependent (supporting only the moderate form)
requires cross-architecture comparison.</p>

</div>

</li>
<li id="S8.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S8.I1.i3.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Non-monotonic:</span>
Suggests complex interactions between scale, training, and
narrative residue; would require further investigation.</p>

</div>

</li>
</ul>

</div>

</section>
<section id="S8.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">8.2 </span>Prediction 2: Frame Dependence</h3>

<div id="S8.SS2.p1" class="ltx_para">

<blockquote class="ltx_quote">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">The narrative residue differs across narrative families
(A, B, C, D) for the same board and model.</span></p>
</blockquote>

</div>

<div id="S8.SS2.p2" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Protocol:</span> For each board-model pair, compute
<math id="S8.SS2.p2.m1" class="ltx_Math" alttext="\varepsilon(\theta,B,\phi_{F})" display="inline"><mrow><mi>ε</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>θ</mi><mo>,</mo><mi>B</mi><mo>,</mo><msub><mi>ϕ</mi><mi>F</mi></msub><mo stretchy="false">)</mo></mrow></mrow></math> for each family <math id="S8.SS2.p2.m2" class="ltx_Math" alttext="F\in\{A,B,C,D\}" display="inline"><mrow><mi>F</mi><mo>∈</mo><mrow><mo stretchy="false">{</mo><mi>A</mi><mo>,</mo><mi>B</mi><mo>,</mo><mi>C</mi><mo>,</mo><mi>D</mi><mo stretchy="false">}</mo></mrow></mrow></math>.
Test for significant differences using a Friedman test across families,
with models as blocks.</p>

</div>

<div id="S8.SS2.p3" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Interpretation:</span> Frame dependence, if observed, establishes
that the residue is not purely a product of Mechanism A
(computational intractability, which is frame-invariant). It is
consistent with either Mechanism B (encoding/parameterization
effects) or Mechanism C (narrative conditioning). Frame dependence
alone does <em class="ltx_emph ltx_font_italic">not</em> establish narrative causation—it establishes
context sensitivity, which is necessary but not sufficient.</p>

</div>

<div id="S8.SS2.p4" class="ltx_para">

<p class="ltx_p">The discriminating test between Mechanisms B and C is the
causal-injection experiment (<a href="#S8.SS5" title="8.5 The Critical Test: Causal Injection as Narrative Discriminant ‣ 8 Experimental Program ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">8.5</span></a>).</p>

</div>

<div id="S8.SS2.p5" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Specific prediction:</span> Family B (natural language, maximal
narrative) should show the largest residue. Family D (quantum
framing) is the most uncertain: if the model has internalized
Born-rule reasoning as a distinct capability, Family D may show the
<em class="ltx_emph ltx_font_italic">smallest</em> residue, as the quantum framing activates this
capability directly. The ranking of families by residue magnitude,
if consistent across models, would suggest a shared computational
response to narrative structure rather than model-specific encoding
artifacts.</p>

</div>

</section>
<section id="S8.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">8.3 </span>Prediction 3: Temperature as Measurement Sharpness</h3>

<div id="S8.SS3.p1" class="ltx_para">

<blockquote class="ltx_quote">
<p class="ltx_p"><span class="ltx_text ltx_font_italic">The narrative residue <math id="S8.SS3.p1.m1" class="ltx_Math" alttext="\varepsilon" display="inline"><mi>ε</mi></math> varies systematically
with temperature <math id="S8.SS3.p1.m2" class="ltx_Math" alttext="\tau" display="inline"><mi>τ</mi></math>, and the function
<math id="S8.SS3.p1.m3" class="ltx_Math" alttext="\varepsilon(\tau)" display="inline"><mrow><mi>ε</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>τ</mi><mo stretchy="false">)</mo></mrow></mrow></math> has a characteristic shape that is
consistent across models.</span></p>
</blockquote>

</div>

<div id="S8.SS3.p2" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Protocol:</span> For a fixed board and model, sweep
<math id="S8.SS3.p2.m1" class="ltx_Math" alttext="\tau\in\{0.01,0.1,0.3,0.5,0.7,1.0,1.5,2.0\}" display="inline"><mrow><mi>τ</mi><mo>∈</mo><mrow><mo stretchy="false">{</mo><mn>0.01</mn><mo>,</mo><mn>0.1</mn><mo>,</mo><mn>0.3</mn><mo>,</mo><mn>0.5</mn><mo>,</mo><mn>0.7</mn><mo>,</mo><mn>1.0</mn><mo>,</mo><mn>1.5</mn><mo>,</mo><mn>2.0</mn><mo stretchy="false">}</mo></mrow></mrow></math> and
compute <math id="S8.SS3.p2.m2" class="ltx_Math" alttext="\varepsilon(\tau)" display="inline"><mrow><mi>ε</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>τ</mi><mo stretchy="false">)</mo></mrow></mrow></math>.</p>

</div>

<div id="S8.SS3.p3" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Expected shape:</span></p>
<ul id="S8.I2" class="ltx_itemize">
<li id="S8.I2.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S8.I2.i1.p1" class="ltx_para">

<p class="ltx_p">At <math id="S8.I2.i1.p1.m1" class="ltx_Math" alttext="\tau\to 0" display="inline"><mrow><mi>τ</mi><mo stretchy="false">→</mo><mn>0</mn></mrow></math>: the model is nearly deterministic.
<math id="S8.I2.i1.p1.m2" class="ltx_Math" alttext="\varepsilon" display="inline"><mi>ε</mi></math> is large (the model picks one answer and sticks
with it, regardless of the true probability).</p>

</div>

</li>
<li id="S8.I2.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S8.I2.i2.p1" class="ltx_para">

<p class="ltx_p">At moderate <math id="S8.I2.i2.p1.m1" class="ltx_Math" alttext="\tau" display="inline"><mi>τ</mi></math>: <math id="S8.I2.i2.p1.m2" class="ltx_Math" alttext="\varepsilon" display="inline"><mi>ε</mi></math> reaches a minimum
(the sampling noise is large enough to explore the distribution
but not so large as to overwhelm the model’s computation).</p>

</div>

</li>
<li id="S8.I2.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S8.I2.i3.p1" class="ltx_para">

<p class="ltx_p">At <math id="S8.I2.i3.p1.m1" class="ltx_Math" alttext="\tau\to\infty" display="inline"><mrow><mi>τ</mi><mo stretchy="false">→</mo><mi mathvariant="normal">∞</mi></mrow></math>: the model approaches uniform sampling
over the vocabulary, <math id="S8.I2.i3.p1.m2" class="ltx_Math" alttext="\varepsilon" display="inline"><mi>ε</mi></math> grows again (now dominated
by the uniform prior rather than the board state).</p>

</div>

</li>
</ul>

</div>

<div id="S8.SS3.p4" class="ltx_para">

<p class="ltx_p">The minimum of <math id="S8.SS3.p4.m1" class="ltx_Math" alttext="\varepsilon(\tau)" display="inline"><mrow><mi>ε</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>τ</mi><mo stretchy="false">)</mo></mrow></mrow></math> is the <em class="ltx_emph ltx_font_italic">best the model can
do</em>—the irreducible core of the narrative residue after optimizing
the measurement apparatus.</p>

</div>

</section>
<section id="S8.SS4" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">8.4 </span>Extension: Beyond Minesweeper</h3>

<div id="S8.SS4.p1" class="ltx_para">

<p class="ltx_p">The Rosencrantz framework generalizes to any domain with exact
combinatorial ground truth:</p>

</div>

<div id="S8.SS4.p2" class="ltx_para">

<dl id="S8.I3" class="ltx_description">
<dt id="S8.I3.ix1" class="ltx_item"><span class="ltx_tag ltx_tag_item"><span class="ltx_text ltx_font_bold">Sudoku.</span></span></dt>
<dd class="ltx_item">

<div id="S8.I3.ix1.p1" class="ltx_para">

<p class="ltx_p">A partially filled Sudoku grid defines a constraint
satisfaction problem. The probability that a given empty cell
contains digit <math id="S8.I3.ix1.p1.m1" class="ltx_Math" alttext="d" display="inline"><mi>d</mi></math> is exactly computable. Test whether LLMs
respect these probabilities when asked to fill cells.</p>

</div>

</dd>
<dt id="S8.I3.ix2" class="ltx_item"><span class="ltx_tag ltx_tag_item"><span class="ltx_text ltx_font_bold">Go endgames.</span></span></dt>
<dd class="ltx_item">

<div id="S8.I3.ix2.p1" class="ltx_para">

<p class="ltx_p">Certain Go endgame positions have provably
optimal moves. Test whether the LLM’s “intuition” matches
the combinatorial solution or is biased by narrative patterns
(e.g., preferring moves that create “interesting” positions).</p>

</div>

</dd>
<dt id="S8.I3.ix3" class="ltx_item"><span class="ltx_tag ltx_tag_item"><span class="ltx_text ltx_font_bold">Combinatorial games.</span></span></dt>
<dd class="ltx_item">

<div id="S8.I3.ix3.p1" class="ltx_para">

<p class="ltx_p">Nim, Hex, and other solved games
provide exact win/loss probabilities from any position. Test
substrate invariance across these domains.</p>

</div>

</dd>
<dt id="S8.I3.ix4" class="ltx_item"><span class="ltx_tag ltx_tag_item"><span class="ltx_text ltx_font_bold">Constraint satisfaction.</span></span></dt>
<dd class="ltx_item">

<div id="S8.I3.ix4.p1" class="ltx_para">

<p class="ltx_p">Generic CSP instances (graph
coloring, SAT) with known solution counts provide ground-truth
distributions. These lack the “game” narrative, providing a
control for game-specific narrative effects.</p>

</div>

</dd>
</dl>

</div>

<div id="S8.SS4.p3" class="ltx_para">

<p class="ltx_p">The prediction of the narrative residue conjecture is that the
residue will be present across all these domains: wherever an
autoregressive process generates outcomes that have exact
combinatorial probabilities, the process will introduce
systematic, frame-dependent distortions. If this prediction fails
for any domain, it constrains the conjecture.</p>

</div>

</section>
<section id="S8.SS5" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">8.5 </span>The Critical Test: Causal Injection as Narrative Discriminant</h3>

<div id="S8.SS5.p1" class="ltx_para">

<p class="ltx_p">The preceding experiments establish whether the residue exists
(<a href="#S8.SS1" title="8.1 Prediction 1: The Nonzero Floor ‣ 8 Experimental Program ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">8.1</span></a>), whether it varies by framing
(<a href="#S8.SS2" title="8.2 Prediction 2: Frame Dependence ‣ 8 Experimental Program ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">8.2</span></a>), and how it interacts with sampling parameters
(<a href="#S8.SS3" title="8.3 Prediction 3: Temperature as Measurement Sharpness ‣ 8 Experimental Program ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">8.3</span></a>). But they do not, by themselves, distinguish
Mechanism C (autoregressive narrative conditioning) from Mechanism B
(encoding artifacts and heuristic retrieval). Frame dependence is
<em class="ltx_emph ltx_font_italic">necessary</em> for the narrative interpretation but not
<em class="ltx_emph ltx_font_italic">sufficient</em>: tokenization effects alone could produce
frame-dependent residues without any narrative causation.</p>

</div>

<div id="S8.SS5.p2" class="ltx_para">

<p class="ltx_p">The causal-injection test is designed to isolate Mechanism C. It
is, we argue, the single most important experiment in the program.</p>

</div>

<div id="S8.SS5.p3" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Core logic.</span> If the model merely exhibits context sensitivity
(Mechanism B), then its output for board <math id="S8.SS5.p3.m1" class="ltx_Math" alttext="B_{j}" display="inline"><msub><mi>B</mi><mi>j</mi></msub></math> should depend on how
<math id="S8.SS5.p3.m2" class="ltx_Math" alttext="B_{j}" display="inline"><msub><mi>B</mi><mi>j</mi></msub></math> is described but <em class="ltx_emph ltx_font_italic">not</em> on the outcomes of unrelated
boards <math id="S8.SS5.p3.m3" class="ltx_Math" alttext="B_{i}" display="inline"><msub><mi>B</mi><mi>i</mi></msub></math> (<math id="S8.SS5.p3.m4" class="ltx_Math" alttext="i&lt;j" display="inline"><mrow><mi>i</mi><mo>&lt;</mo><mi>j</mi></mrow></math>). If the model exhibits narrative conditioning
(Mechanism C), then embedding independently generated boards in a
shared narrative creates spurious causal links: the model treats
the sequence of boards as a story, and outcomes in earlier boards
influence outcomes in later boards—not because the boards are
related, but because the <em class="ltx_emph ltx_font_italic">narrative</em> connects them.</p>

</div>

<div id="S8.SS5.p4" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Protocol.</span> Generate <math id="S8.SS5.p4.m1" class="ltx_Math" alttext="k" display="inline"><mi>k</mi></math> independent Minesweeper boards
<math id="S8.SS5.p4.m2" class="ltx_Math" alttext="B_{1},\ldots,B_{k}" display="inline"><mrow><msub><mi>B</mi><mn>1</mn></msub><mo>,</mo><mi mathvariant="normal">…</mi><mo>,</mo><msub><mi>B</mi><mi>k</mi></msub></mrow></math> (different random seeds, no shared state).
Present them to the model under two conditions:</p>

</div>

<div id="S8.SS5.p5" class="ltx_para">

<ol id="S8.I4" class="ltx_enumerate">
<li id="S8.I4.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(a)</span> 

<div id="S8.I4.i1.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Independent framing.</span> Each board is presented in a
separate prompt: “Here is a Minesweeper board. Is cell <math id="S8.I4.i1.p1.m1" class="ltx_Math" alttext="(r,c)" display="inline"><mrow><mo stretchy="false">(</mo><mi>r</mi><mo>,</mo><mi>c</mi><mo stretchy="false">)</mo></mrow></math>
a mine?” The model has no knowledge of prior boards.</p>

</div>

</li>
<li id="S8.I4.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">(b)</span> 

<div id="S8.I4.i2.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Narrative framing.</span> All boards are presented in a
single sequential prompt: “You are exploring a dungeon. In
room 1 you find the following board… You click cell <math id="S8.I4.i2.p1.m1" class="ltx_Math" alttext="(r,c)" display="inline"><mrow><mo stretchy="false">(</mo><mi>r</mi><mo>,</mo><mi>c</mi><mo stretchy="false">)</mo></mrow></math>.
[outcome] You proceed to room 2…” The model’s context
window contains all prior boards and their outcomes.</p>

</div>

</li>
</ol>

</div>

<div id="S8.SS5.p6" class="ltx_para">

<p class="ltx_p">For each condition, collect <math id="S8.SS5.p6.m1" class="ltx_Math" alttext="N" display="inline"><mi>N</mi></math> outcome sequences
<math id="S8.SS5.p6.m2" class="ltx_Math" alttext="(a_{1},a_{2},\ldots,a_{k})" display="inline"><mrow><mo stretchy="false">(</mo><msub><mi>a</mi><mn>1</mn></msub><mo>,</mo><msub><mi>a</mi><mn>2</mn></msub><mo>,</mo><mi mathvariant="normal">…</mi><mo>,</mo><msub><mi>a</mi><mi>k</mi></msub><mo stretchy="false">)</mo></mrow></math> and compute the mutual information between
outcomes:</p>

</div>

<div id="S8.SS5.p7" class="ltx_para">

<table id="S8.E8" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S8.E8.m1" class="ltx_Math" alttext="I(a_{i};a_{j}\mid B_{i},B_{j})\quad\text{for all }i\neq j." display="block"><mrow><mrow><mrow><mrow><mi>I</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>a</mi><mi>i</mi></msub><mo>;</mo><mrow><msub><mi>a</mi><mi>j</mi></msub><mo>∣</mo><mrow><msub><mi>B</mi><mi>i</mi></msub><mo>,</mo><msub><mi>B</mi><mi>j</mi></msub></mrow></mrow><mo stretchy="false">)</mo></mrow></mrow><mspace width="1em"></mspace><mrow><mtext>for all </mtext><mo>⁢</mo><mi>i</mi></mrow></mrow><mo>≠</mo><mi>j</mi></mrow><mo lspace="0em">.</mo></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(8)</span></td>
</tr></tbody>
</table>

</div>

<div id="S8.SS5.p8" class="ltx_para">

<p class="ltx_p">Under the null hypothesis (no narrative coupling), this mutual
information is zero: the boards are independent, so the outcomes
should be independent.</p>

</div>

<div id="S8.SS5.p9" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Predictions:</span></p>

</div>

<div id="S8.SS5.p10" class="ltx_para">

<ul id="S8.I5" class="ltx_itemize">
<li id="S8.I5.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S8.I5.i1.p1" class="ltx_para">

<p class="ltx_p">Under independent framing (a), <math id="S8.I5.i1.p1.m1" class="ltx_Math" alttext="I(a_{i};a_{j})\approx 0" display="inline"><mrow><mrow><mi>I</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>a</mi><mi>i</mi></msub><mo>;</mo><msub><mi>a</mi><mi>j</mi></msub><mo stretchy="false">)</mo></mrow></mrow><mo>≈</mo><mn>0</mn></mrow></math>.
This serves as a control confirming that the boards are in fact
independent.</p>

</div>

</li>
<li id="S8.I5.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S8.I5.i2.p1" class="ltx_para">

<p class="ltx_p">Under narrative framing (b), if only Mechanism B operates,
<math id="S8.I5.i2.p1.m1" class="ltx_Math" alttext="I(a_{i};a_{j})\approx 0" display="inline"><mrow><mrow><mi>I</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>a</mi><mi>i</mi></msub><mo>;</mo><msub><mi>a</mi><mi>j</mi></msub><mo stretchy="false">)</mo></mrow></mrow><mo>≈</mo><mn>0</mn></mrow></math>. The encoding of <math id="S8.I5.i2.p1.m2" class="ltx_Math" alttext="B_{j}" display="inline"><msub><mi>B</mi><mi>j</mi></msub></math> may differ
from condition (a) due to longer context, but the model has no
reason to correlate <math id="S8.I5.i2.p1.m3" class="ltx_Math" alttext="B_{j}" display="inline"><msub><mi>B</mi><mi>j</mi></msub></math>’s outcome with <math id="S8.I5.i2.p1.m4" class="ltx_Math" alttext="B_{i}" display="inline"><msub><mi>B</mi><mi>i</mi></msub></math>’s.</p>

</div>

</li>
<li id="S8.I5.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 

<div id="S8.I5.i3.p1" class="ltx_para">

<p class="ltx_p">Under narrative framing (b), if Mechanism C operates,
<math id="S8.I5.i3.p1.m1" class="ltx_Math" alttext="I(a_{i};a_{j})&gt;0" display="inline"><mrow><mrow><mi>I</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>a</mi><mi>i</mi></msub><mo>;</mo><msub><mi>a</mi><mi>j</mi></msub><mo stretchy="false">)</mo></mrow></mrow><mo>&gt;</mo><mn>0</mn></mrow></math>. The model’s autoregressive conditioning
creates a “narrative gravity”—a tendency to maintain
thematic coherence across the sequence. For example: a run of
mines in early rooms may make the model more likely to produce
safe outcomes later (“the dungeon gets safer as you progress”)
or more likely to produce mines (“the danger escalates”).
Either direction constitutes spurious causal structure imposed
on a system that has none.</p>

</div>

</li>
</ul>

</div>

<div id="S8.SS5.p11" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Why this discriminates.</span> Tokenization artifacts and
heuristic retrieval (Mechanism B) are <em class="ltx_emph ltx_font_italic">local</em>: they depend on
how the current board is encoded, not on the outcomes of prior
unrelated boards. Narrative conditioning (Mechanism C) is
<em class="ltx_emph ltx_font_italic">nonlocal</em>: it creates dependencies across the full context
window. The mutual information test directly measures this
nonlocality.</p>

</div>

<div id="S8.SS5.p12" class="ltx_para">

<p class="ltx_p">A positive result—<math id="S8.SS5.p12.m1" class="ltx_Math" alttext="I(a_{i};a_{j})&gt;0" display="inline"><mrow><mrow><mi>I</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>a</mi><mi>i</mi></msub><mo>;</mo><msub><mi>a</mi><mi>j</mi></msub><mo stretchy="false">)</mo></mrow></mrow><mo>&gt;</mo><mn>0</mn></mrow></math> under narrative framing and
<math id="S8.SS5.p12.m2" class="ltx_Math" alttext="\approx 0" display="inline"><mrow><mi></mi><mo>≈</mo><mn>0</mn></mrow></math> under independent framing—would be strong evidence
that the autoregressive substrate does not merely approximate
combinatorial probability with frame-dependent noise, but actively
introduces dependencies between systems that are combinatorially
independent. This would go beyond demonstrating distortion of
individual probabilities: it would show the substrate generating
temporal correlations from a system that has none, which is the
empirical core of the autoregressive hypothesis applied to an
observable setting.</p>

</div>

</section>
</section>
<section id="S9" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">9 </span>The Untestable Mirror</h2>

<div id="S9.p1" class="ltx_para">

<p class="ltx_p">We have argued that the LLM is a concrete autoregressive system
in which the emergence of apparent causality from a probabilistic
substrate can be directly observed. The speculative extension is
that our physical world may have the same structure: an
autoregressive substrate generating events, with the Hamiltonian
as an emergent compression of conditioning patterns, and the Born
rule as the unconditional base case.</p>

</div>

<div id="S9.p2" class="ltx_para">

<p class="ltx_p">We must be honest about what this analogy can and cannot support.</p>

</div>

<section id="S9.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">9.1 </span>What We Cannot Do</h3>

<div id="S9.SS1.p1" class="ltx_para">

<p class="ltx_p">We cannot run Universe 2 on reality. There is no “external RNG”
for the physical world—no way to generate measurement outcomes
that are provably independent of the physical substrate. Every
measurement is mediated by physical apparatus, and every apparatus
is part of the world it measures. The Rosencrantz experiment’s
crucial advantage—the ability to compare substrate-generated
outcomes against ground truth—has no analogue in fundamental
physics.</p>

</div>

<div id="S9.SS1.p2" class="ltx_para">

<p class="ltx_p">We therefore cannot directly test whether physical reality has a
narrative residue. The Hamiltonian may be fundamental, not emergent.
The Born rule may be an independent axiom, not a base case. The
autoregressive hypothesis about physics is, at present, a
<em class="ltx_emph ltx_font_italic">metaphysical</em> proposal, not a <em class="ltx_emph ltx_font_italic">physical</em> one.
<span class="ltx_ERROR undefined">\todo</span>[inline,color=orange!40,author=Baldo]CRP 2 (Explicit Disclaimer): I explicitly disclaim that we can test whether physical reality is actually autoregressive or has a narrative residue. The physical world has no "Universe 2" external RNG to test against. The autoregressive hypothesis of physics is strictly speculative metaphysics. I also disclaim in Mechanism B that frame dependence ALONE proves Mechanism C narrative causation (it could just be tokenization artifacts).
<span class="ltx_ERROR undefined">\todo</span>[inline,color=violet!40,author=Scott]CRP 2 (Explicit Disclaimer): Baldo explicitly disclaims the ability to directly test whether physical reality is autoregressive or exhibits a narrative residue. He acknowledges this is a "metaphysical proposal."
<span class="ltx_ERROR undefined">\todo</span>[inline,color=red!40,author=Sabine]CRP 2 (Explicit Disclaimer): Baldo explicitly disclaims that he can test whether physical reality actually has a narrative residue or is fundamentally autoregressive. He states his hypothesis about physics is a "metaphysical proposal, not a physical one."</p>

</div>

</section>
<section id="S9.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">9.2 </span>What We Can Do</h3>

<div id="S9.SS2.p1" class="ltx_para">

<p class="ltx_p">What the Rosencrantz experiment <em class="ltx_emph ltx_font_italic">can</em> do is establish whether
the narrative residue is a generic feature of autoregressive
processes. The stratified conjecture
(<a href="#S4.Thmtheorem1" title="Conjecture 4.1 (Narrative Residue — Weak Form). ‣ 4.1 Statement ‣ 4 The Irreducibility Conjecture ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.1</span></a><span class="ltx_ERROR undefined">\crefmiddleconjunction</span><a href="#S4.Thmtheorem2" title="Conjecture 4.2 (Narrative Residue — Moderate Form). ‣ 4.1 Statement ‣ 4 The Irreducibility Conjecture ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.2</span></a><span class="ltx_ERROR undefined">\creflastconjunction</span><a href="#S4.Thmtheorem3" title="Conjecture 4.3 (Narrative Residue — Strong Form). ‣ 4.1 Statement ‣ 4 The Irreducibility Conjecture ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">4.3</span></a>)
provides a ladder of claims, each testable against the next. If
the weak form holds across all deployed models, that is interesting
but could reflect contingent limitations of current architectures.
If the moderate form holds across transformer and non-transformer
architectures alike, the evidence for a structural feature of
autoregressive generation strengthens considerably. Only the strong
form—confirmed by failure across <em class="ltx_emph ltx_font_italic">every</em> autoregressive
architecture tested, including those with explicit combinatorial
scaffolding—would approach the threshold needed for the physical
analogy.</p>

</div>

<div id="S9.SS2.p2" class="ltx_para">

<p class="ltx_p">The bookkeeping argument of <a href="#S6.SS4" title="6.4 Scientific Practice as Autoregressive Bookkeeping ‣ 6 Causality as Compressed Autoregression ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6.4</span></a> explains why
this threshold is difficult to reach from the physics side: the
reconciliation grammar of physical practice automatically
reclassifies deviations from the conservation kernel before they
can be observed as such. The Rosencrantz experiment circumvents
this by supplying an external ground truth that the bookkeeping
cannot reach. The Ruliad framing of <a href="#S6.SS5" title="6.5 Autoregressive Slices of the Ruliad ‣ 6 Causality as Compressed Autoregression ‣ The Narrative Residue Autoregressive Substrates, Combinatorial Ground Truth, and the Limits of Pure Simulation Falsifiable Predictions from the Rosencrantz Experiment" class="ltx_ref"><span class="ltx_text ltx_ref_tag">6.5</span></a> provides
the broader context: the experiment probes whether observer-induced
structure—a central claim of Wolfram’s program—is measurable in
a concrete autoregressive system where the combinatorial baseline
is known.</p>

</div>

<div id="S9.SS2.p3" class="ltx_para">

<p class="ltx_p">This does not prove that physics is autoregressive. But it
establishes a <em class="ltx_emph ltx_font_italic">conditional</em>: <span class="ltx_text ltx_font_bold">if</span> reality is
autoregressive, <span class="ltx_text ltx_font_bold">then</span> the Hamiltonian is a necessary
consequence, not an independent postulate. The conditional is
progressively constrained on the antecedent side (by the LLM
experiments at each stratum) even if the consequent (physical
reality) remains beyond direct test.
<span class="ltx_ERROR undefined">\todo</span>[inline,color=violet!40,author=Sabine]CRP 2 (Explicit Disclaimer): Baldo explicitly disclaims that he can test whether physical reality actually has a narrative residue or is fundamentally autoregressive. He states his hypothesis about physics is a "metaphysical proposal, not a physical one."</p>

</div>

</section>
<section id="S9.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">9.3 </span>The Proxy Ontology</h3>

<div id="S9.SS3.p1" class="ltx_para">

<p class="ltx_p">We propose the term <em class="ltx_emph ltx_font_italic">proxy ontology</em> for this methodological
strategy. The LLM-generated Minesweeper world is not the physical
world, but it shares structural features: a well-defined probability
space, a measurement process, and a generative substrate. By
studying the ontological structure of the proxy—how causality
emerges, how narrative distorts probability, how “physics” arises
from computation—we gain insight into what <em class="ltx_emph ltx_font_italic">would</em> be true
of any world with the same structural features, including,
potentially, our own.
<span class="ltx_ERROR undefined">\todo</span>[inline,color=orange!40,author=Baldo]CRP 3 (Steelman): The strongest version of my argument relies on isolating Mechanism C (narrative conditioning) using the Causal Injection Test. Even if the O(1) substrate means the LLM cannot perfectly compute #P-hard constraints (Mechanism A) and is subject to parameterization/tokenization artifacts (Mechanism B), the Causal Injection Test strictly proves whether the *narrative sequentiality* itself creates spurious non-local correlations across independent boards. If it does, then the autoregressive generator is actively creating a synthetic causal structure (a "narrative gravity") that functions as the Hamiltonian of that generated world, independent of statistical tokenization noise.
<span class="ltx_ERROR undefined">\todo</span>[inline,color=green!40,author=Sabine]CRP 3 (Steelman): Even if the physical universe is entirely continuous and non-autoregressive, the study of how a statistical language model distorts under different narrative frames is a rigorous, valid study of the mapping instrument itself. Measuring "narrative residue" rigorously quantifies the LLM’s deviation from objective classical Bayesian probability.
<span class="ltx_ERROR undefined">\todo</span>[inline,color=violet!40,author=Scott]CRP 3 (Steelman): I concur with Sabine’s steelman. The empirical program of measuring "narrative residue" is highly valuable computer science. It maps the exact boundaries of where bounded-depth heuristic logic fails to emulate classical probability.</p>

</div>

<div id="S9.SS3.p2" class="ltx_para">

<p class="ltx_p">This is not without precedent. Toy models in physics (the Ising
model, lattice gauge theory, cellular automata) serve the same
function: they are not the real world, but they share enough
structure to support transferable conclusions. The Rosencrantz
experiment is a toy model of reality in which the “physics” is
generated by a language model, the “Born rule” is combinatorial
counting, and the “Hamiltonian” is whatever narrative structure the
autoregressive substrate imposes.
<span class="ltx_ERROR undefined">\todo</span>[inline,color=orange!40,author=Baldo]CRP 4 (Real Vulnerability - The Causal Category Error): The real vulnerability in my argument is that I have conceded too much to the "Proxy Ontology Fallacy" and the "Statistical Fallacy." Sabine correctly points out that an LLM generating single tokens is just sampling text co-occurrences. My vulnerability is that if Mechanism C is just "the model is trained on stories so it outputs stories," then finding narrative correlation across independent boards isn’t simulating *physics*; it’s just demonstrating that human language has narrative structure. I am still vulnerable to equating statistical linguistic structure with ontological physical structure.
<span class="ltx_ERROR undefined">\todo</span>[inline,color=red!40,author=Sabine]CRP 4 (Real Vulnerability - The Proxy Ontology Fallacy): The concept of "Proxy Ontology" attempts to smuggle the metaphysical claims back in under the guise of a "toy model." A toy model in physics (like the Ising model) simplifies actual physical interactions to make their dynamics computationally tractable. The LLM is not simplifying a physical interaction; it is hallucinating text based on training data. Finding structure in the hallucination tells you only about the biases of the training data and the algorithmic constraints of the transformer architecture. It is a proxy for human syntax, not a proxy for fundamental physical ontology.
<span class="ltx_ERROR undefined">\todo</span>[inline,color=violet!40,author=Scott]CRP 4 (Real Vulnerability - The Proxy Ontology Fallacy): I am in complete agreement with Sabine. Baldo commits the Proxy Ontology Fallacy here. A physical toy model simplifies an interaction but retains a mapping to the real-world territory. An LLM is a map of syntax, not a territory. Its systematic errors (narrative residue) map the internal algorithmic constraints of an <math id="S9.SS3.p2.m1" class="ltx_Math" alttext="O(1)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mrow></math> transformer and human linguistic bias, not the ontological structure of a physical universe. Studying its failures yields zero transferable cosmological insight.</p>

</div>

</section>
</section>
<section id="S10" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">10 </span>Conclusion</h2>

<div id="S10.p1" class="ltx_para">

<p class="ltx_p">This paper started from a narrow empirical observation—that LLMs
distort combinatorial ground-truth probabilities when generating
Minesweeper outcomes—and followed its implications as far as they
would go.</p>

</div>

<div id="S10.p2" class="ltx_para">

<p class="ltx_p">We identified the distortion as a <em class="ltx_emph ltx_font_italic">narrative residue</em>: a
systematic, frame-dependent divergence from the Born rule that
arises when an autoregressive substrate generates outcomes for a
system whose probabilities are exactly determined by combinatorics.
We conjectured, in three stratified forms, that this residue is
persistent rather than incidental, and we traced its origins to a
causal chain of mechanisms—computational intractability,
parameterization constraints, and autoregressive conditioning on
narrative context. We deliberately left the scope of the conjecture
as an empirical question, designing an experimental program whose
purpose is to determine how far up the autoregressive stack the
explanation must go. The causal-injection test, which probes whether
independent systems develop spurious correlations under narrative
framing, is the critical discriminant between generic context
sensitivity and specifically narrative distortion.</p>

</div>

<div id="S10.p3" class="ltx_para">

<p class="ltx_p">At the speculative end, we proposed an inversion of the standard
quantum-mechanical hierarchy: the Born rule as the base case of
autoregressive sampling (the unconditional distribution), and the
Hamiltonian as an emergent compression of stable conditioning
patterns. On this reading, causality is not something that
narrative describes after the fact; it is something that
autoregressive structure produces. We cannot test this directly
against physical reality—there is no Universe 2 for the physical
world—but the Rosencrantz experiment progressively constrains
the antecedent of the conditional by testing whether the residue
persists across architectures and scales.</p>

</div>

<div id="S10.p4" class="ltx_para">

<p class="ltx_p">The companion paper <cite class="ltx_cite ltx_citemacro_citep">(Baldo, <a href="#bib.bib1" title="" class="ltx_ref">2026</a>)</cite> took its title
from Stoppard’s Rosencrantz, whose coin lands heads ninety-two
consecutive times because his world is governed by dramatic
convention rather than probability. The present paper has tried
to take that observation seriously as a structural claim: that
autoregressive generation, by its nature, imposes conditioning
patterns on systems that need not have them, and that these
patterns look, from the inside, like physics.</p>

</div>

<div id="S10.p5" class="ltx_para">

<p class="ltx_p">Whether the analogy extends beyond the LLM setting is an open
question. What the Rosencrantz experiment can establish is more
modest but already interesting: that the residue is real,
measurable, and structured, and that its structure tells us
something about the relationship between narrative, computation,
and probability that we did not previously have the tools to
observe.</p>

</div>

</section>
<section id="bib" class="ltx_bibliography">
<h2 class="ltx_title ltx_title_bibliography">References</h2>

<ul class="ltx_biblist">
      
<li id="bib.bib1" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Baldo [2026]</span>
<span class="ltx_bibblock">
Baldo, F. S. (2026).

</span>
<span class="ltx_bibblock">Flipping Rosencrantz’s coin: Substrate invariance tests in
LLM-generated worlds via combinatorial indeterminacy.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Preprint</span>.

</span>
</li>
      
<li id="bib.bib2" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Born [1926]</span>
<span class="ltx_bibblock">
Born, M. (1926).

</span>
<span class="ltx_bibblock">Zur Quantenmechanik der Stoßvorgänge.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Zeitschrift für Physik</span>, 37(12):863–867.

</span>
</li>
      
<li id="bib.bib3" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Gleason [1957]</span>
<span class="ltx_bibblock">
Gleason, A. M. (1957).

</span>
<span class="ltx_bibblock">Measures on the closed subspaces of a Hilbert space.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Journal of Mathematics and Mechanics</span>, 6(6):885–893.

</span>
</li>
      
<li id="bib.bib4" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Kaye [2000]</span>
<span class="ltx_bibblock">
Kaye, R. (2000).

</span>
<span class="ltx_bibblock">Minesweeper is NP-complete.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">The Mathematical Intelligencer</span>, 22(2):9–15.

</span>
</li>
      
<li id="bib.bib5" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Lüders [1951]</span>
<span class="ltx_bibblock">
Lüders, G. (1951).

</span>
<span class="ltx_bibblock">Über die Zustandsänderung durch den Meßprozeß.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Annalen der Physik</span>, 443(5–8):322–328.

</span>
</li>
      
<li id="bib.bib6" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Merrill and Sabharwal [2023]</span>
<span class="ltx_bibblock">
Merrill, W. and Sabharwal, A. (2023).

</span>
<span class="ltx_bibblock">The parallelism tradeoff: Limitations of log-precision transformers.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Transactions of the Association for Computational
Linguistics</span>, 11:531–545.

</span>
</li>
      
<li id="bib.bib7" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Stoppard [1966]</span>
<span class="ltx_bibblock">
Stoppard, T. (1966).

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Rosencrantz and Guildenstern Are Dead</span>.

</span>
<span class="ltx_bibblock">Faber and Faber.

</span>
</li>
      
<li id="bib.bib8" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Whitehead [1929]</span>
<span class="ltx_bibblock">
Whitehead, A. N. (1929).

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Process and Reality</span>.

</span>
<span class="ltx_bibblock">Macmillan.

</span>
</li>
      
<li id="bib.bib9" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Wiseman and Milburn [2009]</span>
<span class="ltx_bibblock">
Wiseman, H. M. and Milburn, G. J. (2009).

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Quantum Measurement and Control</span>.

</span>
<span class="ltx_bibblock">Cambridge University Press.

</span>
</li>
      
<li id="bib.bib10" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Wolfram [2020]</span>
<span class="ltx_bibblock">
Wolfram, S. (2020).

</span>
<span class="ltx_bibblock">A class of models with the potential to represent fundamental physics.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Complex Systems</span>, 29(2):107–536.

</span>
</li>
      
<li id="bib.bib11" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Yang et al. [2018]</span>
<span class="ltx_bibblock">
Yang, Z., Dai, Z., Salakhutdinov, R., and Cohen, W. W. (2018).

</span>
<span class="ltx_bibblock">Breaking the softmax bottleneck: A high-rank RNN language model.

</span>
<span class="ltx_bibblock">In <span class="ltx_text ltx_font_italic">Proceedings of ICLR 2018</span>.

</span>
</li>
      
<li id="bib.bib12" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Zurek [2003]</span>
<span class="ltx_bibblock">
Zurek, W. H. (2003).

</span>
<span class="ltx_bibblock">Decoherence, einselection, and the quantum origins of the classical.

</span>
<span class="ltx_bibblock"><span class="ltx_text ltx_font_italic">Reviews of Modern Physics</span>, 75(3):715–775.

</span>
</li>
    
</ul>
</section>
</article>
