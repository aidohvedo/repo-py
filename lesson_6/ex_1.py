import time

class TrafficLight:

    __color = 'red'

    def running(self):
        #self.a = a
        i = 0

        time_interval = {'red':7,'yellow':2,'green':3}
        for key,value in time_interval.items():
            print (key)
            time.sleep(value);


svetofor = TrafficLight()
svetofor.running()

