petya_mean_speed = int(input())
vasya_mean_speed = int(input())
tolya_mean_speed = int(input())

racers = [(petya_mean_speed, 'Петя'), (vasya_mean_speed, 'Вася'),
          (tolya_mean_speed, 'Толя')]
racers = sorted(racers, key=lambda x: x[0], reverse=True)

for i, racer in enumerate(racers):
    print(f'{i + 1}. {racer[1]}')
