dangerdistance = 20
def disdec():
    motoroff()
    go = False
    sleeptime = 1
    distance_r = [0,False]
    distance_l = [0,False]

    while True:
        
        rotateright()
        time.sleep(sleeptime)
        car.motoroff()
        
        distance = distancescanner(Trigger,Echo)
        if distance > dangerdistance:
            ditance_r = [distance,True]

        rotateleft(10)
        time.sleep(sleeptime + 1)
        distance = distancescanner(Trigger,Echo)
        
        if distance > dangerdistance:
            distance_l = [distance,True]
            
        if distance_l[1]  and distance_r[1]:
            if distance_l > distance_r:
                return 
            else:
                car.rotateright(10)
                time.sleep(sleeptime + 1)
                car.motoroff()
                return
        if distance_l[1]  and not distance_r[1] :
            return
        if distance_r[1] and not distance_l[1]:
            car.rotateright(10)
            time.sleep(sleeptime + 1)
            car.motoroff()
            return
        sleeptime +=1
        
            
def SkyNet():
    car.forward(30)
    distance = distancescanner(Trigger,Echo)

    if distance < dangerdistance:
        car.motoroff()
        disdec()
    
    if black():
        Robocop()
        
    



























    
    
