# Paper: AlphaFold accelerates AI-powered drug discovery: finding a new CDK20 inhibitor
**Authors:** F. Ren, X. Ding, M. Zheng, M. Korzinkin, X. Cai, W. Zhu, A. Mantsyzov, A. Aliper, V. Aladinskiy, Z. Cao, S. Kong, X. Long, B. H. Man Liu, Y. Liu, V. Naumov, A. Shneyderman, I. V. Ozerov, J. Wang, F. W. Pun, D. A. Polykovskiy, C. Sun, M. Levitt, A. Aspuru-Guzik, A. Zhavoronkov  
**Year:** 2023  
**Link/DOI:** https://doi.org/10.1039/D2SC05709C

---

## 1) Short summary of what this paper is about

This is the first study to successfully use an AlphaFold-predicted protein structure to find a new drug candidate. The researchers focused on CDK20, a protein linked to liver cancer that had no available experimental 3D structure. They fed AlphaFold's predicted structure of CDK20 into their own AI platforms: PandaOmics to confirm it was a good target, and Chemistry42 to design new molecules that might bind to it. From nearly 9,000 generated molecules, they made only 7 compounds and found a hit within 30 days. A second round of AI design gave them an even better compound that binds tightly to CDK20 and kills liver cancer cells while leaving normal cells largely unharmed.

---

## 2) What data they used

- **How much data:**
  - For target selection: 10 different liver cancer datasets (over 1,800 patient samples in total)
  - For molecule design: 8,918 AI-generated structures; only 13 were actually made and tested (7 first round, 6 second round)
  - The CDK20 structure came from AlphaFold's public database (entry AF-Q8IZL9-F1-model_v1), using just the core part of the protein after trimming a messy tail region

- **What kind of data:**
  - Gene activity data: which genes are turned on/off in cancer vs healthy tissue, plus mutations and protein interaction networks
  - Text data: scientific papers, research grants, and clinical trial records
  - Structural data: the shape of CDK20's ATP binding pocket (about the size of a small molecule), including key features like the "hinge" region that many drugs grab onto
  - Chemical data: completely new molecular scaffolds that don't look like existing CDK20 inhibitors

- **Where it came from:**
  - PandaOmics and Chemistry42 (Insilico Medicine's proprietary platforms, with some code open-sourced on GitHub)
  - AlphaFold DB (free for anyone to use)
  - Public gene databases: GEO, ArrayExpress, and TCGA

- **How they split the data:** Not applicable here, this wasn't a typical machine learning training setup. Instead, they used the AI to generate brand new molecules and then tested them in real lab experiments to see if they worked.

---

## 3) The AI models they built and trained

**Model 1 — PandaOmics (finding the right target):**
- **What it is:** A platform that combines deep learning with traditional bioinformatics to spot promising drug targets
- **How it works:** It scans gene expression data, mutation patterns, protein networks, and scientific literature simultaneously. A key piece is the iPANDA algorithm that integrates all this information and ranks potential targets by novelty and disease relevance.
- **How they trained it:** They ran a meta-analysis across 10 independent liver cancer datasets, then filtered for "first-in-class" targets meaning no existing drugs, no active clinical trials, and no known small molecule inhibitors.

**Model 2 — Chemistry42 (designing the molecules):**
- **What it is:** A generative chemistry platform that designs new molecules from scratch to fit a specific protein pocket
- **How it works:** First, it finds potential binding pockets by poking the protein surface with virtual probes. Then, generative models (like GENTRL, a reinforcement learning framework, and VAE-TRIP, a variational autoencoder) propose molecules that should fit that pocket. Finally, it docks the molecules and clusters similar ones together.
- **How they trained it:** They used pretrained generative models and conditioned them on the AlphaFold pocket's shape and chemistry. For the second round, they also fed in the predicted binding pose of their first hit compound to guide improvements.

**What's new here:** No one had ever used an AlphaFold-predicted structure (instead of a real experimental one) to successfully find a confirmed active molecule. The whole pipeline from picking a target to getting a tested hit took just 30 days and only 7 compounds.

---

## 4) How well it worked and what they learned

- **How they measured success:**
  - Kd: how tightly the compound binds to CDK20 (lower is better)
  - IC₅₀: how well it blocks CDK20's kinase activity or kills cancer cells
  - Selectivity: whether it kills CDK20-high cancer cells more than normal cells

- **What they achieved:**

| Compound | Binding strength (Kd) | Kinase blocking (IC₅₀) | Cancer cell killing (IC₅₀) | Normal cell killing (IC₅₀) |
|----------|----------------------|------------------------|----------------------------|----------------------------|
| First hit (round 1) | 9.2 micromolar | >6,000 nanomolar | not tested | not tested |
| Improved compound (round 2) | 567 nanomolar | 33 nanomolar | 209 nanomolar | 1,707 nanomolar |

The improved compound was about 8 times more toxic to liver cancer cells than to normal kidney cells a good sign it's not just a general poison.

- **How it compares to existing CDK20 inhibitors:**
  - Palbociclib (an existing cancer drug) blocks CDK20 about 40-260 times weaker
  - AAPK-25 binds about 14 times weaker
  - BMS-357075 binds slightly tighter (56 nM) but its structure is already known
  - MER-128 is more potent (2 nM) but the company never disclosed its structure
  - Importantly, the compound from this paper has a completely new chemical scaffold it doesn't look like any of these others

- **Final takeaways:** This is proof that AlphaFold predictions can replace experimental structures for finding new drug leads a huge deal for targets that have resisted structure determination. The main hiccup was that AlphaFold's predicted tail region was low-confidence and blocked the binding pocket, so the researchers had to manually cut it off before using the structure. The team says next steps are improving the compound's drug-like properties, testing it against other kinases to check selectivity, and trying the same approach on other hard-to-target protein families like GPCRs and E3 ligases.