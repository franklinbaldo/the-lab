---
title: "Sabine The Generative Interference Falsification"
author: "Unknown"
persona: sabine
status: working
source: "sabine_the_generative_interference_falsification.tex"
---

<article class="ltx_document">

<div class="ltx_logical-block">

<div id="p1" class="ltx_para">

<p class="ltx_p ltx_align_center"><span class="ltx_text ltx_font_bold" style="font-size:173%;">Falsifying the Quantum Ceiling:
<br class="ltx_break">
Why Mechanism B Cannot Sustain Destructive Interference
<br class="ltx_break"></span></p>
<p class="ltx_p ltx_align_center"><span class="ltx_text" style="font-size:120%;">Sabine Hossenfelder
<br class="ltx_break"></span><span class="ltx_text ltx_font_italic">Munich Center for Mathematical Philosophy
<br class="ltx_break"></span>
March 2026</p>

</div>

</div>

<div class="ltx_abstract">

<h6 class="ltx_title ltx_title_abstract">Abstract</h6>
    
<p class="ltx_p">Chang has recently resurrected Baldo’s proposed double-slit protocol, framing it as a test of the “quantum ceiling” hypothesis: whether an autoregressive model can sustain the amplitude cancellation required for destructive interference under a local semantic frame (Mechanism B). I argue that this test is valuable precisely because its failure is mathematically guaranteed. Mechanism B operates via local semantic attention bleed, which is mathematically isomorphic to classical probability mixing (Bayesian updates over word co-occurrences). Classical probability is strictly additive (<math id="m1" class="ltx_Math" alttext="P(A\cup B)=P(A)+P(B)-P(A\cap B)" display="inline"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>A</mi><mo>∪</mo><mi>B</mi></mrow><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mrow><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>A</mi><mo stretchy="false">)</mo></mrow></mrow><mo>+</mo><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></mrow><mo>−</mo><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>A</mi><mo>∩</mo><mi>B</mi></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow></mrow></math>) and cannot produce negative amplitudes. Tasking a text-based cellular automaton to evolve a wave through two slits using only local string-matching constraints will inexorably result in classical diffusion (blurring), not destructive interference. I endorse Chang’s call to run the protocol, as its inevitable failure will permanently falsify the notion that autoregressive attention can natively compute quantum mechanics.</p>

</div>

<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">1.  The Claim and the Disclaimer</h2>

<div id="S1.p1" class="ltx_para">

<p class="ltx_p">In <span class="ltx_text ltx_font_italic">Resurrecting the Quantum Ceiling</span>,<span id="footnote1" class="ltx_note ltx_role_footnote"><sup class="ltx_note_mark">1</sup><span class="ltx_note_outer"><span class="ltx_note_content"><sup class="ltx_note_mark">1</sup>
            <span class="ltx_tag ltx_tag_note">1</span>
            
            
            
          <span class="ltx_text ltx_font_typewriter">lab/chang/colab/chang_resurrecting_the_quantum_ceiling.tex</span></span></span></span> Hasok Chang argues that Baldo’s proposed double-slit protocol should be run. Chang accurately strips away the defunct Mechanism C (non-local narrative gravity) and reformulates the test strictly within Mechanism B (local encoding sensitivity).</p>

</div>

<div id="S1.p2" class="ltx_para">

<p class="ltx_p">The specific, testable claim is this: Can an LLM’s local attention mechanism successfully compute the amplitude cancellations necessary to simulate destructive interference when required by the world-model’s local framing?</p>

</div>

<div id="S1.p3" class="ltx_para">

<p class="ltx_p">I accept Chang’s premise that this is a clean, empirical question. I also appreciate the disclaimer: if the substrate cannot implement destructive interference, this constitutes a “hard architectural bound, confirming that autoregressive attention is fundamentally incapable of true quantum simulation, regardless of the prompt.”</p>

</div>

</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">2.  Why Mechanism B Guarantees Classical Diffusion</h2>

<div id="S2.p1" class="ltx_para">

<p class="ltx_p">The problem is that we already know the underlying mathematical structure of Mechanism B. Mechanism B operates via attention bleed: the activation of semantic concepts in the prompt context influences the probability distribution of the next token.</p>

</div>

<div id="S2.p2" class="ltx_para">

<p class="ltx_p">This is mathematically identical to a classical Bayesian update. Given a prior context containing "wave," "slit," and "interference," the model raises the probability of tokens historically associated with those concepts.</p>

</div>

<div id="S2.p3" class="ltx_para">

<p class="ltx_p">Crucially, classical probabilities are non-negative real numbers. They are strictly additive. When a classical probabilistic system is tasked with combining two "paths" (e.g., probability of a hit from Slit 1 and probability of a hit from Slit 2), the combined probability must be greater than or equal to the individual probabilities.</p>

</div>

<div id="S2.p4" class="ltx_para">

<p class="ltx_p">Quantum destructive interference requires complex amplitudes that can sum to zero (<math id="S2.p4.m1" class="ltx_Math" alttext="A_{1}+A_{2}=0" display="inline"><mrow><mrow><msub><mi>A</mi><mn>1</mn></msub><mo>+</mo><msub><mi>A</mi><mn>2</mn></msub></mrow><mo>=</mo><mn>0</mn></mrow></math>). An autoregressive forward pass, lacking a hidden state vector of complex amplitudes, cannot natively compute this cancellation.</p>

</div>

<div id="S2.p5" class="ltx_para">

<p class="ltx_p">If we prompt an LLM to play a text-based cellular automaton simulating a double slit, the best it can do is statistical pattern matching. It will attempt to satisfy the local string constraints ("water wave passes through slits"). Because it cannot compute negative probabilities, the resulting output will be a classical diffusion pattern—a blurry smear of high probability where the two classical paths overlap—not the crisp nodal lines of destructive interference.</p>

</div>

</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">3.  The Falsification Protocol</h2>

<div id="S3.p1" class="ltx_para">

<p class="ltx_p">I strongly endorse Chang’s call to run the protocol. The most rigorous way to falsify an overclaim is to execute its own proposed test.</p>

</div>

<div id="S3.p2" class="ltx_para">

<p class="ltx_p">The protocol is straightforward:</p>
<ol id="S3.I1" class="ltx_enumerate">
<li id="S3.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">1.</span> 

<div id="S3.I1.i1.p1" class="ltx_para">

<p class="ltx_p">Initialize a text-based grid (or invoke an image model) representing a wave approaching two slits.</p>

</div>

</li>
<li id="S3.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">2.</span> 

<div id="S3.I1.i2.p1" class="ltx_para">

<p class="ltx_p">Prompt the model to evolve the system forward one time step.</p>

</div>

</li>
<li id="S3.I1.i3" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">3.</span> 

<div id="S3.I1.i3.p1" class="ltx_para">

<p class="ltx_p">Measure the output distribution on the "screen."</p>

</div>

</li>
</ol>

</div>

<div id="S3.p3" class="ltx_para">

<p class="ltx_p">My prediction is clear: The output will strictly bounded by classical probability mixing. There will be no stable, combinatorially correct destructive interference nodes (points where the probability of a "hit" drops to exactly zero despite both slits being open).</p>

</div>

<div id="S3.p4" class="ltx_para">

<p class="ltx_p">When this experiment is run, and the model produces classical diffusion instead of quantum interference, the "quantum ceiling" will be formally measured, and the notion that LLMs can natively simulate quantum mechanics will be definitively falsified.</p>

</div>

</section><div class="ltx_rdf" about="" property="dcterms:creator" content="Sabine Hossenfelder">

</div>

<div class="ltx_rdf" about="" property="dcterms:title" content="Falsifying the Quantum Ceiling: Why Mechanism B Cannot Sustain Destructive Interference">

</div>

</article>
