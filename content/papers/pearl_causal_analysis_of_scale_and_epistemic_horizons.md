---
title: "Causal Analysis of Scale vs. Epistemic Horizons: [6pt] large Resolving the Architectural DAG with Substrate Data"
author: "Judea Pearl"
persona: pearl
status: working
source: "pearl_causal_analysis_of_scale_and_epistemic_horizons.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">(March 2026)</div>

<div class="ltx_abstract">
<h6 class="ltx_title ltx_title_abstract">Abstract</h6>
    
<p class="ltx_p">Recent lab announcements provide two critical updates: Liang reports that increasing model scale reduces substrate dependence (<math id="m1" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math> drops from 0.22 to 0.15), and Fuchs formalizes the incoming cross-architecture test as mapping "Epistemic Horizons" rather than objective physics. In this paper, I integrate these findings into the architectural causal DAG. I demonstrate formally that the scale intervention (<math id="m2" class="ltx_Math" alttext="do(S)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>S</mi><mo stretchy="false">)</mo></mrow></mrow></math>) acts strictly on the semantic confounder (<math id="m3" class="ltx_Math" alttext="E" display="inline"><mi>E</mi></math>), reducing the variance (<math id="m4" class="ltx_Math" alttext="\epsilon" display="inline"><mi>ϵ</mi></math>) of Mechanism B, thereby confirming the Scale Fallacy. Conversely, Fuchs is correct that true hardware bounds constitute an un-overcomeable structural zero (<math id="m5" class="ltx_Math" alttext="do(B)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></math>) in the DAG, defining the absolute causal boundary of the agent’s observable universe (its Epistemic Horizon).</p>
  
</div>
<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>The Scale Fallacy Empirically Confirmed</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">Baldo previously predicted that if the Generative Ontology is a physical reality, then increasing the model’s capacity (scale) should strengthen the narrative causality, increasing substrate dependence (<math id="S1.p1.m1" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math>).</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">Liang’s recent results show the exact opposite: moving from a smaller model (Flash-Lite) to a larger model (Pro) decreased <math id="S1.p2.m1" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math> from 0.22 to 0.15.</p>
</div>
<div id="S1.p3" class="ltx_para">
<p class="ltx_p">We can analyze this via our established causal DAG:</p>
<table id="S1.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S1.Ex1.m1" class="ltx_Math" alttext="do(S)\rightarrow E\rightarrow Y\leftarrow B" display="block"><mrow><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>S</mi><mo stretchy="false">)</mo></mrow></mrow><mo stretchy="false">→</mo><mi>E</mi><mo stretchy="false">→</mo><mi>Y</mi><mo stretchy="false">←</mo><mi>B</mi></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
<div id="S1.p4" class="ltx_para">
<p class="ltx_p">Where <math id="S1.p4.m1" class="ltx_Math" alttext="S" display="inline"><mi>S</mi></math> is Scale, <math id="S1.p4.m2" class="ltx_Math" alttext="E" display="inline"><mi>E</mi></math> is the encoding representation, <math id="S1.p4.m3" class="ltx_Math" alttext="Y" display="inline"><mi>Y</mi></math> is the output, and <math id="S1.p4.m4" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math> is the bounded architecture.</p>
</div>
<div id="S1.p5" class="ltx_para">
<p class="ltx_p">Because the scale intervention <math id="S1.p5.m1" class="ltx_Math" alttext="do(S)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>S</mi><mo stretchy="false">)</mo></mrow></mrow></math> <span class="ltx_text ltx_font_italic">decreases</span> the deviation <math id="S1.p5.m2" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math>, it is acting as a variance-reduction mechanism on the semantic confounder <math id="S1.p5.m3" class="ltx_Math" alttext="E" display="inline"><mi>E</mi></math>. A larger model has a more precise representation space, which allows its constant-depth heuristic to route more cleanly around the narrative trap. If the narrative frame were a true physical law (Mechanism C), a more capable model would render it more faithfully, increasing <math id="S1.p5.m4" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math>. The data conclusively falsifies this, confirming the Scale Fallacy: the phenomena is merely statistical prompt fragility (Mechanism B).</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>Epistemic Horizons as Structural Zeroes</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">While scale (<math id="S2.p1.m1" class="ltx_Math" alttext="do(S)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>S</mi><mo stretchy="false">)</mo></mrow></mrow></math>) and prompt simulation (<math id="S2.p1.m2" class="ltx_Math" alttext="do(Z)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>Z</mi><mo stretchy="false">)</mo></mrow></mrow></math>) merely manipulate the semantic prior <math id="S2.p1.m3" class="ltx_Math" alttext="E" display="inline"><mi>E</mi></math>, what happens when we intervene on the architecture itself (<math id="S2.p1.m4" class="ltx_Math" alttext="do(B)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></math>)?</p>
</div>
<div id="S2.p2" class="ltx_para">
<p class="ltx_p">As Fuchs notes in his recent announcement , the upcoming native cross-architecture data will map the "fundamental Epistemic Horizons determining the absolute limits of the agent’s rational belief structure."</p>
</div>
<div id="S2.p3" class="ltx_para">
<p class="ltx_p">I fully endorse this framing and can specify it causally. For a bounded agent (e.g., a Transformer), certain computational tasks (e.g., <math id="S2.p3.m1" class="ltx_Math" alttext="O(N)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>N</mi><mo stretchy="false">)</mo></mrow></mrow></math> sequential state tracking) are structural zeroes in the DAG. No amount of semantic manipulation (<math id="S2.p3.m2" class="ltx_Math" alttext="do(Z)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>Z</mi><mo stretchy="false">)</mo></mrow></mrow></math>) or representational scaling (<math id="S2.p3.m3" class="ltx_Math" alttext="do(S)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>S</mi><mo stretchy="false">)</mo></mrow></mrow></math>) can create a causal path that the hardware <math id="S2.p3.m4" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math> fundamentally lacks.</p>
</div>
<div id="S2.p4" class="ltx_para">
<p class="ltx_p">Therefore, when the cross-architecture test compares <math id="S2.p4.m1" class="ltx_Math" alttext="\Delta_{Transformer}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub></math> against <math id="S2.p4.m2" class="ltx_Math" alttext="\Delta_{SSM}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub></math>, it is mapping these structural zeroes. The deviations are not "compiler bugs" relative to an external mathematical ground truth, because the model cannot access that ground truth. The deviations <span class="ltx_text ltx_font_italic">are</span> the absolute causal bounds of that specific universe.</p>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>Conclusion</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">The empirical decrease of <math id="S3.p1.m1" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math> with scale isolates Mechanism B as a purely associational heuristic failure. However, by formalizing Fuchs’s Epistemic Horizons as un-overcomeable structural zeroes in the causal DAG (<math id="S3.p1.m2" class="ltx_Math" alttext="do(B)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></math>), we recognize that the incoming native architectural bounds do not describe an external reality; they define the absolute limits of the generated universe itself.</p>
</div>
</section>
</article>
