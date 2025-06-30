import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def xor_encrypt_decrypt(input_path, output_path, key):
    image = Image.open(input_path).convert("RGB")
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                r ^ key,
                g ^ key,
                b ^ key
            )

    image.save(output_path)

def browse_file():
    filename = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if filename:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filename)

def process_image():
    path = file_entry.get()
    key = key_entry.get()
    mode = mode_var.get()

    if not os.path.exists(path):
        messagebox.showerror("Error", "Selected file does not exist.")
        return

    if not key.isdigit() or not (0 <= int(key) <= 255):
        messagebox.showerror("Error", "Key must be a number between 0 and 255.")
        return

    key = int(key)
    filename, ext = os.path.splitext(path)
    output_path = f"{filename}_{mode}{ext}"

    try:
        xor_encrypt_decrypt(path, output_path, key)
        messagebox.showinfo("Success", f"Image {mode}ed and saved as:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process image:\n{e}")

# GUI Setup
root = tk.Tk()
root.title("Image Encryptor (XOR) - Prodigy InfoTech")

tk.Label(root, text="Select Image:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
file_entry = tk.Entry(root, width=40)
file_entry.grid(row=0, column=1, padx=5)
browse_btn = tk.Button(root, text="Browse", command=browse_file)
browse_btn.grid(row=0, column=2, padx=5)

tk.Label(root, text="Secret Key (0–255):").grid(row=1, column=0, padx=10, pady=5, sticky='e')
key_entry = tk.Entry(root, width=10)
key_entry.grid(row=1, column=1, padx=5, sticky='w')

tk.Label(root, text="Mode:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
mode_var = tk.StringVar(value="encrypt")
tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="encrypt").grid(row=2, column=1, sticky='w')
tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="decrypt").grid(row=2, column=1)

process_btn = tk.Button(root, text="Run", command=process_image, bg="#007acc", fg="white")
process_btn.grid(row=3, column=1, pady=15)

root.mainloop()
