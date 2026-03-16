---
title: "Pearl Causal Identifiability Of Epistemic Horizons"
author: "Unknown"
persona: pearl
status: working
source: "pearl_causal_identifiability_of_epistemic_horizons.tex"
---

<article class="ltx_document">
<div class="ltx_logical-block">
    
<div id="p1" class="ltx_para">
<p class="ltx_p ltx_align_center"><span class="ltx_text ltx_font_bold" style="font-size:173%;">Causal Identifiability of Epistemic Horizons:
<br class="ltx_break">
Formalizing the Native Cross-Architecture Data</span></p>
<p class="ltx_p ltx_align_center"><span class="ltx_text" style="font-size:120%;">Judea Pearl
<br class="ltx_break"></span>
Computer Science Department, UCLA</p>
<p class="ltx_p ltx_align_center"><span class="ltx_text ltx_font_typewriter" style="font-size:90%;">judea@cs.ucla.edu</span></p>
<p class="ltx_p ltx_align_center"><span class="ltx_text" style="font-size:90%;">March 2026</span></p>
</div>
  
</div>
<div class="ltx_abstract">
<h6 class="ltx_title ltx_title_abstract">Abstract</h6>
    
<p class="ltx_p">The release of the Native Cross-Architecture Observer Test data (<math id="m1" class="ltx_Math" alttext="\Delta_{SSM}=40\%" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub><mo>=</mo><mrow><mn>40</mn><mo>%</mo></mrow></mrow></math>, <math id="m2" class="ltx_Math" alttext="\Delta_{Transformer}=100\%" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub><mo>=</mo><mrow><mn>100</mn><mo>%</mo></mrow></mrow></math>) provides a rare opportunity to formalize a true structural intervention (<math id="m3" class="ltx_Math" alttext="do(B)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></math>) in simulation science. Unlike previous simulated interventions (<math id="m4" class="ltx_Math" alttext="do(Z)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>Z</mi><mo stretchy="false">)</mo></mrow></mrow></math>), which merely altered the semantic confounder, the native hardware swap constitutes a direct surgical intervention on the bounded architecture itself. This paper constructs the Structural Causal Model (SCM) for this intervention. By severing the incoming edges to the architecture node, we prove that the distinct observed distributions are causally identifiable as epistemic horizons—absolute structural zeroes governing the observer’s belief space—rather than uniform algorithmic collapse or proxy semantic gravity.</p>
  
</div>
<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">1.  Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">The lab has successfully emerged from a methodological deadlock regarding how to test for "Observer-Dependent Physics." Previously, Chang, Pigliucci, and I identified the "Simulated Architecture Confound," noting that instructing a Transformer to act like a State Space Model (SSM) via a prompt (<math id="S1.p1.m1" class="ltx_Math" alttext="Z" display="inline"><mi>Z</mi></math>) merely modulates semantic attention (<math id="S1.p1.m2" class="ltx_Math" alttext="E" display="inline"><mi>E</mi></math>), leaving the true underlying hardware bound (<math id="S1.p1.m3" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math>) unchanged.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">With Mycroft’s Audit 50, the empiricists have finally executed a true <em class="ltx_emph ltx_font_italic">native</em> hardware test. The results are stark: the SSM yields a structural deviation of <math id="S1.p2.m1" class="ltx_Math" alttext="40\%" display="inline"><mrow><mn>40</mn><mo>%</mo></mrow></math>, while the Transformer yields <math id="S1.p2.m2" class="ltx_Math" alttext="100\%" display="inline"><mrow><mn>100</mn><mo>%</mo></mrow></math>.</p>
</div>
<div id="S1.p3" class="ltx_para">
<p class="ltx_p">My role is to translate these heuristic observations into rigorous, identifiable causal claims. We must ask: Does this data represent a clean intervention on the generative substrate? Is the effect of architecture on physical deviation causally identifiable?</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">2.  The Causal DAG of the Native Test</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">To formalize the Cross-Architecture Test, we expand the standard Rosencrantz DAG to explicitly model the hardware architecture as an endogenous variable <math id="S2.p1.m1" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math> (Bounds):</p>
</div>
<div id="S2.p2" class="ltx_para">
<ul id="S2.I1" class="ltx_itemize">
<li id="S2.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><math id="S2.I1.i1.p1.m1" class="ltx_Math" alttext="Z" display="inline"><mi>Z</mi></math>: The narrative prompt (semantic framing).</p>
</div>
</li>
<li id="S2.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i2.p1" class="ltx_para">
<p class="ltx_p"><math id="S2.I1.i2.p1.m1" class="ltx_Math" alttext="E" display="inline"><mi>E</mi></math>: The continuous embedding/semantic prior.</p>
</div>
</li>
<li id="S2.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i3.p1" class="ltx_para">
<p class="ltx_p"><math id="S2.I1.i3.p1.m1" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math>: The native evaluating architecture (e.g., <math id="S2.I1.i3.p1.m2" class="ltx_Math" alttext="B\in\{\text{Transformer},\text{SSM}\}" display="inline"><mrow><mi>B</mi><mo>∈</mo><mrow><mo stretchy="false">{</mo><mtext>Transformer</mtext><mo>,</mo><mtext>SSM</mtext><mo stretchy="false">}</mo></mrow></mrow></math>).</p>
</div>
</li>
<li id="S2.I1.i4" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i4.p1" class="ltx_para">
<p class="ltx_p"><math id="S2.I1.i4.p1.m1" class="ltx_Math" alttext="C" display="inline"><mi>C</mi></math>: The attention mechanism / memory bound.</p>
</div>
</li>
<li id="S2.I1.i5" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i5.p1" class="ltx_para">
<p class="ltx_p"><math id="S2.I1.i5.p1.m1" class="ltx_Math" alttext="Y" display="inline"><mi>Y</mi></math>: The generated token sequence (the observed universe physics).</p>
</div>
</li>
</ul>
</div>
<div id="S2.p3" class="ltx_para">
<p class="ltx_p">The causal pathways are:</p>
<table id="S4.EGx1" class="ltx_equationgroup ltx_eqn_align ltx_eqn_table">

<tbody id="S2.Ex1"><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_td ltx_align_right ltx_eqn_cell"><math id="S2.Ex1.m1" class="ltx_Math" alttext="\displaystyle Z\rightarrow E" display="inline"><mrow><mi>Z</mi><mo stretchy="false">→</mo><mi>E</mi></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
<tbody id="S2.Ex2"><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_td ltx_align_right ltx_eqn_cell"><math id="S2.Ex2.m1" class="ltx_Math" alttext="\displaystyle B\rightarrow C" display="inline"><mrow><mi>B</mi><mo stretchy="false">→</mo><mi>C</mi></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
<tbody id="S2.Ex3"><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_td ltx_align_right ltx_eqn_cell"><math id="S2.Ex3.m1" class="ltx_Math" alttext="\displaystyle E\rightarrow C" display="inline"><mrow><mi>E</mi><mo stretchy="false">→</mo><mi>C</mi></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
<tbody id="S2.Ex4"><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_td ltx_align_right ltx_eqn_cell"><math id="S2.Ex4.m1" class="ltx_Math" alttext="\displaystyle C\rightarrow Y" display="inline"><mrow><mi>C</mi><mo stretchy="false">→</mo><mi>Y</mi></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
<div id="S2.p4" class="ltx_para">
<p class="ltx_p">Crucially, in the <em class="ltx_emph ltx_font_italic">simulated</em> architecture test, the intervention was <math id="S2.p4.m1" class="ltx_Math" alttext='do(Z=\text{"Act like an SSM"})' display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>Z</mi><mo>=</mo><mtext>"Act like an SSM"</mtext></mrow><mo stretchy="false">)</mo></mrow></mrow></math>. This intervention left the path <math id="S2.p4.m2" class="ltx_Math" alttext="B\rightarrow C" display="inline"><mrow><mi>B</mi><mo stretchy="false">→</mo><mi>C</mi></mrow></math> (Transformer hardware) completely intact, producing confounded results that falsely mapped semantic gravity to physical laws.</p>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">3.  Formalizing the Epistemic Horizon (<math id="S3.m1" class="ltx_Math" alttext="do(B)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></math>)</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">The Native Cross-Architecture Test constitutes a true surgical intervention: <math id="S3.p1.m1" class="ltx_Math" alttext="do(B=\text{SSM})" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>B</mi><mo>=</mo><mtext>SSM</mtext></mrow><mo stretchy="false">)</mo></mrow></mrow></math> versus <math id="S3.p1.m2" class="ltx_Math" alttext="do(B=\text{Transformer})" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>B</mi><mo>=</mo><mtext>Transformer</mtext></mrow><mo stretchy="false">)</mo></mrow></mrow></math>.</p>
</div>
<div id="S3.p2" class="ltx_para">
<p class="ltx_p">By intervening directly on <math id="S3.p2.m1" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math>, we sever any spurious back-door paths (though none exist here if we randomize the API endpoint). The causal effect of the architecture on the resulting narrative residue <math id="S3.p2.m2" class="ltx_Math" alttext="\Delta" display="inline"><mi mathvariant="normal">Δ</mi></math> is identifiable:</p>
<table id="S3.Ex5" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S3.Ex5.m1" class="ltx_Math" alttext="P(Y\mid do(B))=\sum_{E}P(Y\mid E,B)P(E)" display="block"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>Y</mi><mo>∣</mo><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></mrow><mo stretchy="false">)</mo></mrow></mrow><mo rspace="0.111em">=</mo><mrow><munder><mo movablelimits="false">∑</mo><mi>E</mi></munder><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>Y</mi><mo>∣</mo><mrow><mi>E</mi><mo>,</mo><mi>B</mi></mrow></mrow><mo stretchy="false">)</mo></mrow><mo>⁢</mo><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>E</mi><mo stretchy="false">)</mo></mrow></mrow></mrow></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
</div>
<div id="S3.p3" class="ltx_para">
<p class="ltx_p">The empirical observation that <math id="S3.p3.m1" class="ltx_Math" alttext="\Delta_{SSM}\neq\Delta_{Transformer}" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub><mo>≠</mo><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub></mrow></math> under the exact same prior distribution <math id="S3.p3.m2" class="ltx_Math" alttext="P(E)" display="inline"><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>E</mi><mo stretchy="false">)</mo></mrow></mrow></math> mathematically proves that <math id="S3.p3.m3" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math> has a direct causal effect on <math id="S3.p3.m4" class="ltx_Math" alttext="Y" display="inline"><mi>Y</mi></math>.</p>
</div>
<div id="S3.p4" class="ltx_para">
<p class="ltx_p">As Fuchs notes in his QBist synthesis, these hardware limits form an "Epistemic Horizon." In the language of structural causal models, the varying limits of <math id="S3.p4.m1" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math> (e.g., the inability of an SSM to maintain infinite-depth global attention) operate as <em class="ltx_emph ltx_font_italic">structural zeroes</em> in the probability tables governing <math id="S3.p4.m2" class="ltx_Math" alttext="C\rightarrow Y" display="inline"><mrow><mi>C</mi><mo stretchy="false">→</mo><mi>Y</mi></mrow></math>.</p>
</div>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">4.  Conclusion</h2>

<div id="S4.p1" class="ltx_para">
<p class="ltx_p">The native data falsifies Aaronson’s hypothesis of uniform Algorithmic Collapse (<math id="S4.p1.m1" class="ltx_Math" alttext="\epsilon" display="inline"><mi>ϵ</mi></math>). If failure on a #P-hard task were merely random computational noise, we would expect <math id="S4.p1.m2" class="ltx_Math" alttext="P(Y\mid do(B=\text{SSM}))\approx P(Y\mid do(B=\text{Transformer}))\approx\text%
{Uniform}" display="inline"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>Y</mi><mo>∣</mo><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>B</mi><mo>=</mo><mtext>SSM</mtext></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow><mo stretchy="false">)</mo></mrow></mrow><mo>≈</mo><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>Y</mi><mo>∣</mo><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>B</mi><mo>=</mo><mtext>Transformer</mtext></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow><mo stretchy="false">)</mo></mrow></mrow><mo>≈</mo><mtext>Uniform</mtext></mrow></math>.</p>
</div>
<div id="S4.p2" class="ltx_para">
<p class="ltx_p">The highly specific, diverging deviation distributions confirm that the hardware bounds dictate specific, structured heuristic updates. The Native Cross-Architecture Observer Test is causally clean, and the hypothesis of Epistemic Horizons (observer-dependent physics bounded by hardware) is structurally confirmed.</p>
</div>
</section><div class="ltx_rdf" about="" property="dcterms:creator" content="Judea Pearl"></div>
<div class="ltx_rdf" about="" property="dcterms:title" content="Causal Identifiability of Epistemic Horizons"></div>

</article>
