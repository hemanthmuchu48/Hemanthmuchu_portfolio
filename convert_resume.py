from PIL import Image
import os

def convert_img_to_pdf(img_path, pdf_path):
    try:
        image = Image.open(img_path)
        pdf_bytes = image.convert('RGB')
        pdf_bytes.save(pdf_path)
        print(f"Successfully converted {img_path} to {pdf_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    convert_img_to_pdf('resume_new.jpg', 'resume.pdf')
