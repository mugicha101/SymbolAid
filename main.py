from pynput import keyboard


symbols = {
    "Sigma": "Σ"
}

command = {
    "str": "",
    "reading": False
}


def process_input(inp):
    print(inp)


def on_press(key):
    if key is None:
        return True
    if command["reading"]:
        if str(key) == "Key.space":
            process_input(command["str"])
            reading = False
        elif str(key).isalpha():
            command["str"] += str(key)
        else:
            command["reading"] = False
    else:
        if str(key) == "/":
            command["str"] = ""
            command["reading"] = True
    return True

def on_release(key):
    return True

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



if __name__ == '__main__':
    print_hi('PyCharm')