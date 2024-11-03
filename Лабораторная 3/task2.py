participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(group1: str, group2: str, delimiter: str = ',') -> list:

    participants_first_group = group1.split(delimiter)
    participants_second_group = group2.split(delimiter)

    common_participants = set(participants_first_group) & set(participants_second_group)

    return sorted(common_participants)

common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter = '|')
print(common_participants)
