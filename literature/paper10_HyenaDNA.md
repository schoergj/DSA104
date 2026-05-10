# HyenaDNA

Authors: Eric Nguyen, Michael Poli , Marjan Faizi, Armin W. Thomas, Callum Birch Sykes, Michael Wornow, Aman Patel, Clayton Rabideau, Stefano Massaroli, Yoshua Bengio, Stefano Ermon, Stephen A. Baccus, Christopher Ré1
Published: arXiv, November 15., 2023

### Summary

The paper introduces HyenaDNA which is a genomic foundation model that aims to overcome limitations of transformer based approaches in DNA sequence modelling. In transformer based approaches, the models struggle with genomic data due to their quadratic scaling in the length of sequences. They often have a restriction of a few thousand tokens which is insufficient to capture long-range dependencies in a DNA sequence. Many transformer based models also rely on k-mer tokenisation, which reduces resolution and can obscure biologically important single nucleotide polymorphisms (SNPs). HyenaDNA uses a long convolution-based architecture (Hyena operator) to replace normal attention based transformer mechanisms. This enables efficient processing of long sequences. The model is thus able to work at single nucleotide resolution where each base is treated as a token for up to 1 million tokens which is a 500x increase over previous models. The model was pre-trained on the human reference genome using a next-token prediction approach and techniques like sequence length warm-up for stable training and soft prompting were introduced for downstream adaptation. HyenaDNA achieved strong performance across multiple genomic tasks and showed the ability to model long-range dependencies while maintaining high resolution while outperforming current state-of-the-art models.

### Data and tools

HyenaDNA is pretrained on the human reference genome and treats DNA as a continuous sequence of nucleotides. The difference to previous approaches is that HyenaDNA avoids tokenisation into k-mers and instead uses the 4 bases as well as some special tokens. The model then processes extremely long sequences to allow long-range genomic interactions such as regulatory dependencies. To allow stable training on such long sequences, the authors used sequence length warm-up which gradually increases the input length during training. The model was evaluated on:
- Genomic Benchmarks -> Regulatory element classification
- Nucleotide Transformer benchmarks
- Custom long-range tasks such as species classification

### Model architecture

The model is based on a decoder-only architecture where attention is replaced by the Hyena operator which is a convolution-based mechanisms to remove the quadratic length complexity. HyenaDNA uses long convolutions instead of attention which drastically reduces the computational complexity and allows single nucleotide resolution. It also uses a global receptive field at each layer. THe convolutional filters are generated dynamically using a small neural networks which allows efficient handling of long sequences. This architecture allows the model to be significantly faster than transformer based models at long sequences while maintaining comparable or even better performance.

### Evaluation

HyenaDNA was evaluated across multiple genomic tasks which include classification, regulatory prediction and long-range modeling.

| Task type                           | HyenaDNA                          | Other models | Outcome                |
| ----------------------------------- | --------------------------------- | ------------ | ---------------------- |
| Regulatory element classification   | High accuracy                     | Strong       | HyenaDNA better        |
| Enhancer identification             | Very high                         | Moderate     | Up to +20% improvement |
| Species classification (long-range) | Strong                            | Weak         | HyenaDNA much better   |
| General genomic benchmarks          | state-of-the-art on most datasets | Variable     | HyenaDNA better        |
HyenaDNA achieved state-of-the-art performance on most of the benchmarks. It also performed well with far fewer parameters and less data but long context significantly improved performance. This enabled in-context learning in genomics.

Limitations:
- Complex training for long sequences
- Dependence on large-scale genomic data
- Early exploratory research for biological tasks
