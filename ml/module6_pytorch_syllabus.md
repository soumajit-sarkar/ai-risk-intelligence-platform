# Module 6 — PyTorch AI Risk Model

**Project:** AI Risk Intelligence Platform  
**Environment:** Office Ubuntu desktop, VS Code, `uv`, Python 3.12  
**Framework:** PyTorch (CPU initially)  
**Format:** Python scripts (`.py`), no Jupyter Notebook or Anaconda  
**Syllabus:** 12 chapters  
**Status:** Working syllabus established on October 15, 2026

## Module Objective

Build a practical understanding of PyTorch, progressing from tensor fundamentals to a trained transaction risk-classification model that can be integrated into the AI Risk Intelligence Platform.

The goal is to understand the reasoning behind the model, not simply to write code that runs.

---

## Chapter 1 — PyTorch Fundamentals and Tensors

**Topics**
- What PyTorch is and why the project needs it
- Tensors and their relationship to NumPy arrays
- Tensor dimensions, shapes, data types, and values
- Creating, inspecting, and manipulating tensors
- Understanding tensor shapes in the context of transaction features

**Practical deliverable:** `ml/experiments/pytorch_day1.py`

**Completion goal:** Understand how PyTorch represents numerical data and inspect tensors representing transaction risk features.

## Chapter 2 — From Pandas Feature Matrix to PyTorch Tensors

**Topics**
- Converting engineered Pandas features into tensors
- Preserving feature order and data types
- Understanding input matrix dimensions
- Preparing numerical data for model input
- Avoiding accidental changes to feature meaning during conversion

**Practical deliverable:** `ml/experiments/pytorch_day2.py`

**Completion goal:** Convert the project's existing numerical feature matrix into model-ready inputs correctly.

## Chapter 3 — Training Data, Target Labels, and Datasets

**Topics**
- Difference between features (`X`) and target labels (`y`)
- What a training example represents
- PyTorch `Dataset` fundamentals
- Representing classification targets
- Understanding where trustworthy fraud or risk labels come from
- Distinguishing illustrative labels from verified outcomes

**Practical deliverable:** `ml/experiments/pytorch_day3.py`

**Completion goal:** Build a small dataset with clearly defined inputs and targets, while understanding its limitations.

## Chapter 4 — Training, Validation, and Test Splits

**Topics**
- Why data is divided into separate subsets
- Training, validation, and test data
- Data leakage and how to avoid it
- Reproducible data splitting
- Applying preprocessing without leaking information from held-out data

**Practical deliverable:** `ml/experiments/pytorch_day4.py`

**Completion goal:** Prepare a defensible data-splitting strategy for evaluating a risk model.

## Chapter 5 — Building a Neural Network

**Topics**
- Neural network fundamentals
- PyTorch's `nn.Module`
- Input, hidden, and output layers
- Weights, biases, and activation functions
- Input and output dimensions
- Producing transaction risk-classification outputs

**Practical deliverable:** `ml/experiments/pytorch_day5.py`

**Completion goal:** Build a small neural network and understand how inputs pass through its layers.

## Chapter 6 — Predictions, Loss, and Learning Objectives

**Topics**
- Model predictions and target labels
- Classification outputs and class scores
- Loss functions and what they measure
- Understanding the difference between prediction and error
- Choosing a suitable loss function for the classification setup

**Practical deliverable:** `ml/experiments/pytorch_day6.py`

**Completion goal:** Calculate predictions and loss and explain what the loss tells us about model performance during training.

## Chapter 7 — Gradients and Backpropagation

**Topics**
- Why neural networks need gradients
- Automatic differentiation in PyTorch
- `requires_grad` and computational graphs
- The `.backward()` operation
- Inspecting gradients
- How gradients indicate directions for parameter updates

**Practical deliverable:** `ml/experiments/pytorch_day7.py`

**Completion goal:** Understand how PyTorch calculates gradients and how they help a model learn.

## Chapter 8 — Optimizers and the Training Loop

**Topics**
- What an optimizer does
- Optimizer fundamentals
- Learning rate
- Clearing gradients
- Forward pass, loss calculation, backpropagation, and parameter updates
- Structuring a repeatable training loop

**Practical deliverable:** `ml/experiments/pytorch_day8.py`

**Completion goal:** Train a small neural network through a complete, understandable training loop.

## Chapter 9 — Training Behavior and Model Improvement

**Topics**
- Training over multiple epochs
- Monitoring loss
- Recognizing ineffective or unstable training
- Overfitting and generalization
- Using validation results to guide improvements
- Changing model settings based on evidence rather than guesswork

**Practical deliverable:** `ml/experiments/pytorch_day9.py`

**Completion goal:** Interpret training behavior and make reasoned decisions about whether a model needs improvement.

## Chapter 10 — Evaluating a Risk-Classification Model

**Topics**
- Evaluating predictions on held-out data
- Confusion matrices
- Precision and recall
- False positives and false negatives
- Accuracy and its limitations for imbalanced fraud data
- Selecting evaluation metrics based on risk-engine requirements

**Practical deliverable:** `ml/experiments/pytorch_day10.py`

**Completion goal:** Evaluate a model and explain the practical consequences of its classification errors.

## Chapter 11 — Saving, Reloading, and Predicting

**Topics**
- Saving model parameters
- Reconstructing and loading a trained model
- Inference versus training
- Using evaluation mode and disabling gradient tracking for inference
- Preparing unseen transaction features
- Keeping feature order and preprocessing consistent

**Practical deliverable:** `ml/experiments/pytorch_day11.py`

**Completion goal:** Reload a trained model and use it to generate predictions for previously unseen transactions.

## Chapter 12 — End-to-End AI Risk Model Integration

**Topics**
- Organizing model code for reuse
- Connecting preprocessing and model inference
- Integrating with the existing risk-engine service architecture
- Separating training code from inference code
- Handling invalid inputs and prediction errors
- Writing appropriate tests
- Preparing the model component for later FastAPI integration

**Practical deliverable:** An integrated model-inference component, with supporting tests, inside the existing project.

**Completion goal:** Connect the trained model to the project's risk-engine architecture in a maintainable and testable way.

---

## Learning Rules

1. Follow the established 12-chapter sequence without unnecessary scope expansion.
2. Do not repeat NumPy or Pandas topics that have already been completed unless a specific prerequisite needs clarification.
3. Use the existing project, VS Code, `uv`, Python 3.12, and `.py` scripts.
4. Learn concepts through explanation, reasoning, and meaningful practical work.
5. Use challenge-based exercises where the required outcome is given first, allowing the learner to decide how to approach the problem.
6. Do not artificially extend a chapter with repetitive exercises. Move forward once the essential reasoning has been demonstrated.
7. Explain important formulas and mathematical reasoning clearly and preserve useful derivations in a project reference file when appropriate.
8. Treat illustrative or synthetic labels as demonstrations only; do not present their results as evidence of real-world fraud detection.
9. Verify model performance with appropriate held-out data and metrics rather than assuming that successful training means the model is reliable.
10. Make curriculum and sequencing decisions as the mentor, explaining the reasoning instead of requiring the beginner to design the curriculum.

## Expected Outcome

By the end of Module 6, the learner should be able to explain the main steps of PyTorch model training, prepare model inputs, train and evaluate a basic neural network, save and reload it, and connect its inference functionality to the AI Risk Intelligence Platform.

This module establishes the foundation for subsequent improvements in model quality and production-oriented risk intelligence. Completing these chapters does not, by itself, establish that the model is production-ready or capable of detecting real fraud.

---

**Mentoring principle:** Build understanding first, demonstrate it through meaningful project work, and progress toward more advanced AI engineering without unnecessary repetition.