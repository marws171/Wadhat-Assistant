# Wadhat - Smart Assistant for Government Services

**Wadhat** is an intelligent assistant powered by the **ALLaM-7B-Instruct-preview** model from SDAIA, designed to simplify access to Saudi government services via the Absher platform. It provides accurate and clear responses in Arabic, with an interactive experience that always ends with "وضحت؟".

## Features
- Custom greeting when the user says "اهلا".
- Clean responses without showing the prompt.
- Support for formal Arabic (Fusha).
- Runs on Google Colab using the quantized model.

## Setup
1. Install dependencies: `pip install -r requirements.txt`.
2. Run the code in `src/main.py` or use `notebooks/wadhat_colab.ipynb` on Colab.
3. Follow setup instructions in `docs/setup.md`.

## Usage
1. Say "اهلا" to receive a greeting from Wadhat.
2. Ask a question like "How do I renew my driver's license?" to get a response ending with "وضحت؟".

## Dependencies
- Python 3.8+
- ctransformers
- torch

