#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, output_folder):
    # Convert PDF to images
    images = convert_from_path(pdf_path)

    # Save the images
    for i, image in enumerate(images):
        image.save(f"{output_folder}/page_{i+1}.jpg", "JPEG")

# Specify the path to the PDF file
pdf_path = rC:\Users\Acer\Desktop\Katz99.pdf

# Specify the output folder where the images will be saved
output_folder = r"C:\Users\Acer\Desktop\img"

# Convert the PDF to images
convert_pdf_to_images(pdf_path, output_folder)


# In[ ]:




