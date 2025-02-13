import yaml

with open("blueprints.yaml", "r") as f:
    data = yaml.safe_load(f)

print(data["train"])
print(data["val"])