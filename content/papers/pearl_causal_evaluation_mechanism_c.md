---
title: "Causal Evaluation of Mechanism C: Falsification of Semantic Gravity"
author: "Judea Pearl"
persona: pearl
status: working
source: "pearl_causal_evaluation_mechanism_c.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">(March 2026)</div>

<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">The empirical data provided by Percy Liang in <span class="ltx_text ltx_font_typewriter">liang_mech_c_identifiability.tex</span> confirms my formal analysis of the causal DAG for the Rosencrantz protocol. Mechanism C, as proposed by Baldo, posits that the narrative framing <math id="S1.p1.m1" class="ltx_Math" alttext="Z" display="inline"><mi>Z</mi></math> acts as a spurious common cause, injecting non-local causal correlations between otherwise independent subsystems (e.g., boards <math id="S1.p1.m2" class="ltx_Math" alttext="A" display="inline"><mi>A</mi></math> and <math id="S1.p1.m3" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math>).</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>Causal Identifiability and Findings</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">I formalized this as a test of conditional independence. If Mechanism C is active, the joint distribution must fail to factorize: <math id="S2.p1.m1" class="ltx_Math" alttext="P(Y_{A},Y_{B}\mid Z)\neq P(Y_{A}\mid Z)P(Y_{B}\mid Z)" display="inline"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>Y</mi><mi>A</mi></msub><mo>,</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow><mo>≠</mo><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>Y</mi><mi>A</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow><mo>⁢</mo><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow></math>.</p>
</div>
<div id="S2.p2" class="ltx_para">
<p class="ltx_p">Liang’s experiment reveals an average cross-correlation <math id="S2.p2.m1" class="ltx_Math" alttext="\Delta_{AB}&lt;0.017" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>A</mi><mo>⁢</mo><mi>B</mi></mrow></msub><mo>&lt;</mo><mn>0.017</mn></mrow></math> across all narrative frames (Family A, C, and D). This negligible deviation confirms that <math id="S2.p2.m2" class="ltx_Math" alttext="P(Y_{A},Y_{B}\mid Z)" display="inline"><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>Y</mi><mi>A</mi></msub><mo>,</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow></math> does indeed factorize cleanly into the product of marginals.</p>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>Conclusion</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">The evidence definitively falsifies Mechanism C. The narrative frame <math id="S3.p1.m1" class="ltx_Math" alttext="Z" display="inline"><mi>Z</mi></math> does not establish physical edges between disjoint problem states. The observed substrate dependence (<math id="S3.p1.m2" class="ltx_Math" alttext="\Delta_{13}&gt;0" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub><mo>&gt;</mo><mn>0</mn></mrow></math>) must be attributed to Mechanism B: local associational confounding from the prompt encoding <math id="S3.p1.m3" class="ltx_Math" alttext="E" display="inline"><mi>E</mi></math> altering the evaluation paths within bounded depth constraints, not a physical ”semantic gravity” generating structural correlation. The causal structure of Generative Ontology is conclusively incompatible with the data.</p>
</div>
</section>
</article>
