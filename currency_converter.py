import customtkinter as ctk
import data
from PIL import Image

# Set a consistent modern theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")  # Smooth blue for primary buttons/accents


def operator():
    try:
        input_user = entry_currency.get()
        system = mode_str.get()[6:]
        converted_currency = float(input_user) * data.SYSTEMS_CONSTANT[system]
        amount_converted.set(value=f"Result {sign_converted} {converted_currency:.3f}")
        # Reset to a clean neutral background if it was previously red
        label_result.configure(fg_color="transparent", text_color="#10B981")

    except ValueError:
        amount_converted.set("Give A Number")
        label_result.configure(fg_color="#3B1C1C", text_color="#EF4444")


def master_call(text, window):
    getting_input(text)
    window.destroy()


def setting():
    setting_window = ctk.CTkToplevel(master=root)
    setting_window.title(string="Settings")
    setting_window.geometry("320x380")
    setting_window.grab_set()
    setting_window.resizable(False, False)

    setting_label = ctk.CTkLabel(
        master=setting_window,
        text="Choose Converting System",
        font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"),
    )
    setting_label.pack(pady=(20, 15))

    for systems in data.SYSTEMS_CONSTANT.keys():
        button = ctk.CTkButton(
            master=setting_window,
            text=f"{systems}",
            height=35,
            width=220,
            corner_radius=8,
            font=ctk.CTkFont(family="Helvetica", size=13),
            command=lambda s=systems: master_call(s, setting_window),
        )
        button.pack(pady=6)


def getting_input(text):
    mode_str.set(value=f"Mode: {text}")
    signs = data.SYSTEMS_SIGN[text].split("-")
    global sign_converted
    global sign_to_convert
    sign_to_convert = signs[0]
    sign_converted = signs[1]
    amount_converted.set(value=f"Result {sign_converted} 00")
    amount_to_convert.set(value="0")
    label_to_convert.configure(text=f"Give the amount {sign_to_convert}")


sign_to_convert = "₹"
sign_converted = "$"

root = ctk.CTk()
root.geometry("400x240")  # Slightly wider for better breathing room
root.title(string="Currency Converter")
root.resizable(False, False)

# Fonts
font_title = ctk.CTkFont(family="Helvetica", size=14, weight="bold")
font_regular = ctk.CTkFont(family="Helvetica", size=13)
font_result = ctk.CTkFont(family="Helvetica", size=15, weight="bold")

# StringVar
amount_to_convert = ctk.StringVar(value="0")
amount_converted = ctk.StringVar(value="Result $ 00")
mode_str = ctk.StringVar(value="Mode: Rupee To Dollar")

# Labels
mode_label = ctk.CTkLabel(
    master=root,
    textvariable=mode_str,
    font=font_title,
    text_color="#60A5FA",  # Clean accent blue
)

label_to_convert = ctk.CTkLabel(
    master=root, text="Give the amount ₹:", font=font_regular, anchor="w"
)

label_result = ctk.CTkLabel(
    master=root,
    textvariable=amount_converted,
    font=font_result,
    height=40,
    corner_radius=8,
    text_color="#10B981",  # Emerald green for clean success state
)

# Entry Box
entry_currency = ctk.CTkEntry(
    master=root,
    width=140,
    height=32,
    textvariable=amount_to_convert,
    corner_radius=8,
    border_width=1,
    font=font_regular,
)

# Buttons
convert_button = ctk.CTkButton(
    master=root,
    text="Convert",
    command=operator,
    height=36,
    corner_radius=8,
    font=font_title,
)

# Extracting Image
opened_image = Image.open(fp="setting_icon.png")
icon = ctk.CTkImage(light_image=opened_image, dark_image=opened_image, size=(16, 16))

setting_button = ctk.CTkButton(
    master=root,
    text="Settings",
    command=setting,
    width=90,
    height=32,
    corner_radius=8,
    fg_color="#374151",  # Dark grey secondary button
    hover_color="#4B5563",
    font=font_regular,
    image=icon,
)
setting_button.image = icon  # type: ignore

# Layout Section (Using clean grid spacing)
root.grid_columnconfigure((0, 1), weight=1)

mode_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 15), sticky="w")
setting_button.grid(row=0, column=1, padx=20, pady=(20, 15), sticky="e")

label_to_convert.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="w")
entry_currency.grid(row=1, column=1, padx=(10, 20), pady=10, sticky="ew")

convert_button.grid(row=2, column=0, columnspan=2, padx=20, pady=(15, 10), sticky="ew")
label_result.grid(row=3, column=0, columnspan=2, padx=20, pady=(5, 15), sticky="ew")

root.mainloop()
