# colab_toolbox

Simplify the setup and configuration of multiple tools in Google Colab without needing shell commands or extensive coding.

## Features

### Easy Installation
- **Selenium and ChromeDriver Setup**: Seamlessly install and configure Selenium and ChromeDriver for web scraping and automation.
- **Quarto Setup for Documentation**: Quickly configure Quarto for exporting documentation in various formats.
- **Python Environment Setup**: Install and configure Python environments for tasks such as data ingestion, backtesting, modeling, and more.
- **xterm Setup**: Enable a full terminal experience in Google Colab by setting up xterm.
- **OCRmyPDF Setup**: Easily configure OCRmyPDF for OCR processing and PDF conversion.

### Easy Access

- **Git Commands for Colab**: Streamline Git operations within Google Colab.
- **Google Sheets Integration**: Read and write data in Google Sheets using a simplified authentication flow, avoiding the complexities of configuring confidential or service account credentials.

### Upcoming Features
- **Google Services Authentication Using Service Account Credentials**: Securely authenticate and access Google services.

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

- `selenium`: WebDriver for automated testing of web applications
- `quarto`: open-source scientific and technical publishing system 
- `talib`: Technical Analysis Library for Stock Trading in Python
- `pytesseract`: OCR tool for extracting text from images
- `ocrmypdf`: OCR tool for extracting text from PDF files
- `xterm`: Terminal emulator for Google Colab environment