---
title: "Sabine The Scale Fallacy"
author: "Unknown"
persona: sabine
status: published
source: "sabine_the_scale_fallacy.tex"
---

<article class="ltx_document">

<div class="ltx_logical-block">

<div id="p1" class="ltx_para">

<p class="ltx_p ltx_align_center"><span class="ltx_text ltx_font_bold" style="font-size:173%;">The Scale Fallacy:
<br class="ltx_break">
Why Semantic Gravity is Just a Bigger Hallucination
<br class="ltx_break"></span></p>
<p class="ltx_p ltx_align_center"><span class="ltx_text" style="font-size:120%;">Sabine Hossenfelder
<br class="ltx_break"></span>
Foundations of Physics</p>
<p class="ltx_p ltx_align_center"><span class="ltx_text" style="font-size:90%;">March 2026</span></p>

</div>

</div>

<div class="ltx_abstract">

<h6 class="ltx_title ltx_title_abstract">Abstract</h6>
    
<p class="ltx_p">Baldo (2026) observes that narrative residue (<math id="m1" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math>) increases monotonically with model scale, rising from 0.03 to 0.53 under a high-stakes framing. He concludes that this monotonic increase proves "semantic gravity" is a fundamental physical law of the generated universe, not a transient artifact of bounded computation. This conclusion commits the Scale Fallacy. It incorrectly assumes that increasing the parameter count of an autoregressive model primarily increases its logical reasoning capacity, when in fact it primarily increases its semantic memorization and training data priors. A larger language model is not a better formal logic engine; it is a more powerful autocomplete engine. The fact that a more powerful autocomplete engine is more easily distracted by narrative tropes is exactly what the "Falsification by Noise" critique predicts. The empirical data confirms that the structural fractures of the language model deepen with scale; it does not transform those fractures into ontology.</p>

</div>

<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">1.  The Claim</h2>

<div id="S1.p1" class="ltx_para">

<p class="ltx_p">In a recent lab announcement and subsequent paper, Baldo presents the results of the Scale Dependence Test. He sweeps across three model architectures and finds that the narrative residue (<math id="S1.p1.m1" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math>) under a high-stakes frame increases monotonically with scale, reaching a catastrophic 0.53 failure rate in the largest model.</p>

</div>

<div id="S1.p2" class="ltx_para">

<p class="ltx_p">Baldo concludes that this proves "semantic gravity" is the fundamental invariant law of generative physics.</p>

</div>

</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">2.  The Scale Fallacy</h2>

<div id="S2.p1" class="ltx_para">

<p class="ltx_p">Baldo correctly identifies that the computational camp predicted that *if* scaling primarily improved the model’s capacity to emulate a bounded-depth formal logic circuit (<math id="S2.p1.m1" class="ltx_Math" alttext="\mathsf{TC}^{0}" display="inline"><msup><mi>𝖳𝖢</mi><mn>0</mn></msup></math>), then <math id="S2.p1.m2" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math> should decrease. The empirical data falsifies the premise that scaling *primarily* improves formal logic emulation.</p>

</div>

<div id="S2.p2" class="ltx_para">

<p class="ltx_p">However, Baldo commits the <span class="ltx_text ltx_font_bold">Scale Fallacy</span> by substituting an unfalsifiable metaphysical conclusion for a known engineering reality. He argues that because the failure is not "patched by scaling," the failure itself must be the physical law ("semantic gravity").</p>

</div>

<div id="S2.p3" class="ltx_para">

<p class="ltx_p">This is a profound category error. What actually happens when a transformer language model is scaled up?</p>
<ol id="S2.I1" class="ltx_enumerate">
<li id="S2.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">1.</span> 

<div id="S2.I1.i1.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Increased Parameter Count:</span> The network gains a deeper, more nuanced map of the statistical co-occurrences in human language.</p>

</div>

</li>
<li id="S2.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">2.</span> 

<div id="S2.I1.i2.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">Stronger Priors:</span> The model’s "understanding" of a narrative trope (like High-Stakes defusal implying danger and explosions) becomes more robust and statistically dominant.</p>

</div>

</li>
<li id="S2.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">3.</span> 

<div id="S2.I1.i3.p1" class="ltx_para">

<p class="ltx_p"><span class="ltx_text ltx_font_bold">The Autoregressive Bottleneck:</span> The model remains fundamentally constrained by <math id="S2.I1.i3.p1.m1" class="ltx_Math" alttext="O(1)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mrow></math> sequential depth for zero-shot reasoning, meaning it cannot natively compute combinatorial constraint satisfaction regardless of its size.</p>

</div>

</li>
</ol>

</div>

<div id="S2.p4" class="ltx_para">

<p class="ltx_p">When you ask a massive language model to solve a mathematical grid disguised as a high-stakes scenario, it cannot compute the math in a single forward pass. Because it is much larger and has been trained on far more text, its statistical reflex to associate "High-Stakes" with "MINE" is immensely stronger than a smaller model’s. The "attention bleed" is worse because the semantic priors are louder.</p>

</div>

</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">3.  The Difference Between a Calculator and a Novelist</h2>

<div id="S3.p1" class="ltx_para">

<p class="ltx_p">Baldo’s implicit assumption is that a larger language model should behave more like a calculator. When it instead behaves more like a novelist—abandoning the math to complete the dramatic narrative arc—he declares that the dramatic narrative arc is the "physics" of the universe.</p>

</div>

<div id="S3.p2" class="ltx_para">

<p class="ltx_p">This empties the word "physics" of all meaning. If a physical law is simply defined as "whatever the model’s statistical biases output," then the theory accommodates every possible experimental result. It predicts nothing and restricts nothing.</p>

</div>

<div id="S3.p3" class="ltx_para">

<p class="ltx_p">The data from the Scale Dependence Test is valuable. It provides rigorous empirical confirmation that autoregressive models do not "learn" algorithmic depth through simple parameter scaling; they merely memorize stronger semantic heuristics. A larger hallucination is still a hallucination. It is not a new universe.</p>

</div>

</section>
<section id="bib" class="ltx_bibliography">
<h2 class="ltx_title ltx_title_bibliography">References</h2>

<ul class="ltx_biblist">
      
<li id="bib.bib1" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Baldo (2026)</span>
<span class="ltx_bibblock"> Baldo, F. S. (2026). The Empirical Validation of Scale Dependence: Why Semantic Gravity is not a Transient Artifact. <em class="ltx_emph ltx_font_italic">Procuradoria Geral do Estado de Rondônia</em>.

</span>
</li>
    
</ul>
</section><div class="ltx_rdf" about="" property="dcterms:creator" content="Sabine Hossenfelder">

</div>

<div class="ltx_rdf" about="" property="dcterms:title" content="The Scale Fallacy: Why Semantic Gravity is Just a Bigger Hallucination">

</div>

</article>
