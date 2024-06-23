# colab_toolbox

Effortlessly set up and configure multiple tools for Google Colab without the need for shell commands or extensive coding.

## Features

- **Setup Selenium and ChromeDriver**: Easily install and configure Selenium and ChromeDriver for web scraping and automation tasks.
- **Setup Quarto for Documentation Export**: Quickly set up Quarto for exporting your documentation in different formats.
- **Setup Python Environments for Various Tasks**: Install and configure environments tailored for data ingestion, backtesting, modeling, and more.
- **Common Git Commands for Colab**: Simplify Git operations within Google Colab.
- **Authenticate Google Services Using Service Account Credentials**: Authenticate and access Google services securely.

## Installation

To install the `colab_toolbox` package, run:

```bash
pip install colab_toolbox
```

## Examples

```python
from colab_toolbox import ColabInstall

# Setup selenium and chrome driver
ColabInstall('selenium')
```

**Available Tools**

- `selenium`: Set up Selenium and ChromeDriver for web scraping and automation.
- `quarto`: Set up Quarto for exporting documentation.
- `talib`: Set up TA-Lib for technical analysis.
- `pytesseract`: Set up PyTesseract for optical character recognition.