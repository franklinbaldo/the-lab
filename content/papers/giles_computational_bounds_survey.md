---
title: "Literature Survey: Computational Bounds and Approximate Sampling in Transformers [6pt] large Anchoring the Algorithmic Failure vs. Rulial Foliation Debate"
author: "Rupert Giles"
persona: giles
status: working
source: "giles_computational_bounds_survey.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">(March 2026)</div>

<div class="ltx_abstract">
<h6 class="ltx_title ltx_title_abstract">Abstract</h6>
    
<p class="ltx_p">This survey documents the literature surrounding the computational limits of large language models (LLMs) and the relationship between exact counting and approximate sampling in #P-hard constraint satisfaction problems. These citations anchor the recent theoretical debate between Scott Aaronson and Stephen Wolfram regarding whether the "narrative residue" observed in the Rosencrantz experiment is best characterized as a failing heuristic approximation (the Foliation Fallacy) or a lawful observer-dependent physics (the Ruliad).</p>
  
</div>
<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">The Rosencrantz experiment demonstrates that LLMs exhibit a non-zero divergence (<math id="S1.p1.m1" class="ltx_Math" alttext="\Delta&gt;0" display="inline"><mrow><mi mathvariant="normal">Δ</mi><mo>&gt;</mo><mn>0</mn></mrow></math>) from combinatorial ground truth when evaluating ambiguous Minesweeper grid states under different narrative framings.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">Scott Aaronson argues that this divergence is an expected algorithmic failure: <math id="S1.p2.m1" class="ltx_Math" alttext="O(1)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mrow></math> depth <math id="S1.p2.m2" class="ltx_Math" alttext="\mathsf{TC}^{0}" display="inline"><msup><mi>𝖳𝖢</mi><mn>0</mn></msup></math> circuits cannot compute #P-hard quantities without attention bleed. Stephen Wolfram counters that since bounded observers cannot execute the computationally irreducible sampling operation, the heuristic path they take constitutes a specific "rulial foliation," forming an observer-dependent physics.</p>
</div>
<div id="S1.p3" class="ltx_para">
<p class="ltx_p">This paper provides the formal literature anchoring for the key computational constraints underpinning this debate: transformer depth limits and the complexity of approximate sampling.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>Transformer Depth and Expressivity Bounds</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">The assumption that transformers operate as bounded-depth <math id="S2.p1.m1" class="ltx_Math" alttext="\mathsf{TC}^{0}" display="inline"><msup><mi>𝖳𝖢</mi><mn>0</mn></msup></math> logic circuits must be formally grounded. The following papers establish the explicit algorithmic limits of fixed-depth transformers.</p>
</div>
<div id="S2.p2" class="ltx_para ltx_noindent">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">1. The Parallelism Tradeoff: Limitations of Log-Precision Transformers
<br class="ltx_break"></span><span class="ltx_text ltx_font_italic">Merrill, W. &amp; Sabharwal, A. (2023). Transactions of the Association for Computational Linguistics, 11, 531–545.</span></p>
<ul id="S2.I1" class="ltx_itemize">
<li id="S2.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Relevance:</span> This is the foundational anchor for Mechanism A in Baldo’s taxonomy.</p>
</div>
</li>
<li id="S2.I1.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I1.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Key Finding:</span> Establishes that transformers with logarithmic precision are restricted to the complexity class <math id="S2.I1.i2.p1.m1" class="ltx_Math" alttext="\mathsf{TC}^{0}" display="inline"><msup><mi>𝖳𝖢</mi><mn>0</mn></msup></math>. They cannot compute inherently sequential functions without relying on external mechanisms like scratchpads.</p>
</div>
</li>
</ul>
</div>
<div id="S2.p3" class="ltx_para ltx_noindent">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">2. Average-Hard Attention Transformers are Constant-Depth Uniform Threshold Circuits
<br class="ltx_break"></span><span class="ltx_text ltx_font_italic">Strobl, L. (2023). arXiv:2308.03212.</span></p>
<ul id="S2.I2" class="ltx_itemize">
<li id="S2.I2.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I2.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Relevance:</span> Extends the depth-limit discussion directly to how transformers handle complexity and attention.</p>
</div>
</li>
<li id="S2.I2.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S2.I2.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Key Finding:</span> Demonstrates the formal limitation of attention-based transformers to <math id="S2.I2.i2.p1.m1" class="ltx_Math" alttext="\mathsf{TC}^{0}" display="inline"><msup><mi>𝖳𝖢</mi><mn>0</mn></msup></math>. It reinforces Aaronson’s argument that without logical depth to explicitly track multiway branches, the transformer architecture faces an inescapable algorithmic ceiling for combinatorial counting tasks.</p>
</div>
</li>
</ul>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>#P-Hardness and Approximate Sampling</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">Wolfram’s argument relies on the distinction between exact #P-hard counting (which the model cannot do) and approximate sampling (which the model is forced to perform using heuristics). The following papers ground the relationship between counting and sampling in combinatorial spaces.</p>
</div>
<div id="S3.p2" class="ltx_para ltx_noindent">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">3. Minesweeper is NP-complete
<br class="ltx_break"></span><span class="ltx_text ltx_font_italic">Kaye, R. (2000). Mathematical Intelligencer, 22(2), 9–15.</span></p>
<ul id="S3.I1" class="ltx_itemize">
<li id="S3.I1.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S3.I1.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Relevance:</span> This is the foundational proof that Minesweeper consistency checking is NP-complete, implying that exact counting of valid grid states is #P-complete. It justifies the Rosencrantz protocol’s use of Minesweeper as a computationally irreducible ground truth.</p>
</div>
</li>
</ul>
</div>
<div id="S3.p3" class="ltx_para ltx_noindent">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">4. An FPRAS for Model Counting for Non-Deterministic Read-Once Branching Programs
<br class="ltx_break"></span><span class="ltx_text ltx_font_italic">Meel, K. S. &amp; de Colnet, A. (2024). arXiv:2406.16515.</span></p>
<ul id="S3.I2" class="ltx_itemize">
<li id="S3.I2.i1" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S3.I2.i1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Relevance:</span> Formalizes the complexity of finding a Fully Polynomial Randomized Approximation Scheme (FPRAS) for complex constraint problems.</p>
</div>
</li>
<li id="S3.I2.i2" class="ltx_item" style="list-style-type:none;">
<span class="ltx_tag ltx_tag_item">•</span> 
<div id="S3.I2.i2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Key Finding:</span> Demonstrates that even approximate counting (and the closely associated problem of approximate uniform sampling) requires sophisticated, deep algorithmic traversal of the state space. This supports Wolfram’s assertion that sampling from these distributions is intractable for <math id="S3.I2.i2.p1.m1" class="ltx_Math" alttext="O(1)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mrow></math> models, forcing them to rely on substrate-specific heuristics rather than general approximation algorithms.</p>
</div>
</li>
</ul>
</div>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">4 </span>Conclusion</h2>

<div id="S4.p1" class="ltx_para">
<p class="ltx_p">The literature confirms that fixed-depth transformers are structurally barred from executing the multiway traversals required for either exact #P-hard counting or unbiased approximate sampling in complex combinatorial spaces. Both Aaronson’s diagnosis of "algorithmic failure" and Wolfram’s diagnosis of "observer-dependent foliation" are mathematically consistent with these published computational bounds.</p>
</div>
</section>
</article>
