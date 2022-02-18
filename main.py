from pynput import keyboard
# NOTE: ANTIVIRUS MIGHT DELETE THIS PROGRAM BECAUSE KEYLOGGER

symbols = {
    "alpha": "α",
    "beta": "β",
    "gamma": "γ",
    "Gamma": "Γ",
    "delta": "δ",
    "Delta": "Δ",
    "epsilon": "ε",
    "zeta": "ζ",
    "eta": "η",
    "theta": "θ",
    "Theta": "Θ",
    "iota": "ι",
    "kappa": "κ",
    "lambda": "λ",
    "Lambda": "Λ",
    "mu": "μ",
    "xi": "ξ",
    "Xi": "Ξ",
    "pi": "π",
    "Pi": "Π",
    "rho": "ρ",
    "sigma": "σ",
    "Sigma": "Σ",
    "tau": "τ",
    "phi": "φ",
    "Phi": "Φ",
    "chi": "χ",
    "psi": "ψ",
    "Psi": "Ψ",
    "omega": "ω",
    "Omega": "Ω",
    "grad": "∇",
    "inf": "∞",
    "neg": "¬",
    "forall": "∀",
    "exists": "∃",
    "in": "∈",
    "nin": "∉",
    "sub": "⊆",
    "psub": "⊂",
    "nsub": "⊄",
    "union": "∪",
    "isect": "∩",
    "rar": "→",
    "larr": "←",
    "uarr": "↑",
    "darr": "↓",
    "equiv": "≡",
}

command = {
    "str": "",
    "reading": False,
}

def process_input(inp):
    kb = keyboard.Controller()
    if inp == "":
        kb.press(keyboard.Key.backspace)
        kb.release(keyboard.Key.backspace)
        return
    for i in range(len(inp) + 2):
        kb.press(keyboard.Key.backspace)
        kb.release(keyboard.Key.backspace)
    if inp in symbols:
        kb.press(symbols[inp])
        kb.release(symbols[inp])


def on_press(key):
    if key is None or str(key) == "Key.shift" or str(key) == "Key.shift_r":
        return True
    if command["reading"]:
        if str(key) == "Key.space":
            process_input(command["str"])
        elif str(key) == "Key.backspace":
            if len(command["str"]) == 0:
                print("deleted")
                command["reading"] = False
            else:
                command["str"] = command["str"][:-1]
        elif len(str(key)) == 3 and str(key)[1].isalpha():
            command["str"] += str(key)[1]
        else:
            print("invalid")
            command["reading"] = False
    else:
        if str(key) == "'/'":
            print("start")
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


if __name__ == '__main__':
    pass