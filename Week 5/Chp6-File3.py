def inventory(items):
    for item in items:
        print(item)
        items.clear()
    return


backpack = ["Water bottle", "Map", "Compass"]
inventory(backpack)
print(backpack)
# backpack.append("Swiss Army knife")
# inventory(backpack)
