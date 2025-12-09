import tkinter as tk
from tkinter import messagebox

# Define the items and prices
items = {
    "101": {"name": "Chips", "price": 10, "stock": 1},
    "102": {"name": "Soda", "price": 20, "stock": 5},
    "103": {"name": "Candy", "price": 10, "stock": 5},
    "104": {"name": "Juice", "price": 20, "stock": 5},
    "105": {"name": "Water", "price": 30, "stock": 5},
    "106": {"name": "Cake", "price": 10, "stock": 5},
}

# Main function to create the vending machine UI
def vending_machine():
    # Create main window
    window = tk.Tk()
    window.title("Vending Machine Simulation")
    window.geometry("700x700")
    window.configure(bg="#f0f0f0")  # Light background color

    # Get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate position x and y coordinates to center the window
    x_coordinate = int((screen_width / 2) - (700 / 2))
    y_coordinate = int((screen_height / 2) - (700 / 2))

    # Set the geometry to center the window
    window.geometry(f"700x700+{x_coordinate}+{y_coordinate}")

    # Function to handle item selection
    def select_item():
        code = item_code.get()
        if code not in items:
            messagebox.showerror("Error", "Invalid selection. Please try again.")
            return
        selected_item = items[code]
        item_name_label.config(text=f"Selected Item: {selected_item['name']}")
        item_price_label.config(text=f"Price: Rs{selected_item['price']:.2f}")

    # Function to exit the window
    def exit():
        window.destroy()

    # Function to update the display of stock levels
    def update_stock_display():
        for label, (code, item) in zip(stock_labels, items.items()):
            label.config(text=f"{code}: {item['name']} - Rs{item['price']:.2f} (Stock Left: {item['stock']})")

    # Function to handle the transaction
    def buy_item():
        code = item_code.get()
        if code not in items:
            messagebox.showerror("Error", "Invalid selection. Please select an item first.")
            return
        
        selected_item = items[code]
        if selected_item["stock"] <= 0:
            messagebox.showerror("Out of Stock", f"Sorry, {selected_item['name']} is out of stock.")
            return
        
        try:
            money_inserted = float(money_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
            return

        if money_inserted >= selected_item['price']:
            change = money_inserted - selected_item['price']
            selected_item["stock"] -= 1  # Deduct stock after purchase
            messagebox.showinfo("Purchase Successful", 
                                f"Dispensing {selected_item['name']}...\nChange Returned: Rs{change:.2f}\nThank You for the Purchase")
            update_stock_display()  # Refresh stock display after purchase
            item_code.set("")  # Reset item code
            money_entry.delete(0, tk.END)  # Clear money entry
            item_name_label.config(text="Selected Item: None")
            item_price_label.config(text="Price: Rs0.00")
        else:
            messagebox.showerror("Error", "Insufficient funds. Please insert more money.")

    # Create frames for better layout and centering
    header_frame = tk.Frame(window, bg="#127bb0", pady=10, padx=10)
    header_frame.pack(fill="x", pady=10)
    selection_frame = tk.Frame(window, bg="#f0f0f0", pady=10)
    selection_frame.pack(pady=10)
    transaction_frame = tk.Frame(window, bg="#f0f0f0", pady=10)
    transaction_frame.pack(pady=10)

    # Center widgets within frames
    tk.Label(header_frame, text="Welcome to the Vending Machine!", font=("Arial", 18, "bold"), bg="#127bb0", fg="white").pack(anchor="center")

    # Display items and their prices
    tk.Label(selection_frame, text="Available Items:", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(anchor="center")
    stock_labels = []
    for code, item in items.items():
        label = tk.Label(selection_frame, text=f"{code}: {item['name']} - Rs{item['price']:.2f} (Stock Left: {item['stock']})", bg="#f0f0f0", font=("Arial", 10))
        label.pack(anchor="center")
        stock_labels.append(label)

    # Entry for item code
    item_code = tk.StringVar()
    tk.Label(transaction_frame, text="Enter Item Code:", font=("Arial", 12), bg="#f0f0f0").pack(anchor="center", pady=5)
    tk.Entry(transaction_frame, textvariable=item_code, width=10).pack(anchor="center")
    # Button to select item
    select_button = tk.Button(transaction_frame, text="Select Item", command=select_item, bg="#de7010", fg="white", font=("Arial", 10), pady=5)
    select_button.pack(anchor="center", pady=5)
    # Labels to display selected item and price
    item_name_label = tk.Label(transaction_frame, text="Selected Item: None", bg="#f0f0f0", font=("Arial", 12))
    item_name_label.pack(anchor="center")
    item_price_label = tk.Label(transaction_frame, text="Price: Rs0.00", bg="#f0f0f0", font=("Arial", 12))
    item_price_label.pack(anchor="center")

    # Entry for money insertion
    tk.Label(transaction_frame, text="Insert Money:", font=("Arial", 12), bg="#f0f0f0").pack(anchor="center", pady=5)
    money_entry = tk.Entry(transaction_frame, width=10)
    money_entry.pack(anchor="center")

    # Button to buy item
    buy_button = tk.Button(transaction_frame, text="Buy", command=buy_item, bg="#17734e", fg="white", font=("Arial", 12), pady=5)
    buy_button.pack(anchor="center", pady=10)

    # Button to exit
    exit_button =  tk.Button(transaction_frame, text="Exit", command=exit, bg="#5c0107", fg="white", font=("Arial", 12), pady=5)
    exit_button.pack(anchor="center", pady=10)

    # Run the application
    window.mainloop()
# Run the vending machine graphical user interface (GUI)
vending_machine()