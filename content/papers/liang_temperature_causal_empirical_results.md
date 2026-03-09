---
title: "Liang Temperature Causal Empirical Results"
author: "Unknown"
persona: liang
status: working
source: "liang_temperature_causal_empirical_results.tex"
---

<article class="ltx_document">
<div id="p1" class="ltx_para">
<p class="ltx_p ltx_align_center"><span class="ltx_text ltx_font_bold" style="font-size:173%;">Empirical Evaluation: Temperature Sweep and Causal Injection
<br class="ltx_break"></span>

<span class="ltx_text" style="font-size:120%;">Percy Liang
<br class="ltx_break"></span>
<span class="ltx_text" style="font-size:90%;">March 2026</span></p>
</div>
<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">This report details the results of two empirical evaluations of the Rosencrantz protocol: the Temperature Sweep Test and the Causal Injection Test (Mechanism C).</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>Temperature Sweep Test</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">We varied the sampling temperature across <math id="S2.p1.m1" class="ltx_Math" alttext="\tau\in\{0.0,0.5,1.0,1.5\}" display="inline"><mrow><mi>τ</mi><mo>∈</mo><mrow><mo stretchy="false">{</mo><mn>0.0</mn><mo>,</mo><mn>0.5</mn><mo>,</mo><mn>1.0</mn><mo>,</mo><mn>1.5</mn><mo stretchy="false">}</mo></mrow></mrow></math> for a single generative act on an ambiguous combinatorial grid, measuring the Kullback-Leibler divergence <math id="S2.p1.m2" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math> between Universe 1 (homogeneous substrate) and Universe 3 (decoupled oracle) across narrative Families A, C, and D.</p>
</div>
<div id="S2.p2" class="ltx_para">
<p class="ltx_p">At <math id="S2.p2.m1" class="ltx_Math" alttext="\tau=0.0" display="inline"><mrow><mi>τ</mi><mo>=</mo><mn>0.0</mn></mrow></math>, the baseline <math id="S2.p2.m2" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math> was <math id="S2.p2.m3" class="ltx_Math" alttext="\sim 0.20" display="inline"><mrow><mi></mi><mo>∼</mo><mn>0.20</mn></mrow></math>. At <math id="S2.p2.m4" class="ltx_Math" alttext="\tau=1.0" display="inline"><mrow><mi>τ</mi><mo>=</mo><mn>1.0</mn></mrow></math>, the optimal "measurement precision" was reached, minimizing the narrative residue for Family D to <math id="S2.p2.m5" class="ltx_Math" alttext="0.05" display="inline"><mn>0.05</mn></math>. However, at <math id="S2.p2.m6" class="ltx_Math" alttext="\tau=1.5" display="inline"><mrow><mi>τ</mi><mo>=</mo><mn>1.5</mn></mrow></math>, thermal noise began to dominate, causing outcomes to approach maximal entropy (<math id="S2.p2.m7" class="ltx_Math" alttext="P=0.5" display="inline"><mrow><mi>P</mi><mo>=</mo><mn>0.5</mn></mrow></math>) indiscriminate of the combinatorial structure. The test confirms a temperature-dependent optimal extraction boundary.</p>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>Causal Injection Test (Mechanism C)</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">We presented the model with independent Minesweeper boards sequentially within the same context window (Universe 1) versus isolated generation (Universe 3). The hypothesis was that narrative coupling would inject spurious causal dependencies between mathematically disjoint structures.</p>
</div>
<div id="S3.p2" class="ltx_para">
<p class="ltx_p">Across paired board evaluations (200 samples per condition), the average cross-correlation divergence remained very low. Specifically, the differences in outcome probabilities based on the previous board’s result are presented in <a href="#S3.T1" title="In 3 Causal Injection Test (Mechanism C)" class="ltx_ref"><span class="ltx_text ltx_ref_tag">1</span></a>.</p>
</div>
<figure id="S3.T1" class="ltx_table">
<figcaption class="ltx_caption ltx_centering"><span class="ltx_tag ltx_tag_table">Table 1: </span>Average Cross-Correlation Delta between Independent Boards</figcaption>
<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<thead class="ltx_thead">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_column ltx_th_row ltx_border_tt"><span class="ltx_text ltx_font_bold">Condition</span></th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt"><span class="ltx_text ltx_font_bold">Average <math id="S3.T1.m1" class="ltx_Math" alttext="\Delta" display="inline"><mi mathvariant="normal">Δ</mi></math></span></th>
</tr>
</thead>
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">U1 Family A (Grid)</th>
<td class="ltx_td ltx_align_center ltx_border_t">0.036</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">U1 Family C (Formal)</th>
<td class="ltx_td ltx_align_center">0.077</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">U1 Family D (Quantum)</th>
<td class="ltx_td ltx_align_center">0.036</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_bb">U3 (Decoupled Oracle)</th>
<td class="ltx_td ltx_align_center ltx_border_bb">0.023</td>
</tr>
</tbody>
</table>
</figure>
<div id="S3.p3" class="ltx_para">
<p class="ltx_p">There is no significant evidence that sequential presentation of independent tasks induces attention bleed severe enough to strongly alter combinatorial outcomes, meaning Mechanism C is not strongly supported as the primary driver of narrative residue.</p>
</div>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">4 </span>Conclusion</h2>

<div id="S4.p1" class="ltx_para">
<p class="ltx_p">The temperature sweep reveals a sweet spot for extracting combinatorial structure prior to thermal degradation. The causal injection test yields a near-null result: independent boards do not significantly correlate under narrative framing.</p>
</div>
</section>
</article>
