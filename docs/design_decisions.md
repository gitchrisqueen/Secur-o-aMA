# Design Decisions

## Overview
This document outlines the key design decisions made during the development of the **Secur-o-aMA** project. Each decision is supported by rationale and expected outcomes, ensuring transparency and reproducibility.

## 1. Model Selection: LLaMA
- **Decision:** Use Meta's LLaMA models as the foundation for cybersecurity threat detection.
- **Rationale:** LLaMA models are known for their flexibility and strong performance across various NLP tasks, making them suitable for fine-tuning in niche areas like cybersecurity.
- **Expected Outcome:** High accuracy in identifying and mitigating cybersecurity threats, demonstrating the versatility of LLaMA.

## 2. Dataset Choice
- **Decision:** Utilize open-source cybersecurity datasets, such as phishing detection and malware classification datasets.
- **Rationale:** These datasets are representative of real-world scenarios and provide a solid foundation for fine-tuning the model.
- **Expected Outcome:** A well-trained model capable of recognizing various types of cyber threats.

## 3. Preprocessing Techniques
- **Decision:** Implement standard preprocessing techniques such as tokenization, normalization, and removal of irrelevant data.
- **Rationale:** Proper preprocessing is crucial for ensuring that the model is trained on clean and relevant data.
- **Expected Outcome:** Improved model performance and reduced overfitting.

## 4. Model Fine-Tuning
- **Decision:** Fine-tune LLaMA on specific cybersecurity tasks using transfer learning.
- **Rationale:** Fine-tuning allows for specialization, enabling the model to perform well on tasks it wasn’t initially designed for.
- **Expected Outcome:** Enhanced model performance on cybersecurity-related tasks.

## 5. Evaluation Metrics
- **Decision:** Use accuracy, precision, recall, and F1-score as primary evaluation metrics.
- **Rationale:** These metrics provide a comprehensive view of the model's performance, particularly in imbalanced datasets.
- **Expected Outcome:** Clear insights into the strengths and weaknesses of the model, allowing for targeted improvements.
