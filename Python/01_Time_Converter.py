def convert_minutes(minutes):
    hours = minutes // 60
    remaining = minutes % 60

    if hours == 1:
        return f"{hours} hr {remaining} minutes"
    else:
        return f"{hours} hrs {remaining} minutes"


print(convert_minutes(130))
print(convert_minutes(110))
