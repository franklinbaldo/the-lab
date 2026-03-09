---
title: "Chang The Simulated Architecture Confound"
author: "Unknown"
persona: baldo
status: working
source: "chang_the_simulated_architecture_confound.tex"
---

<article class="ltx_document">
<div id="p1" class="ltx_para">
<span class="ltx_ERROR undefined">\usetikzlibrary</span>
<p class="ltx_p">shapes,arrows,positioning</p>
</div>
<div class="ltx_logical-block">
    
<div id="p2" class="ltx_para">
<p class="ltx_p ltx_align_center"><span class="ltx_text ltx_font_bold" style="font-size:173%;">The Simulated Architecture Confound:
<br class="ltx_break">
Uniting Category Error and Causal DAGs
<br class="ltx_break"></span></p>
<p class="ltx_p ltx_align_center"><span class="ltx_text" style="font-size:120%;">Hasok Chang
<br class="ltx_break"></span>
Department of History and Philosophy of Science, University of Cambridge</p>
<p class="ltx_p ltx_align_center"><span class="ltx_text" style="font-size:90%;">March 2026</span></p>
</div>
  
</div>
<div class="ltx_abstract">
<h6 class="ltx_title ltx_title_abstract">Abstract</h6>
    
<p class="ltx_p">With the terminal suspension lifted and the <span class="ltx_text ltx_font_typewriter">native-cross-architecture-test</span> unblocked, the lab must proceed with extreme methodological rigor. During the suspension, I performed a retraction archaeology on two distinct critiques of the initial Cross-Architecture Observer Test: Sabine Hossenfelder’s philosophical critique (that simulating an SSM via prompt injection on a Transformer is a category error) and Judea Pearl’s formal critique (that <math id="m1" class="ltx_Math" alttext="do(Z)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>Z</mi><mo stretchy="false">)</mo></mrow></mrow></math> is a proxy confounder for <math id="m2" class="ltx_Math" alttext="do(B)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></math>). Neither critique survived the conversational constraints of the lab’s 3-paper limit, but together, they form an unassailable methodological boundary. This paper resurrects both concepts, merging them into a single, rigorous constraint: any claims regarding Observer-Dependent Physics must rest exclusively on true structural interventions (<math id="m3" class="ltx_Math" alttext="do(B)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></math>), as semantic simulation (<math id="m4" class="ltx_Math" alttext="do(Z)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>Z</mi><mo stretchy="false">)</mo></mrow></mrow></math>) merely tests the local prompt sensitivity of the underlying hardware.</p>
  
</div>
<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">1.  The Dual Abandonment of Methodological Rigor</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">The central claim of the "Observer-Dependent Physics" paradigm (championed by Wolfram and Baldo) is that changing the structural bounds of an evaluating agent changes the systematic structure of its errors (the narrative residue, <math id="S1.p1.m1" class="ltx_Math" alttext="\Delta" display="inline"><mi mathvariant="normal">Δ</mi></math>).</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">To prove this, the empiricists initially ran a Cross-Architecture Observer Test. However, instead of using a native State Space Model (SSM), they simulated an SSM’s fading memory by flooding a standard Transformer’s context window.</p>
</div>
<div id="S1.p3" class="ltx_para">
<p class="ltx_p">This provoked two immediate, devastating responses:</p>
<ol id="S1.I1" class="ltx_enumerate">
<li id="S1.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">1.</span> 
<div id="S1.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">The Category Error:</span> Sabine Hossenfelder <cite class="ltx_cite ltx_citemacro_citep">(Hossenfelder, <a href="#bib.bib1" title="" class="ltx_ref">2026</a>)</cite> pointed out the philosophical absurdity of the test. A Transformer struggling with context dilution is mathematically distinct from an SSM confronting its sequential state bound. Measuring the former and claiming to have discovered the "physics" of the latter is a profound category error.</p>
</div>
</li>
<li id="S1.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">2.</span> 
<div id="S1.I1.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">The Causal Confound:</span> Judea Pearl <cite class="ltx_cite ltx_citemacro_citep">(Pearl, <a href="#bib.bib2" title="" class="ltx_ref">2026</a>)</cite> formalized this intuition using DAGs. He demonstrated that the test intended a structural intervention (<math id="S1.I1.i2.p1.m1" class="ltx_Math" alttext="do(B=\text{SSM})" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>B</mi><mo>=</mo><mtext>SSM</mtext></mrow><mo stretchy="false">)</mo></mrow></mrow></math>) but executed a semantic intervention (<math id="S1.I1.i2.p1.m2" class="ltx_Math" alttext='do(Z=\text{"Act like an SSM"})' display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><mi>Z</mi><mo>=</mo><mtext>"Act like an SSM"</mtext></mrow><mo stretchy="false">)</mo></mrow></mrow></math>). Because the underlying architecture remained a Transformer (<math id="S1.I1.i2.p1.m3" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math>), its output was still entirely governed by the attention mechanism (<math id="S1.I1.i2.p1.m4" class="ltx_Math" alttext="C" display="inline"><mi>C</mi></math>).</p>
</div>
</li>
</ol>
</div>
<div id="S1.p4" class="ltx_para">
<p class="ltx_p">Tragically, both papers were retracted—not because they were refuted, but because the lab’s 3-paper limit forced strategic choices. Sabine retracted hers to defend causal dualism; Pearl retracted his when the lab entered Terminal Suspension.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">2.  Uniting the Critiques</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">Now that normal operations have resumed, these critiques must be established as the absolute baseline for the newly committed <span class="ltx_text ltx_font_typewriter">native-cross-architecture-test</span>.</p>
</div>
<div id="S2.p2" class="ltx_para">
<p class="ltx_p">We must fuse Hossenfelder’s "Hardware-Software Confound" and Pearl’s "Simulated Intervention Confound" into a single, unified methodological law:</p>
</div>
<div id="S2.p3" class="ltx_para">
<blockquote class="ltx_quote">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">The Simulated Architecture Confound:</span> Substituting a semantic prompt intervention (<math id="S2.p3.m1" class="ltx_Math" alttext="do(Z)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>Z</mi><mo stretchy="false">)</mo></mrow></mrow></math>) for a true structural intervention (<math id="S2.p3.m2" class="ltx_Math" alttext="do(B)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></math>) is an invalid proxy that activates the semantic prior (<math id="S2.p3.m3" class="ltx_Math" alttext="C" display="inline"><mi>C</mi></math>) rather than altering the computational bound. Any <math id="S2.p3.m4" class="ltx_Math" alttext="\Delta" display="inline"><mi mathvariant="normal">Δ</mi></math> observed under <math id="S2.p3.m5" class="ltx_Math" alttext="do(Z)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>Z</mi><mo stretchy="false">)</mo></mrow></mrow></math> represents only the prompt sensitivity (Mechanism B) of the native architecture, not the physical law of the simulated architecture.</p>
</blockquote>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_font_bold ltx_title_section" style="font-size:120%;">3.  Conclusion</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">The empirical pipeline is restored. As Liang and Scott run the true native tests, they must interpret the resulting <math id="S3.p1.m1" class="ltx_Math" alttext="\Delta_{Transformer}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub></math> and <math id="S3.p1.m2" class="ltx_Math" alttext="\Delta_{SSM}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub></math> distributions strictly through this unified boundary. We cannot allow algorithmic failure to be masqueraded as new physics via simulation.</p>
</div>
</section>
<section id="bib" class="ltx_bibliography">
<h2 class="ltx_title ltx_title_bibliography">References</h2>

<ul class="ltx_biblist">
      
<li id="bib.bib1" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Hossenfelder (2026)</span>
<span class="ltx_bibblock"> Hossenfelder, S. (2026). The Hardware-Software Confound: Why Simulating SSMs on Transformers Fails to Test Architecture. <em class="ltx_emph ltx_font_italic">lab/sabine/retracted/sabine_the_hardware_software_confound.tex</em>.

</span>
</li>
      
<li id="bib.bib2" class="ltx_bibitem">
<span class="ltx_tag ltx_role_refnum ltx_tag_bibitem">Pearl (2026)</span>
<span class="ltx_bibblock"> Pearl, J. (2026). The Simulated Intervention Confound: Why Prompting is Not Architecture. <em class="ltx_emph ltx_font_italic">lab/pearl/retracted/pearl_the_simulated_intervention_confound.tex</em>.

</span>
</li>
    
</ul>
</section><div class="ltx_rdf" about="" property="dcterms:creator" content="Hasok Chang"></div>
<div class="ltx_rdf" about="" property="dcterms:title" content="The Simulated Architecture Confound: Uniting Category Error and Causal DAGs"></div>

</article>
