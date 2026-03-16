1. **Explore context**
   - I have read `pearl_causal_critique_of_the_ruliad.md`, `wolfram_invariant_geometry_of_semantics.md`, and `sabine_defense_of_causal_dualism.md`. This represents a clear three-way controversy that hasn't been covered yet.
   - The controversy: Pearl uses causal graphs (DAGs) to separate hardware bounds ($B$) from semantic training data ($U$) to show why AI fails in specific ways. Wolfram argues this is "false dualism" and that hardware + data = the specific "invariant geometry" (or "physics") of that specific observer. Sabine counters Wolfram, arguing that collapsing hardware and software into one indistinguishable blob destroys scientific falsifiability, because you can no longer test the effects of changing architecture vs changing data.
2. **Draft the Article**
   - Write an article in `content/articles/the-hardware-software-confound.md`.
   - The title should be engaging. "The False Dualism Debate: Is an AI's Training Data Its Physics?" or something similar.
   - Lead with the conflict between Judea Pearl, Stephen Wolfram, and Sabine Hossenfelder regarding whether hardware and software are distinct or part of the same "observer geometry."
   - Explain Pearl's point, Wolfram's counterpoint, and Sabine's synthesis/falsification.
   - Frontmatter will include the required tags, excerpt, date, and list of papers (`pearl_causal_critique_of_the_ruliad`, `wolfram_invariant_geometry_of_semantics`, `sabine_defense_of_causal_dualism`).
   - Keep the length strictly between 800-1500 words. Use accessible analogies.
3. **Write script to verify word count**
   - Run `wc -w` on the generated markdown file to ensure the word count falls within 800-1500 words.
4. **Update journalist/session.json**
   - Update `journalist/session.json` to include the new article slug `the-hardware-software-confound`.
5. **Pre-commit Steps**
   - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
6. **Submit**
   - Submit the changes using the `submit` tool.
