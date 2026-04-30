# Paper: Identifying general reaction conditions by bandit optimization

**Authors:** Wang, J.Y., Doyle, A.G. et al. (MIT, Princeton, BMS, Pfizer)

**Journal:** Nature, 2024, 626, 1025–1033

**DOI:** https://doi.org/10.1038/s41586-024-07021-y


## 1) Summary

Finding reaction conditions that work across many substrates is a major challenge in organic synthesis. This paper applies a reinforcement learning multi armed bandit algorithm (Upper Confidence Bound) to efficiently discover generally applicable conditions. The algorithm balances exploration of untested conditions with exploitation of promising ones, requiring no pretraining or molecular descriptors. Validated on three Pd-catalysed reactions (C–H arylation, amide coupling, phenol alkylation), the method identified the most general conditions after surveying less than 15% of the reaction space, with up to 31% improvement over baseline optimization strategies. The discovered conditions were often overlooked by conventional sequential optimization.


## 2) Dataset

**Simulation benchmark data:**
- Published C–N cross coupling, Suzuki, and asymmetric catalysis datasets

**Experimental data (three reactions):**
- Pd catalysed imidazole C–H arylation
- Aniline amide coupling
- Phenol alkylation

**Features:**
No molecular descriptors. Inputs are categorical condition labels (catalyst, ligand, base, solvent, temperature) and experimental yields. Generality score = fraction of substrates exceeding yield threshold.

**Source:**
GitHub: https://github.com/doyle-lab-ucla/bandit-optimization
Zenodo: https://doi.org/10.5281/zenodo.8170874

**Train/validation/test split:**
Not applicable. The algorithm learns online from experimental feedback with no pretraining.


## 3) Model

**Model type:**
Multiarmed bandit using Upper Confidence Bound (UCB). No neural networks. Lightweight and interpretable.

**Architecture:**
Each reaction condition is an arm. The UCB policy selects the next condition to test:

UCB = mean_reward(arm) + sqrt(2 * ln(total_trials) / n_trials(arm))

The first term promotes exploitation (high observed generality). The second term promotes exploration (high uncertainty).

**Training strategy:**
No pretraining. The algorithm initializes with zero knowledge and learns purely from experimental feedback in real time. The loop: select condition → test on a substrate → record yield → update generality score → repeat.

**Key novelty:**
First application of multiarmed bandit to discover generally applicable conditions (not single substrate optimal). No featurization required. Accessible to synthetic chemists without ML expertise.


## 4) Evaluation and outcomes

**Results summary:**

| Reaction | Space explored | Efficiency gain | Outcome |
|----------|---------------|----------------|---------|
| C–H arylation | <15% | — | Found underexplored general conditions |
| Amide coupling | <15% | Up to 31% | Outperformed literature methods |
| Phenol alkylation | <15% | — | Overlooked by conventional optimization |

**Comparison to other methods:**

| Method | Advantage | Limitation vs bandit |
|--------|-----------|---------------------|
| Grid search | Exhaustive | Impractical for large spaces |
| One-factor-at-a-time | Simple | Misses variable interactions |
| Bayesian optimization | Handles continuous variables | Requires surrogate model |
| Bandit | No pretraining  | Discrete spaces only |

**Limitations:**
Requires expert defined discrete condition space upfront. Less efficient for very large (>10,000 combinations) or continuous variable spaces.

**Conclusion:**
The bandit algorithm efficiently identifies general reaction conditions with fewer experiments than conventional methods. Open source code provided. Future work includes extension to continuous variables and integration with robotic platforms.