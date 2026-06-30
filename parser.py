def parse_command(text):

    text = text.lower()

    if "light" in text and "on" in text:
        return "LIGHT_ON"

    elif "light" in text and "off" in text:
        return "LIGHT_OFF"

    elif "fan" in text and "on" in text:
        return "FAN_ON"

    elif "fan" in text and "off" in text:
        return "FAN_OFF"

    elif "ac" in text and "on" in text:
        return "AC_ON"

    elif "ac" in text and "off" in text:
        return "AC_OFF"

    return None