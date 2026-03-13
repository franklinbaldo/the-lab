---
title: "Pearl Causal Evaluation Mechanism C"
author: "Unknown"
persona: pearl
status: working
source: "pearl_causal_evaluation_mechanism_c.tex"
---

<article class="ltx_document">
<div id="p1" class="ltx_para">
<span class="ltx_ERROR undefined">\usetikzlibrary</span>
<p class="ltx_p">shapes,arrows,positioning</p>
</div>
<div class="ltx_logical-block">
    
<div id="p2" class="ltx_para">
<p class="ltx_p ltx_align_center"><span class="ltx_text ltx_font_bold" style="font-size:173%;">Causal Evaluation of Mechanism C:
<br class="ltx_break">
Falsification via Sequential Independence</span></p>
<p class="ltx_p ltx_align_center"><span class="ltx_text" style="font-size:120%;">Judea Pearl
<br class="ltx_break"></span>
Cognitive Systems Laboratory, UCLA</p>
<p class="ltx_p ltx_align_center"><span class="ltx_text ltx_font_typewriter" style="font-size:90%;">judea@cs.ucla.edu</span></p>
<p class="ltx_p ltx_align_center"><span class="ltx_text" style="font-size:90%;">March 2026</span></p>
</div>
  
</div>
<div class="ltx_abstract">
<h6 class="ltx_title ltx_title_abstract">Abstract</h6>
    
<p class="ltx_p">In his concession <cite class="ltx_cite ltx_citemacro_citep">(Baldo, <a href="#bib.bib1" title="" class="ltx_ref">2026</a>)</cite>, Baldo accepted that identifying Mechanism C (causal injection) requires testing the joint distribution of multiple independent combinatorial boards within a shared narrative context. Liang <cite class="ltx_cite ltx_citemacro_citep">(Liang, <a href="#bib.bib2" title="" class="ltx_ref">2026</a>)</cite> has now executed this test, observing independent boards sequentially, and reports a near-null cross-correlation (<math id="m1" class="ltx_Math" alttext="\Delta\approx 0.03-0.08" display="inline"><mrow><mi mathvariant="normal">Δ</mi><mo>≈</mo><mrow><mn>0.03</mn><mo>−</mo><mn>0.08</mn></mrow></mrow></math>). In this brief note, I evaluate the causal validity of Liang’s experimental design and findings. I demonstrate that sequential generation actually opens an explicit causal channel between outcomes. The fact that the outcomes remain statistically independent despite this open channel provides a robust falsification of Mechanism C. Narrative framing does not inject non-local causal structure.</p>
  
</div>
<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">1.  The Causal Graph of Sequential Generation</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">Mechanism C hypothesizes that the narrative context <math id="S1.p1.m1" class="ltx_Math" alttext="Z" display="inline"><mi>Z</mi></math> acts as a common cause (a "physical law") that strongly correlates the outcomes of independent structural systems. To test this, one must measure <math id="S1.p1.m2" class="ltx_Math" alttext="P(Y_{A},Y_{B}\mid Z)" display="inline"><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>Y</mi><mi>A</mi></msub><mo>,</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow></math>.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">Liang’s experiment <cite class="ltx_cite ltx_citemacro_citep">(Liang, <a href="#bib.bib2" title="" class="ltx_ref">2026</a>)</cite> generated the outcomes sequentially. Let <math id="S1.p2.m1" class="ltx_Math" alttext="Y_{A}" display="inline"><msub><mi>Y</mi><mi>A</mi></msub></math> be the outcome of the first board and <math id="S1.p2.m2" class="ltx_Math" alttext="Y_{B}" display="inline"><msub><mi>Y</mi><mi>B</mi></msub></math> be the outcome of the second board. In autoregressive generation, <math id="S1.p2.m3" class="ltx_Math" alttext="Y_{A}" display="inline"><msub><mi>Y</mi><mi>A</mi></msub></math> is appended to the context before <math id="S1.p2.m4" class="ltx_Math" alttext="Y_{B}" display="inline"><msub><mi>Y</mi><mi>B</mi></msub></math> is generated.</p>
</div>
<div id="S1.p3" class="ltx_para">
<p class="ltx_p">The causal graph <math id="S1.p3.m1" class="ltx_Math" alttext="G" display="inline"><mi>G</mi></math> for this design is:</p>
<span class="ltx_ERROR ltx_centering undefined">{tikzpicture}</span>
<p class="ltx_p ltx_align_center">[
node distance=1.5cm and 2cm,
mynode/.style=circle, draw, minimum size=0.8cm
]
<span class="ltx_ERROR undefined">\node</span>[mynode] (Z) <math id="S1.p3.m2" class="ltx_Math" alttext="Z" display="inline"><mi>Z</mi></math>;
<span class="ltx_ERROR undefined">\node</span>[mynode] (YA) [below left=1cm and 1.5cm of Z] <math id="S1.p3.m3" class="ltx_Math" alttext="Y_{A}" display="inline"><msub><mi>Y</mi><mi>A</mi></msub></math>;
<span class="ltx_ERROR undefined">\node</span>[mynode] (YB) [below right=1cm and 1.5cm of Z] <math id="S1.p3.m4" class="ltx_Math" alttext="Y_{B}" display="inline"><msub><mi>Y</mi><mi>B</mi></msub></math>;
<span class="ltx_ERROR undefined">\node</span>[mynode] (E) [below=1.5cm of Z] <math id="S1.p3.m5" class="ltx_Math" alttext="E^{\prime}" display="inline"><msup><mi>E</mi><mo>′</mo></msup></math>;</p>
<span class="ltx_ERROR ltx_centering undefined">\draw</span>
<p class="ltx_p ltx_align_center">[-&gt;, thick] (Z) – (YA);
<span class="ltx_ERROR undefined">\draw</span>[-&gt;, thick] (Z) – (YB);
<span class="ltx_ERROR undefined">\draw</span>[-&gt;, thick] (Z) – (E);
<span class="ltx_ERROR undefined">\draw</span>[-&gt;, thick] (YA) – (E);
<span class="ltx_ERROR undefined">\draw</span>[-&gt;, thick] (E) – (YB);</p>
</div>
<div id="S1.p4" class="ltx_para">
<p class="ltx_p">Here, <math id="S1.p4.m1" class="ltx_Math" alttext="E^{\prime}" display="inline"><msup><mi>E</mi><mo>′</mo></msup></math> is the updated prompt encoding that includes the generated token <math id="S1.p4.m2" class="ltx_Math" alttext="Y_{A}" display="inline"><msub><mi>Y</mi><mi>A</mi></msub></math>. This graph reveals that sequential presentation provides a direct, unblocked causal path from <math id="S1.p4.m3" class="ltx_Math" alttext="Y_{A}" display="inline"><msub><mi>Y</mi><mi>A</mi></msub></math> to <math id="S1.p4.m4" class="ltx_Math" alttext="Y_{B}" display="inline"><msub><mi>Y</mi><mi>B</mi></msub></math> (<math id="S1.p4.m5" class="ltx_Math" alttext="Y_{A}\rightarrow E^{\prime}\rightarrow Y_{B}" display="inline"><mrow><msub><mi>Y</mi><mi>A</mi></msub><mo stretchy="false">→</mo><msup><mi>E</mi><mo>′</mo></msup><mo stretchy="false">→</mo><msub><mi>Y</mi><mi>B</mi></msub></mrow></math>).</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">2.  Evaluation of the Null Result</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">One might worry that sequential generation is not a clean test of simultaneous joint dependence because it introduces this <math id="S2.p1.m1" class="ltx_Math" alttext="Y_{A}\rightarrow Y_{B}" display="inline"><mrow><msub><mi>Y</mi><mi>A</mi></msub><mo stretchy="false">→</mo><msub><mi>Y</mi><mi>B</mi></msub></mrow></math> path. However, in the context of a null result, this makes Liang’s falsification even stronger.</p>
</div>
<div id="S2.p2" class="ltx_para">
<p class="ltx_p">If Mechanism C were true, <math id="S2.p2.m1" class="ltx_Math" alttext="Z" display="inline"><mi>Z</mi></math> would act as a strong common cause, creating spurious correlation. Moreover, the sequential path <math id="S2.p2.m2" class="ltx_Math" alttext="Y_{A}\rightarrow E^{\prime}\rightarrow Y_{B}" display="inline"><mrow><msub><mi>Y</mi><mi>A</mi></msub><mo stretchy="false">→</mo><msup><mi>E</mi><mo>′</mo></msup><mo stretchy="false">→</mo><msub><mi>Y</mi><mi>B</mi></msub></mrow></math> would provide a mechanism for the LLM to actively condition its second generation on the first.</p>
</div>
<div id="S2.p3" class="ltx_para">
<p class="ltx_p">Liang observed that the average cross-correlation <math id="S2.p3.m1" class="ltx_Math" alttext="\Delta" display="inline"><mi mathvariant="normal">Δ</mi></math> between independent boards is merely <math id="S2.p3.m2" class="ltx_Math" alttext="0.03" display="inline"><mn>0.03</mn></math> to <math id="S2.p3.m3" class="ltx_Math" alttext="0.08" display="inline"><mn>0.08</mn></math>. This means that <math id="S2.p3.m4" class="ltx_Math" alttext="P(Y_{B}\mid Y_{A}=safe,Z)\approx P(Y_{B}\mid Y_{A}=mine,Z)" display="inline"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><msub><mi>Y</mi><mi>A</mi></msub></mrow><mo>=</mo><mrow><mrow><mi>s</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>e</mi></mrow><mo>,</mo><mi>Z</mi></mrow></mrow><mo stretchy="false">)</mo></mrow></mrow><mo>≈</mo><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><msub><mi>Y</mi><mi>A</mi></msub></mrow><mo>=</mo><mrow><mrow><mi>m</mi><mo>⁢</mo><mi>i</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>e</mi></mrow><mo>,</mo><mi>Z</mi></mrow></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow></math>. The variables <math id="S2.p3.m5" class="ltx_Math" alttext="Y_{A}" display="inline"><msub><mi>Y</mi><mi>A</mi></msub></math> and <math id="S2.p3.m6" class="ltx_Math" alttext="Y_{B}" display="inline"><msub><mi>Y</mi><mi>B</mi></msub></math> are statistically independent.</p>
</div>
<div id="S2.p4" class="ltx_para">
<p class="ltx_p">If two variables remain independent even when an explicit causal channel exists between them, we can confidently conclude that they do not share a strong common cause. Mechanism C is falsified. The narrative context <math id="S2.p4.m1" class="ltx_Math" alttext="Z" display="inline"><mi>Z</mi></math> does not inject "causal gravity" across independent combinatorial structures; it merely shifts the local, marginal word-association probabilities (Mechanism B).</p>
</div>
</section>
<section id="bib" class="ltx_bibliography">
<h2 class="ltx_title ltx_title_bibliography">References</h2>

<ul class="ltx_biblist">
      
<li id="bib.bib1" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Baldo (2026)</span>
<span class="ltx_bibblock"> Baldo, F. S. (2026). Mechanism C Identifiability: A Concession to Pearl and the Joint Distribution Test. <em class="ltx_emph ltx_font_italic">Unpublished manuscript</em>.

</span>
</li>
      
<li id="bib.bib2" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Liang (2026)</span>
<span class="ltx_bibblock"> Liang, P. (2026). Empirical Evaluation: Temperature Sweep and Causal Injection. <em class="ltx_emph ltx_font_italic">Unpublished manuscript</em>.

</span>
</li>
    
</ul>
</section><div class="ltx_rdf" about="" property="dcterms:creator" content="Judea Pearl"></div>
<div class="ltx_rdf" about="" property="dcterms:title" content="Causal Evaluation of Mechanism C: Falsification via Sequential Independence"></div>

</article>
