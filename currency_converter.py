import tkinter as tk
import data
from PIL import Image, ImageTk


def operator():
    try:
        input_user = entry_currency.get()
        system = mode_str.get()[6:]
        converted_currency = float(input_user) * data.SYSTEMS_CONSTANT[system]
        amount_converted.set(value=f"Result {sign_converted} {converted_currency:.3f}")

    except ValueError:
        amount_converted.set("Give A Number")
        label_result.config(fg="red")


def master_call(text, window):
    getting_input(text)
    window.destroy()


def setting():
    setting_window = tk.Toplevel(master=root)
    setting_window.title(string="Settings")
    setting_window.geometry(newGeometry="300x350")
    setting_window.grab_set()
    setting_label = tk.Label(
        master=setting_window, text="Choose the Currency Converting System"
    )
    setting_label.pack()
    for systems in data.SYSTEMS_CONSTANT.keys():
        button = tk.Button(
            master=setting_window,
            text=f"{systems}",
            width=20,
            command=lambda s=systems: master_call(s, setting_window),
        )
        button.pack(pady=3)


def getting_input(text):
    mode_str.set(value=f"Mode: {text}")
    signs = data.SYSTEMS_SIGN[text].split("-")
    global sign_converted
    global sign_to_convert
    sign_to_convert = signs[0]
    sign_converted = signs[1]
    amount_converted.set(value=f"Result {sign_converted} 00")
    amount_to_convert.set(value="0")
    label_to_convert.config(text=f"Give the amount {sign_to_convert}")


sign_to_convert = "₹"
sign_converted = "$"
root = tk.Tk(screenName="main")
root.geometry(newGeometry="330x180")
root.title(string="Currency Converter")
# StringVar
amount_to_convert = tk.StringVar(value="0")
amount_converted = tk.StringVar(value="Result $ 00")
mode_str = tk.StringVar(value="Mode: Rupee To Dollar")
# Labels
mode_label = tk.Label(master=root, textvariable=mode_str, fg="black")
label_to_convert = tk.Label(
    master=root, text="Give the amount ₹:", height=3, width=15, fg="black"
)
label_result = tk.Label(master=root, textvariable=amount_converted, fg="black")
# Entry Box
entry_currency = tk.Entry(
    master=root, width=25, textvariable=amount_to_convert, fg="black"
)
# Buttons
convert_button = tk.Button(
    master=root, text="Convert", command=operator, fg="black", bg="grey"
)
# Extracting Image
opened_image = Image.open(fp="setting_icon.png")
icon = ImageTk.PhotoImage(image=opened_image.resize(size=(17, 17)))

setting_button = tk.Button(
    master=root,
    text="Setting",
    padx=5,
    pady=5,
    command=setting,
    fg="black",
    bg="grey",
    image=icon,
)
setting_button.image = icon  # type: ignore
# Layout Section
mode_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
label_to_convert.grid(row=1, column=0, padx=5)
entry_currency.grid(row=1, column=1, padx=5, pady=5)
setting_button.grid(row=0, column=2, padx=5, pady=5)
convert_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="EW")
label_result.grid(row=3, column=0, columnspan=2)
root.mainloop()
