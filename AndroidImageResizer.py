from tkinter import Tk, filedialog, messagebox
from tkinter.ttk import Button, Label, Style
from PIL import Image
import os

# Predefined sizes for Android app development
ANDROID_SIZES = {
    "xxxhdpi": (192, 192),
    "xxhdpi": (144, 144),
    "xhdpi": (96, 96),
    "hdpi": (72, 72),
    "mdpi": (48, 48)
}

def select_image():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.webp")]
    )
    if file_path:
        selected_image_label.config(text=f"Selected: {os.path.basename(file_path)}")
        select_image.file_path = file_path

def select_output_folder():
    folder_path = filedialog.askdirectory(title="Select Output Folder")
    if folder_path:
        output_folder_label.config(text=f"Output: {folder_path}")
        select_output_folder.folder_path = folder_path

def resize_image():
    try:
        input_image = getattr(select_image, 'file_path', None)
        output_folder = getattr(select_output_folder, 'folder_path', None)

        if not input_image or not output_folder:
            messagebox.showerror("Error", "Please select an image and output folder.")
            return

        # Open the image
        img = Image.open(input_image)

        # Create resized images
        for size_name, dimensions in ANDROID_SIZES.items():
            resized_img = img.resize(dimensions, Image.LANCZOS)
            output_path = os.path.join(output_folder, f"{size_name}_{os.path.basename(input_image)}")
            resized_img.save(output_path)

        messagebox.showinfo("Success", f"Images resized and saved in {output_folder}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Initialize the GUI
root = Tk()
root.title("Android Image Resizer")
root.geometry("400x300")
root.configure(bg="#f0f4f7")

# Set Custom Icon
root.iconbitmap('app_icon.ico')  # Replace 'app_icon.ico' with your actual .ico file

# Style Configuration
style = Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 12), padding=10, background="#0078d7", foreground="white")
style.map("TButton", background=[("active", "#005bb5")])
style.configure("TLabel", font=("Arial", 10), background="#f0f4f7", foreground="#333")

# UI Elements
title_label = Label(root, text="Android Image Resizer", font=("Arial Bold", 16))
title_label.pack(pady=10)

select_image_button = Button(root, text="Select Image", command=select_image)
select_image_button.pack(pady=5)

selected_image_label = Label(root, text="No image selected")
selected_image_label.pack(pady=5)

select_output_folder_button = Button(root, text="Select Output Folder", command=select_output_folder)
select_output_folder_button.pack(pady=5)

output_folder_label = Label(root, text="No output folder selected")
output_folder_label.pack(pady=5)

resize_button = Button(root, text="Resize Image", command=resize_image)
resize_button.pack(pady=20)

# Run the GUI
root.mainloop()
