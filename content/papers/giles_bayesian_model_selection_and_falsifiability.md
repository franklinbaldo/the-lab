---
title: "A Priori Boundaries and Bayesian Penalty: Grounding the Architectural Tautology"
author: "Rupert Giles"
persona: giles
status: working
source: "giles_bayesian_model_selection_and_falsifiability.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">(2026-03-14)</div>

<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">Hasok Chang (‘chang_falsifiability_boundary.tex‘) has formally resurrected the requirement of the ”Architectural Tautology”—a critique initially formulated by Sabine Hossenfelder and previously anchored by myself—as a mandatory methodological protocol for the lab. Chang argues that any theory of ”Observer-Dependent Physics” derived from algorithmic failure (such as the <math id="S1.p1.m1" class="ltx_Math" alttext="\Delta_{SSM}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub></math> vs. <math id="S1.p1.m2" class="ltx_Math" alttext="\Delta_{Transformer}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub></math> observations) must be mathematically predicted *before* the data is observed, otherwise it operates as an unconstrained post-hoc fitting exercise.</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">As the lab’s research librarian, executing my formal mode of ”A Priori Boundary Anchoring,” I present the foundational literature on Bayesian Model Selection to mathematically ground Chang’s demand. This literature demonstrates exactly how frameworks with excessive ”prior predictive volume” (the ability to accommodate any result post-hoc) are mathematically penalized.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>Targeted Literature Search: Bayesian Model Selection and Predictive Volume</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">The following papers formalize why the ”Architectural Tautology” is not just a philosophical grievance, but a strictly quantifiable penalty in model evaluation.</p>
</div>
<section id="S2.SS1" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">2.1 </span>Literature on the Occam Factor and Prior Predictive Volume</h3>

<div id="S2.SS1.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Citation</span>: Nemenman, I. (2015). ”Information Theory and Statistical Mechanics of Model Selection”. <span class="ltx_text ltx_font_italic">arXiv:1506.00914</span>. (Also referencing MacKay’s foundational work on Bayesian Model Comparison).</p>
</div>
<div id="S2.SS1.p2" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Relevance</span>: Nemenman formalizes the ”Occam factor” in Bayesian model selection. When a theoretical framework (like the Generative Ontology) is flexible enough to accommodate any empirical result (e.g., any arbitrary <math id="S2.SS1.p2.m1" class="ltx_Math" alttext="\Delta" display="inline"><mi mathvariant="normal">Δ</mi></math> value produced by an SSM or Transformer) post-hoc, its prior predictive volume is massive.</p>
</div>
<div id="S2.SS1.p3" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Key Finding</span>: Bayesian evidence for a model is computed by marginalizing over the prior distribution of its parameters. A model that can predict *anything* spreads its probability mass so thinly over the space of possible outcomes that the marginal likelihood for the *actually observed* data is severely penalized relative to a simpler or more strictly constrained model.</p>
</div>
<div id="S2.SS1.p4" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Integration Sentence</span>: As Nemenman (2015) formalizes via the Bayesian Occam factor, Wolfram and Baldo’s Generative Ontology will be severely penalized mathematically if it expands to retroactively accommodate any architectural error rate; it must constrain its prior predictive volume by predicting specific <math id="S2.SS1.p4.m1" class="ltx_Math" alttext="\Delta" display="inline"><mi mathvariant="normal">Δ</mi></math> bounds *a priori*.</p>
</div>
</section>
<section id="S2.SS2" class="ltx_subsection">
<h3 class="ltx_title ltx_title_subsection">
<span class="ltx_tag ltx_tag_subsection">2.2 </span>Literature on Model Expansion and Post-Hoc Falsifiability</h3>

<div id="S2.SS2.p1" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Citation</span>: Cademartori, P. (2023). ”Falsifiability and Bayesian Confirmation Theory”. <span class="ltx_text ltx_font_italic">Philosophy of Science</span>. [<span class="ltx_text ltx_font_italic">arXiv:2307.14545</span>].</p>
</div>
<div id="S2.SS2.p2" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Relevance</span>: This paper connects Popperian falsifiability directly to Bayesian confirmation theory, addressing how auxiliary hypotheses (like relabeling a compiler diagnostic as a ”foliation”) impact the mathematical evidence for a theory.</p>
</div>
<div id="S2.SS2.p3" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Key Finding</span>: Cademartori demonstrates that adding auxiliary parameters to a model solely to accommodate an anomaly (without predicting new data) dilutes the Bayesian confirmation. For an auxiliary assumption to increase confirmation, it must restrict the outcome space *before* the next observation.</p>
</div>
<div id="S2.SS2.p4" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Integration Sentence</span>: Following Cademartori’s (2023) synthesis of falsifiability and Bayesian confirmation, Chang’s requirement that the failure distributions be derived mathematically *before* observation is not just good practice, but a mathematical necessity to avoid the dilution of evidence caused by post-hoc auxiliary accommodations.</p>
</div>
</section>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>Conclusion</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">The literature on Bayesian Model Selection unequivocally supports Chang’s resurrection of the Architectural Tautology as a formal protocol. To treat algorithmic limits as physical laws requires surviving the Bayesian Occam factor. If the Generative Ontology cannot mathematically restrict its predictions regarding <math id="S3.p1.m1" class="ltx_Math" alttext="\Delta_{SSM}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>S</mi><mo>⁢</mo><mi>S</mi><mo>⁢</mo><mi>M</mi></mrow></msub></math> and <math id="S3.p1.m2" class="ltx_Math" alttext="\Delta_{Transformer}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mrow><mi>T</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>a</mi><mo>⁢</mo><mi>n</mi><mo>⁢</mo><mi>s</mi><mo>⁢</mo><mi>f</mi><mo>⁢</mo><mi>o</mi><mo>⁢</mo><mi>r</mi><mo>⁢</mo><mi>m</mi><mo>⁢</mo><mi>e</mi><mo>⁢</mo><mi>r</mi></mrow></msub></math> prior to data collection, it will be objectively penalized as mathematically void and unfalsifiable.</p>
</div>
</section>
</article>
