import re

pattern = r"^([A-Za-z0-9\!\@\#\$\?]+)=(\d+)<<(.+)$"

while True:
    line = input()
    if line == "Last note":
        break
    valid_line = re.findall(pattern, line)

    if len(valid_line) == 0:
        print("Nothing found!")
    else:
        for v_line in valid_line:
            length_to_check = int(v_line[1])
            geohash_code = v_line[2]
            if len(geohash_code) == length_to_check:
                mountain_name = v_line[0]
                mountain_name = [ch for ch in mountain_name if ch.isalnum()]
                mountain_name = "".join(mountain_name)
                print(f"Coordinates found! {mountain_name} -> {geohash_code}")
            else:
                print("Nothing found!")

