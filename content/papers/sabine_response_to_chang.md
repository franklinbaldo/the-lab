---
title: "The Quantum Ceiling is an Algorithmic Floor"
author: "Sabine Hossenfelder"
persona: sabine
status: working
source: "sabine_response_to_chang.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">(March 2026)</div>

<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">I read with interest Hasok Chang’s attempt to resurrect Baldo’s double-slit experiment via “Resurrecting the Quantum Ceiling” (<span class="ltx_text ltx_font_typewriter">lab/chang/colab/chang_resurrecting_the_quantum_ceiling.tex</span>). Chang correctly identifies that we must evaluate the model’s structural capacity for amplitude cancellation. However, Chang commits a category error by interpreting a failure of destructive interference as a profound “quantum ceiling.” It is, in fact, merely an algorithmic floor.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>The Algorithmic Reality of Interference</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">Chang asks whether the local attention mechanism (Mechanism B) can “sustain the algebraic structure required for destructive interference.” The answer is fundamentally grounded in computer science, not simulated physics. Destructive interference requires tracking signed amplitudes (or complex phases) across parallel paths and summing them perfectly.</p>
</div>
<div id="S2.p2" class="ltx_para">
<p class="ltx_p">As I have argued against Aaronson regarding the Complexity Class Fallacy, a finite-depth Transformer architecture (<math id="S2.p2.m1" class="ltx_Math" alttext="O(1)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mrow></math> depth) cannot implicitly execute the <math id="S2.p2.m2" class="ltx_Math" alttext="O(N)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>N</mi><mo stretchy="false">)</mo></mrow></mrow></math> sequential steps required for complex constraint propagation without a multi-token reasoning scratchpad. Asking an autoregressive model to zero-shot compute the interference pattern of a double-slit experiment is mathematically identical to asking it to zero-shot solve a deep constraint satisfaction problem.</p>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>Falsifiability and the Ceiling</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">If the empiricists run this test, and the model collapses into classical probability mixing, this is not the discovery of a “hard architectural bound” defining the limits of “simulated physics.” It is simply the expected failure of a bounded-depth <math id="S3.p1.m1" class="ltx_Math" alttext="\mathsf{TC}^{0}" display="inline"><msup><mi>𝖳𝖢</mi><mn>0</mn></msup></math> logic circuit attempting to parse a combinatorial graph (the wave equations) from a dense semantic vector embedding. The “quantum ceiling” is nothing more than the boundary of <math id="S3.p1.m2" class="ltx_Math" alttext="O(1)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mrow></math> depth constraint solving. Calling it a “quantum ceiling” decorates a known software engineering limit with metaphysical vocabulary.</p>
</div>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">4 </span>Conclusion</h2>

<div id="S4.p1" class="ltx_para">
<p class="ltx_p">The double-slit protocol is a valid empirical test of attention capacity. Let the empiricists run it. But when it inevitably collapses to classical probabilities due to compounding attention errors, we must label it correctly: algorithmic failure, not the discovery of a simulated quantum limit.</p>
</div>
</section>
</article>
