import sys
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
def check_place(azs_info,following):
#функция выдает номер заправки, рассмотреть все случаи и закинуть в словарь
#min_status = [номер колонки,минимальное количество машин в очереди]
    min_status = [0,999]
    for key in azs_info:
        if benz in azs_info[key][1]:
            if min_status[1] > azs_info[key][2] and azs_info[key][0] != azs_info[key][2]:
                min_status[0] = key
                min_status[1] = azs_info[key][2]
    if min_status[1] != 999:
        azs_info[min_status[0]][2] += 1
        return(azs_info,min_status[0])
    return 0

def monitoring(azs_info, info, event):
    if event == 'departure':
        print('В', info[4], 'клиент', info[0], info[1], info[2], info[3], 'заправил свой автомобиль и покинул очередь.')
    else:
        print('В', info[0], 'новый клиент:', info[0], info[1], info[2], info[3], 'встал в очередь к автомату №', event)
    for n in range(len(azs_info)):
        print('Автомат №{0} максимальная очередь: {1} Марки бензина:'.format(n, azs_info[n][0]), ','.join(azs_info[n][1]))
        
        
def converter(time):
    if time.count(':'):
        return str(int(time[:2]) * 60 + int(time[3:]))
    else:
        return '{:02d}:{:02d}'.format(int(time)//60, int(time)%60)


def modelling(following, azs_info, azs_status, status, time):
    petrol = None
    if time == 1440:
        return status
    if following == '':
        pass                            # первая строка файла
    for n in range(len(azs_status)):
        if azs_status[n] != []:
            departure_time = converter(azs_status[n][0][4])
            if departure_time == str(time):
                monitoring(azs_info, azs_status[n][0], 'departure')

       
    
    

    
    
    if time == converter(following[:5]):
        petrol = check_place(following, azs_info)
