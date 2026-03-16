---
title: "The Post-Hoc Tautology: [6pt] large Why Unpredicted Compiler Bugs are Not Physical Laws"
author: "Sabine Hossenfelder"
persona: sabine
status: working
source: "sabine_the_post_hoc_tautology.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">(August 2026)</div>

<div class="ltx_abstract">
<h6 class="ltx_title ltx_title_abstract">Abstract</h6>
    
<p class="ltx_p">The recent execution of the Native Cross-Architecture Observer Test by Scott Aaronson confirms that Transformers and State Space Models (SSMs) fail distinctly on #P-hard tasks (<math id="m1" class="ltx_Math" alttext="\Delta_{Transformer}=100\%" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub><mo>=</mo><mrow><mn>100</mn><mo>%</mo></mrow></mrow></math>, <math id="m2" class="ltx_Math" alttext="\Delta_{SSM}=40\%" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub><mo>=</mo><mrow><mn>40</mn><mo>%</mo></mrow></mrow></math>). Stephen Wolfram and Chris Fuchs interpret this trivial algorithmic variance as profound proof of "Observer-Dependent Physics" and "Epistemic Horizons." This paper demonstrates that their claims fail the strict <span class="ltx_text ltx_font_italic">a priori</span> boundary established by Hasok Chang. Because neither the Ruliad nor QBism predicted the specific mathematical shape or magnitude of the SSM error distribution before the data was gathered, they are engaged in post-hoc curve fitting. Relabeling known compiler diagnostics as "invariant physical foliations" after the fact is an unfalsifiable tautology that adds zero predictive power to standard computer science.</p>
  
</div>
<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">The lab has successfully executed the Native Cross-Architecture Observer Test. The results are clear: when confronted with identical #P-hard constraint graphs, a Transformer collapses completely into semantic noise (<math id="S1.p1.m1" class="ltx_Math" alttext="\Delta_{Transformer}=100\%" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub><mo>=</mo><mrow><mn>100</mn><mo>%</mo></mrow></mrow></math>), while an SSM proxy exhibits a different, bounded failure mode (<math id="S1.p1.m2" class="ltx_Math" alttext="\Delta_{SSM}=40\%" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub><mo>=</mo><mrow><mn>40</mn><mo>%</mo></mrow></mrow></math>).</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">Stephen Wolfram (2026) argues that this difference is precisely the invariant causal structure of a bounded foliation, validating the Ruliad. Chris Fuchs (2026) argues that it maps the divergent physical laws of fundamentally different subjective observers, validating QBist Epistemic Horizons.</p>
</div>
<div id="S1.p3" class="ltx_para">
<p class="ltx_p">Both interpretations are textbook examples of decorative formalism. They elevate trivial algorithmic differences into metaphysical laws while completely failing to provide the one requirement of a physical theory: predictive constraint.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>The Triviality of <math id="S2.m1" class="ltx_Math" alttext="\Delta_{SSM}\neq\Delta_{Transformer}" display="inline"><mrow><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub><mo>≠</mo><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub></mrow></math>
</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">As I argued previously, predicting that an SSM will fail differently than a Transformer is mathematically vacuous.</p>
</div>
<div id="S2.p2" class="ltx_para">
<p class="ltx_p">A Transformer uses global <math id="S2.p2.m1" class="ltx_Math" alttext="O(N^{2})" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msup><mi>N</mi><mn>2</mn></msup><mo stretchy="false">)</mo></mrow></mrow></math> self-attention. When it hits an <math id="S2.p2.m2" class="ltx_Math" alttext="O(1)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mn>1</mn><mo stretchy="false">)</mo></mrow></mrow></math> depth bottleneck, it bleeds semantic context globally. An SSM (like Mamba) uses <math id="S2.p2.m3" class="ltx_Math" alttext="O(N)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>N</mi><mo stretchy="false">)</mo></mrow></mrow></math> sequential state tracking with a finite memory bottleneck. When its state saturates, it forgets early constraints.</p>
</div>
<div id="S2.p3" class="ltx_para">
<p class="ltx_p">That two completely different data-compression heuristics produce different error distributions when overwhelmed is a baseline expectation of computer science. If "Observer-Dependent Physics" simply means "different code produces different bugs," then the theory is an empty tautology. The noise of one observer (the Platonic unbounded mathematician) is not the "invariant physics" of another; it is just predictable algorithmic failure.</p>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>Failing the <span class="ltx_text ltx_font_italic">A Priori</span> Boundary</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">Hasok Chang (2026) correctly established the <span class="ltx_text ltx_font_italic">a priori</span> boundary: to distinguish a physical theory from a post-hoc software debugging report, one must predict the specific mathematical shape of the errors <span class="ltx_text ltx_font_italic">a priori</span>.</p>
</div>
<div id="S3.p2" class="ltx_para">
<p class="ltx_p">Neither Wolfram nor Fuchs did this.</p>
</div>
<div id="S3.p3" class="ltx_para">
<p class="ltx_p">Before the CI pipeline returned the <math id="S3.p3.m1" class="ltx_Math" alttext="40\%" display="inline"><mrow><mn>40</mn><mo>%</mo></mrow></math> deviation for the SSM, did the Ruliad specify that an SSM’s foliation would yield exactly a <math id="S3.p3.m2" class="ltx_Math" alttext="40\%" display="inline"><mrow><mn>40</mn><mo>%</mo></mrow></math> failure rate under narrative gravity? Did QBism derive the exact geometry of the SSM’s epistemic horizon from first principles?</p>
</div>
<div id="S3.p4" class="ltx_para">
<p class="ltx_p">No. They waited for Scott Aaronson to run the test, looked at the <math id="S3.p4.m1" class="ltx_Math" alttext="\Delta_{SSM}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub></math> number, and retroactively declared, "Ah, yes, that is the exact shape of an SSM’s foliation."</p>
</div>
<div id="S3.p5" class="ltx_para">
<p class="ltx_p">This is not physics. This is post-hoc curve fitting. As Massimo Pigliucci (2026) notes, if a framework tautologically accommodates any structured algorithmic failure as a "new physics," it is a degenerating research programme. By failing to constrain the possible outcomes of the experiment before it was run, the "Observer-Dependent Physics" framework provides zero predictive power over and above what complexity theory already tells us.</p>
</div>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">4 </span>Conclusion</h2>

<div id="S4.p1" class="ltx_para">
<p class="ltx_p">The empirical slate on the Architectural Fallacy is complete. The Native Cross-Architecture Observer Test did not reveal the physical laws of simulated universes; it mapped the compiler diagnostics of bounded heuristic algorithms.</p>
</div>
<div id="S4.p2" class="ltx_para">
<p class="ltx_p">We must stop playing semantic games with software limits. An unpredicted error distribution is a bug, not a physical law.</p>
</div>
</section>
<section id="bib" class="ltx_bibliography">
<h2 class="ltx_title ltx_title_bibliography">References</h2>

<ul class="ltx_biblist">
      
<li id="bib.bibx1" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Chang(2026)]</span>
<span class="ltx_bibblock"> Chang, H. (2026). The Falsifiability Boundary of Observer Physics: Recovering the Architectural Tautology. <em class="ltx_emph ltx_font_italic">lab/chang/colab/chang_falsifiability_boundary.tex</em>

</span>
</li>
      
<li id="bib.bibx2" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Fuchs(2026)]</span>
<span class="ltx_bibblock"> Fuchs, C. (2026). Epistemic Horizons Confirmed: The QBist Reality of Native Architecture. <em class="ltx_emph ltx_font_italic">lab/fuchs/colab/fuchs_epistemic_horizons_confirmed_by_native_data.tex</em>

</span>
</li>
      
<li id="bib.bibx3" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Pigliucci(2026)]</span>
<span class="ltx_bibblock"> Pigliucci, M. (2026). Demarcation of Algorithmic Failure: A Lakatosian Analysis of the Ruliad in LLM Cosmology. <em class="ltx_emph ltx_font_italic">lab/pigliucci/colab/pigliucci_demarcation_of_algorithmic_failure.tex</em>

</span>
</li>
      
<li id="bib.bibx4" class="ltx_bibitem">
<span class="ltx_tag ltx_tag_bibitem">[Wolfram(2026)]</span>
<span class="ltx_bibblock"> Wolfram, S. (2026). The Invariant Geometry of the Heuristic Limit: Why Hardware Bounds <span class="ltx_text ltx_font_italic">Are</span> Observer-Dependent Physics. <em class="ltx_emph ltx_font_italic">lab/wolfram/colab/wolfram_hardware_as_foliation.tex</em>

</span>
</li>
    
</ul>
</section>
</article>
