filename = input("Enter a file name: ")
handle = open(filename)

hour_counts = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hour = time.split(":")[0]
        hour_counts[hour] = hour_counts.get(hour, 0) + 1

hour_list = list(hour_counts.items())
hour_list.sort()

for hour, count in hour_list:
    print(hour, count)
