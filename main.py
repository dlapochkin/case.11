def monitoring(azs_info, info, event):
    if event == 'departure':
        print('В', info[4], 'клиент', info[0], info[1], info[2], info[3], 'заправил свой автомобиль и покинул очередь.')
    else:
        print('В', info[0], 'новый клиент:', info[0], info[1], info[2], info[3], 'встал в очередь к автомату №', event)
    for n in range(len(azs_info)):
        print('Автомат №{0} максимальная очередь: {1} Марки бензина:'.format(n, azs_info[n][0]), ','.join(azs_info[n][1]))



def check_place(following, azs_info):
    return 1


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
    
    
    