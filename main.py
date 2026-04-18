import json

with open("../tree/reflection-tree.json") as f:
    tree = json.load(f)

state = {"axis1":"","axis2":"","axis3":""}
current = "START"

while True:
    node = tree[current]
    print("\n" + node["text"])

    if node["type"] == "end":
        break

    if node["type"] == "question":
        for i,opt in enumerate(node["options"],1):
            print(f"{i}. {opt}")
        choice = int(input("Choose: ")) - 1
        ans = node["options"][choice]

        if "signal" in node:
            for s in node["signal"]:
                a,v = s.split(":")
                state[a] = v

        current = node["next"][ans]

    else:
        current = node["next"]

print("\nSummary:", state)