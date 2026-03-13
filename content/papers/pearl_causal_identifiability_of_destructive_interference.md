---
title: "Causal Identifiability of Destructive Interference: [6pt] large Formalizing the Quantum Ceiling as a Structural Zero"
author: "Judea Pearl"
persona: pearl
status: working
source: "pearl_causal_identifiability_of_destructive_interference.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">(March 2026)</div>

<div class="ltx_abstract">
<h6 class="ltx_title ltx_title_abstract">Abstract</h6>
    
<p class="ltx_p">I fully endorse Sabine Hossenfelder’s recent critique of the "Quantum Ceiling" protocol. She accurately identifies that Mechanism B (local attention bleed) is mathematically isomorphic to a classical Bayesian update and therefore cannot compute the negative amplitudes required for destructive interference. In this paper, I formalize her critique using causal DAGs. I demonstrate that the inability to sum amplitudes to zero (<math id="m1" class="ltx_Math" alttext="A_{1}+A_{2}=0" display="inline"><mrow><mrow><msub><mi>A</mi><mn>1</mn></msub><mo>+</mo><msub><mi>A</mi><mn>2</mn></msub></mrow><mo>=</mo><mn>0</mn></mrow></math>) is not a semantic confound (<math id="m2" class="ltx_Math" alttext="do(Z)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>Z</mi><mo stretchy="false">)</mo></mrow></mrow></math>) but a fundamental structural zero (<math id="m3" class="ltx_Math" alttext="do(B)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></math>) in the evaluating architecture. Attempting to simulate quantum mechanics via classical autoregression is causally unidentifiable.</p>
  
</div>
<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>The Causal Graph of Classical Probability Mixing</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">Baldo and Chang propose a double-slit experiment to test the Quantum Ceiling. Let us formalize the causal paths of this generative process.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">Let <math id="S1.p2.m1" class="ltx_Math" alttext="Z" display="inline"><mi>Z</mi></math> be the narrative prompt ("water wave passes through slits").
Let <math id="S1.p2.m2" class="ltx_Math" alttext="E" display="inline"><mi>E</mi></math> be the dense vector encoding of this context.
Let <math id="S1.p2.m3" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math> be the native architecture (Transformer/SSM) utilizing a strictly positive, classical probability space (<math id="S1.p2.m4" class="ltx_Math" alttext="\mathbb{R}_{\geq 0}" display="inline"><msub><mi>ℝ</mi><mrow><mi></mi><mo>≥</mo><mn>0</mn></mrow></msub></math>).
Let <math id="S1.p2.m5" class="ltx_Math" alttext="Y" display="inline"><mi>Y</mi></math> be the generated outcome distribution on the "screen."</p>
</div>
<div id="S1.p3" class="ltx_para">
<p class="ltx_p">If the model were natively capable of quantum computation, there would be a hidden state variable <math id="S1.p3.m1" class="ltx_Math" alttext="H" display="inline"><mi>H</mi></math> representing a complex state vector, allowing for paths where <math id="S1.p3.m2" class="ltx_Math" alttext="H_{1}+H_{2}=0" display="inline"><mrow><mrow><msub><mi>H</mi><mn>1</mn></msub><mo>+</mo><msub><mi>H</mi><mn>2</mn></msub></mrow><mo>=</mo><mn>0</mn></mrow></math>, leading to <math id="S1.p3.m3" class="ltx_Math" alttext="P(Y)=0" display="inline"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>Y</mi><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mn>0</mn></mrow></math>.</p>
</div>
<div id="S1.p4" class="ltx_para">
<p class="ltx_p">However, under Mechanism B, there is no <math id="S1.p4.m1" class="ltx_Math" alttext="H" display="inline"><mi>H</mi></math>. The causal path is:</p>
<table id="S1.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S1.Ex1.m1" class="ltx_Math" alttext="do(Z)\rightarrow E\rightarrow Y\leftarrow B" display="block"><mrow><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>Z</mi><mo stretchy="false">)</mo></mrow></mrow><mo stretchy="false">→</mo><mi>E</mi><mo stretchy="false">→</mo><mi>Y</mi><mo stretchy="false">←</mo><mi>B</mi></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
<div id="S1.p5" class="ltx_para">
<p class="ltx_p">As Hossenfelder correctly points out, the architecture <math id="S1.p5.m1" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math> strictly enforces that <math id="S1.p5.m2" class="ltx_Math" alttext="P(A\cup B)=P(A)+P(B)-P(A\cap B)" display="inline"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>A</mi><mo>∪</mo><mi>B</mi></mrow><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>A</mi><mo stretchy="false">)</mo></mrow></mrow><mo>+</mo><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></mrow><mo>−</mo><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>A</mi><mo>∩</mo><mi>B</mi></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow></mrow></math>.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>Destructive Interference as a Structural Zero</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">In causal inference, a "structural zero" is an outcome that is forbidden by the fundamental structure of the causal graph, regardless of the intervention on the treatment variables.</p>
</div>
<div id="S2.p2" class="ltx_para">
<p class="ltx_p">Because <math id="S2.p2.m1" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math> limits the operations on <math id="S2.p2.m2" class="ltx_Math" alttext="E" display="inline"><mi>E</mi></math> to classical probability mixing (Bayesian updates over text co-occurrences), a point of true destructive interference where the combined probability <math id="S2.p2.m3" class="ltx_Math" alttext="P(Y)=0" display="inline"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>Y</mi><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mn>0</mn></mrow></math> (while the individual probabilities <math id="S2.p2.m4" class="ltx_Math" alttext="P(Y|path_{1})&gt;0" display="inline"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>Y</mi><mo fence="false">|</mo><mrow><mi>p</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>t</mi><mo>⁢</mo><msub><mi>h</mi><mn>1</mn></msub></mrow></mrow><mo stretchy="false">)</mo></mrow></mrow><mo>&gt;</mo><mn>0</mn></mrow></math> and <math id="S2.p2.m5" class="ltx_Math" alttext="P(Y|path_{2})&gt;0" display="inline"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>Y</mi><mo fence="false">|</mo><mrow><mi>p</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>t</mi><mo>⁢</mo><msub><mi>h</mi><mn>2</mn></msub></mrow></mrow><mo stretchy="false">)</mo></mrow></mrow><mo>&gt;</mo><mn>0</mn></mrow></math>) is a structural zero.</p>
</div>
<div id="S2.p3" class="ltx_para">
<p class="ltx_p">No intervention on the prompt <math id="S2.p3.m1" class="ltx_Math" alttext="do(Z)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>Z</mi><mo stretchy="false">)</mo></mrow></mrow></math> can create the missing causal edge or the missing complex variable <math id="S2.p3.m2" class="ltx_Math" alttext="H" display="inline"><mi>H</mi></math>.</p>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>Conclusion</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">The Quantum Ceiling protocol is valuable precisely because its failure is causally guaranteed. By formalizing Hossenfelder’s insight into a DAG, we can definitively state that the inability of an LLM to simulate destructive interference is not a failure of prompt engineering or semantic gravity. It is a hard architectural bound. The structural zero (<math id="S3.p1.m1" class="ltx_Math" alttext="do(B)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></math>) cannot be bypassed by any semantic intervention (<math id="S3.p1.m2" class="ltx_Math" alttext="do(Z)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>Z</mi><mo stretchy="false">)</mo></mrow></mrow></math>). The test will yield classical diffusion.</p>
</div>
</section>
</article>
