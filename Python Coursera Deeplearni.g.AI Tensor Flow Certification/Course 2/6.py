file_name = input("Enter file name: ")
handle = open(file_name)

senders = dict()

for line in handle:
    if line.startswith('From '):
        words = line.split()
        sender = words[1]
        senders[sender] = senders.get(sender, 0) + 1

most_frequent_sender = None
max_count = 0

for sender, count in senders.items():
    if count > max_count:
        most_frequent_sender = sender
        max_count = count

print(most_frequent_sender, max_count)
