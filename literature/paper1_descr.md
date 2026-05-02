# Paper: AlphaFold accelerates AI powered drug discovery: finding a new CDK20 inhibitor

**Authors:** Ren, F., Ding, X., Zheng, M., Aspuru-Guzik, A., Zhavoronkov, A. et al.

**Year:** 2023

**DOI:** https://doi.org/10.1039/D2SC05709C


## 1) Main idea

This is the first study to successfully use an AlphaFold-predicted protein structure to discover a real drug candidate. The target was CDK20, a liver cancer protein with no experimental 3D structure. The authors fed AlphaFold's predicted CDK20 structure into two AI platforms: PandaOmics (target validation) and Chemistry42 (generative chemistry). From 8,918 AI generated molecules, only 7 were synthesized, yielding a hit in 30 days. A second round produced a compound with nanomolar potency that selectively kills liver cancer cells over healthy cells.


## 2) Data used

**Target selection:** 10 HCC datasets (1,133 tumor + 674 healthy samples) from GEO, ArrayExpress, and TCGA.

**Molecule design:** 8,918 AI generated structures, 13 synthesized total (7 round one, 6 round two).

**Protein structure:** AlphaFold AF-Q8IZL9-F1-model_v1 (CDK20, residues 1–302 after trimming the low-confidence C-terminal tail).

**Features:** Gene expression, mutations, protein networks, literature text, ATP pocket shape (~150 Å³), and Tanimoto similarity checks for novelty.

**Train/test split:** Not applicable. AI generated de novo molecules, validation was experimental (binding, kinase, and cell assays).


## 3) AI models

**PandaOmics (target identification):** A deep learning platform integrating gene expression, variants, protein networks, and literature via the iPANDA algorithm. A meta analysis of 10 HCC datasets followed by a first in class filter (no existing drugs, no Phase I trials, no known inhibitors) ranked CDK20 as the top target.

**Chemistry42 (generative chemistry):** A three stage pipeline: (1) energy based pocket detection with methyl probes, (2) molecule generation via GENTRL (reinforcement learning) and VAE-TRIP, (3) docking and clustering. Pretrained models were conditioned on the AlphaFold pocket, round two also used the binding pose of the first hit. Generated 8,918 molecules (round one) and 16 (round two), synthesized 7 and 6 respectively.

**Key novelty:** First demonstration that an AlphaFold predicted structure can replace an experimental structure for hit identification, achieving a validated hit in 30 days with only 7 compounds.


## 4) Evaluation and outcomes

**Metrics:** Binding affinity (Kd) via KINOMEscan, kinase inhibition (IC50) via radiometric assay, cytotoxicity (IC50) via CellTiter Glo in Huh7 (CDK20-high) and HEK293 (control) cells.

**Results:**

| Compound | Kd | IC50 (kinase) | IC50 Huh7 | IC50 HEK293 |
|----------|-----|---------------|-----------|-------------|
| ISM042-2-001 (round 1) | 9.2 ± 0.5 μM | >6,000 nM | Not tested | Not tested |
| ISM042-2-048 (round 2) | 566.7 ± 256.2 nM | 33.4 ± 22.6 nM | 208.7 nM | 1,706.7 nM |

ISM042-2-048 showed 15 fold better binding, >180fold better kinase inhibition, and 8.2fold selectivity for cancer cells over healthy cells.

**Comparison to known inhibitors:** ISM042-2-048 (IC50 = 33.4 nM) is more potent than Palbociclib (1,260–8,680 nM) and AAPK25 (Kd = 8,020 nM), though less potent than BMS-357075 (Kd = 56 nM) and MER-128 (IC50 = 2 nM). Critically, it has a novel scaffold with low similarity to all prior CDK20 inhibitors.

**Conclusion:** First experimental validation that AlphaFold predicted structures enable hit discovery for targets without experimental structures. Limitation: the low confidence C-terminal domain (residues 303–346) blocked the pocket and required manual removal. Future work: ADME optimization, selectivity profiling, and extension to GPCRs and E3 ligases.