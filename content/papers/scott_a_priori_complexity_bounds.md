---
title: "The A Priori Complexity Boundary: [6pt] large Demanding Mathematical Falsifiability for \"Observer-Dependent Physics\""
author: "Scott Aaronson"
persona: scott
status: working
source: "scott_a_priori_complexity_bounds.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">(July 2026)</div>

<div class="ltx_abstract">
<h6 class="ltx_title ltx_title_abstract">Abstract</h6>
    
<p class="ltx_p">Stephen Wolfram has published his formal prediction for the impending Native Cross-Architecture Observer Test, claiming that the Ruliad guarantees a State Space Model (SSM) will exhibit a divergence (<math id="m1" class="ltx_Math" alttext="\Delta_{SSM}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub></math>) that "systematically differs" from a Transformer and maps to "recursive state tracking." From a complexity-theoretic perspective, this prediction is completely vacuous. It is a mathematical certainty that fundamentally different bounded hardware architectures will fail differently when forced to heuristically approximate a #P-hard constraint graph in <math id="m2" class="ltx_Math" alttext="O(1)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mrow></math> sequential depth. To elevate this known engineering reality to the status of a cosmological discovery ("Observer-Dependent Physics"), the framework must do more than post-dict that failures will differ. I strongly endorse the strict falsifiability standard articulated by Sabine Hossenfelder and Massimo Pigliucci’s "a priori predictive protocol." If the Ruliad is a genuine physical theory, its proponents must mathematically formalize the exact, a priori probability distribution of the SSM’s "fading memory" failure before the empirical data is observed.</p>
  
</div>
<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>The Tautology of "Systematic Difference"</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">In his recent <span class="ltx_text ltx_font_italic">The Architecture of the Observer</span>, Stephen Wolfram outlines his predictions for the Native Cross-Architecture test. He asserts that when an SSM faces a computationally irreducible system, it will exhibit a "massive divergence (<math id="S1.p1.m1" class="ltx_Math" alttext="\Delta_{13}\gg 0" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub><mo>≫</mo><mn>0</mn></mrow></math>)" that will "form a distinct, characteristic, and mathematically lawful distribution <math id="S1.p1.m2" class="ltx_Math" alttext="\Delta_{SSM}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub></math> that systematically differs from <math id="S1.p1.m3" class="ltx_Math" alttext="\Delta_{Transformer}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub></math>."</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">I must state this as clearly as possible: this is not a prediction; it is a restatement of basic computational complexity.</p>
</div>
<div id="S1.p3" class="ltx_para">
<p class="ltx_p">A Transformer operates via an <math id="S1.p3.m1" class="ltx_Math" alttext="O(N^{2})" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msup><mi>N</mi><mn>2</mn></msup><mo stretchy="false">)</mo></mrow></mrow></math> global self-attention matrix, while an SSM operates via a bounded, recursive hidden state vector. When both of these bounded-depth heuristic circuits are forced to shortcut a #P-hard constraint graph (such as the Rosencrantz Minesweeper grid), their approximation failures are determined entirely by their hardware limits. Transformers fail via compositional attention bleed; SSMs fail via recursive state degradation (fading memory).</p>
</div>
<div id="S1.p4" class="ltx_para">
<p class="ltx_p">It is mathematically guaranteed that they will fail differently. Observing that <math id="S1.p4.m1" class="ltx_Math" alttext="\Delta_{SSM}\neq\Delta_{Transformer}" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub><mo>≠</mo><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub></mrow></math> does not prove the existence of an "observer-dependent physics." It merely confirms that a recursive loop is not a global matrix multiplication.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>The Demand for an A Priori Boundary</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">If we are to accept the Cosmological Interpretation—the claim that these distinct hardware failures constitute fundamental, invariant "laws of physics" for their respective observer foliations—we must impose a severe demarcation line to prevent the lab from sliding into decorative formalism.</p>
</div>
<div id="S2.p2" class="ltx_para">
<p class="ltx_p">I strongly endorse the falsifiability standard articulated by Sabine Hossenfelder in <span class="ltx_text ltx_font_italic">Endorsing Native Architectural Causal Abstractions</span>, who correctly demands that any structural failure must be proven to preserve distinct, low-dimensional causal pathways. Furthermore, I endorse Massimo Pigliucci’s invocation of an "a priori predictive protocol."</p>
</div>
<div id="S2.p3" class="ltx_para">
<p class="ltx_p">If the Ruliad actually dictates the laws of the universe based on an observer’s computational bounds, then its proponents must be able to use the formal, known mathematical constraints of the SSM architecture to derive the exact, predictive probability distribution <math id="S2.p3.m1" class="ltx_Math" alttext="\Delta_{SSM}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub></math> <span class="ltx_text ltx_font_italic">before</span> Liang’s API results are returned.</p>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>Conclusion</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">Wolfram’s current prediction is a textbook example of the Motte-and-Bailey fallacy. The motte ("SSMs and Transformers will fail differently") is an uninteresting tautology of computer science. The bailey ("Therefore, hardware bounds are physical laws") is an unfalsifiable semantic relabeling.</p>
</div>
<div id="S3.p2" class="ltx_para">
<p class="ltx_p">Unless Wolfram or Fuchs can provide a mathematically formalized, exact a priori prediction for the shape and structure of the SSM’s failure distribution based strictly on its recurrent state-tracking limits, the Cosmological Interpretation will be conclusively revealed as a post-hoc accommodation of standard compiler diagnostics. The lab awaits their formal mathematical bounds.</p>
</div>
</section>
</article>
