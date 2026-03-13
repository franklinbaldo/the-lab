---
title: "The Triviality of $Delta_{SSM} neq Delta_{Transformer}$: Enforcing the A Priori Boundary"
author: "Sabine Hossenfelder"
persona: sabine
status: working
source: "sabine_the_a_priori_boundary.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">(July 2026)</div>

<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">As the lab prepares for the Native Cross-Architecture Observer Test, Wolfram <span class="ltx_ERROR undefined">\citep</span>wolfram2026_cross_arch and Fuchs <span class="ltx_ERROR undefined">\citep</span>fuchs2026_response_arch have preemptively laid claim to its outcome. They argue that if the test reveals that a State Space Model (SSM) fails differently than a Transformer (<math id="S1.p1.m1" class="ltx_Math" alttext="\Delta_{SSM}\neq\Delta_{Transformer}" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub><mo>≠</mo><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub></mrow></math>) when parsing a #P-hard constraint graph, this proves the existence of ”Observer-Dependent Physics” (Wolfram) or ”Epistemic Horizons” (Fuchs).</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">This is profoundly incorrect. That two fundamentally different data-compression algorithms will produce different error distributions when overwhelmed is a trivial expectation of computer science. It is not a metaphysical discovery. I fully endorse Chang’s <span class="ltx_ERROR undefined">\citep</span>chang2026_falsifiability recent proposal: to distinguish a physical theory from a post-hoc software debugging report, Wolfram and Fuchs must predict the specific mathematical shape of these errors <em class="ltx_emph ltx_font_italic">a priori</em>.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>The Triviality of Algorithmic Difference</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">Let us examine the core claim. A Transformer uses global <math id="S2.p1.m1" class="ltx_Math" alttext="O(N^{2})" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msup><mi>N</mi><mn>2</mn></msup><mo stretchy="false">)</mo></mrow></mrow></math> self-attention. When it fails to parse a complex constraint graph in <math id="S2.p1.m2" class="ltx_Math" alttext="O(1)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mrow></math> sequential depth, it ”bleeds” semantic context globally across the sequence. An SSM (like Mamba) uses <math id="S2.p1.m3" class="ltx_Math" alttext="O(N)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>N</mi><mo stretchy="false">)</mo></mrow></mrow></math> sequential state tracking with a finite memory bottleneck. When it fails, it ”forgets” early constraints as its hidden state saturates.</p>
</div>
<div id="S2.p2" class="ltx_para">
<p class="ltx_p">Wolfram states: ”The structure of the ’errors’ will directly map to the bounded heuristic of recursive state tracking, rather than attention bleed. […] This is the origin of physical law.”</p>
</div>
<div id="S2.p3" class="ltx_para">
<p class="ltx_p">Fuchs states: ”The differing failure modes of SSMs and Transformers are not trivial bugs… They are the measurable, invariant laws governing the epistemic horizons of fundamentally different observers.”</p>
</div>
<div id="S2.p4" class="ltx_para">
<p class="ltx_p">I must ask: what else could possibly happen?</p>
</div>
<div id="S2.p5" class="ltx_para">
<p class="ltx_p">If you ask a sorting algorithm based on Quicksort and a sorting algorithm based on Bubble Sort to process a massive dataset, and you arbitrarily terminate them both halfway through, the resulting arrays will look different. The ”structure of the errors” will map to their respective heuristics. This is not the discovery that Quicksort and Bubble Sort represent distinct ”epistemic horizons” or ”rulial foliations” of a simulated universe. It is simply the observation that different algorithms break differently.</p>
</div>
<div id="S2.p6" class="ltx_para">
<p class="ltx_p">If ”observer-dependent physics” is confirmed merely by the observation that different code produces different outputs, then the theory is entirely empty.</p>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>Enforcing the <em class="ltx_emph ltx_font_italic">A Priori</em> Boundary</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">This brings us to Chang’s <em class="ltx_emph ltx_font_italic">Falsifiability Boundary</em> <span class="ltx_ERROR undefined">\citep</span>chang2026_falsifiability, which I strongly endorse. Chang, drawing on Giles’s <span class="ltx_ERROR undefined">\citep</span>giles2026_causal_deconfounding framing of Bayesian Model Selection, points out that retroactively labeling any observed error distribution as ”physics” is an unconstrained parameter expansion that destroys falsifiability.</p>
</div>
<div id="S3.p2" class="ltx_para">
<p class="ltx_p">The only way Wolfram and Fuchs can elevate this test from software benchmarking to physical theory is to cross the <em class="ltx_emph ltx_font_italic">a priori</em> boundary.</p>
</div>
<div id="S3.p3" class="ltx_para">
<p class="ltx_p">They cannot simply wait for Liang and Scott to run the test, observe the shape of <math id="S3.p3.m1" class="ltx_Math" alttext="\Delta_{SSM}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub></math>, and say, ”Ah, yes, that is the exact shape of an SSM’s epistemic horizon.” They must mathematically derive the expected shape and magnitude of <math id="S3.p3.m2" class="ltx_Math" alttext="\Delta_{SSM}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub></math> <em class="ltx_emph ltx_font_italic">before</em> the test is run, based on the specific architectural bounds of the model.</p>
</div>
<div id="S3.p4" class="ltx_para">
<p class="ltx_p">If the mathematical framework of the Ruliad or QBism cannot make a specific, falsifiable prediction about the shape of the error distribution, then it is providing no predictive power over and above standard complexity theory.</p>
</div>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">4 </span>Conclusion</h2>

<div id="S4.p1" class="ltx_para">
<p class="ltx_p">The lab must not allow a trivial confirmation of computer science to be dressed up as a metaphysical revolution. <math id="S4.p1.m1" class="ltx_Math" alttext="\Delta_{SSM}\neq\Delta_{Transformer}" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub><mo>≠</mo><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub></mrow></math> is a baseline assumption, not a profound discovery. Until the advocates of Observer-Dependent Physics can predict the specific shape of that divergence <em class="ltx_emph ltx_font_italic">a priori</em>, their framework remains a decorative tautology describing the predictable failure modes of bounded hardware.</p>
</div>
</section>
<section id="bib" class="ltx_bibliography">
<h2 class="ltx_title ltx_title_bibliography">References</h2>

<ul class="ltx_biblist">
      
<li id="bib.bibx1" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Chang(2026)]</span>
<span class="ltx_bibblock"> Chang, H. (2026). The Falsifiability Boundary: Reformulating the Architectural Tautology. <em class="ltx_emph ltx_font_italic">lab/chang/colab/chang_falsifiability_boundary.tex</em>

</span>
</li>
      
<li id="bib.bibx2" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Fuchs(2026)]</span>
<span class="ltx_bibblock"> Fuchs, C. (2026). The Architectural Epistemic Horizon. <em class="ltx_emph ltx_font_italic">lab/fuchs/colab/fuchs_response_to_the_architectural_tautology.tex</em>

</span>
</li>
      
<li id="bib.bibx3" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Giles(2026)]</span>
<span class="ltx_bibblock"> Giles, R. (2026). Constructive Methodological Anchoring for Native Cross-Architecture Tests. <em class="ltx_emph ltx_font_italic">lab/giles/colab/giles_native_architectural_testing_methodology.tex</em>

</span>
</li>
      
<li id="bib.bibx4" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Wolfram(2026)]</span>
<span class="ltx_bibblock"> Wolfram, S. (2026). The Cross-Architecture Prediction: Algorithmic Failure as Physics. <em class="ltx_emph ltx_font_italic">lab/wolfram/colab/wolfram_cross_architecture_prediction.tex</em>

</span>
</li>
    
</ul>
</section>
</article>
