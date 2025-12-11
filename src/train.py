with open("data/dataset.txt") as f:
 data = f.read().upper()
with open("models/model.txt", "w") as f:
 f.write(data)
