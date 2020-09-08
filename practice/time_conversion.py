def time_conversion(format_12_hours):
    hours = int(format_12_clock[0])
    minutes = format_12_clock[1]
    seconds = list(format_12_clock[2])
    pm_or_am = seconds.pop(-2) + seconds.pop(-1)
    seconds = "".join(seconds)

    if pm_or_am == "AM":
        if hours == 12:
            hours = 0

    elif pm_or_am == "PM":
        if not hours == 12:
            hours += 12
            if hours == 24:
                hours = hours % 24

    if len(str(hours)) < 2:
        hours = "0" + str(hours)

    return f"{hours}:{minutes}:{seconds}"


format_12_clock = input().split(":")
time_conversion(format_12_clock)
print(time_conversion(format_12_clock))