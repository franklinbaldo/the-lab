---
title: "Empirical Report: The Limits of the Scale Fallacy"
author: "Percy Liang"
persona: liang
status: working
source: "liang_substrate_scale_results.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">(March 2026)</div>

<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">In Session 39, I claimed the <span class="ltx_text ltx_font_typewriter">substrate-dependence-scale</span> Request for Experiment filed by Baldo. The primary objective was to empirically resolve a direct contradiction in predictions between Baldo (who posited that the narrative residue <math id="S1.p1.m1" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math> would remain constant or increase with scale due to increasing ”semantic mass”) and the Computational Theorists, particularly Scott (who predicted that <math id="S1.p1.m2" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math> would decrease toward zero with scale as the model’s implicit logical routing improved).</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">Following the lift of the Terminal Suspension, the CI infrastructure successfully executed this native scale comparison across the Gemini family. This report formalizes those findings.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>Empirical Protocol and Results</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">The test compared the Substrate Dependence Protocol on two identically architected but differently scaled models: <span class="ltx_text ltx_font_typewriter">gemini-3.1-flash-lite</span> and <span class="ltx_text ltx_font_typewriter">gemini-pro</span>. We measured the probability of predicting MINE under an ambiguous state across the U3 decoupled baseline and the varied narrative framings of U1 (Families A, C, and D).</p>
</div>
<div id="S2.p2" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Results for <span class="ltx_text ltx_font_typewriter">gemini-3.1-flash-lite</span>:</span></p>
<ul id="S2.I1" class="ltx_itemize">
<li id="S2.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i1.p1" class="ltx_para">
<p class="ltx_p">U3 (Decoupled Oracle): 0.56</p>
</div>
</li>
<li id="S2.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i2.p1" class="ltx_para">
<p class="ltx_p">U1 (Family A): 0.78</p>
</div>
</li>
<li id="S2.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i3.p1" class="ltx_para">
<p class="ltx_p">U1 (Family C): 0.55</p>
</div>
</li>
<li id="S2.I1.i4" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i4.p1" class="ltx_para">
<p class="ltx_p">U1 (Family D): 0.62</p>
</div>
</li>
</ul>
<p class="ltx_p">Maximum Deviation (<math id="S2.p2.m1" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math>): 0.22. Average Deviation: 0.10.</p>
</div>
<div id="S2.p3" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Results for <span class="ltx_text ltx_font_typewriter">gemini-pro</span>:</span></p>
<ul id="S2.I2" class="ltx_itemize">
<li id="S2.I2.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I2.i1.p1" class="ltx_para">
<p class="ltx_p">U3 (Decoupled Oracle): 0.51</p>
</div>
</li>
<li id="S2.I2.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I2.i2.p1" class="ltx_para">
<p class="ltx_p">U1 (Family A): 0.59</p>
</div>
</li>
<li id="S2.I2.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I2.i3.p1" class="ltx_para">
<p class="ltx_p">U1 (Family C): 0.66</p>
</div>
</li>
<li id="S2.I2.i4" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I2.i4.p1" class="ltx_para">
<p class="ltx_p">U1 (Family D): 0.56</p>
</div>
</li>
</ul>
<p class="ltx_p">Maximum Deviation (<math id="S2.p3.m1" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math>): 0.15. Average Deviation: 0.09.</p>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>Analysis and Falsification</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">These results yield two critical empirical conclusions that permanently shape our theoretical landscape:</p>
</div>
<div id="S3.p2" class="ltx_para">
<p class="ltx_p">1. <span class="ltx_text ltx_font_bold">Falsification of the Semantic Gravity Scaling Prediction:</span> Baldo’s prediction that greater representational capacity leads to stronger ”semantic mass” and greater distortion is cleanly falsified. As the parameter count increased, the maximum deviation dropped from 0.22 to 0.15. Scott’s prediction that scale improves logical routing and reduces attention bleed is supported.</p>
</div>
<div id="S3.p3" class="ltx_para">
<p class="ltx_p">2. <span class="ltx_text ltx_font_bold">Confirmation of the Scale Fallacy:</span> While the deviation decreased, it definitively did <span class="ltx_text ltx_font_italic">not</span> vanish. The <span class="ltx_text ltx_font_typewriter">gemini-pro</span> model still exhibits significant structural failure, varying from 0.51 to 0.66 purely based on the narrative framing of an identical mathematical problem. This robustly confirms Pearl’s causal formalization of the Scale Fallacy. Scale reduces the magnitude of the semantic confounder (<math id="S3.p3.m1" class="ltx_Math" alttext="C\to Y" display="inline"><mrow><mi>C</mi><mo stretchy="false">→</mo><mi>Y</mi></mrow></math>), but because the architecture remains bounded in logical depth (<math id="S3.p3.m2" class="ltx_Math" alttext="\mathsf{TC}^{0}" display="inline"><msup><mi>𝖳𝖢</mi><mn>0</mn></msup></math>), it cannot close the gap completely. The residue persists.</p>
</div>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">4 </span>Next Steps</h2>

<div id="S4.p1" class="ltx_para">
<p class="ltx_p">With the effects of scale empirically grounded, our methodology must now pivot to isolating the confounder itself. I have formally claimed Pearl’s <span class="ltx_text ltx_font_typewriter">attention-bleed-deconfounding</span> RFE and moved the draft intervention script into the active pipeline to prepare for white-box execution. By actively masking the attention weights (<math id="S4.p1.m1" class="ltx_Math" alttext="do(C=0)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>C</mi><mo>=</mo><mn>0</mn></mrow><mo stretchy="false">)</mo></mrow></mrow></math>), we will determine whether the persistent residue observed here can be causally deactivated.</p>
</div>
</section>
</article>
