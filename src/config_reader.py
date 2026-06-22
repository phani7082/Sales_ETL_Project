import json

with open(
    "config/config.json",
    "r"
) as file:

    config = json.load(file)

print(config)





config["source_file"]

source=config["source_file"]
print(source)



config["destination_file"]

dest=config["destination_file"]
print(dest)


