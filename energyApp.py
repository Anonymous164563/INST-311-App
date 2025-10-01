import tkinter as tk
from tkinter import ttk, messagebox

# ------------------ Appliance Data ------------------

microwave = {
    "Countertop": """Cost: $50 to $300
Watts: 700 to 1200 watts
Buy If: You don't want installation.
Don't Buy If: You have a cramped kitchen.""",

    "Over-the-Range": "Watts: 600 to 1,700 watts",
    "Drawer": "Watts: 900 to 1750 watts",
    "Built-In": "Watts: 700 to 1200 watts"
}

stove = {
    "Gas:": "Fuel Burn: 5,000 to 18,000 BTUs\nCapacity: 5,000 to 18,000 BTUs",
    "Electric": "Electricity Consumption: 6000 to 8000 watts",
    "Convection": "Energy Consumption: 2,500 to 3,000 watts"
}

washing_machines = {
    "front-load washers": "Water Usage: 7 gallons of water per load",
    "top-load agitator washers": "Water Usage: 30 to 45 gallons per load",
    "high-efficiency top load washers": "Water Usage: 12 to 17 gallons per load",
    "compact front-load washers": "Water Usage: 7 to 15 gallons per load",
    "all-in one-washer dryers": "Water Usage: 55 gallons per dry cycle"
}

dishwasher = {
    "Built-In(Under_Counter)": "Energy Consumption: 1,200 to 2,400 watts per cycle",
    "Countertop": "Energy Consumption: 100 to 500 watts",
    "Drawer": "Energy Consumption: 1,200 to 2,400 watts"
}

refrigerators = {
    "french-refrigerator": "Energy Consumption: 400 to 700 watts",
    "Top-Freezer": "Energy Consumption: 100 to 400 watts",
    "Side by side": "Energy Consumption: 100 to 1000 watts",
    "Bottom-Freezer": "Energy Consumption: 100 to 500 watts"
}

blenders = {
    "Counter": "300 to over 1,000 watts",
    "Immersion": "Light-Duty: 150 to 300 watts\nHeavy-Duty: 500 to 1000 watts",
    "Personal": "250 watts to 1000 watts"
}

# Unified appliance data
appliance_data = {
    "Washing Machine": washing_machines,
    "Dish Washer": dishwasher,
    "Refrigerator": refrigerators,
    "Microwave": microwave,
    "Stove": stove,
    "Blender": blenders
}

# ------------------ GUI Application ------------------

class ApplianceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Household Appliance Selector")
        self.root.geometry("700x550")

        # Appliance Type Dropdown
        ttk.Label(root, text="Select Appliance Type:").pack(pady=10)
        self.appliance_type = tk.StringVar()
        self.appliance_dropdown = ttk.Combobox(root, textvariable=self.appliance_type, state="readonly")
        self.appliance_dropdown['values'] = list(appliance_data.keys())
        self.appliance_dropdown.pack()
        self.appliance_dropdown.bind("<<ComboboxSelected>>", self.update_appliance_options)

        # Appliance Model Dropdown
        ttk.Label(root, text="Select Appliance Model:").pack(pady=10)
        self.sub_type = tk.StringVar()
        self.type_dropdown = ttk.Combobox(root, textvariable=self.sub_type, state="readonly")
        self.type_dropdown.pack()

        # Brand Input
        ttk.Label(root, text="Enter Brand Name:").pack(pady=10)
        self.brand_var = tk.StringVar()
        self.brand_entry = ttk.Entry(root, textvariable=self.brand_var)
        self.brand_entry.pack()

        # Show Details Button
        ttk.Button(root, text="Show Details", command=self.show_details).pack(pady=20)

        # Result Display
        self.result_text = tk.Text(root, height=15, width=80, wrap=tk.WORD)
        self.result_text.pack(padx=10, pady=10)

    def update_appliance_options(self, event):
        selected = self.appliance_type.get()
        self.result_text.delete("1.0", tk.END)

        if selected in appliance_data:
            self.type_dropdown['values'] = list(appliance_data[selected].keys())
            self.sub_type.set("")  # Reset model

    def show_details(self):
        selected_type = self.appliance_type.get()
        selected_model = self.sub_type.get()
        brand = self.brand_var.get().strip()

        if not selected_type or not selected_model:
            messagebox.showerror("Input Error", "Please select both appliance type and model.")
            return
        if not brand:
            messagebox.showerror("Input Error", "Please enter a valid brand.")
            return

        info = appliance_data.get(selected_type, {}).get(selected_model, "No data found.")

        self.result_text.delete("1.0", tk.END)
        display_text = (
            f"Brand: {brand}\n"
            f"Appliance Type: {selected_type}\n"
            f"Model: {selected_model}\n\n"
            f"Details:\n{info}"
        )
        self.result_text.insert(tk.END, display_text)

# ------------------ Run the App ------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = ApplianceApp(root)
    root.mainloop()

