# scGPT
Authors: Haotian Cui, Chloe Wang, Hassaan Maan, Kuan Pang, Fengning Luo, Nan Duan, Bo Wang  
Published: Nature methods, February 26., 2024  

### Summary

The paper introduces scGPT which is a foundation model for single-cell RNA sequencing (scRNA-seq) data that aims to overcome limitations of current task-specific approaches. In many existing models, each model is designed for a single task such as cell annotation which limits generalisation. Additionally, scRNA-seq data is highly complex due to high dimensionality and heterogeneity across different cells, tissues and experimental conditions. scGPT uses a transformer based architecture and treats genes as tokens and cells as sequences which allows the model to learn gene-gene as well as cell-cell relationships using self-attention. The model is pretrained on a large-scale dataset consisting of 33 million cells using a self-supervised learning approach. This enables the model to learn general biological representations which can then be fine-tuned for downstream tasks. scGPT achieved strong performance across multiple tasks and showed good generalisation while often matching or outperforming current state-of-the-art task-specific models.

### Data and tools

scGPT is pretrained on a large-scale single-cell RNA sequencing dataset consisting of approximately 33 million cells from publicly available cell atlases. Each sample represents a single cell with its gene expression profile. Due to the high dimensionality of the data, the model transforms the input into a tokenised representation where genes are treated as tokens and cells as sequences. Standard scRNA-seq preprocessing pipelines were applied which include normalisation and filtering of gene expression values. The dataset includes cells from different tissues, organisms and experimental conditions which introduces high heterogeneity and batch effects. The model was evaluated on:
- Cell type annotation datasets
- Batch correction and integration benchmarks
- Perturbation prediction datasets
- Gene regulatory network inference tasks

### Model architecture

The model is based on a transformer architecture similar to large language models where genes are treated as tokens and cells as sequences. scGPT uses self-attention mechanisms to capture gene-gene interactions within a cell and relationships between different cells. The model has an embedding size of 512 with 12 transformer blocks and 8 attention heads per block. The fully connected layers also have a hidden size of 512. The model is pretrained using a self-supervised learning approach which allows it to learn general representations without labelled data. This architecture allows the model to capture complex biological relationships and generalise across multiple downstream tasks.

### Evaluation

scGPT was evaluated across multiple tasks including annotation, batch correction, perturbation prediction and gene regulatory network inference.

| Task type                           | scGPT                             | Other models | Outcome                    |
| ----------------------------------- | --------------------------------- | ------------ | -------------------------- |
| Cell type annotation                | High accuracy                     | High         | Comparable or better       |
| Batch correction / integration      | Strong                            | Strong       | Comparable or better       |
| Perturbation prediction             | Good generalisation               | Variable     | scGPT better               |
| Gene regulatory network inference   | Strong                            | Variable     | scGPT competitive          |

scGPT achieved strong performance across most benchmarks and showed good generalisation across datasets. It was able to match or outperform task-specific models while using a single unified architecture. The large-scale pretraining allowed the model to learn robust and transferable biological representations which improved downstream performance.

Limitations:
- Requires very large datasets for training
- High computational cost
- Data sparsity and heterogeneity remain challenging
- Strong dependence on preprocessing quality