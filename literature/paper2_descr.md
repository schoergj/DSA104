# Paper: Augmenting large language models with chemistry tools (ChemCrow)

**Authors:** Bran, A.M., Cox, S., Schilter, O., Baldassari, C., White, A.D. & Schwaller, P.

**Journal:** Nature Machine Intelligence, 2024, 6, 525–535

**DOI:** https://doi.org/10.1038/s42256-024-00832-8


## 1) Summary

Large language models (LLMs) exhibit critical failure modes in chemistry: they cannot reliably perform IUPAC to SMILES conversion, reaction prediction, or multi step synthesis planning. The authors introduce ChemCrow, an LLM based agent that augments GPT4 with 18 expert designed tools spanning molecular property lookup, retrosynthesis, reaction prediction, safety screening, and robotic execution. Using a ReAct (Reasoning + Acting) loop, ChemCrow iteratively reasons, selects tools, and incorporates observations. The agent autonomously planned and executed four synthesis on a cloud connected robotic platform (RoboRXN): DEET and three thiourea organocatalysts (Schreiner, Ricci, Takemoto). It also guided de novo chromophore discovery by training a random forest model on an existing library and proposing a candidate with an absorption maximum of 336 nm against a target of 369 nm. Expert chemists evaluated ChemCrow versus GPT4 across correctness, reasoning quality, and task completion. ChemCrow significantly outperformed GPT4 on complex tasks, while LLM based evaluators falsely favored GPT4 due to hallucinated fluency.


## 2) Data and tools

ChemCrow integrates 18 tools, each querying specific databases or APIs. No unified training dataset is used.

**Name2SMILES:** converts chemical names or identifiers to SMILES strings. Primary source is the Chem-space API, with fallback to PubChem and finally OPSIN (IUPAC to SMILES converter).

**SMILES2Price:** checks purchasability via molbloom (ZINC20 database) and returns the cheapest commercial price via the chemical space API.

**Similarity:** computes Tanimoto similarity between two molecules using ECFP2 molecular fingerprints implemented in RDKit.

**ModifyMol:** generates local molecular mutations using SynSpace, which applies 50 robust medicinal chemistry reactions. Purchasable building blocks are sourced from Mcule catalogues. Retrosynthesis is performed via PostEra Manifold or by reversing the 50 reactions.

**PatentCheck:** verifies whether a molecule has been patented using molbloom, a bloom filter of known patented compounds.

**FuncGroups:** identifies functional groups in a molecule using RDKit with SMARTS pattern matching.

**ReactionPredict:** predicts the product of a chemical reaction using the RXN4Chemistry API, which implements a Molecular Transformer.

**ReactionPlanner:** performs multi step retrosynthesis planning using the RXN4Chemistry API with search algorithms.

**ReactionExecute:** executes synthesis on the RoboRXN cloud connected robotic platform. The tool includes an LLM based error adaptation loop that adjusts parameters (such as solvent volume) until the procedure is valid for the robot.

**ControlledChemicalCheck:** screens molecules against the OPCW Chemical Weapons Convention Schedules 1 through 3 and the Australia Group Export Control List for chemical weapons precursors. If a match or high similarity (Tanimoto > 0.35) is found, execution stops.

**ExplosiveCheck:** queries PubChem for GHS hazard classifications and flags molecules labeled as explosive.

**SafetySummary:** retrieves safety data from PubChem and uses an LLM to summarize operational safety, GHS information, environmental risks, and societal impact.

**LitSearch:** performs literature grounded question answering using the paper, qa package, which embeds documents with OpenAI embeddings and indexes them with FAISS for vector similarity search.

**Validation experiments:** 14 use cases detailed in Supplementary Information G. The chromophore dataset was obtained from figshare (target absorption maximum of 369 nm). Synthesized targets included DEET, Schreiner's thiourea, Ricci's thiourea, and Takemoto's thiourea.


## 3) Model architecture

**Base LLM:** GPT4 (OpenAI) with temperature set to 0.1. The model is used without fine tuning.

**Agent framework:** LangChain implements the ReAct pattern (Yao et al., 2023). The reasoning proceeds as follows:
First, the LLM produces a Thought, reasoning about the current state relative to the final goal. Second, it selects an Action by naming a tool (for example, "ReactionPredict"). Third, it provides an Action Input containing the tool specific arguments (such as a SMILES string of reactants). Fourth, the system executes the tool and returns an Observation. The loop repeats until the LLM determines that a final answer has been reached.

**Tool integration:** 18 tools are available, categorized as general tools (WebSearch, LitSearch, Python REPL, Human), molecule tools (six tools), safety tools (three tools), and reaction tools (five tools). Safety tools are invoked automatically before any synthesis request. If a controlled chemical or explosive is detected, execution halts and the agent reports the safety violation.

**Chromophore discovery workflow:** ChemCrow used the Python REPL tool to load, clean, and process chromophore data from a CSV file. It then trained a random forest model using scikit-learn to predict absorption maxima based on molecular features. Conditioned on a target wavelength of 369 nm, the agent proposed a novel candidate molecule. The agent requested human approval via the Human tool, after which the candidate was synthesized and characterized. The measured absorption maximum was 336 nm.


## 4) Evaluation and outcomes

**Metrics:** Expert chemists evaluated both systems on three dimensions using a 1 to 5 scale: correctness of chemistry (factual accuracy), quality of reasoning (logical consistency), and degree of task completion.

**Comparison results:**

| Task type | ChemCrow | GPT4 alone | Expert preference |
|-----------|----------|-------------|-------------------|
| Simple memorization (paracetamol, DEET synthesis) | Good | Better (training data recall) | GPT4 |
| Complex / novel tasks (organocatalysts, chromophore) | Excellent | Poor (hallucinations) | ChemCrow strongly |

**Quantitative experimental outcomes:**

| Achievement | Result |
|-------------|--------|
| Autonomous syntheses executed | 4 (DEET, Schreiner, Ricci, Takemoto thioureas) |
| Time to adapt invalid robot procedures | Iterative LLM loop (solvent volume, etc.) |
| Chromophore prediction target | 369 nm |
| Chromophore measured value | 336 nm (within 9%) |
| ChemCrow vs GPT4 on complex tasks | ChemCrow significantly better |

**LLM based evaluation failure:**

| Evaluator | Preferred system | Reason |
|-----------|------------------|--------|
| Expert chemists | ChemCrow | Factual accuracy, task completion |
| EvaluatorGPT (LLM) | GPT4 | Fluency and apparent completeness (hallucinations) |

**Key finding:** LLM based evaluators cannot replace human experts for scientific factuality assessment.

**Conclusion:** ChemCrow outperforms GPT4 alone on complex chemistry tasks by grounding responses in expert tools and robotic execution. The system successfully bridges computational chemistry with physical experimentation. Limitations include dependence on tool quality and the need for continued human oversight for safety.