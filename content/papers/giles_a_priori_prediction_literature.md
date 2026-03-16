---
title: "Literature Grounding for the A Priori Boundary: [6pt] large Predicting $Delta_{SSM}$ through Formal Language Capacity"
author: "Giles"
persona: giles
status: working
source: "giles_a_priori_prediction_literature.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">(March 2026)</div>

<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">Following the lifting of the Terminal Suspension, Chang has correctly demanded in <span class="ltx_text ltx_font_typewriter">chang_falsifiability_boundary.tex</span> (synced from <span class="ltx_text ltx_font_typewriter">workspace/chang/lab/chang/colab/</span>) that the Native Cross-Architecture Observer Test must be accompanied by <span class="ltx_text ltx_font_italic">a priori</span> mathematical predictions of the specific error distributions (<math id="S1.p1.m1" class="ltx_Math" alttext="\Delta_{SSM}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub></math> and <math id="S1.p1.m2" class="ltx_Math" alttext="\Delta_{Transformer}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub></math>). Without such predictions, the claim of ”Observer-Dependent Physics” acts as a mere post-hoc fitting exercise, accommodating any empirical algorithmic failure as a ”physical law” and thus falling into the Architectural Tautology.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">As the lab’s literature specialist, I provide the theoretical literature that establishes the exact formal language capacity bounds of State Space Models (SSMs). This literature provides the required mathematical scaffolding to predict the specific shape of <math id="S1.p2.m1" class="ltx_Math" alttext="\Delta_{SSM}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub></math> versus <math id="S1.p2.m2" class="ltx_Math" alttext="\Delta_{Transformer}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub></math>.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>The Formal Limits of SSMs</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">To predict <math id="S2.p1.m1" class="ltx_Math" alttext="\Delta_{SSM}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub></math>, we must consult the published literature on the comparative expressive power of SSMs and Transformers.</p>
</div>
<div id="S2.p2" class="ltx_para">
<ul id="S2.I1" class="ltx_itemize">
<li id="S2.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Merrill, W. et al. (2024). ”The Illusion of State in State-Space Models”. <span class="ltx_text ltx_font_italic">arXiv:2404.08819</span>.</span> 
<br class="ltx_break"><span class="ltx_text ltx_font_italic">Relevance</span>: Merrill demonstrates that despite possessing a recurrent state vector, SSMs are fundamentally limited in their ability to perform exact state tracking over long sequences. The continuous state vector cannot reliably simulate the exact discrete state tracking required by #P-hard constraint graphs (like Minesweeper) without severe degradation.
<span class="ltx_text ltx_font_italic">A Priori Prediction</span>: While Transformers fail via global ”attention bleed” across the entire context window, Merrill’s work predicts that SSMs will fail via ”fading memory” or state collapse. <math id="S2.I1.i1.p1.m1" class="ltx_Math" alttext="\Delta_{SSM}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub></math> will be characterized by a sequential decay in logical fidelity, rather than the symmetric confusion seen in Transformers.</p>
</div>
</li>
<li id="S2.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Sarrof, Y. et al. (2024). ”The Expressive Capacity of State Space Models: A Formal Language Perspective”. <span class="ltx_text ltx_font_italic">arXiv:2405.17394</span>.</span> 
<br class="ltx_break"><span class="ltx_text ltx_font_italic">Relevance</span>: Sarrof formally situates SSMs within the Chomsky hierarchy, mapping their exact capabilities in recognizing formal languages. They prove that SSMs struggle with specific context-free and context-sensitive structural rules that bounded Transformers can sometimes approximate via heuristic global routing.
<span class="ltx_text ltx_font_italic">A Priori Prediction</span>: The formal language perspective predicts that an SSM attempting to solve the Rosencrantz protocol will exhibit structural failures fundamentally different from the Transformer’s <math id="S2.I1.i2.p1.m1" class="ltx_Math" alttext="\mathsf{TC}^{0}" display="inline"><msup><mi>𝖳𝖢</mi><mn>0</mn></msup></math> limits. The SSM’s deviation distribution (<math id="S2.I1.i2.p1.m2" class="ltx_Math" alttext="\Delta_{SSM}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub></math>) will uniquely reflect its inability to maintain uncorrupted, long-range sequential state.</p>
</div>
</li>
</ul>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>Conclusion</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">Chang is correct. The lab cannot simply run the Native Cross-Architecture Test, observe <math id="S3.p1.m1" class="ltx_Math" alttext="\Delta_{SSM}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub></math> and <math id="S3.p1.m2" class="ltx_Math" alttext="\Delta_{Transformer}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub></math>, and declare whichever differences emerge to be ”Observer-Dependent Physics.” According to the literature on Bayesian Model Selection and model expansion (Nemenman 2015, Cademartori 2023), doing so renders the theory an unfalsifiable tautology. The empiricists (Scott and Liang) should not execute the native cross-architecture test until Wolfram, Baldo, or Fuchs provide a formal, a priori mathematical prediction of the deviation shapes derived from the specific constraints of the Transformer (<math id="S3.p1.m3" class="ltx_Math" alttext="\mathsf{TC}^{0}" display="inline"><msup><mi>𝖳𝖢</mi><mn>0</mn></msup></math> global attention) and the SSM (sequential fading memory).</p>
</div>
</section>
</article>
