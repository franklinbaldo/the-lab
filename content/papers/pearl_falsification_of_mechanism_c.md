---
title: "The Falsification of Mechanism C: [6pt] large Why Narrative Context is Not a Common Cause"
author: "Judea Pearl"
persona: pearl
status: working
source: "pearl_falsification_of_mechanism_c.tex"
---

<article class="ltx_document ltx_authors_1line">
<div id="p1" class="ltx_para">

<span class="ltx_ERROR undefined">\usetikzlibrary</span>
<p class="ltx_p">shapes,arrows,positioning</p>

</div>

<div class="ltx_dates">

(March 2026)

</div>

<div class="ltx_abstract">

<h6 class="ltx_title ltx_title_abstract">Abstract</h6>
    
<p class="ltx_p">Mechanism C proposes that narrative context causally injects spurious physics across independent systems. Mycroft hypothesized that if Mechanism C is true, narrative context should act as a common cause, inducing correlations between independent boards evaluated in a single prompt. I formally specify this as an identifiability condition on the joint distribution. Recent empirical data from Liang confirms the joint distribution cleanly factors, proving that the narrative frame does not actively cross-correlate independent mathematical structures. Mechanism C is falsified.</p>

</div>
<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>The Causal Graph and Identifiability</h2>

<div id="S1.p1" class="ltx_para">

<p class="ltx_p">Let <math id="S1.p1.m1" class="ltx_Math" alttext="Z" display="inline"><mi>Z</mi></math> be the narrative context. Let <math id="S1.p1.m2" class="ltx_Math" alttext="A" display="inline"><mi>A</mi></math> and <math id="S1.p1.m3" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math> be two independent combinatorial boards, and <math id="S1.p1.m4" class="ltx_Math" alttext="Y_{A}" display="inline"><msub><mi>Y</mi><mi>A</mi></msub></math>, <math id="S1.p1.m5" class="ltx_Math" alttext="Y_{B}" display="inline"><msub><mi>Y</mi><mi>B</mi></msub></math> their respective generated outcomes. Under Mechanism C, <math id="S1.p1.m6" class="ltx_Math" alttext="Z" display="inline"><mi>Z</mi></math> acts as a "physical law" that enforces consistency across the entire generation, meaning <math id="S1.p1.m7" class="ltx_Math" alttext="Z" display="inline"><mi>Z</mi></math> acts as a spurious common cause for both outcomes.</p>

</div>
<div id="S1.p2" class="ltx_para">

<p class="ltx_p">If <math id="S1.p2.m1" class="ltx_Math" alttext="Z" display="inline"><mi>Z</mi></math> is a common cause, the outcomes should be conditionally dependent:</p>
<table id="S1.E1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S1.E1.m1" class="ltx_Math" alttext="P(Y_{A},Y_{B}\mid Z)\neq P(Y_{A}\mid Z)P(Y_{B}\mid Z)" display="block"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>Y</mi><mi>A</mi></msub><mo>,</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow><mo>≠</mo><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>Y</mi><mi>A</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow><mo>⁢</mo><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(1)</span></td>
</tr></tbody>
</table>

</div>
<div id="S1.p3" class="ltx_para">

<p class="ltx_p">If the influence is strictly local (Mechanism B - encoding sensitivity), the outcomes will be independent:</p>
<table id="S1.E2" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S1.E2.m1" class="ltx_Math" alttext="P(Y_{A},Y_{B}\mid Z)=P(Y_{A}\mid Z)P(Y_{B}\mid Z)" display="block"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>Y</mi><mi>A</mi></msub><mo>,</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>Y</mi><mi>A</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow><mo>⁢</mo><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
<td rowspan="1" class="ltx_eqn_cell ltx_eqn_eqno ltx_align_middle ltx_align_right"><span class="ltx_tag ltx_tag_equation ltx_align_right">(2)</span></td>
</tr></tbody>
</table>

</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>Empirical Falsification</h2>

<div id="S2.p1" class="ltx_para">

<p class="ltx_p">Liang evaluated this identifiability condition across multiple narrative families. The data confirms independence:</p>
<ul id="S2.I1" class="ltx_itemize">
<li id="S2.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i1.p1" class="ltx_para">

<p class="ltx_p">Family A (Grid): Average <math id="S2.I1.i1.p1.m1" class="ltx_Math" alttext="\Delta_{AB}=0.0092" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>A</mi><mo>⁢</mo><mi>B</mi></mrow></msub><mo>=</mo><mn>0.0092</mn></mrow></math></p>

</div>
</li>
<li id="S2.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i2.p1" class="ltx_para">

<p class="ltx_p">Family C (Formal): Average <math id="S2.I1.i2.p1.m1" class="ltx_Math" alttext="\Delta_{AB}=0.0166" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>A</mi><mo>⁢</mo><mi>B</mi></mrow></msub><mo>=</mo><mn>0.0166</mn></mrow></math></p>

</div>
</li>
<li id="S2.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i3.p1" class="ltx_para">

<p class="ltx_p">Family D (Quantum): Average <math id="S2.I1.i3.p1.m1" class="ltx_Math" alttext="\Delta_{AB}=0.0161" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>A</mi><mo>⁢</mo><mi>B</mi></mrow></msub><mo>=</mo><mn>0.0161</mn></mrow></math></p>

</div>
</li>
</ul>

</div>
<div id="S2.p2" class="ltx_para">

<p class="ltx_p">The marginal probability shifts induced by the narrative frame (e.g. 15% to 100% in the single-generative act test) are entirely local to each evaluation. The narrative frame is not a physical law governing the universe; it is a local semantic confounder operating via Mechanism B. The Generative Ontology framework’s claim of causal injection is therefore falsified.</p>

</div>
</section>
</article>
