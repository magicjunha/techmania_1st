class Sensing:
   '''Sensing from Environments'''
   # Role ID : 1 -> Temperature
   #           2 -> Humidity
   #           3 -> intensity of illumination (IOI)
   #           4 -> Air flow
   #           5 -> Water
   def __init__(self, ObjRoleId, Value=0,):
      self.ObjRoleId = ObjRoleId
      self.Value = Value
      print('Initialized Sensing Member: "{}  {}")'.format(self.ObjRoleId, self.Value))

   def SetValue(self,Value):
      self.Value = Value

   def SerialData(self):
      Data = str(self.ObjRoleId) + ':' + str(self.Value)
      return Data


class ObjAction:
   def __init__(self, ActionValue=0,):
      self.ActionValue = ActionValue
      

   def GetValue(self):
      return self.ActionValue

   def SetValue(self,ActionValue):
      self.ActionValue = ActionValue

   def SerialData(self):
      Data = 'Realy:' + str(self.ActionValue)
      return Data

   def PrintValue(self):
      if self.ActionValue == 0:
         print("Relay Off")
      else:
         print("Relay On")
