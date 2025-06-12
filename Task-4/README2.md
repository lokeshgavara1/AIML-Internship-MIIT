# QR Code Generator

## Overview
This Python project generates QR codes from user-provided text or URLs and saves them as PNG images. It uses the `qrcode` library for QR code generation and `Pillow` for image processing. The script features a command-line interface for easy input and allows customization of QR code size and border thickness.

## Features
- **QR Code Generation**: Encodes text or URLs into QR codes.
- **Customizable Output**: Specify output filename, QR code size, and border thickness.
- **Input Validation**: Ensures valid inputs for size and border thickness.
- **Image Output**: Saves QR codes as PNG files with black fill and white background.

## Requirements
- Python 3.6+
- Libraries:
  ```bash
  pip install qrcode pillow
  ```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/qr-code-generator.git
   cd qr-code-generator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or directly install:
   ```bash
   pip install qrcode pillow
   ```
3. Ensure Python 3.6+ is installed:
   ```bash
   python --version
   ```

## Usage
1. Run the script:
   ```bash
   python qr_code_generator.py
   ```
2. Follow the prompts to specify:
   - Text or URL to encode (e.g., `https://example.com`)
   - Output filename (default: `qrcode.png`)
   - QR code size (default: 10)
   - Border thickness (default: 4)
3. The script will generate and save the QR code as a PNG file in the current directory.

### Example
```bash
QR Code Generator
----------------
Enter the text or URL to encode in the QR code: https://example.com
Enter output filename (default: qrcode.png): my_qr_code
Enter QR code size (default: 10): 12
Enter border thickness (default: 4): 5

QR code saved as my_qr_code.png
```
The generated QR code can be scanned with any QR code reader to access the encoded text or URL.

## Outputs
- A PNG file (e.g., `my_qr_code.png`) containing the QR code.
- Console message confirming the file save location.

## Notes
- The default settings (size=10, border=4) produce a standard-sized QR code suitable for most uses.
- Ensure the output filename is unique to avoid overwriting existing files.
- The QR code uses low error correction (`ERROR_CORRECT_L`) for simplicity; modify the script for higher error correction if needed.
- Scan the generated QR code with a QR code reader to verify the encoded data.
