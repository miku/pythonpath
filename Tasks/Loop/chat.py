
import json

data = json.loads(open("eur.json").read())

latest = "usd" # keep the latest around

while True:
    user_input = input("> ")
    if user_input in ("q", "quit", "exit"):
        break
    if user_input in ("ls", "info", "c"):
        print(", ".join(data["eur"].keys()))
        continue
    s = user_input.lower()
    try:
        amount = float(s)
        print("EUR {} => {} {}".format(amount, latest, data["eur"][latest] * amount))

    except ValueError:
        if s not in data["eur"].keys():
            print("unknown currency: {}".format(s))
            continue
    else:
        continue
    latest = s
    print("1 EUR => {} {}".format(s.upper(), data["eur"][s]))

