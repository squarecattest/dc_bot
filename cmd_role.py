import discord
def is_int(string: str):
    if string.isdecimal(): return True
    if string.startswith("-") and string.split("-", maxsplit = 1)[1].isdecimal(): return True
    return False

def to_color(string: str):
    if string == False:
        return discord.Color.default()
    if is_int(string): return discord.Color(int(string))
    elif string.startswith("#") and len(string) == 7:
        hex_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
                    "A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f"]
        for i in range(1, 7):
            if not string[i] in hex_list: return None
        return discord.Color(int(string.split("#")[1], 16))
    else:
        color_list = {"teal": "teal", "dark_teal": "dark_teal", "light_green": "green", 
                        "green": "dark_green", "blue": "blue", "cyan": "dark_blue", 
                        "light_purple": "purple", "purple": "dark_purple",  "magenta": "magenta", 
                        "dark_magenta": "dark_magenta", "gold": "gold", "dark_gold": "dark_gold", 
                        "orange": "orange", "brown": "dark_orange", "red": "red", "dark_red": "dark_red", 
                        "lighter_gray": "lighter_grey", "dark_gray": "dark_grey", "light_gray": "light_grey", 
                        "darker_gray": "darker_grey", "blurple": "blurple", "greyple": "greyple", 
                        "dark_theme": "dark_theme"}
        if string in color_list: return eval("discord.Color." + color_list.get(string) + "()")
        elif string == "lavender": return discord.Color(int("b57edc", 16))
        elif string == "aqua": return discord.Color(int("00e0e0", 16))
        elif string == "pink": return discord.Color(int("ffc0cb", 16))
        elif string == "white": return discord.Color(int("ffffff", 16))
        elif string == "black": return discord.Color(int("010101", 16))
        
    return None

def to_bool(string: str):
    if string == False or string == "false" or string == "0": return False
    if string == "true" or string == "1": return True
    return None

def to_permission(string: str):
    if string == False:
        return discord.Permissions()
    if is_int(string):
        integer = int(string)
        if integer >= 0:
            if integer < 1 << 33: return discord.Permissions(integer)
            return -2
        return -1
    return None

def to_position(string: str):
    if string == False:
        return 1
    if is_int(string):
        position = int(string)
        if position <= 0:
            return -1
        return position
    return None
