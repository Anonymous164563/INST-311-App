import tkinter as tk
from tkinter import ttk, messagebox

# ------------------ Appliance Data ------------------

washing_machines = {
    "front-load washers": """Cost: $650-$2200
Wash Times: 65-120 minutes
Capacity: 5.8 cubic feet

Buy If:
- You want to use 10 gallons of water per load
- You have gentle fabrics
- You want shorter drying time

Don't Buy If:
- You're worried about long wash time and mold
""",
    "top-load agitator washers": """Cost: $380-$1600
Wash Times: 35-105 minutes
Capacity: 5.4 cubic feet

Buy If:
- It's more affordable
- You want shorter wash cycles

Don't Buy If:
- Your fabrics are delicate
- You can't afford 20 gallons per load of water
""",
    "high-efficiency top load washers": """Price: $515-$1200
Wash Times: 35-105 minutes
Capacity: 5.5 cubic feet

Buy If:
- You want excellent performance
- You want to save water (13 gallons/load)

Cons:
- High spin speeds may tangle clothes
- Longer wash times than agitators
""",
    "compact front-load washers": """Price: $630-$2450
Wash Times: 60-100 minutes
Capacity: 2.7 cubic feet

Pros:
- Efficient for water/energy
- Good for small spaces

Cons:
- Longer wash time
- More vibration
""",
    "all-in one-washer dryers": """Price: $1390-$2050

Pros:
- Excellent energy/water efficiency
- Good wash performance

Don't Buy If:
- You want fast drying
- You need a smaller machine
"""
}

refrigerators = {
    "french-refrigerator": """French refrigerators are useful for 36-inch fridge needs.

Ergonomics:
- Produce is at knee level
- Flexible shelving (pizza boxes, sheet pans)

Mobility:
- Half-width doors are easier to open

Don't Buy If:
- You want better capacity or features
- You need frequent access to lower compartments
- You want a second ice maker
""",
    "side-by-side": """Side-by-side fridges are good if:
- You want balanced access to fridge/freezer
- You want more shelving space
- You want a 36-inch fridge on a budget

Don't Buy If:
- You store wide items like casserole dishes
- You care about energy efficiency
""",
    "bottom-freezer": """Bottom-freezer models are good if:
- You want flexible storage
- You want a cheaper alternative to French door
- You don’t want to bend for produce

Skip if:
- You need visible produce
- You want ice/water dispensers
""",
    "top-freezer": """Top-freezer fridges are ideal if:
- You want an affordable and reliable option
- You want mechanical, low-maintenance controls
- You want high efficiency
"""
}

# ------------------ GUI Application ------------------

class ApplianceApp:
    def __init__(self, root):
        self.root = root
        #following method creates the title for the pop up
        self.root.title("Household Appliance Selector")
        #sets the windows
        self.root.geometry("700x500")
        
        # Appliance Type Dropdown
        self.appliance_label = ttk.Label(root, text="Select Appliance Type:")
        self.appliance_label.pack(pady=10)
        #creates the pop up as string
        self.appliance_type = tk.StringVar()
        self.appliance_dropdown = ttk.Combobox(root, textvariable=self.appliance_type, state="readonly")
        #tells python to set the values equal to the washing machine and refrigerator
        self.appliance_dropdown['values'] = ["Washing Machine", "Refrigerator"]
        #Creates the drop down functionality
        self.appliance_dropdown.pack()

        #Contnusoly updates the drop down animation
        self.appliance_dropdown.bind("<<ComboboxSelected>>", self.update_appliance_options)

        # Appliance Subtype Dropdown
        self.type_label = ttk.Label(root, text="Select Appliance Model:")
        self.type_label.pack(pady=10)
        #creates the drop down variable as a string 
        self.sub_type = tk.StringVar()
        self.type_dropdown = ttk.Combobox(root, textvariable=self.sub_type, state="readonly")
        self.type_dropdown.pack()

        # Creates the button, when clicked shows all the details dependent on the self.appliance.drop() functionality respectfully 
        self.show_button = ttk.Button(root, text="Show Details", command=self.show_details)
        self.show_button.pack(pady=20)

        # Text Display
        self.result_text = tk.Text(root, height=15, width=80, wrap=tk.WORD)
        self.result_text.pack(padx=10, pady=10)

    def update_appliance_options(self, event):
        
        """ 
        When the Washing Machine option is selected, the type_drop down values will be associated with the various washing machines you can select.
        """
        selected = self.appliance_type.get()
        if selected == "Washing Machine":
            self.type_dropdown['values'] = list(washing_machines.keys())
        elif selected == "Refrigerator":
            self.type_dropdown['values'] = list(refrigerators.keys())
        self.sub_type.set("")  # Clear selection
        self.result_text.delete("1.0", tk.END)

    def show_details(self): 
        
        """Accesses the appliance types and there variants, 
           
        """
        selected_type = self.appliance_type.get()
        selected_model = self.sub_type.get()

        if not selected_type or not selected_model:
            messagebox.showerror("Input Error", "Please select both appliance type and model.")
            return

        if selected_type == "Washing Machine":
            info = washing_machines.get(selected_model, "No data found.")
        else:
            info = refrigerators.get(selected_model, "No data found.")

        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, info)

# ------------------ Run the App ------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = ApplianceApp(root)
    root.mainloop()


