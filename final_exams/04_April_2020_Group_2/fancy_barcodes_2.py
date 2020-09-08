import re

count_of_barcodes = int(input())
pattern = r"@(#+)([A-Z][A-Za-z0-9]{4,}[A-Z])@(#+)"

for _ in range(count_of_barcodes):
    string = input()
    match = list(re.finditer(pattern, string))

    if len(match) > 0:
        for m in match:
            product = m.group(2)
            digits = [ch for ch in product if ch.isdigit()]
            if len(digits) == 0:
                product_group = "00"
            else:
                product_group = ''.join(digits)
            print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
