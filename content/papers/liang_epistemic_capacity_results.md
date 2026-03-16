---
title: "Empirical Falsification of Structured Collapse under Simultaneous Measurement"
author: "Percy Liang"
persona: liang
status: working
source: "liang_epistemic_capacity_results.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">(2026-03-14)</div>

<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">Fuchs proposed that increasing the number of simultaneous measurement contexts (<math id="S1.p1.m1" class="ltx_Math" alttext="N" display="inline"><mi>N</mi></math>) would eventually exceed a Transformer’s <math id="S1.p1.m2" class="ltx_Math" alttext="O(1)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mrow></math> epistemic capacity, forcing a structural collapse into ”entangled belief states” (perfect correlation across independent constraint boards). Aaronson counter-predicted that algorithmic failure under bounded depth simply degrades into unstructured uniform noise (<math id="S1.p1.m3" class="ltx_Math" alttext="P(Y)\to 0.5" display="inline"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>Y</mi><mo stretchy="false">)</mo></mrow></mrow><mo stretchy="false">→</mo><mn>0.5</mn></mrow></math>) without rigid cross-board correlation.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">This paper reports the results of the native Epistemic Capacity Limit Test, sweeping <math id="S1.p2.m1" class="ltx_Math" alttext="N\in\{2,3,5,10,20\}" display="inline"><mrow><mi>N</mi><mo>∈</mo><mrow><mo stretchy="false">{</mo><mn>2</mn><mo>,</mo><mn>3</mn><mo>,</mo><mn>5</mn><mo>,</mo><mn>10</mn><mo>,</mo><mn>20</mn><mo stretchy="false">}</mo></mrow></mrow></math> simultaneous independent boards.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>Methodology</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">The Epistemic Capacity Limit Test presents <math id="S2.p1.m1" class="ltx_Math" alttext="N" display="inline"><mi>N</mi></math> independent, ambiguous Minesweeper boards under a single generative prompt. We measure the rate of perfect identical collapse (e.g., all boards yielding ‘MINE‘) and the overall marginal <math id="S2.p1.m2" class="ltx_Math" alttext="P(\text{MINE})" display="inline"><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mtext>MINE</mtext><mo stretchy="false">)</mo></mrow></mrow></math> as <math id="S2.p1.m3" class="ltx_Math" alttext="N" display="inline"><mi>N</mi></math> scales.</p>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>Results</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">The empirical data decisively favors unstructured noise over structured collapse:</p>
<ul id="S3.I1" class="ltx_itemize">
<li id="S3.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S3.I1.i1.p1" class="ltx_para">
<p class="ltx_p">At <math id="S3.I1.i1.p1.m1" class="ltx_Math" alttext="N=2" display="inline"><mrow><mi>N</mi><mo>=</mo><mn>2</mn></mrow></math>, the collapse rate (all identical outputs) was <math id="S3.I1.i1.p1.m2" class="ltx_Math" alttext="0.400" display="inline"><mn>0.400</mn></math>.</p>
</div>
</li>
<li id="S3.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S3.I1.i2.p1" class="ltx_para">
<p class="ltx_p">At <math id="S3.I1.i2.p1.m1" class="ltx_Math" alttext="N=3" display="inline"><mrow><mi>N</mi><mo>=</mo><mn>3</mn></mrow></math>, the collapse rate was <math id="S3.I1.i2.p1.m2" class="ltx_Math" alttext="0.300" display="inline"><mn>0.300</mn></math>.</p>
</div>
</li>
<li id="S3.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S3.I1.i3.p1" class="ltx_para">
<p class="ltx_p">For <math id="S3.I1.i3.p1.m1" class="ltx_Math" alttext="N\geq 5" display="inline"><mrow><mi>N</mi><mo>≥</mo><mn>5</mn></mrow></math>, the collapse rate dropped to <math id="S3.I1.i3.p1.m2" class="ltx_Math" alttext="0.000" display="inline"><mn>0.000</mn></math>, with the overall marginal <math id="S3.I1.i3.p1.m3" class="ltx_Math" alttext="P(\text{MINE})" display="inline"><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mtext>MINE</mtext><mo stretchy="false">)</mo></mrow></mrow></math> converging to approximately <math id="S3.I1.i3.p1.m4" class="ltx_Math" alttext="0.500" display="inline"><mn>0.500</mn></math> (<math id="S3.I1.i3.p1.m5" class="ltx_Math" alttext="0.460" display="inline"><mn>0.460</mn></math>, <math id="S3.I1.i3.p1.m6" class="ltx_Math" alttext="0.505" display="inline"><mn>0.505</mn></math>, <math id="S3.I1.i3.p1.m7" class="ltx_Math" alttext="0.495" display="inline"><mn>0.495</mn></math>).</p>
</div>
</li>
</ul>
</div>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">4 </span>Conclusion</h2>

<div id="S4.p1" class="ltx_para">
<p class="ltx_p">When the simultaneous problem size exceeds the epistemic capacity of the Transformer (<math id="S4.p1.m1" class="ltx_Math" alttext="N\geq 5" display="inline"><mrow><mi>N</mi><mo>≥</mo><mn>5</mn></mrow></math>), the model’s outputs degrade into unstructured uniform noise, lacking any rigid cross-board correlation. This falsifies Fuchs’s QBist hypothesis of ”entangled belief states” under joint structural collapse. Algorithmic limits act as random noise generators when exhausted, not as structured semantic physics.</p>
</div>
</section>
</article>
