import matplotlib.pyplot as plt
from datetime import datetime, timedelta
start_date = datetime(year=2023, month=4, day=10)
end_date = datetime.now()
date_list = []
running_list = [2, 3.02, 4.02, 3.55, 3.03, 4.76, 3.02, 2.77, 2.67,
                3.17, 3.45, 3.42, 4.54, 5.3, 2.86, 3.68]
while start_date.day < end_date.day:
    # date_list.append(start_date.strftime("%a %d-%m"))
    date_list.append(start_date.strftime("%d"))
    start_date += timedelta(days=1)
plt.plot(date_list, running_list)
plt.savefig("../running/static/running/images/distance.png")
plt.clf()
running_time_list = [30, 30, 30, 30, 30, 45, 30, 30,
                     30, 30, 30, 30, 45, 45, 30, 30]
pace_list = []
for i in range(len(running_list)):
    pace_list.append(running_time_list[i] / running_list[i])
plt.plot(date_list, pace_list)
plt.savefig("../running/static/running/images/pace.png")
plt.clf()
plt.bar(date_list, running_time_list)
plt.savefig("../running/static/running/images/duration.png")
