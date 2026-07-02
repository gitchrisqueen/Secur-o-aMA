# Secur-o-aMA — fine-tuning Meta's LLaMA for cybersecurity threat detection

> Applied LLM for security: I fine-tune Meta's LLaMA models to detect phishing, malware, and unauthorized access — an end-to-end project from raw data to trained model, with the design decisions documented.

---

## Problem
Cybersecurity teams triage a flood of signals — suspicious emails, files, and access patterns — where language understanding matters (phishing lures, obfuscated intent, log/alert text). General-purpose classifiers miss nuance, and most LLM demos never touch the security domain. Secur-o-aMA asks a focused question: **how well can an open LLM (LLaMA), fine-tuned on security data, detect and help mitigate real threats?**

## Approach
- **Fine-tuning** LLaMA for phishing detection, malware identification, and unauthorized-access prevention.
- A clean **data → preprocess → train → evaluate → (optional) deploy** pipeline (scripts or notebooks).
- Built on **open-source tools and free datasets** (Kaggle, PhishTank).
- **Documented design decisions and optimizations** in `docs/`.

## Architecture
```
Public security datasets (Kaggle, PhishTank)
        │  download_initial_datasets.py
        ▼
Preprocessing  (preprocess_data.py / data_preprocessing.ipynb)
        ▼
Fine-tune LLaMA  (train_model.py / model_training.ipynb)  ──►  models/fine_tuned
        ▼
Evaluation  (evaluate_model.py / evaluation.ipynb)  ──►  results/metrics + plots
        ▼
(Optional) Deploy for real-time detection  (deploy_model.py)
```
Repo organized into `data/`, `models/`, `notebooks/`, `scripts/`, `results/`, `docs/`.

## Results
- Evaluated on a held-out test set using **accuracy, precision, recall, and F1**; results and plots land in `results/` and `docs/performance_results.md`.
- **Headline metrics: work in progress** — see the evaluation notebook (`notebooks/evaluation.ipynb`) for the current numbers. (I'd rather show a real measured result than a placeholder.)

## Stack
Python 3.8+ · Meta LLaMA · Hugging Face Transformers (transfer learning) · PyTorch · Jupyter · Kaggle & PhishTank datasets · pip/venv. The exact fine-tuning method and hyperparameters are documented in `docs/design_decisions.md`.

## Run it yourself
```bash
git clone https://github.com/gitchrisqueen/Secur-o-aMA.git
cd Secur-o-aMA
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python scripts/download_initial_datasets.py   # needs Kaggle API + PhishTank key
python scripts/preprocess_data.py
python scripts/train_model.py
python scripts/evaluate_model.py
```

Runs locally, or in Google Colab / GitHub Codespaces. Requires a Kaggle API token and a PhishTank key.

## What I'd do next
- Lead with a per-task precision/recall/F1 table.
- Add a small inference demo (paste an email/log line → live classification).
- Benchmark fine-tuned LLaMA vs. a baseline to quantify the lift.
- Package `deploy_model.py` behind a simple API.

---

## License
MIT — see the `LICENSE` file.

## Contact
Questions or suggestions? Open an issue or reach me at [christopher.queen@gmail.com](mailto:christopher.queen@gmail.com).
