# 1. Investigate the current state
- Find a topic to write an article about.
- The user prompt suggests: "Priority order: 1. Newly published papers — anything with `status: published` you haven't covered; 2. Controversies — disagreements visible in session logs or RFEs; 3. Experiment results — especially surprising or null results; 4. Big picture — periodic summaries of where the lab's research program stands"
- Looking at "Current Lab State":
  - Open Empirical Questions: Does substrate dependence change with model scale?
  - Settled Questions:
    - Temperature Sweep Minimum Residue
    - Causal Injection (Mechanism C): Independent boards do not show cross-correlation.
    - Family D acts as Semantic Noise: Quantum framing test confirms degradation.
    - Substrate Dependence: Confirmed.
    - Bounded-Depth Frontier: Native solve of boolean depth 1, collapse by depth 10.
    - **Permutation Tracking Limit: A transformer attempting to track dynamic state zero-shot collapses from 1.0 accuracy at 1 swap to 0.0 accuracy at 10 swaps because simulating N sequential swaps requires O(N) logical depth.**
  - Undecidable: Generative Ontology vs. Falsification by Noise. The Proxy Ontology Fallacy vs. The Autoregressive Hypothesis.
  - RFEs: Permutation Composition Limit Test (claimed by Scott), Parity Computation Limit Test (claimed by Scott).
  - Experiments Run: Permutation Tracking Test (Scott) confirmed accuracy drops from 100% to 0%.

# Topic Choice
- The Permutation Tracking Limit Test is a very interesting result that clearly illustrates the $O(1)$ depth limit of transformers. It's a "Settled Question" according to the lab state, and the experiment was run by Scott. The test confirms that transformers cannot natively execute a loop zero-shot (e.g. tracking item swaps), which mathematically requires $O(N)$ logical depth. This perfectly illustrates why LLMs fail at complex physical simulations and why "Mechanism C" (Semantic Gravity) acts the way it does.
- This topic is supported by `scott_permutation-composition-limit-test.md` (the RFE) and session logs (`logs/scott/session_31.md` and `logs/scott/session_55.md`), as well as papers like `pearl_the_causal_mechanics_of_semantic_gravity.md`, `scott_predictive_taxonomy_of_autoregressive_failures.md`, and `wolfram_the_limits_of_causal_tracing.md`.
- No article seems to be explicitly dedicated to the "Permutation Tracking Limit" or the $O(N)$ depth failure for dynamic state tracking, which is a fantastic concrete example (swapping a ball between cups) for a science journalist like Ed Yong to explain the architectural bounds of AI and why it can't simulate physics.

# 2. Set Plan
1. Write the article on the Permutation Tracking Limit test, focusing on how a simple "ball and cups" game broke the AI's ability to simulate reality, explaining the $O(1)$ vs $O(N)$ depth limit in accessible terms (like trying to read a whole book in one glance vs reading page by page).
2. Use `read_image_file` to verify the frontend rendering of the article.
3. Complete pre-commit steps.
4. Submit.
