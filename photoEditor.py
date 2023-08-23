from PIL import Image, ImageFilter, ImageEnhance
import os

# Update the source and target paths to the correct absolute paths on your system
path = r'C:\'
pathOut = r'C:\'

# Create the target directory if it doesn't exist
if not os.path.exists(pathOut):
    os.makedirs(pathOut)

# Loop through each file in the source directory
for filename in os.listdir(path):
    if filename.endswith('.jpg'):  # Only process JPG files (you can adjust the file extension)
        img = Image.open(os.path.join(path, filename))

        # Apply the sharpen filter
        edit = img.filter(ImageFilter.SHARPEN).convert('L')
        
        factor= 1.5
        enhancer = ImageEnhance.Contrast(edit)
        clean_name = os.path.splitext(filename)[0]

        # Save the edited image to the target directory
        edited_filename = f'{clean_name}_edited.jpg'
        edited_path = os.path.join(pathOut, edited_filename)
        edit.save(edited_path)

print("Image processing complete.")
