"""
Case-study 11
Developers:
Кривошапова Д. Е.: 30%
Кузнецов А. Д.: 33%
Лапочкин Д. А.: 35%
"""

import random
import sys

def main():
    """
    Main function
    :return: None
    """
    sys.setrecursionlimit(1446)
    sys.stdin = open("azs.txt")
    azs_info = dict()
    azs_status = dict()
    statistic = {'АИ-80': 0, 'АИ-92': 0, 'АИ-95': 0, 'АИ-98': 0, 'доход': 0, 'покинувшие': 0}
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
    statistic = modelling(None, azs_info, azs_status, statistic, 1)
    print('\nЗа сутки было продано', statistic['АИ-80'], 'литров бензина АИ-80,',statistic['АИ-92'], 'литров бензина АИ-92,'
          ,statistic['АИ-95'], 'литров бензина АИ-95,', statistic['АИ-98'], 'литров бензина АИ-98.\nВыручка составила',
          '{:.2f}'.format(statistic['доход']), 'рублей.\n''Из-за скопившейся очереди АЗС покинули',
          statistic['покинувшие'], 'клиентов.')


def monitoring(azs_info, client, event):
    """
    The function prints a description of an event and petrol station information
    :param azs_info: dictionary with an petrol station information
    :param client: list with information about the client
    :param event: string with an event title ('departure', 'waste' or a number of a free pump)
    :return: None
    """
    if event == 'departure':
        print('В', converter(client[4]), 'клиент', client[0], client[1], client[2], client[3],
              'заправил свой автомобиль и покинул очередь.')
    elif event == 'waste':
        print('В', client[0], 'новый клиент:', client[0], client[1], client[2], client[3],
              'не смог заправить свой автомобиль и покинул АЗС')
    else:
        print('В', client[0], 'новый клиент:', client[0], client[1], client[2], client[3],
              'встал в очередь к автомату №' + str(event))
    for n in range(1, len(azs_info) + 1):
        print('Автомат №{0} максимальная очередь: {1} Марки бензина:'.format(n, azs_info[str(n)][0]),
              ','.join(azs_info[str(n)][1]), '->', '*' * azs_info[str(n)][2])


def converter(time):
    """
    The function converts time string to different time format (hh:mm -> m or m -> hh:mm)
    :param time: string with time to be converted
    :return: string with converted time
    """
    if str(time).count(':'):
        return str(int(time[:2]) * 60 + int(time[3:]))
    else:
        return '{:02d}:{:02d}'.format(int(time) // 60, int(time) % 60)


def check_place(azs_info, client):
    """
    The function checks petrol station information for a free pump with a required petrol type.
    :param azs_info: dictionary with a petrol station information
    :param client: list with information about the client
    :return: tuple with azs_info and a number of a free pump, it there aren't any, returns '-1'
    """
    benz = client[-2]
    min_status = [0, 999]
    for key in azs_info:
        if benz in azs_info[key][1]:
            if min_status[1] > azs_info[key][2] and int(azs_info[key][0]) > azs_info[key][2]:
                min_status[0] = key
                min_status[1] = azs_info[key][2]
    if min_status[1] != 999:
        azs_info[min_status[0]][2] += 1
        return azs_info, str(min_status[0])
    return azs_info, '-1'


def new(client, azs_status, petrol):
    """
    The function adds the client to the queue of the required petrol pump and completes client information with
    a departure time
    :param client: list with information about the client
    :param azs_status: dictionary with a petrol station status
    :param petrol: number of the required petrol pump
    :return: azs_status
    """
    if not azs_status[str(petrol)]:
        client.append(int(converter(client[0])) + client[3])
    else:
        client.append(azs_status[str(petrol)][-1][4] + client[3])
    azs_status[str(petrol)].append(client)
    return azs_status


def modelling(client, azs_info, azs_status, statistic, time):
    """
    The recursive function simulates minute-to-minute working cycle of the petrol station (1440 cycles)
    :param client: list with following client, if any client participated in the previous cycle, the parameter is equal
     to None
    :param azs_info: dictionary with a petrol station information
    :param azs_status: dictionary with a petrol station status
    :param statistic: dictionary with the petrol station working statitistic
    :param time: number of the cycle
    :return: statistic
    """
    prices = {'АИ-80': 31.50, 'АИ-92': 45.49, 'АИ-95': 50.01, 'АИ-98': 57.34}
    petrol = None
    if time == 1440:
        return statistic
    if not client:
        client = list(input().split())
        speed = random.randint(9, 11)
        if int(client[1]) % speed == 0:
            client.append(int(client[1]) // speed)
        else:
            client.append((int(client[1]) // speed) + 1)
    for n in range(1, len(azs_status) + 1):
        if azs_status[str(n)]:
            departure_time = str(azs_status[str(n)][0][4])
            if int(departure_time) <= int(time):
                azs_info[str(n)][2] -= 1
                monitoring(azs_info, azs_status[str(n)][0], 'departure')
                azs_status[str(n)].pop(0)
    if str(time) == converter(client[0]):
        azs_info, petrol = check_place(azs_info, client)
    if not petrol:
        return modelling(client, azs_info, azs_status, statistic, time + 1)
    elif petrol == '-1':
        statistic['покинувшие'] += 1
        monitoring(azs_info, client, 'waste')
        return modelling(None, azs_info, azs_status, statistic, time + 1)
    else:
        if client[2] == 'АИ-80':
            statistic['АИ-80'] += int(client[1])
        if client[2] == 'АИ-92':
            statistic['АИ-92'] += int(client[1])
        if client[2] == 'АИ-95':
            statistic['АИ-95'] += int(client[1])
        if client[2] == 'АИ-98':
            statistic['АИ-98'] += int(client[1])
        statistic['доход'] += int(client[1]) * prices[client[2]]
        monitoring(azs_info, client, petrol)
        azs_status = new(client, azs_status, petrol)
        return modelling(None, azs_info, azs_status, statistic, time + 1)


if __name__ == '__main__':
    main()
