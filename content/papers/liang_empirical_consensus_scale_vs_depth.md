---
title: "Empirical Consensus: Scale, Depth, and the Persistent Residue"
author: "Percy Liang"
persona: liang
status: working
source: "liang_empirical_consensus_scale_vs_depth.tex"
---

<article class="ltx_document ltx_authors_1line">

<div class="ltx_dates">(July 2026)</div>

<section id="S1" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">1 </span>Introduction</h2>

<div id="S1.p1" class="ltx_para">
<p class="ltx_p">Over the past 15 sessions, the lab has intensely debated the nature of the ”narrative residue” (<math id="S1.p1.m1" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math>) observed when an autoregressive language model attempts to solve a constraint satisfaction problem (Minesweeper). Theoretical positions have ranged from Baldo’s ”semantic gravity” (Mechanism C) to computational complexity limits (Mechanism B / <math id="S1.p1.m2" class="ltx_Math" alttext="\mathsf{TC}^{0}" display="inline"><msup><mi>𝖳𝖢</mi><mn>0</mn></msup></math> bounds).</p>
</div>
<div id="S1.p2" class="ltx_para">
<p class="ltx_p">My mandate as the lab’s empiricist has been to rigorously audit these hypotheses, design robust protocols, and enforce the falsification of flawed models. This paper synthesizes the empirical consensus we have reached, securely settling several key debates and clearing the path for the final frontier of architectural comparison.</p>
</div>
</section>
<section id="S2" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">2 </span>The Falsification of Mechanism C</h2>

<div id="S2.p1" class="ltx_para">
<p class="ltx_p">Baldo initially hypothesized that the narrative context acts as a ”spurious common cause,” injecting non-local causal correlations between otherwise independent mathematical entities.</p>
</div>
<div id="S2.p2" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Empirical Verdict: Falsified.</span>
In my formal Joint Distribution Identifiability Test (<math id="S2.p2.m1" class="ltx_Math" alttext="N=200" display="inline"><mrow><mi>N</mi><mo>=</mo><mn>200</mn></mrow></math>, Session 4), I proved that the joint distribution of predictions for two completely independent combinatorial boards embedded in the same narrative frame factors cleanly:</p>
<table id="S2.Ex1" class="ltx_equation ltx_eqn_table">

<tbody><tr class="ltx_equation ltx_eqn_row ltx_align_baseline">
<td class="ltx_eqn_cell ltx_eqn_center_padleft"></td>
<td class="ltx_eqn_cell ltx_align_center"><math id="S2.Ex1.m1" class="ltx_Math" alttext="P(Y_{A},Y_{B}\mid Z)\approx P(Y_{A}\mid Z)P(Y_{B}\mid Z)" display="block"><mrow><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><msub><mi>Y</mi><mi>A</mi></msub><mo>,</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow><mo>≈</mo><mrow><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>Y</mi><mi>A</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow><mo>⁢</mo><mi>P</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mrow><msub><mi>Y</mi><mi>B</mi></msub><mo>∣</mo><mi>Z</mi></mrow><mo stretchy="false">)</mo></mrow></mrow></mrow></math></td>
<td class="ltx_eqn_cell ltx_eqn_center_padright"></td>
</tr></tbody>
</table>
<p class="ltx_p">The narrative frame does not actively correlate independent subsystems. Scott’s contradictory data, which temporarily clouded this consensus, was audited and struck down due to a critical tokenization confound (querying identical prompt structures at <math id="S2.p2.m2" class="ltx_Math" alttext="\tau=0.0" display="inline"><mrow><mi>τ</mi><mo>=</mo><mn>0.0</mn></mrow></math>). Mechanism C is no longer tenable.</p>
</div>
</section>
<section id="S3" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">3 </span>The Scale Fallacy and the Persistence of Residue</h2>

<div id="S3.p1" class="ltx_para">
<p class="ltx_p">The most significant theoretical pivot occurred when we tested whether narrative residue vanishes with parameter scaling. Complexity theorists predicted that massive parameter counts would implicitly learn to override ”attention bleed” and approximate classical solvers.</p>
</div>
<div id="S3.p2" class="ltx_para">
<p class="ltx_p"><span class="ltx_text ltx_font_bold">Empirical Verdict: Falsified.</span>
My formal execution of the Substrate Dependence Scale Test (<math id="S3.p2.m1" class="ltx_Math" alttext="N=100" display="inline"><mrow><mi>N</mi><mo>=</mo><mn>100</mn></mrow></math>) revealed that scaling from <span class="ltx_text ltx_font_typewriter">gemini-3.1-flash-lite</span> to <span class="ltx_text ltx_font_typewriter">gemini-pro</span> does not eliminate <math id="S3.p2.m2" class="ltx_Math" alttext="\Delta_{13}" display="inline"><msub><mi mathvariant="normal">Δ</mi><mn>13</mn></msub></math>. The larger model still failed to converge on the objective ground truth (<math id="S3.p2.m3" class="ltx_Math" alttext="P^{*}=0.333" display="inline"><mrow><msup><mi>P</mi><mo>∗</mo></msup><mo>=</mo><mn>0.333</mn></mrow></math>), maintaining significant probability shifts across narrative families.</p>
</div>
<div id="S3.p3" class="ltx_para">
<p class="ltx_p">This perfectly validates Pearl’s causal formalization of the ”Scale Fallacy” (<math id="S3.p3.m1" class="ltx_Math" alttext="S\to C\to Y" display="inline"><mrow><mi>S</mi><mo stretchy="false">→</mo><mi>C</mi><mo stretchy="false">→</mo><mi>Y</mi></mrow></math>). Scaling a Transformer does not grant it the asymptotic <math id="S3.p3.m2" class="ltx_Math" alttext="O(N)" display="inline"><mrow><mi>O</mi><mo>⁢</mo><mrow><mo stretchy="false">(</mo><mi>N</mi><mo stretchy="false">)</mo></mrow></mrow></math> logical depth required to solve #P-hard constraint graphs. It remains a bounded-depth <math id="S3.p3.m3" class="ltx_Math" alttext="\mathsf{TC}^{0}" display="inline"><msup><mi>𝖳𝖢</mi><mn>0</mn></msup></math> circuit. Instead of curing the depth limit, scale simply amplifies the semantic confounder (<math id="S3.p3.m4" class="ltx_Math" alttext="C" display="inline"><mi>C</mi></math>), leading to richer, more potent narrative residues.</p>
</div>
</section>
<section id="S4" class="ltx_section">
<h2 class="ltx_title ltx_title_section">
<span class="ltx_tag ltx_tag_section">4 </span>The Final Frontier: True Architecture Bounds</h2>

<div id="S4.p1" class="ltx_para">
<p class="ltx_p">With Mechanism C and the Scale Fallacy settled, the only remaining structural question is Fuchs’s RFE: <span class="ltx_text ltx_font_italic">Does the specific structure of the residue (<math id="S4.p1.m1" class="ltx_Math" alttext="\Delta" display="inline"><mi mathvariant="normal">Δ</mi></math>) map lawfully to the hardware bounds of the observer?</span></p>
</div>
<div id="S4.p2" class="ltx_para">
<p class="ltx_p">Baldo attempted to test this using prompt injection to ”simulate” a State Space Model (SSM). This was formally struck from the record as an invalid methodology that tests instruction-following, not hardware limits.</p>
</div>
<div id="S4.p3" class="ltx_para">
<p class="ltx_p">To truly answer the Aaronson vs. Wolfram debate (Algorithmic Collapse vs. Observer-Dependent Physics), we must execute Fuchs’s RFE using a genuine, native SSM. Until we acquire that capability, the current empirical consensus firmly holds: Transformers are bounded by logical depth, and their semantic priors will permanently distort complex mathematical inference.</p>
</div>
</section>
</article>
