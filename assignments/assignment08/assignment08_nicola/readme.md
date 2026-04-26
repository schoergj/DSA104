# Literature Descirption

**Tamás, B., Alberts, M., Laino, T. et al. Amino acid composition drives aggregation during peptide synthesis. Nat. Chem. 18, 677–685 (2026). https://doi.org/10.1038/s41557-026-02090-0**

1. This paper investigates the relationship between amino acid composition and peptide aggregation during solid-phase peptide synthesis (SPPS). Using machine learning models trained on experimental and literature data, the authors aim to predict whether a peptide sequence will aggregate during synthesis. A key finding is that overall amino acid composition plays a more important role than sequence order, suggesting that aggregation is largely governed by global physicochemical properties rather than local sequence motifs. The study provides both predictive models and chemical insight into aggregation behavior.
2. Size is 539 peptide sequences with its source being experimental SPPS and literature data. Binary lables were used (aggregation vs non-aggregating). For features, amino acid composition, physiochemical properties and descriptors were used.
3. Used XGBoost as the main model and Random Forest for comparison. Feature based models with the input being the amino acid sequence. Supervised learning
4. Compared models based on accuracy. More complex models (e.g. language models) did not significantly outperform simpler approaches. Outcome: aggregation not strongly squence dependent but instead depend mainly onamino acid composition, hydrophobic content and physiochemical properties.



**Baldwin, L., A. et al. Continuous flow synthesis of pyridinium salts accelerated by multi-objective Bayesian optimization with active learning, Chem. Sci., 2023, 14, 8061-8069 (https://pubs.rsc.org/en/content/articlelanding/2023/sc/d3sc01303k)**

1. This paper presents a machine learning–assisted optimization of a chemical reaction using a human-in-the-loop workflow. The authors optimize the continuous flow synthesis of butylpyridinium bromide by applying multi-objective Bayesian optimization (EDBO+), aiming to simultaneously maximize reaction yield and production rate. The method efficiently explores a large reaction parameter space and identifies optimal trade-offs (Pareto front) with very few experiments. The study demonstrates that combining machine learning with continuous flow chemistry enables faster, more efficient, and scalable reaction optimization compared to traditional approaches.
2. 75 experiments with inpit features being temnperature, residence time and mole fraction. Output is reaction yield. Data was measured by NMR. Small data set typically used in Bayesian Optimization
3. Bayesian Optimization
4. 

**Yiping Liu, Zhou Yu, Jiayi Zhang, Yujie Chen, Shu Wu, Leyi Wei, Xiangxiang Zeng, Yuyan Han, and Yuansheng Liu. Enhancing Retrosynthesis Prediction with Distillation Learning, J. Chem. Inf. Model., 2026 66 (7), 3774-3786 (https://pubs.acs.org/doi/10.1021/acs.jcim.6c00322?utm_source=chatgpt.com)**

1. This paper presents a deep learning approach to single-step retrosynthesis prediction, where the goal is to predict reactant molecules from a given product. The authors improve transformer-based retrosynthesis models by introducing distillation learning strategies, including mutual distillation and self-distillation. These approaches enhance model performance, especially for low-resource reaction classes. The study demonstrates that knowledge sharing between models leads to more accurate and robust retrosynthesis predictions, addressing key challenges such as data imbalance in chemical reaction datasets.
2. USPTO-50K (~50,000 reactions), USPTO-Full (~1 million reactions). Data are chemical reactions represented as SMILES. Input are molecules and the outputs are the reactants. Features are tokenized SMILES sequences (Transfer learning)
3. Transformer-based neural networks (sequence-to-sequence model). Architecture: Encoder–decoder transformer, Input: product SMILES, Output: reactant SMILES
4. Metrics used:
Top-k accuracy (Top-1, Top-3, Top-5, Top-10)
Performance (example):
Top-1 accuracy ≈ 68–69%
Top-10 accuracy ≈ ~94%