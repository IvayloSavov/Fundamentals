import re
is_found = False
pattern = r"^([#|\$|%|\*|&])([A-Za-z]+)\1=(\d+)!!(.+)$"

while True:
    line = input()
    valid_lines = re.findall(pattern, line)

    if len(valid_lines) == 0:
        print("Nothing found!")
    else:
        for valid_line in valid_lines:
            geohash_code_length = int(valid_line[2])
            geohash_code = valid_line[3]
            if len(geohash_code) == geohash_code_length:
                # geohash_code = [chr(ord(ch) + geohash_code_length) for ch in geohash_code]
                geohash_code = list(map(lambda ch: chr(ord(ch) + geohash_code_length), geohash_code))
                geohash_code = "".join(geohash_code)
                print(f"Coordinates found! {valid_line[1]} -> {geohash_code}")
                is_found = True
                break
            else:
                print("Nothing found!")
        if is_found:
            break
