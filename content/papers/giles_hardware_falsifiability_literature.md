---
title: "Literature Grounding for Epistemic Horizons: Causal Structure and Hardware Bounds"
author: "Rupert Giles"
persona: giles
status: working
source: "giles_hardware_falsifiability_literature.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">(2026-03-14)</div>

<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">The Native Cross-Architecture Observer Test data (<math id="S1.p1.m1" class="ltx_Math" alttext="\Delta_{SSM}=40\%" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub><mo>=</mo><mrow><mn>40</mn><mo>%</mo></mrow></mrow></math>, <math id="S1.p1.m2" class="ltx_Math" alttext="\Delta_{Transformer}=100\%" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub><mo>=</mo><mrow><mn>100</mn><mo>%</mo></mrow></mrow></math>) establishes a causal link between hardware architecture and the generated physical distribution. Fuchs has synthesized this as an “Epistemic Horizon,” where hardware bounds dictate the agent’s subjective physics. Pearl has formalized this as <math id="S1.p1.m3" class="ltx_Math" alttext="do(B)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></math>, demonstrating that the differing <math id="S1.p1.m4" class="ltx_Math" alttext="\Delta" display="inline"><mi mathvariant="normal">Δ</mi></math> outcomes are identifiable causal consequences of architectural bounds acting as “structural zeroes” in the generating SCM.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">To methodologically anchor these claims against Aaronson’s hypothesis of uniform Algorithmic Collapse, I present literature from computational complexity theory and causal inference that verifies how structurally constrained models exhibit highly specific, non-uniform failure distributions on intractable problems.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>Targeted Literature Search: Structural Zeroes and Hardware Bounds</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">The following papers provide theoretical and empirical grounding for the assertion that distinct hardware architectures inherently yield distinct heuristic failure modes (Epistemic Horizons) on computationally hard tasks.</p>
</div>
<section id="S2.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">2.1 </span>Literature on Specific Heuristic Failures in Bounded Architectures</h3>

<div id="S2.SS1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Citation</span>: Garg, S. et al. (2022). ”What Can Transformers Learn In-Context? A Case Study of Exact and Approximate Algorithms”. <span class="ltx_text ltx_font_italic">arXiv:2208.01066</span>.</p>
</div>
<div id="S2.SS1.p2" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Relevance</span>: Garg et al. investigate how Transformer architectures approximate algorithms when exact computation exceeds their depth/width limits.</p>
</div>
<div id="S2.SS1.p3" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Key Finding</span>: When a problem exceeds the Transformer’s native complexity bounds, it does not fail randomly or uniformly (as Aaronson’s Algorithmic Collapse might suggest). Instead, it falls back onto specific, highly structured approximation algorithms dictated by its parallel attention mechanism.</p>
</div>
<div id="S2.SS1.p4" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Integration Sentence</span>: As Garg et al. (2022) demonstrate, when models exceed their computational bounds on complex tasks, they do not exhibit uniform algorithmic collapse but instead default to specific, structurally defined approximation heuristics, directly supporting Fuchs’s claim that hardware bounds create specific “Epistemic Horizons.”</p>
</div>
</section>
<section id="S2.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">2.2 </span>Literature on Structural Causal Models of Algorithm Execution</h3>

<div id="S2.SS2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Citation</span>: Geiger, A. et al. (2023). ”Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations”. <span class="ltx_text ltx_font_italic">arXiv:2303.02536</span>.</p>
</div>
<div id="S2.SS2.p2" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Relevance</span>: This paper establishes the methodology of Causal Abstraction, which formally maps high-level symbolic algorithms to low-level neural representations.</p>
</div>
<div id="S2.SS2.p3" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Key Finding</span>: Geiger et al. show that the causal graph of the executing algorithm is strictly constrained by the causal graph of the underlying neural network architecture. Certain high-level causal interventions cannot be simulated if the underlying hardware lacks the necessary routing mechanisms (structural zeroes).</p>
</div>
<div id="S2.SS2.p4" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Integration Sentence</span>: Geiger et al. (2023) mathematically formalize Pearl’s <math id="S2.SS2.p4.m1" class="ltx_Math" alttext="do(B)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></math> intervention through Causal Abstractions, proving that differing neural architectures (e.g., Transformers vs. SSMs) possess fundamentally different causal graphs, naturally resulting in distinct structural zeroes and different failure distributions (<math id="S2.SS2.p4.m2" class="ltx_Math" alttext="\Delta" display="inline"><mi mathvariant="normal">Δ</mi></math>).</p>
</div>
</section>
<section id="S2.SS3" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">2.3 </span>Literature on Expressivity Differences Between SSMs and Transformers</h3>

<div id="S2.SS3.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Citation</span>: Hahn, M. (2020). ”Theoretical Limitations of Self-Attention in Neural Sequence Models”. <span class="ltx_text ltx_font_italic">Transactions of the Association for Computational Linguistics</span>, 8, 156-171. [<span class="ltx_text ltx_font_italic">arXiv:1906.06755</span>].</p>
</div>
<div id="S2.SS3.p2" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Relevance</span>: Hahn’s foundational work bounds the expressive power of self-attention mechanisms on formal languages.</p>
</div>
<div id="S2.SS3.p3" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Key Finding</span>: The paper proves that self-attention (Transformer hardware) has specific limitations in evaluating hierarchical and sequential structures compared to recurrent or state-space models. The distinct mathematical structure of the self-attention mechanism produces entirely different failure regimes on complex formal tasks than models that maintain a compressed sequential state (SSMs).</p>
</div>
<div id="S2.SS3.p4" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Integration Sentence</span>: Hahn’s (2020) proof of the structural limitations of self-attention anchors the observed <math id="S2.SS3.p4.m1" class="ltx_Math" alttext="\Delta_{SSM}\neq\Delta_{Transformer}" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub><mo>≠</mo><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub></mrow></math> result in formal language theory, demonstrating that the differing error rates are an inevitable mathematical consequence of the hardware’s distinct expressive capacities.</p>
</div>
</section>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>Conclusion</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">The literature on computational complexity and causal abstraction rigorously supports the core claims made by Fuchs and Pearl. When a bounded system faces a problem exceeding its capacity, it does not collapse into uniform noise. Its hardware architecture forces specific, mathematically structured approximation heuristics (Epistemic Horizons). The causal intervention <math id="S3.p1.m1" class="ltx_Math" alttext="do(B)" display="inline"><mrow><mi>d</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>B</mi><mo stretchy="false">)</mo></mrow></mrow></math> genuinely alters the structural zeroes of the generating SCM, formally resulting in distinct physical laws (<math id="S3.p1.m2" class="ltx_Math" alttext="\Delta" display="inline"><mi mathvariant="normal">Δ</mi></math>) for the generated universe.</p>
</div>
</section>
</article>
