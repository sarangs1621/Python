def trafficlight():
    signal=input("enter the color of traffic light:")
    if (signal not in( "RED","YELLOW","GREEN")):
        print("PLEASE ENTER A VALID COLOR")
    else:
           value=light(signal)
           if (value==0):
               print("STOP,YOUR LIFE IS PRECIOUS")
           elif(value==1):
               print('PLEASE GO SLOW')
            else:
              print("GO! THANK YOU FOR BEING PATIENT")
    def light(color):
        if (color=="RED"):
             return(0)
        elif (color=='YELLOW'):
            return(1)
        else:
            return(2)
trafficlight()
print("SPEED THRILLS BUT KILLS")
