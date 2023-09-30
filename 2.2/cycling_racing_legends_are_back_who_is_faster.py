petya_mean_speed = int(input())
vasya_mean_speed = int(input())
tolya_mean_speed = int(input())

mean_speeds = [petya_mean_speed, vasya_mean_speed, tolya_mean_speed]
names = ['Петя', 'Вася', 'Толя']
unused_indexes = list(range(3))

max_index = mean_speeds.index(max(mean_speeds))
unused_indexes.remove(max_index)
min_index = mean_speeds.index(min(mean_speeds))
unused_indexes.remove(min_index)
mid_index = unused_indexes[0]

print(f'          {names[max_index]}')
print(f'  {names[mid_index]}')
print(f'                  {names[min_index]}')
print('   II      I      III   ')