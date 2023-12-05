def find_common_participants(members1:str, members2:str, separator=','):
    elem1 = set(members1.split(separator))
    elem2 = set(members2.split(separator))
    return sorted(list(elem1.intersection(elem2)))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, separator='|'))