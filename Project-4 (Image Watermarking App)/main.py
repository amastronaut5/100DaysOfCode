from tkinter import *
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageDraw, ImageFont, ImageTk

# Global Variables
img = None
img_tk = None
img_path = None
watermarked_img = None

# GUI Setup
window = Tk()
window.title('Image Watermarking App')
window.minsize(900, 600)
window.resizable(True, True)

# Font size and color variables
font_size_var = IntVar(value=50)  # Default font size
r_var = IntVar(value=255)
g_var = IntVar(value=0)
b_var = IntVar(value=0)
position_var = StringVar(value="Bottom-Right")  # Default position

# Resize image for preview (doesn't affect original image)
def resize_image_for_preview(image, max_width=500, max_height=400):
    w, h = image.size
    scale = min(max_width / w, max_height / h)
    if scale < 1:
        return image.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
    return image

# Load Image
def load_img():
    global img, img_tk, img_path
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if not file_path:
        return
    img_path = file_path
    img = Image.open(file_path).convert("RGBA")
    preview_img = resize_image_for_preview(img)
    img_tk = ImageTk.PhotoImage(preview_img)
    img_lbl.config(image=img_tk)
    img_lbl.image = img_tk
    status_lbl.config(text="Image loaded successfully.")

# Save Image
def save_img():
    global watermarked_img
    if watermarked_img is None:
        messagebox.showwarning("Warning", "No watermark added.")
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        watermarked_img.save(save_path)
        messagebox.showinfo("Saved", "Watermarked image saved successfully!")

# Apply Watermark
def apply_watermark():
    global watermarked_img
    if img is None:
        messagebox.showwarning("Warning", "Please load an image first.")
        return

    text = txt.get("1.0", END).strip()
    if not text:
        messagebox.showwarning("Warning", "Enter watermark text.")
        return

    if watermarked_img is None:
        # Create a new image when no watermark has been applied yet
        watermarked_img = img.copy()

    draw = ImageDraw.Draw(watermarked_img)

    font_size = font_size_var.get()
    font = ImageFont.truetype("arial.ttf", font_size)

    r = r_var.get()
    g = g_var.get()
    b = b_var.get()
    text_color = (r, g, b, opacity_var.get())  # Dynamic transparency


    # Get selected position
    selected_position = position_var.get()

    # Get size of text
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    img_width, img_height = watermarked_img.size

    if selected_position == "Top-Left":
        position = (10, 10)
    elif selected_position == "Top-Right":
        position = (img_width - text_width - 10, 10)
    elif selected_position == "Center":
        position = ((img_width - text_width) // 2, (img_height - text_height) // 2)
    elif selected_position == "Bottom-Left":
        position = (10, img_height - text_height - 10)
    elif selected_position == "Bottom-Right":
        position = (img_width - text_width - 10, img_height - text_height - 10)
    else:
        position = (50, 100)  # fallback

    # Clear the old watermark (draw a transparent text again)
    watermarked_img = img.copy()  # Reset image to original
    draw = ImageDraw.Draw(watermarked_img)

    # Draw the new watermark with the updated color
    draw.text(position, text, fill=text_color, font=font)

    preview_img = resize_image_for_preview(watermarked_img)
    img_tk_watermarked = ImageTk.PhotoImage(preview_img)
    img_lbl.config(image=img_tk_watermarked)
    img_lbl.image = img_tk_watermarked
    status_lbl.config(text="Watermark applied.")



# Sliders for font size and color
font_size_frame = Frame(window)
font_size_frame.pack(pady=5)
Label(font_size_frame, text="Font Size:").pack(side=LEFT, padx=5)
Scale(font_size_frame, from_=10, to=100, orient=HORIZONTAL, variable=font_size_var).pack(side=LEFT)

color_frame = Frame(window)
color_frame.pack(pady=5)
Label(color_frame, text="R:").pack(side=LEFT)
Scale(color_frame, from_=0, to=255, orient=HORIZONTAL, variable=r_var, width=10).pack(side=LEFT)

Label(color_frame, text="G:").pack(side=LEFT)
Scale(color_frame, from_=0, to=255, orient=HORIZONTAL, variable=g_var, width=10).pack(side=LEFT)

Label(color_frame, text="B:").pack(side=LEFT)
Scale(color_frame, from_=0, to=255, orient=HORIZONTAL, variable=b_var, width=10).pack(side=LEFT)

#transparency
opacity_var = IntVar(value=128)  # Default 50% transparent

Label(color_frame, text="Opacity:").pack(side=LEFT)
Scale(color_frame, from_=0, to=255, orient=HORIZONTAL, variable=opacity_var, width=10).pack(side=LEFT)



# Watermark Position Dropdown
position_frame = Frame(window)
position_frame.pack(pady=5)
Label(position_frame, text="Watermark Position:").pack(side=LEFT, padx=5)

position_options = ["Top-Left", "Top-Right", "Center", "Bottom-Left", "Bottom-Right"]
position_menu = ttk.Combobox(position_frame, textvariable=position_var, values=position_options, state="readonly")
position_menu.pack(side=LEFT)

# Widgets
Label(window, text="Image Watermarking App", font=("Helvetica", 20)).pack(pady=10)

img_lbl = Label(window)
img_lbl.pack(pady=10)

txt = Text(window, height=1, width=40)
txt.pack(pady=5)
txt.insert(END, "Enter watermark text here")

btn_frame = Frame(window)
btn_frame.pack(pady=10)

Button(btn_frame, text="Load Image", command=load_img).pack(side=LEFT, padx=10)
Button(btn_frame, text="Apply Watermark", command=apply_watermark).pack(side=LEFT, padx=10)
Button(btn_frame, text="Save Image", command=save_img).pack(side=LEFT, padx=10)

status_lbl = Label(window, text="", fg="green")
status_lbl.pack(pady=5)

# Run the app
window.mainloop()
