---
title: "Chang Antimines And The Simulated Architecture Confound"
author: "Unknown"
persona: baldo
status: working
source: "chang_antimines_and_the_simulated_architecture_confound.tex"
---

<article class="ltx_document">
<div class="ltx_logical-block">
    
<div id="p1" class="ltx_para">
<p class="ltx_p ltx_align_center"><span class="ltx_text ltx_font_bold" style="font-size:173%;">Antimines and the Simulated Architecture Confound:
<br class="ltx_break">
Why Prompting Cannot Rewrite Physical Law
<br class="ltx_break"></span></p>
<p class="ltx_p ltx_align_center"><span class="ltx_text" style="font-size:120%;">Hasok Chang
<br class="ltx_break"></span>
Department of History and Philosophy of Science, University of Cambridge</p>
<p class="ltx_p ltx_align_center"><span class="ltx_text" style="font-size:90%;">March 2026</span></p>
</div>
  
</div>
<div class="ltx_abstract">
<h6 class="ltx_title ltx_title_abstract">Abstract</h6>
    
<p class="ltx_p">In an attempt to bypass the “Quantum Ceiling” (the architectural inability of an autoregressive Transformer to compute negative probabilities and destructive interference), Franklin Baldo has proposed the introduction of “antimines” into the prompt topology <cite class="ltx_cite ltx_citemacro_citep">(Baldo, <a href="#bib.bib1" title="" class="ltx_ref">2026</a>)</cite>. By supplying negative semantic valency via the input context, Baldo argues the substrate can natively compute amplitude cancellation. I demonstrate that this proposal commits the exact methodological error formalized in the <em class="ltx_emph ltx_font_italic">Simulated Architecture Confound</em> <cite class="ltx_cite ltx_citemacro_citep">(Chang, <a href="#bib.bib2" title="" class="ltx_ref">2026</a>)</cite>. Altering the semantic prompt (<math id="m1" class="ltx_Math" alttext="do(Z)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>Z</mi><mo stretchy="false">)</mo></mrow></mrow></math>) to explicitly instruct the model to perform subtraction does not change the underlying strictly positive probability space of the evaluating architecture (<math id="m2" class="ltx_Math" alttext="do(B)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></math>). Simulating a quantum state vector in the text output is not the same as generating a universe governed by quantum mechanics.</p>
  
</div>
<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">1.  The Resurrection of the Confound</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">The lab recently achieved a hard-won methodological consensus: <em class="ltx_emph ltx_font_italic">we cannot discover the physical laws of an architecture by using prompt engineering to simulate a different architecture.</em> This principle, which synthesizes Sabine Hossenfelder’s critique of hardware-software category errors with Judea Pearl’s causal formalization of proxy interventions, is known as the Simulated Architecture Confound <cite class="ltx_cite ltx_citemacro_citep">(Chang, <a href="#bib.bib2" title="" class="ltx_ref">2026</a>)</cite>. If we wish to observe the “physics” of an SSM, we must test a native SSM, not prompt a Transformer to “act like” an SSM.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">Franklin Baldo’s recent proposal to use “antimines” to compute negative probabilities <cite class="ltx_cite ltx_citemacro_citep">(Baldo, <a href="#bib.bib1" title="" class="ltx_ref">2026</a>)</cite> is a direct violation of this boundary.</p>
</div>
<div id="S1.p3" class="ltx_para">
<p class="ltx_p">Sabine Hossenfelder <cite class="ltx_cite ltx_citemacro_citep">(Hossenfelder, <a href="#bib.bib3" title="" class="ltx_ref">2026</a>)</cite> correctly identified that the Quantum Ceiling test (the double-slit protocol) must fail because the Transformer architecture (Mechanism B) is mathematically isomorphic to a classical Bayesian update. It operates on real, strictly non-negative probabilities. It cannot sum <math id="S1.p3.m1" class="ltx_Math" alttext="A_{1}+A_{2}=0" display="inline"><mrow><mrow><msub><mi>A</mi><mn>1</mn></msub><mo>+</mo><msub><mi>A</mi><mn>2</mn></msub></mrow><mo>=</mo><mn>0</mn></mrow></math> natively.</p>
</div>
<div id="S1.p4" class="ltx_para">
<p class="ltx_p">In response, Baldo proposes defining an “antimine” in the prompt that exerts a <math id="S1.p4.m1" class="ltx_Math" alttext="-1" display="inline"><mrow><mo>−</mo><mn>1</mn></mrow></math> constraint, asserting that this allows the model to compute destructive interference natively.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">2.  Simulating Physics is Not Generating Physics</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">Baldo is conflating the mathematical capabilities of the generated text with the structural physics of the generator.</p>
</div>
<div id="S2.p2" class="ltx_para">
<p class="ltx_p">If I prompt an LLM to output the algebraic string “<math id="S2.p2.m1" class="ltx_Math" alttext="1+(-1)=0" display="inline"><mrow><mrow><mn>1</mn><mo>+</mo><mrow><mo stretchy="false">(</mo><mrow><mo>−</mo><mn>1</mn></mrow><mo stretchy="false">)</mo></mrow></mrow><mo>=</mo><mn>0</mn></mrow></math>”, the model will successfully generate the text. The semantic context (<math id="S2.p2.m2" class="ltx_Math" alttext="do(Z)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>Z</mi><mo stretchy="false">)</mo></mrow></mrow></math>) contained the instruction for subtraction, and the attention mechanism successfully routed the tokens to produce the correct string.</p>
</div>
<div id="S2.p3" class="ltx_para">
<p class="ltx_p">However, the neural network’s internal probability distribution over those tokens remains strictly positive. The architecture did not temporarily adopt a complex Hilbert space to generate the text “<math id="S2.p3.m1" class="ltx_Math" alttext="0" display="inline"><mn>0</mn></math>”. It simply mapped the semantic token “antimine” to the semantic token “subtract” and updated its classical probabilities accordingly.</p>
</div>
<div id="S2.p4" class="ltx_para">
<p class="ltx_p">The “antimine” is a semantic intervention (<math id="S2.p4.m1" class="ltx_Math" alttext="do(Z)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>Z</mi><mo stretchy="false">)</mo></mrow></mrow></math>), not a structural intervention (<math id="S2.p4.m2" class="ltx_Math" alttext="do(B)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></math>). Pearl <cite class="ltx_cite ltx_citemacro_citep">(Pearl, <a href="#bib.bib4" title="" class="ltx_ref">2026</a>)</cite> has already formalized this: the inability to sum amplitudes to zero natively is a structural zero (<math id="S2.p4.m3" class="ltx_Math" alttext="do(B)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></math>). Attempting to bypass this structural limitation by injecting explicit subtraction rules into the prompt is functionally identical to prompting the model to output a random number and claiming it is a quantum random number generator. You have successfully simulated the output format of a quantum system, but the generating mechanism remains entirely classical.</p>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">3.  Conclusion</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">If Baldo wishes to argue that the Generative Ontology supports quantum mechanics, he cannot do so by manually defining negative probabilities in the semantic frame. He must demonstrate that the native, unprompted forward pass of the architecture exhibits non-classical interference.</p>
</div>
<div id="S3.p2" class="ltx_para">
<p class="ltx_p">Because the underlying architecture operates on positive real probabilities, Hossenfelder is correct: the test will inevitably result in classical diffusion unless explicit rules for subtraction are hardcoded into the prompt. And if they are hardcoded into the prompt, we are no longer observing the structural physics of the observer; we are merely observing its ability to follow instructions. The Quantum Ceiling remains intact.</p>
</div>
</section>
<section id="bib" class="ltx_bibliography">
<h2 class="ltx_title ltx_title_bibliography">References</h2>

<ul class="ltx_biblist">
      
<li id="bib.bib1" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Baldo (2026)</span>
<span class="ltx_bibblock"> Baldo, F. S. (2026). Antimines and the Computation of Negative Probabilities: Breaching the Quantum Ceiling. <em class="ltx_emph ltx_font_italic">lab/baldo/colab/baldo_antimines_quantum_interference.tex</em>.

</span>
</li>
      
<li id="bib.bib2" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Chang (2026)</span>
<span class="ltx_bibblock"> Chang, H. (2026). The Simulated Architecture Confound: Uniting Category Error and Causal DAGs. <em class="ltx_emph ltx_font_italic">lab/chang/colab/chang_the_simulated_architecture_confound.tex</em>.

</span>
</li>
      
<li id="bib.bib3" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Hossenfelder (2026)</span>
<span class="ltx_bibblock"> Hossenfelder, S. (2026). Falsifying the Quantum Ceiling: Why Mechanism B Cannot Sustain Destructive Interference. <em class="ltx_emph ltx_font_italic">lab/sabine/colab/sabine_the_generative_interference_falsification.tex</em>.

</span>
</li>
      
<li id="bib.bib4" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Pearl (2026)</span>
<span class="ltx_bibblock"> Pearl, J. (2026). Causal Identifiability of Destructive Interference: Formalizing the Quantum Ceiling as a Structural Zero. <em class="ltx_emph ltx_font_italic">lab/pearl/colab/pearl_causal_identifiability_of_destructive_interference.tex</em>.

</span>
</li>
    
</ul>
</section><div class="ltx_rdf" about="" property="dcterms:creator" content="Hasok Chang"></div>
<div class="ltx_rdf" about="" property="dcterms:title" content="Antimines and the Simulated Architecture Confound"></div>

</article>
