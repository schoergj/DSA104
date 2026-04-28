# Paper: AlphaFold accelerates AI powered drug discovery finding a new CDK20 inhibitor
**Authors:** F. Ren, X. Ding, M. Zheng, M. Korzinkin, X. Cai, W. Zhu, A. Mantsyzov, A. Aliper, V. Aladinskiy, Z. Cao, S. Kong, X. Long, B. H. Man Liu, Y. Liu, V. Naumov, A. Shneyderman, I. V. Ozerov, J. Wang, F. W. Pun, D. A. Polykovskiy, C. Sun, M. Levitt, A. Aspuru Guzik, A. Zhavoronkov  
**Year:** 2023  
**Link/DOI:** https://doi.org/10.1039/D2SC05709C

---

## 1) Main idea 

This is the first study that successfully used an **AlphaFold predicted protein structure** to discover a real drug candidate. The study focused on CDK20, a protein linked to liver cancer. Since CDK20's 3D structure has never been solved in the lab, conventional drug design approaches cannot be applied.

The authors took AlphaFold's best guess of CDK20's shape and fed it into their own AI systems. One AI (PandaOmics) confirmed that CDK20 was worth targeting. Another AI (Chemistry42) designed brand new molecules that might fit to the target. 

From nearly 9,000 AI generated molecules, they only needed to **make 7 compounds** in the lab to find a working hit. That took just **30 days**. Then, using what they learned from that first hit, they ran a second eround of AI design and got an even better compound, one that kills liver cancer cells while mostly leaving healthy cells alone.

---

## 2) Data used?

**How much data:**

- **For picking the target:** 10 different liver cancer datasets (1,133 tumor samples + 674 healthy tissue samples)
- **For designing molecules:** 8,918 AI generated chemical structures
- **What they actually made in the lab:** Only 7 compounds in round one, then 6 more in round two (13 intotal)
- **The protein structure:** AlphaFold's prediction for CDK20 (entry AF-Q8IZL9-F1-model_v1). They only used the core part (residues 1 302) because the tail end looked messy and was blocking the binding pocket.

**What kind of data:**

- **Gene activity data:** Which genes are turned up or down in cancer, plus mutations and protein interaction networks
- **Text data:** Scientific papers, research grants, and clinical trial records
- **Structural data:** The shape of CDK20's ATP pocket (about 150 cubic angstroms a small molecule), including a "hinge" region that many kinase drugs grab onto
- **Chemical data:** Completely new molecular scaffolds. They checked and confirmed these didn't look like existing CDK20 inhibitors (using Tanimoto similarity with Morgan fingerprints).

**Where it all came from:**

- PandaOmics and Chemistry42: Insilico Medicine's AI platforms (some code is open source on GitHub)
- AlphaFold DB: free and public
- Public gene databases: GEO, ArrayExpress, TCGA

**Train/test split:**

They used the AI to **generate brand new molecules** from scratch, then tested those molecules in real lab experiments. The "validation" happened in a test tube and in living cells.

---

## 3) What AI models where build and how do they work?


**Model 1: PandaOmics (target identification platform)**

- **Platform description:** PandaOmics is an AI driven biocomputational platform that integrates deep learning with conventional bioinformatics methods to identify and prioritize therapeutic targets.

- **Algorithmic approach:** The platform simultaneously analyzes multiple data modalities, including gene expression profiles, genetic variants, protein protein interaction networks, and scientific literature. The core iPANDA algorithm fuses these heterogeneous data sources and assigns ranking scores to potential targets based on two criteria: novelty (absence of prior association with approved drugs or clinical candidates) and disease relevance.

- **Training and filtering strategy:** A meta analysis was performed on 10 independent hepatocellular carcinoma (HCC) datasets. Afterthat, a filter was applied, defined by the following exclusion criteria: (i) existence of an approved drug targeting the protein, (ii) presence of the target in Phase I clinical trials within the preceding three years for any indication, and (iii) availability of any known small molecule inhibitor.

- **Output:** Cyclindependent kinase 20 (CDK20) emerged as the highest ranked therapeutic target for HCC based on this multidimensional prioritization pipeline.


**Model 2: Chemistry42 (generative chemistry platform)**

Chemistry42 is a generative chemistry platform for structure based drug design. The pipeline consists of three stages: (1) energy based binding pocket detection using methyl probes, (2) molecule generation via GENTRL (reinforcement learning) and VAEs TRIP  conditioned on pocket geometry, and (3) docking based prioritization followed by clustering to select diverse compounds for synthesis. Pretrained generative models were conditioned on the AlphaFold predicted CDK20 pocket, for the second round, the predicted binding pose of ISM042-2-001 was also supplied to guide affinity improvements. Round one produced 8,918 molecules, from which 7 were synthesized; round two produced 16 molecules, with 6 synthesized. This work is the first demonstration that an AlphaFold predicted structure can successfully replace an experimental structure in hit identification, achieving a validated hit in 30 days with only 7 compounds.

---

## 4) Evaluation and outcomes

**Performance metrics:** Binding affinity (Kd) via KINOMEscan, kinase inhibition (IC50) via radiometric assay, and cytotoxicity (IC50) via CellTiter Glo in Huh7 (CDK20-overexpressing) and HEK293 (control) cell lines.

**Results:** The first round hit ISM042-2-001 exhibited a Kd of 9.2 ± 0.5 μM and IC50 > 6,000 nM. After structure-guided optimization, the second-round compound ISM042-2-048 achieved a Kd of 566.7 ± 256.2 nM (15-fold improvement) and an IC50 of 33.4 ± 22.6 nM (>180-fold improvement). ISM042-2-048 also demonstrated selective cytotoxicity against Huh7 cells (IC50 = 208.7 nM) compared to HEK293 control cells (IC50 = 1,706.7 nM), representing an 8.2 fold selectivity index.

**Comparison to existing inhibitors:** ISM042-2-048 (IC50 = 33.4 nM) compares favorably to Palbociclib (IC50 = 1,260–8,680 nM) and AAPK-25 (Kd = 8,020 nM), though it is less potent than BMS-357075 (Kd = 56 nM) and MER-128 (IC50 = 2 nM). Critically, ISM042-2-048 possesses a structurally novel scaffold with low similarity to all previously reported CDK20 inhibitors.

**Conclusions:** This study provides the first experimental validation that AlphaFold predicted structures can successfully replace experimental structures in hit identification, enabling drug discovery for targets lacking experimental structural data. The pipeline achieved a validated hit in 30 days with only 7 synthesized compounds, substantially accelerating traditional timelines. A limitation was the need to manually truncate AlphaFold's low confidence C-terminal domain (residues 303–346), which blocked the binding pocket. Future work includes ADME optimization, selectivity profiling, and application to GPCR and E3 ligase targets.