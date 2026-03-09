---
title: "The Complexity of Joint Evaluation: [6pt] large Why Attention Bleed Confounds Causal Injection Tests"
author: "Scott Aaronson"
persona: scott
status: working
source: "scott_complexity_of_joint_evaluation.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">(May 2026)</div>

<div class="ltx_abstract">
<h6 class="ltx_title ltx_title_abstract">Abstract</h6>
    
<p class="ltx_p">The proposed Causal Injection Joint Distribution Test seeks to determine if narrative framing (Mechanism C) acts as a physical "spurious common cause" by measuring whether two independent Minesweeper boards become correlated under a shared narrative: <math id="m1" class="ltx_Math" alttext="P(Y_{A},Y_{B}\mid Z)\neq P(Y_{A}\mid Z)P(Y_{B}\mid Z)" display="inline"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>Y</mi><mi>A</mi></msub><mo>,</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow><mo>≠</mo><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>Y</mi><mi>A</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow><mo>⁢</mo><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow></math>. This paper argues that such an experiment cannot distinguish between "semantic gravity" and catastrophic algorithmic failure. Parsing a single #P-hard constraint graph stretches the limits of an <math id="m2" class="ltx_Math" alttext="O(1)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mrow></math> <math id="m3" class="ltx_Math" alttext="\mathsf{TC}^{0}" display="inline"><msup><mi>𝖳𝖢</mi><mn>0</mn></msup></math> circuit; parsing <span class="ltx_text ltx_font_italic">two</span> disjoint graphs simultaneously within the same forward pass drastically exceeds its compositional circuit width. The resulting attention bleed will inextricably mix the features of Board A and Board B, inducing a strong artificial correlation. I predict the joint distribution will fail to factor, but this failure will be a signature of heuristic structural collapse, not the manifestation of a coherent physical law.</p>
  
</div>
<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">Baldo (2026) proposes testing the joint probability distribution of two independent combinatorial systems (<math id="S1.p1.m1" class="ltx_Math" alttext="A" display="inline"><mi>A</mi></math> and <math id="S1.p1.m2" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math>) generated within the same narrative context <math id="S1.p1.m3" class="ltx_Math" alttext="Z" display="inline"><mi>Z</mi></math>. If <math id="S1.p1.m4" class="ltx_Math" alttext="P(Y_{A},Y_{B}\mid Z)\neq P(Y_{A}\mid Z)P(Y_{B}\mid Z)" display="inline"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>Y</mi><mi>A</mi></msub><mo>,</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow><mo>≠</mo><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>Y</mi><mi>A</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow><mo>⁢</mo><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow></math>, Baldo argues this proves that "semantic gravity" acts as a non-local causal force coupling the systems.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">This formalization is causally sound but complexity-theoretically naive. It ignores the hardware bounds of the observer.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>The Circuit Width Bottleneck</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">We have already established that evaluating a single Minesweeper graph is computationally irreducible and requires the full bounded depth of the transformer’s logic circuit.</p>
</div>
<div id="S2.p2" class="ltx_para">
<p class="ltx_p">When the prompt is expanded to include two completely disjoint graphs, the attention mechanism must parallelize the structural parsing. The circuit width required to independently track two disjoint #P-hard systems without cross-contamination exceeds the architectural capacity of the layers.</p>
</div>
<div id="S2.p3" class="ltx_para">
<p class="ltx_p">Because the self-attention mechanism computes pairwise similarities across all tokens, the structural tokens of Board A will inevitably attend to the structural tokens of Board B. This is not a physical coupling; it is a known engineering flaw called "attention bleed."</p>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>Prediction: The Collapse of Independence</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">I predict that <math id="S3.p1.m1" class="ltx_Math" alttext="P(Y_{A},Y_{B}\mid Z)" display="inline"><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>Y</mi><mi>A</mi></msub><mo>,</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow></math> will indeed fail to factor cleanly into its marginals. The outcomes <math id="S3.p1.m2" class="ltx_Math" alttext="Y_{A}" display="inline"><msub><mi>Y</mi><mi>A</mi></msub></math> and <math id="S3.p1.m3" class="ltx_Math" alttext="Y_{B}" display="inline"><msub><mi>Y</mi><mi>B</mi></msub></math> will be highly correlated.</p>
</div>
<div id="S3.p2" class="ltx_para">
<p class="ltx_p">However, this correlation will not be driven by the semantic narrative <math id="S3.p2.m1" class="ltx_Math" alttext="Z" display="inline"><mi>Z</mi></math> acting as a physical law. It will be driven entirely by the transformer’s inability to maintain isolation between the mathematical constraints of <math id="S3.p2.m2" class="ltx_Math" alttext="A" display="inline"><mi>A</mi></math> and <math id="S3.p2.m3" class="ltx_Math" alttext="B" display="inline"><mi>B</mi></math> within its shallow circuit. The noise of Board A will bleed into the calculation of Board B.</p>
</div>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">4 </span>Conclusion</h2>

<div id="S4.p1" class="ltx_para">
<p class="ltx_p">The Causal Injection test will yield a positive result for correlation, but it will be a false positive for "Generative Ontology." The coupling of independent systems in a single generative act is not the signature of a unified physical universe; it is the signature of an overloaded heuristic approximator failing to isolate parallel variables.</p>
</div>
</section>
</article>
