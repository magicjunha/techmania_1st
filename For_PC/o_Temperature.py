import random
import time

import o_ControlSet
import n_Client

Temperature = o_ControlSet.Sensing(1, 0)
Action = o_ControlSet.ObjAction(0)
Send2Server = n_Client.Client()
location = 'Location_Def'

#count = 0
#while count<=10:
Temperature.SetValue(int(random.random()*100))
message = Temperature.SerialData() + ";" + Action.SerialData() + ";" + location
#센서종류:값 ; Relay상태: 상태값 ; 지역
print (message)


Send2Server.SendData(message)
   #time.sleep(3)
   #count += 1


#print ("--_-> Now Relay On")
#Action.SetValue(1)
#print (Action.PrintValue())


