first_file = open('first_tour.txt', 'r', encoding='utf8')
k = int(first_file.readline())
participants = []

for line in first_file:
    if int(line.split()[2]) > k:
        participants.append(line.split())
first_file.close()

participants.sort(key=lambda x: int(x[2]), reverse=True)

with open('second_tour.txt', 'w', encoding='utf8') as file:
    file.write(str(len(participants)) + '\n')
    for line_number, participant_details in enumerate(participants):
        file.write(f'{line_number + 1}) {participant_details[1][0]}. '
                   f'{participant_details[0]} {participant_details[2]}\n')

