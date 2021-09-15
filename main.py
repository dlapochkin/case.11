import sys, random
sys.setrecursionlimit(1500)




def check_place(azs_info, following):
    # функция выдает номер заправки, рассмотреть все случаи и закинуть в словарь
    # min_status = [номер колонки,минимальное количество машин в очереди]
    benz = following[-2]
    min_status = [0, 999]
    for key in azs_info:
        if benz in azs_info[key][1]:
            if min_status[1] > azs_info[key][2] and int(azs_info[key][0]) > azs_info[key][2]:
                min_status[0] = key
                min_status[1] = azs_info[key][2]
    if min_status[1] != 999:
        azs_info[min_status[0]][2] += 1
        return (azs_info, str(min_status[0]))
    return (azs_info, '-1')


def new(following, azs_status, petrol):
    following.append(int(converter(following[0])) + following[3])
    azs_status[str(petrol)].append(following)
    return azs_status


def monitoring(azs_info, info, event):
    if event == 'departure':
        print('В', converter(info[4]), 'клиент', info[0], info[1], info[2], info[3], 'заправил свой автомобиль и покинул очередь.')
    elif event == 'waste':
        print('В', info[0], 'новый клиент:', info[0], info[1], info[2], info[3], 'не смог заправить свой автомобиль и покинул АЗС')
    else:
        print('В', info[0], 'новый клиент:', info[0], info[1], info[2], info[3], 'встал в очередь к автомату №', event)
    for n in range(1,len(azs_info)+1):
        print('Автомат №{0} максимальная очередь: {1} Марки бензина:'.format(n, azs_info[str(n)][0]),
            ','.join(azs_info[str(n)][1]), azs_info[str(n)][2])



def converter(time):
    if str(time).count(':'):
        return str(int(time[:2]) * 60 + int(time[3:]))
    else:
        return '{:02d}:{:02d}'.format(int(time) // 60, int(time) % 60)


def modelling(following, azs_info, azs_status, status, time):
    petrol = None
    if time == 1440:
        return status
    if not following:
        following = list(input().split())
        speed = random.randint(9, 11)
        if int(following[1]) % speed == 0:
            following.append(int(following[1]) // speed)
        else:
            following.append((int(following[1]) // speed) + 1)  # первая строка файла
    for n in range(1,len(azs_status)+1):
        if azs_status[str(n)] != []:
            departure_time = str(azs_status[str(n)][0][4])
            if departure_time <= str(time):
                azs_info[str(n)][2] -= 1
                monitoring(azs_info, azs_status[str(n)][0], 'departure')
                azs_status[str(n)].pop()
    if str(time) == converter(following[0]):
        azs_info, petrol = check_place(azs_info,following)
    if not petrol:
        return modelling(following, azs_info, azs_status, status, time + 1)
    elif petrol == '-1':
        monitoring(azs_info, following, 'waste')
        following = None
        return modelling(following, azs_info, azs_status, status, time + 1)
    else:
        monitoring(azs_info, following, petrol)
        azs_status = new(following, azs_status, petrol)
        following = None
        return modelling(following, azs_info, azs_status, status, time + 1)

def main():
    sys.stdin = open("azs.txt")
    azs_info = dict()
    azs_status = dict()
    status = dict()
    while True:
        try:
            line = list(input().split())
            azs_info[line[0]] = [line[1], line[2:], 0]
            azs_status[line[0]] = []
            if line == '':
                break
        except (ValueError, EOFError):
            break
    sys.stdin = open('input.txt')
    modelling(None, azs_info, azs_status, status, 1)

main()