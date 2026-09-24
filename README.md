# Twitter Sentiment Analysis Using Deep Learning

A Streamlit web application that classifies a tweet as **Negative**, **Neutral**, or **Positive** using a trained recurrent neural network (RNN).

## Overview

The application accepts tweet text, converts it into a token sequence using the saved tokenizer, pads the sequence to 99 tokens, and sends it to the trained Keras model. The class with the highest predicted probability is displayed as the sentiment result.

## Features

- Simple browser-based Streamlit interface
- Three-class sentiment prediction: Negative, Neutral, and Positive
- Saved TensorFlow/Keras model for inference
- Saved tokenizer reused during prediction
- Training and validation datasets included in the repository

## Project Structure

```text
.
├── app.py                  # Streamlit application
├── rnn_model.h5            # Trained RNN model
├── tokenizer.pkl           # Tokenizer used during model training
├── twitter_training.csv    # Training dataset
├── twitter_validation.csv  # Validation dataset
├── project.ipynb           # Notebook used for exploration/training
├── requirement.txt         # Python dependencies
└── .gitattributes          # Git LFS configuration
```

## Requirements

- Python 3.9 or newer
- Git
- Git LFS for downloading the model file correctly

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/erharsh2104/Twitter-Sentiment-Analysis-Using-Deep-learning.git
   cd Twitter-Sentiment-Analysis-Using-Deep-learning
   ```

2. Install and initialize Git LFS before checking out large model files:

   ```bash
   git lfs install
   git lfs pull
   ```

3. Create and activate a virtual environment:

   Windows PowerShell:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   macOS/Linux:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

4. Install the dependencies:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirement.txt
   ```

## Run the Application

Start the Streamlit server from the project directory:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal, usually `http://localhost:8501`.

Enter a tweet in the text area and select **Predict Sentiment** to view the result.

## Inference Pipeline

```text
Tweet text
	↓
Saved tokenizer (tokenizer.pkl)
	↓
Padded sequence (maximum length: 99)
	↓
Trained RNN (rnn_model.h5)
	↓
Sentiment label
```

The output class mapping used by the application is:

| Class | Label |
| ---: | --- |
| 0 | Negative |
| 1 | Neutral |
| 2 | Positive |

## Troubleshooting

### `tokenizer.pkl` or `rnn_model.h5` is missing

These files are required at application startup. Install Git LFS and download tracked files:

```bash
git lfs install
git lfs pull
```

### PowerShell blocks virtual-environment activation

Run PowerShell with an execution policy that permits local scripts, or activate the environment from Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### TensorFlow installation issues

Use a supported Python version and install dependencies inside a fresh virtual environment. TensorFlow availability can vary by operating system and Python version.

## Development Notes

- The model and tokenizer are loaded when `app.py` starts.
- Input sequences are pre-padded and truncated to a maximum length of 99.
- Empty or whitespace-only input is not sent for prediction.
- The notebook is included for reference and experimentation; the Streamlit app uses the saved artifacts for inference.

## License

This project is distributed under the license in [LICENSE](LICENSE).