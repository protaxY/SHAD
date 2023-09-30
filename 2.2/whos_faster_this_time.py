petya_mean_speed = int(input())
vasya_mean_speed = int(input())
tolya_mean_speed = int(input())

racers = [petya_mean_speed, vasya_mean_speed, tolya_mean_speed]
winner = max(racers)

if winner == petya_mean_speed:
    print('Петя')
if winner == vasya_mean_speed:
    print('Вася')
if winner == tolya_mean_speed:
    print('Толя')
