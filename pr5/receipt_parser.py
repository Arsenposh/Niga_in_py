import re
import json

def parse_receipt(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        return "Ошибка: Файл не найден"

    items = re.findall(r'([A-Za-z\s]{2,})\s+(\d+(?:\.\d{2})?)', text)
    
    products = [name.strip() for name, price in items if "TOTAL" not in name.upper()]
    prices = [float(price) for name, price in items if "TOTAL" not in name.upper()]

    date = re.search(r'\d{2}[/-]\d{2}[/-]\d{4}', text)
    time = re.search(r'\d{2}:\d{2}(?::\d{2})?', text)
    total_match = re.search(r'(?:TOTAL|AMOUNT)\s*\$?(\d+\.\d{2})', text, re.I)
    
    methods = ["CASH", "CARD", "VISA", "MASTERCARD", "DEBIT", "CREDIT", "KASPI"]
    payment = next((m for m in methods if re.search(m, text, re.I)), "UNKNOWN")

    return {
        "products": products,
        "prices": prices,
        "calculated_total": round(sum(prices), 2),
        "receipt_total": float(total_match.group(1)) if total_match else None,
        "datetime": {"date": date.group() if date else None, "time": time.group() if time else None},
        "payment_method": payment
    }

if __name__ == "__main__":
    data = parse_receipt("pr5/raw.txt")
    print(json.dumps(data, indent=4))
