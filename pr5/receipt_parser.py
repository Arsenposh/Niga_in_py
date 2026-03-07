import re
import json

def parse_receipt(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        return "Ошибка: Файл не найден"

    items = re.findall(
    r'([A-Za-zА-Яа-я0-9\[\].,() \-]+?)\s*\n(\d+,\d+)\s*x\s*([\d\s]+,\d{2})',
    text
)
    
    products = [name.strip() for name, qty, price in items]
    quantities = [float(qty.replace(',', '.')) for name, qty, price in items]
    prices = [float(price.replace(' ', '').replace(',', '.')) for name, qty, price in items]

    calculated_total = round(sum(q*p for q, p in zip(quantities, prices)), 2)

    total_match = re.search(r'ИТОГО:\s*([\d\s]+,\d{2})', text)
    receipt_total = float(total_match.group(1).replace(' ', '').replace(',', '.')) if total_match else None

    dt_match = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})', text)
    date, time = (dt_match.group(1), dt_match.group(2)) if dt_match else (None, None)

    payment = "CASH" if "НАЛИЧНЫМИ" in text.upper() else "CARD" if "Банковская карта" in text else "UNKNOWN"

    return {
        "products": products,
        "quantities": quantities,
        "prices": prices,
        "calculated_total": calculated_total,
        "receipt_total": receipt_total,
        "datetime": {"date": date, "time": time},
        "payment_method": payment
    }

if __name__ == "__main__":
    data = parse_receipt("pr5/raw.txt")
    print(json.dumps(data, indent=4, ensure_ascii=False))