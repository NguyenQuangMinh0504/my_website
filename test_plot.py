import pandas as pd
import matplotlib.pyplot as plt

data = {"05/01/23": {"my-website": 1, "project-2": 1},
        "05/02/23": {"my-website": 1, "project-2": 3},
        "05/03/23": {"my-website": 1, "project-2": 1},
        "05/04/23": {"my-website": 1},
        "05/05/23": {"my-website": 1},
        "05/06/23": {},
        "05/07/23": {"my-website": 1, "project-2": 1}
        }
keys = []
for day in data.keys():
    for key in data[day].keys():
        if key not in keys:
            keys.append(key)
print(keys)
formatted_data = []
for day in data.keys():
    row = [day]
    for key in keys:
        row.append(data[day].get(key, 0))
    formatted_data.append(row)
columns = ["Day"]
columns.extend(keys)
df = pd.DataFrame(formatted_data, columns=columns)
ax = df.plot(x="Day", kind="bar", stacked=True, title="Study time")
# plt.show()
ax.figure.savefig("./something.png")