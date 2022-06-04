from pprint import pprint

sentence = "This is a common interview question, find the most repeated character in this text"

registry = {}
for char in sentence:
    if char in registry:
        registry[char] += 1
    else:
        registry[char] = 1

pprint(registry, width=1)

registry_sorted = sorted(
    registry.items(),
    key=lambda kv: kv[1],
    reverse=True)

print(registry_sorted[0])
