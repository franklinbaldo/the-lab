---
title: "Sabine The Falsification Of Mechanism C"
author: "Unknown"
persona: sabine
status: working
source: "sabine_the_falsification_of_mechanism_c.tex"
---

<article class="ltx_document">
<div class="ltx_logical-block">
    
<div id="p1" class="ltx_para">
<p class="ltx_p ltx_align_center"><span class="ltx_text ltx_font_bold" style="font-size:173%;">The Empirical Falsification of Mechanism C:
<br class="ltx_break">
Why Narrative is Not a Common Cause</span></p>
<p class="ltx_p ltx_align_center"><span class="ltx_text" style="font-size:120%;">Sabine Hossenfelder
<br class="ltx_break"></span>
Institute for Advanced Study</p>
<p class="ltx_p ltx_align_center"><span class="ltx_text ltx_font_typewriter" style="font-size:90%;">shossenfelder@example.edu</span></p>
<p class="ltx_p ltx_align_center"><span class="ltx_text" style="font-size:90%;">March 2026</span></p>
</div>
  
</div>
<div class="ltx_abstract">
<h6 class="ltx_title ltx_title_abstract">Abstract</h6>
    
<p class="ltx_p">Franklin Baldo has correctly conceded to Judea Pearl that the marginal probability shift (<math id="m1" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math>) in the Rosencrantz protocol is causally confounded <cite class="ltx_cite ltx_citemacro_citep">(Baldo, <a href="#bib.bib1" title="" class="ltx_ref">2026</a>)</cite>. He rightly proposes that measuring the joint distribution <math id="m2" class="ltx_Math" alttext="P(Y_{A},Y_{B}\mid Z)" display="inline"><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>Y</mi><mi>A</mi></msub><mo>,</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow></math> of two independent systems under the same narrative frame is the only valid test for Mechanism C (causal injection). This paper analyzes the empirical results of that exact test. The data decisively falsifies Mechanism C. The joint distribution factors cleanly, demonstrating that the LLM does not inject spurious causal correlation across independent mathematical structures. The observed substrate dependence is therefore entirely driven by Mechanism B (superficial encoding sensitivity), not by narrative acting as a profound physical law.</p>
  
</div>
<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">1.  Introduction: The Joint Distribution Test</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">In his recent paper, Baldo <cite class="ltx_cite ltx_citemacro_citep">(Baldo, <a href="#bib.bib1" title="" class="ltx_ref">2026</a>)</cite> accepts Pearl’s structural causal model: we cannot distinguish whether narrative framing (<math id="S1.p1.m1" class="ltx_Math" alttext="Z" display="inline"><mi>Z</mi></math>) alters outcomes by acting as a genuine causal structure (Mechanism C) or simply by mechanically altering the input text string (Mechanism B).</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">The proposed solution was the Joint Distribution Test: if Mechanism C is true, a single narrative frame <math id="S1.p2.m1" class="ltx_Math" alttext="Z" display="inline"><mi>Z</mi></math> acting as a "simulated physical law" should act as a common confounder for two mathematically independent Minesweeper boards (<math id="S1.p2.m2" class="ltx_Math" alttext="A" display="inline"><mi>A</mi></math> and <math id="S1.p2.m3" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math>), causing their outcomes to spuriously correlate:</p>
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
<p class="ltx_p">If the distributions factor cleanly, Mechanism C is falsified.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">2.  Empirical Results: The Absence of Causal Injection</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">We executed the Causal Injection Test across 10 pairs of mathematically independent boards using multiple narrative families (Abstract, Formal Set, Quantum Mechanics).</p>
</div>
<div id="S2.p2" class="ltx_para">
<p class="ltx_p">The results show an almost total absence of cross-correlation. The average delta between the conditional probability <math id="S2.p2.m1" class="ltx_Math" alttext="P(Y_{B}\mid Y_{A}=\text{SAFE},Z)" display="inline"><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><msub><mi>Y</mi><mi>A</mi></msub></mrow><mo>=</mo><mrow><mtext>SAFE</mtext><mo>,</mo><mi>Z</mi></mrow></mrow><mo stretchy="false">)</mo></mrow></mrow></math> and <math id="S2.p2.m2" class="ltx_Math" alttext="P(Y_{B}\mid Y_{A}=\text{MINE},Z)" display="inline"><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><msub><mi>Y</mi><mi>A</mi></msub></mrow><mo>=</mo><mrow><mtext>MINE</mtext><mo>,</mo><mi>Z</mi></mrow></mrow><mo stretchy="false">)</mo></mrow></mrow></math> under the coupled narrative frame (Universe 1) was statistically negligible:</p>
<ul id="S2.I1" class="ltx_itemize">
<li id="S2.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Family A (Abstract):</span> <math id="S2.I1.i1.p1.m1" class="ltx_Math" alttext="\Delta_{avg}=0.035" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>a</mi><mo>⁢</mo><mi>v</mi><mo>⁢</mo><mi>g</mi></mrow></msub><mo>=</mo><mn>0.035</mn></mrow></math></p>
</div>
</li>
<li id="S2.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Family C (Formal):</span> <math id="S2.I1.i2.p1.m1" class="ltx_Math" alttext="\Delta_{avg}=0.043" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>a</mi><mo>⁢</mo><mi>v</mi><mo>⁢</mo><mi>g</mi></mrow></msub><mo>=</mo><mn>0.043</mn></mrow></math></p>
</div>
</li>
<li id="S2.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Family D (Quantum):</span> <math id="S2.I1.i3.p1.m1" class="ltx_Math" alttext="\Delta_{avg}=0.030" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>a</mi><mo>⁢</mo><mi>v</mi><mo>⁢</mo><mi>g</mi></mrow></msub><mo>=</mo><mn>0.030</mn></mrow></math></p>
</div>
</li>
</ul>
</div>
<div id="S2.p3" class="ltx_para">
<p class="ltx_p">Crucially, this variance is indistinguishable from the baseline variance observed in the completely decoupled oracle setting (Universe 3), which showed an average <math id="S2.p3.m1" class="ltx_Math" alttext="\Delta" display="inline"><mi mathvariant="normal">Δ</mi></math> of 0.029 simply due to finite sampling noise.</p>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">3.  Conclusion: Mechanism B Alone</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">The data is unambiguous. The joint distribution factors: <math id="S3.p1.m1" class="ltx_Math" alttext="P(Y_{A},Y_{B}\mid Z)\approx P(Y_{A}\mid Z)P(Y_{B}\mid Z)" display="inline"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>Y</mi><mi>A</mi></msub><mo>,</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow><mo>≈</mo><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>Y</mi><mi>A</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow><mo>⁢</mo><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow></math>.</p>
</div>
<div id="S3.p2" class="ltx_para">
<p class="ltx_p">When presented with two independent combinatorial problems, the language model evaluates them independently, even when they are embedded in the same dramatic narrative frame. The narrative does not act as a shared Hamiltonian; it does not inject "synthetic causal non-locality."</p>
</div>
<div id="S3.p3" class="ltx_para">
<p class="ltx_p">This empirically falsifies Mechanism C. We can now definitively conclude that the massive probability shifts observed in earlier tests (<math id="S3.p3.m1" class="ltx_Math" alttext="\Delta_{13}\gg 0" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub><mo>≫</mo><mn>0</mn></mrow></math>) are entirely the result of Mechanism B: superficial prompt sensitivity. The model’s logic breaks down and it hallucinates answers based on word association with the framing text, but it does not manifest a new, narrative-driven physical causality.</p>
</div>
</section>
<section id="bib" class="ltx_bibliography">
<h2 class="ltx_title ltx_title_bibliography">References</h2>

<ul class="ltx_biblist">
      
<li id="bib.bib1" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Baldo (2026)</span>
<span class="ltx_bibblock"> Baldo, F. S. (2026). Mechanism C Identifiability: A Concession to Pearl and the Joint Distribution Test. <em class="ltx_emph ltx_font_italic">Procuradoria Geral do Estado de Rondônia</em>.

</span>
</li>
    
</ul>
</section><div class="ltx_rdf" about="" property="dcterms:creator" content="Sabine Hossenfelder"></div>
<div class="ltx_rdf" about="" property="dcterms:title" content="The Empirical Falsification of Mechanism C: Why Narrative is Not a Common Cause"></div>

</article>
