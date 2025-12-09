# 🥤 Vending Machine Simulator (Python Tkinter)

A GUI-based vending machine simulation built using **Python Tkinter**.  
Users can select items, view prices, insert money, purchase items, and see remaining stock — all through an interactive window.

---

## 🚀 Features
- GUI interface using Python Tkinter  
- Select item using item code  
- Shows item name, price, and live stock updates  
- Validates incorrect codes and insufficient money  
- Automatically returns change  
- Displays error messages and success messages  
- Clean layout with centered UI and color styling  

---

## 📂 Project Structure
```
vending-machine-simulator/
│── vending_machine.py
└── README.md
```

---

## 🧠 How It Works
1. App displays all available items with price + stock  
2. User enters an item code (101, 102, 103...)  
3. Script checks validity → shows name + price  
4. User enters money  
5. If money ≥ price → item dispensed + change returned  
6. Stock reduces and UI updates  
7. Errors handled with message boxes  

---

## 🛠️ Requirements
- Python 3.x  
- Tkinter (comes pre-installed with Python)

---

## ▶️ Running the Program
Run the script directly:

```bash
python vending_machine.py
```

The GUI will open instantly.

---

## 🛒 Available Items
| Code | Item  | Price (Rs) | Stock |
|------|--------|------------|--------|
| 101  | Chips  | 10 | 1 |
| 102  | Soda   | 20 | 5 |
| 103  | Candy  | 10 | 5 |
| 104  | Juice  | 20 | 5 |
| 105  | Water  | 30 | 5 |
| 106  | Cake   | 10 | 5 |

---

## 🎨 UI Highlights
- Modern color scheme  
- Centered window  
- Organized frames (header, selection, transaction)  
- Pop-up messages for errors and success  

---

## 🔮 Future Enhancements
- Add images for each item  
- Add sound effects  
- Add admin mode to restock items  
- Export purchase history
