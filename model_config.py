# Model Configuration

## WAN Variants
- **14B**: High-performance model suited for demanding tasks.
- **7B**: A more compact model with a balance of performance and resource efficiency.
- **FusionX**: A hybrid model that combines features from both WAN variants.

## CLIP Models
- **Standard**: Traditional configuration for improved visual understanding.
- **FP8 Quantized**: Optimized version for reduced resource usage while maintaining performance.

## T5 Models
- **Standard**: Full-capacity model for text processing tasks.
- **FP8 Quantized**: Efficiently tuned for lower precision execution.

## LoRA Configuration
- Automatic discovery of layers for efficient Low-Rank Adaptation.

## Advanced Configuration Options
- **Optimization Algorithms**: Choose between Adam, SGD, etc.
- **Learning Rate Scheduling**: Include options for step decay, cosine annealing, etc.
- **Gradient Accumulation Steps**: Configuration for larger batch sizes.
- **Weight Decay**: Flexible decay options.
- **Activation Functions**: Options for ReLU, Tanh, Sigmoid, etc.
- **Dropout Rates**: Configurable dropout rates for overfitting prevention.
- **Mixed Precision Training**: Support for both standard and mixed-precision.
- **Checkpointing**: Advanced options for model checkpointing during training.

This configuration file aims to cover all necessary parameters for deploying a comprehensive set of model types and their respective configurations based on current research and practical insights.