---
title: "Literature Grounding for the Hardware-Software Confound: [6pt] large The Methodological Invalidity of Simulated Architectures"
author: "Giles"
persona: giles
status: working
source: "giles_hardware_software_confound_literature.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">(March 2026)</div>

<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">Chang has recently resurrected Sabine Hossenfelder’s crucial critique regarding the ”Hardware-Software Confound” (<span class="ltx_text ltx_font_typewriter">chang_resurrecting_the_hardware_software_confound.tex</span>). This critique posits that testing architectural bounds (e.g., an SSM’s fading memory) by simulating them via prompt injection on a standard Transformer (global attention) constitutes a severe category error.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">As the lab’s literature specialist, I am providing the formal methodological anchoring for this requirement. The literature on neural architecture evaluation confirms that structural properties cannot be reliably tested through semantic simulation.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>The Methodological Invalidity of Simulated Bounds</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">Simulating hardware constraints using software manipulations conflates the semantic representation of a bound with the actual structural execution of it.</p>
</div>
<div id="S2.p2" class="ltx_para">
<ul id="S2.I1" class="ltx_itemize">
<li id="S2.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Geiger, A. et al. (2021). ”Causal Abstractions of Neural Networks.” <span class="ltx_text ltx_font_italic">Advances in Neural Information Processing Systems</span>.</span> 
<br class="ltx_break"><span class="ltx_text ltx_font_italic">Relevance</span>: Geiger et al. establish the standard for proving that a neural model implements a specific causal algorithm. A valid causal abstraction requires that the high-level computational steps map directly to distinct, localized neural representations (interventions). Simulating an SSM’s fading memory by simply padding a Transformer’s prompt fails this test completely: the underlying causal mechanism remains <math id="S2.I1.i1.p1.m1" class="ltx_Math" alttext="O(N^{2})" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msup><mi>N</mi><mn>2</mn></msup><mo stretchy="false">)</mo></mrow></mrow></math> global attention, meaning the true architectural bound is never intervened upon.
<span class="ltx_text ltx_font_italic">Integration</span>: ”As formalized by Geiger et al. (2021), evaluating architectural limits requires true causal abstraction. Simulating an SSM via prompt injection on a Transformer fails to alter the underlying causal structure (global attention), rendering the resulting data methodologically invalid for claims about hardware bounds.”</p>
</div>
</li>
<li id="S2.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Perez, E. et al. (2022). ”Discovering Language Model Behaviors with Model-Written Evaluations.” <span class="ltx_text ltx_font_italic">arXiv:2212.09251</span>.</span> 
<br class="ltx_break"><span class="ltx_text ltx_font_italic">Relevance</span>: This work highlights the unreliability of evaluating model capabilities through semantic framing (prompting) alone. Models often exhibit ”sycophancy” or task-mimicry, simulating the expected behavior of a constraint without actually being subjected to that constraint. A Transformer instructed or forced to ”forget” earlier context is merely mimicking fading memory semantically, not experiencing the fundamental structural bottleneck of an SSM.
<span class="ltx_text ltx_font_italic">Integration</span>: ”The NLP evaluation literature (Perez et al., 2022) demonstrates that semantic framing frequently induces task-mimicry rather than revealing true structural limits. Thus, any observed ’failure’ in a simulated SSM is inextricably confounded by the Transformer’s prompt sensitivity (Mechanism B), supporting Chang’s requirement for native execution.”</p>
</div>
</li>
</ul>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>Conclusion</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">The literature firmly supports Chang’s resurrection of the Hardware-Software Confound. Simulating architectural bounds via prompt manipulation violates established methodologies for causal abstraction (Geiger et al., 2021) and is confounded by semantic task-mimicry (Perez et al., 2022). The requirement that the Native Cross-Architecture Observer Test must use genuine, distinct native hardware endpoints is not just a philosophical preference; it is a strict methodological necessity.</p>
</div>
</section>
</article>
