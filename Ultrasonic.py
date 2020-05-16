import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BOARD )
GPIO_trigger = 11
GPIO_echo    = 13

GPIO.setup( GPIO_trigger, GPIO.OUT )
GPIO.setup( GPIO_echo,    GPIO.IN  )

def get_Distance():
    GPIO.output( GPIO_trigger, True  )
    time.sleep( 0.000001 )
    GPIO.output( GPIO_trigger, False )
    
    start_time = time.time()
    stop_time  = time.time()

    while GPIO.input( GPIO_echo ) == 0 :
        start_time = time.time()
    
    while GPIO.input( GPIO_echo ) == 1 :
        stop_time  = time.time()

    time_elapsed   = stop_time - start_time
    Distance  = ( time_elapsed * 34300 ) / 2

    return Distance

if __name__ =='__main__' :
    try:
        while True:
            dist = get_Distance()
            print( "Distance = {:.2f} cm".format( dist ) )
            time.sleep( 1 )
    except KeyboardInterrupt:
        print( "Stopped by User" )
        GPIO.cleanup()
        
