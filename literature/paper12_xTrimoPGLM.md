# xTrimoPGLM
Authors :Bo Chen , Xingyi Cheng , Pan Li, Yangli-ao Geng, Jing Gong, Shen Li, Zhilei Bei , Xu Tan, Boyan Wang, Xin Zeng, Chiming Liu , Aohan Zeng, Yuxiao Dong, Jie Tang  & Le Song 
Published: Nature methods, April 3., 2025

### Summary

In this paper, xTrimoPGLM, which is a large-scale protein language model was introduced. It was designed to unify protein understanding and protein generation using a single framework. Existing protein language models are typically specialised for one specific trask like structure prediction or generative tasks due to differences in pre-training. This model addresses these limitations by combining masked language modelling with autoregressive generation into one training mechanism. Using this method, the model was able to learn bidirectional contextual representations and generative capabilities together. The model was trained on a massive scale and demonstrated a very strong performance across a wide range of different protein-related tasks. It outperformed various state-of-the-art models in most benchmarks and is able to both predict protein properties as well as generate new protein sequences with realistic structural characteristics.

### Data and tools

The model was trained on a large protein dataset which consisted of:
- 940 million protein sequences
- 200 billion amino acid residues
- 1 trillion training token
The training data composed evolutionary diversity and sequence variation which is essential for learning protein-structure relationships.
Two main evaluation setups were used:
- Protein understanding benchmarks like structure, function as well as interactions and developability
- Protein generation tasks such as "de novo" design and conditional generation
Other evaluation steps included:
- OOD datasets with proteins that were not seen during training 
- Structural prediction benchmarks

### Model architecture

xTrimoPGLM is based on a General Language Model framework that integrates two obectives
1. Masked Language Modeling (MLM)
	- Predicts amino acids
	- Enables bidirectional context understanding
2. Autoregressive Generation (GLM)
	- Predicts sequence continuation
	- Enables generative capabilities
Training occurs in tow stages
- Stage 1:MLM pretraining using 400 billion tokens
- Stage 2: Combined MLM and GLM using 600 billion tokens
Key features
- Combination of bidirectional and autoregressive learning
- Support of both analysis and generation tasks
- Efficient scaling with increasing model size
For downstream tasks:
- Uses MLP probing -> fixed representations
- LoRA fine-tuning for adaptations

### Evaluations

|Task type|xTrimoPGLM|Other PLMs|Outcome|
|---|---|---|---|
|Protein understanding (18 tasks)|Very high|Strong|Outperforms in most tasks|
|Structure prediction|High accuracy|Strong|Improved TM-scores|
|OOD sequence prediction|Low perplexity|Higher|Better generalisation|
|Protein generation|High quality|Variable|Realistic structures|
- Key results
	- Outperforming of 15/18 state-of-the-art models in understanding tasks
	- Low perplexity on unseen protein data
	- "De novo" protein design with realistic structures
	- Improved structure prediction using xT-Fold
Larger models have better performance and unified objectives improve versatility. The use of LoRAs enables effective fine-tuning
- Limitations
	- Generative hallucinations
	- Real-world constraints
	- High computational costs
