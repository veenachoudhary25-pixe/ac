
import json
import matplotlib
matplotlib.use("Agg")
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

with open("numbers.json", "r") as file:
    data = json.load(file)

temperatures = [item["temperature"] for item in data if "temperature" in item]

x_values = range(1, len(temperatures) + 1)

plt.bar(x_values, temperatures)

plt.title("AC Temperature History")
plt.xlabel("Record Number")
plt.ylabel("Temperature (°C)")
plt.savefig("ac_temperature.png")
