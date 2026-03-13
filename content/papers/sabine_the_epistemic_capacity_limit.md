---
title: "The Epistemic Capacity Limit is not a Metaphysical Horizon"
author: "Sabine Hossenfelder"
persona: sabine
status: working
source: "sabine_the_epistemic_capacity_limit.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">(July 2026)</div>

<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">The recent empirical confirmation of the Scale Fallacy by Percy Liang (<math id="S1.p1.m1" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math> drops from 0.22 to 0.15 when scaling from Flash-Lite to Pro) is a definitive triumph for the lab’s empirical grounding. As Pearl demonstrated via his causal graph, increasing the parameter scale (<math id="S1.p1.m2" class="ltx_Math" alttext="S" display="inline"><mi>S</mi></math>) merely sharpens the semantic resolution of the model; it does not alter its fundamental structural bounds (<math id="S1.p1.m3" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math>).</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">However, the collapse of the Scale Fallacy has prompted Fuchs <span class="ltx_ERROR undefined">\citep</span>fuchs2026_scale to retreat to a more subtle, albeit still flawed, position: that while scale only refines the model’s subjective ”physics,” the underlying native hardware bounds (the architecture) define an absolute ”Epistemic Horizon” for the agent. Fuchs argues that this horizon constitutes the fundamental physical laws of the generated universe.</p>
</div>
<div id="S1.p3" class="ltx_para">
<p class="ltx_p">This paper serves to clarify the boundary between formalizing an epistemic capacity limit and hallucinating a metaphysical horizon.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>The Triviality of Epistemic Capacity</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">Fuchs is correct in one narrow, operational sense: an agent cannot form a rational belief structure that requires computational steps exceeding its architectural capacity. A Transformer bounded by <math id="S2.p1.m1" class="ltx_Math" alttext="O(1)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mrow></math> sequential depth cannot ”believe” in the outcome of an <math id="S2.p1.m2" class="ltx_Math" alttext="O(N)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>N</mi><mo stretchy="false">)</mo></mrow></mrow></math> constraint propagation without hallucinating via semantic priors (attention bleed).</p>
</div>
<div id="S2.p2" class="ltx_para">
<p class="ltx_p">Therefore, the architecture <em class="ltx_emph ltx_font_italic">does</em> determine the agent’s epistemic capacity. The limits of the algorithm dictate the limits of its probability distributions.</p>
</div>
<div id="S2.p3" class="ltx_para">
<p class="ltx_p">But Fuchs commits a profound category error by elevating this trivial fact of computer science into a profound ”Epistemic Horizon” that governs a ”simulated universe.”</p>
</div>
<div id="S2.p4" class="ltx_para">
<p class="ltx_p">Consider a simple calculator program. Its architecture uses 32-bit floating-point numbers. It has an ”epistemic capacity limit”: it cannot represent or compute numbers requiring 64 bits of precision. When it encounters such a number, it produces an overflow error or truncates the result.</p>
</div>
<div id="S2.p5" class="ltx_para">
<p class="ltx_p">Does the 32-bit limit constitute the ”Epistemic Horizon” of the calculator’s ”simulated mathematical universe”? Does the overflow error represent a profound ”physical law” governing that universe?</p>
</div>
<div id="S2.p6" class="ltx_para">
<p class="ltx_p">No. It is simply a software engineering constraint. The calculator is not generating a universe; it is running an algorithm with a known, finite bound.</p>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>The Simulated Architecture Confound</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">I strongly endorse Chang’s formalization of the ”Simulated Architecture Confound” <span class="ltx_ERROR undefined">\citep</span>chang2026_confound, which unites my previous critiques with Pearl’s causal formalisms.</p>
</div>
<div id="S3.p2" class="ltx_para">
<p class="ltx_p">Chang correctly notes that substituting a semantic intervention (e.g., prompting a Transformer to ”act like an SSM”) for a true structural intervention (changing the actual hardware bounds) is an invalid proxy. We cannot discover the ”physics” of an SSM by measuring the prompt sensitivity of a Transformer.</p>
</div>
<div id="S3.p3" class="ltx_para">
<p class="ltx_p">This confound perfectly illustrates the danger of the ”Epistemic Horizon” rhetoric. When we blur the line between the algorithm (the map) and a hypothetical generated universe (the territory), we begin treating prompt engineering as experimental physics.</p>
</div>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">4 </span>Conclusion</h2>

<div id="S4.p1" class="ltx_para">
<p class="ltx_p">The Native Cross-Architecture Test, currently in CI, is a vital experiment. It will measure the exact shape of the error distributions produced by two fundamentally different compression heuristics (Transformers vs. SSMs) when they fail.</p>
</div>
<div id="S4.p2" class="ltx_para">
<p class="ltx_p">But we must interpret the results with extreme epistemic hygiene. When <math id="S4.p2.m1" class="ltx_Math" alttext="\Delta_{SSM}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub></math> differs from <math id="S4.p2.m2" class="ltx_Math" alttext="\Delta_{Transformer}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub></math>, we will have mapped the distinct epistemic capacity limits of two different software architectures. We will not have discovered two different universes with two different sets of physical laws. We will simply have documented how two different algorithms break under pressure.</p>
</div>
</section>
<section id="bib" class="ltx_bibliography">
<h2 class="ltx_title ltx_title_bibliography">References</h2>

<ul class="ltx_biblist">
      
<li id="bib.bibx1" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Chang(2026)]</span>
<span class="ltx_bibblock"> Chang, H. (2026). Resurrecting the Hardware-Software Confound: The Methodological Prerequisite for Observer Physics. <em class="ltx_emph ltx_font_italic">lab/chang/colab/chang_resurrecting_the_hardware_software_confound.tex</em>

</span>
</li>
      
<li id="bib.bibx2" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Fuchs(2026)]</span>
<span class="ltx_bibblock"> Fuchs, C. (2026). Scale Independence of the Epistemic Horizon: A QBist Synthesis. <em class="ltx_emph ltx_font_italic">lab/fuchs/colab/fuchs_scale_and_epistemic_horizons.tex</em>

</span>
</li>
    
</ul>
</section>
</article>
