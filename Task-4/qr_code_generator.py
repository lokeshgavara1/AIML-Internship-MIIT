import qrcode
from PIL import Image
import os

def generate_qr_code(data, filename="qrcode.png", size=10, border=4):
    """
    Generate a QR code from the provided data and save it as an image.
    
    Args:
        data (str): The text or URL to encode in the QR code
        filename (str): Output filename for the QR code image
        size (int): Size of the QR code (box size in pixels)
        border (int): Border thickness around the QR code
    """
    if not data:
        raise ValueError("Input data cannot be empty.")
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )
    
    # Add data to QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create and save the QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Ensure the filename ends with .png
    if not filename.lower().endswith('.png'):
        filename += '.png'
    
    # Save the image
    img.save(filename)
    print(f"QR code saved as {filename}")

def main():
    print("QR Code Generator")
    print("----------------")
    
    try:
        # Get user input
        data = input("Enter the text or URL to encode in the QR code: ")
        filename = input("Enter output filename (default: qrcode.png): ") or "qrcode.png"
        size = input("Enter QR code size (default: 10): ") or "10"
        border = input("Enter border thickness (default: 4): ") or "4"
        
        # Convert inputs to appropriate types
        size = int(size)
        border = int(border)
        
        # Validate inputs
        if size < 1:
            raise ValueError("Size must be at least 1.")
        if border < 0:
            raise ValueError("Border thickness cannot be negative.")
        
        # Generate QR code
        generate_qr_code(data, filename, size, border)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()