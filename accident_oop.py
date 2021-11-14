from datetime import datetime
import math
import decimal
from decimal import Decimal

################# CLASS INITIALISATION ###############################

# Parent class initialised
class Accident:
  def __init__(self, bT, eT, loc, noc, cas_list, noi,inj_list, fLoss):
    self.bT=bT                  # beginning time of accident
    self.eT=eT                  # ending time of accident
    self.loc=str(loc)           # location of accident
    self.noc=noc                # number of casualties
    self.noi=noi                # number of injuries   
    self.fLoss= fLoss           # financial loss
    self.cas_list=cas_list      # list of casualties
    self.inj_list=inj_list      # list of injuries
    self.imp= Decimal(math.log(noi+1)+math.sqrt(noc)+(math.pow(1.12,(fLoss/100))))   # impact factor

  # method to print all recorded items
  def __str__(self):
    return ''' --------- General accident details: --------- 
  Begin time: {}
  End time: {}
  Location: {}                                    
  Num of casualties: {}
  Casualty list: 
  {}
  Num of injuries: {}
  Injury list: 
  {}
  Financial loss: BDT {}'''.format(self.bT,self.eT,self.loc,self.noc,self.cas_list,self.noi,self.inj_list,self.fLoss)

  # Update casualties:
  # value of noc increased by 1 so that updated casualty 
  # and injury list does not replace existing values, 
  # instead starts from one index after last recorded value
  def upd_cas(self):
    x = self.noc + 1
    n = int(input('How many new casualties?: '))
    self.noc = self.noc + n + 1
    det = input('Add details? (Y/N): ')
    if c in ('y','Y'):
      for i in range(x,self.noc):
        self.cas_list[i] = {}
        print('Casualty',i)
        self.cas_list[i]['name'] = input('Enter name: ')
        self.cas_list[i]['age'] = input('Enter age: ')
        self.cas_list[i]['NID'] = input('Enter NID num: ')
      list=Accident(self.bT,self.eT,self.loc,self.noc,self.cas_list,self.noi,self.inj_list,self.fLoss)
      return list

    elif c in ('n','N'):
      for i in range(x,self.noc):
      self.cas_list[i] = {}
      self.cas_list[i]['name'] = 'unknown'
      self.cas_list[i]['age'] = 'unknown'
      self.cas_list[i]['NID'] ='unknown'
    list=Accident(self.bT,self.eT,self.loc,self.noc,self.cas_list,self.noi,self.inj_list,self.fLoss)
    return list

    

  # Update injuries method:
  # same as update casualties method
  def upd_inj(self):
    x = self.noi + 1
    n = int(input('How many new casualties?: '))
    self.noi = self.noi + n + 1  
    for i in range(x,self.noi):
      self.inj_list[i] = {}
      print('Injury',i)
      self.inj_list[i]['name'] = input('Enter name: ')
      self.inj_list[i]['age'] = input('Enter age: ')
      self.inj_list[i]['NID'] = input('Enter NID num: ')
    list=Accident(self.bT,self.eT,self.loc,self.noc,self.cas_list,self.noi,self.inj_list,self.fLoss)
    return list
    


# road accident subclass
class road_acc(Accident):                       
  
  # 'list of cars' (car_list) attribute added
  def __init__(self, bT, eT, loc, noc, cas_list, noi, inj_list, fLoss, car_list):
    super().__init__(bT, eT, loc, noc, cas_list, noi, inj_list, fLoss) # super method to call data from parent class(Accident)
    self.car_list=car_list                       
  
  def __str__(self):                            
    return ''' --------- Car accident details: --------- 
  Begin time: {}
  End time: {}
  Location: {}                                    
  Num of casualties: {}
  Casualty list: 
  {}
  Num of injuries: {}
  Injury list: 
  {}
  Financial loss: BDT {}
  List of cars: {}'''.format(self.bT,self.eT,self.loc,self.noc,self.cas_list,self.noi,self.inj_list,self.fLoss,self.car_list)


# plane crash subclass
class plane_acc(Accident): 
  def __init__(self, bT, eT, loc, noc, cas_list, noi, inj_list, fLoss, plane_list):
    super().__init__(bT, eT, loc, noc, cas_list, noi, inj_list, fLoss)
    self.plane_list=plane_list # list of planes attribute added
  def __str__(self):
    return ''' --------- Plane crash details: --------- 
  Begin time: {}
  End time: {}
  Location: {}
  Num of casualties: {}
  Casualty list: {}
  Num of injuries: {}
  Injury list: {}
  Financial loss: BDT {}
  List of planes: {}'''.format(self.bT,self.eT,self.loc,self.noc,self.cas_list,self.noi,self.inj_list,self.fLoss,self.plane_list) 

# fire accident subclass
class fire_acc(Accident): 
  def __init__(self, bT, eT, loc, noc, cas_list, noi, inj_list, fLoss, fire_src):
    super().__init__(bT, eT, loc, noc, cas_list, noi, inj_list, fLoss)
    self.fire_src=fire_src # source of fire attribute added
  def __str__(self):
    return ''' --------- Fire accident details: --------- 
  Begin time: {}
  End time: {}
  Location: {}
  Num of casualties: {}
  Casualty list: 
  {}
  Num of injuries: {}
  Injury list: 
  {}
  Financial loss: BDT {}
  Source of fire: {}'''.format(self.bT,self.eT,self.loc,self.noc,self.cas_list,self.noi,self.inj_list,self.fLoss,self.fire_src)

 # marine accident subclass
class mar_acc(Accident): 
  def __init__(self, bT, eT, loc, noc, cas_list, noi, inj_list, fLoss, launchtrack_num):
    super().__init__(bT, eT, loc, noc, cas_list, noi, inj_list, fLoss)
    self.launchtrack_num=launchtrack_num # launch tracking number attribute added
  def __str__(self):
    return ''' --------- Marine accident details: --------- 
  Begin time: {}
  End time: {}
  Location: {}
  Num of casualties: {}
  Casualty list: 
  {}
  Num of injuries: {}
  Injury list: 
  {}
  Financial loss: BDT {}
  Launch tracking number: {}'''.format(self.bT,self.eT,self.loc,self.noc,self.cas_list,self.noi,self.inj_list,self.fLoss,self.launchtrack_num)

###################### DRIVER CODE ###############################

# check if data being added is new or an update

  # TIME INPUT:
  # a decision tree is implemented to check if starting and ending
  # time of accident has been recorded. The conditions are as follows:
  #
  #   > Check if start time is available. If true, it is recorded
  #     and we move to end time. If end time available, record
  #     end time, else end time = start time.
  #
  #   > If start time unavailable, set start as null. Check if
  #     end time is available. If true, record end time. If
  #     both start and end unavailable, set start=end='2021'. 

check = input('Is start time recorded? (y/n): ')
if check in ('y','Y'):
  start = str(input('Enter start time of accident (hh:mm dd-mm-yyyy): '))
  bT= datetime.strptime(start, "%H:%M %d-%m-%Y")
  check = input('Is end time recorded? (y/n): ')
  if check in ('y','Y'):
    end = str(input('Enter end time of accident (hh:mm dd-mm-yyyy): '))
    eT= datetime.strptime(end, "%H:%M %d-%m-%Y")
  elif check in ('n','N'):
    eT=bT    
  elif check in ('n','N'):
    bt=0

check = input('Is end time recorded? (y/n): ')
if check in ('y','Y'):
  end = str(input('Enter end time of accident (hh:mm dd-mm-yyyy): '))
  eT= datetime.strptime(end, "%H:%M %d-%m-%Y")
elif check in ('n','N'):
    bT=2021
    eT=bT

# Location input:
# if null or unspecified, value set to 'Dhaka'
loc=str(input('Enter accident location (enter X if unknown): '))
if loc in ('x','X'):
  loc = 'Dhaka'

# create casualty and injury dictionaries
new_key_lis = ['name','age','nid']
c = dict(zip(new_key_lis, [None]*len(new_key_lis)))


# Casualty list:
# Number of casualties (noc) is taken as integer value, 
# initially set to 0. Nested dictionary is created recording
# name, age and NID for multiple entries. Total number 
# of entries = noc.

cas_list = {}
noc=0
noc=int(input('Enter number of casualties: '))
x = noc+1
for i in range(1,x):
  cas_list[i] = {}
  print('Casualty ',i)
  cas_list[i]['name'] = input('Enter name: ')
  cas_list[i]['age'] = input('Enter age: ')
  cas_list[i]['NID'] = input('Enter NID num: ')

# Injury list:
# Same method of working as Casualty list, replace 
# 'noc' & 'cas_list' with 'noi' & 'inj_list'

inj_list = {}
noi=0
noi=int(input('Enter number of injures: '))
x = noi+1
for i in range(1,x):
  inj_list[i] = {}
  print('Injury ',i)
  inj_list[i]['name'] = input('Enter name: ')
  inj_list[i]['age'] = input('Enter age: ')
  inj_list[i]['NID'] = input('Enter NID num: ') 

# Financial loss:
fLoss=int(input('Enter financial loss: BDT '))

# check accident type and call corresponding subclass/child
print("""What type of accident? 
1. Car accident
2. Plane crash
3. Fire accident
4. Marine accident
5. Other""")
acc_type=int(input('Enter corresponding number: '))

#call car accident subclass
if acc_type == 1:
  car_num=int(input('Enter number of cars: '))
  car_list = []
  for i in range(0,car_num):
    name = str(input('Enter name of car: '))
    car_list.append(name)
  list = road_acc(bT, eT, loc, noc,  cas_list, noi, inj_list, fLoss,car_list)
  print(list)
  format_float = "{:.2f}".format(list.imp)
  print("  Impact factor: ", format_float)

#call plane crash subclass
elif acc_type == 2:
  plane_num=int(input('Enter number of planes: '))
  plane_list = []
  for i in range(0,plane_num):
   name = str(input('Enter name of plane: '))
   plane_list.append(name)
   list=plane_acc(bT, eT, loc, noc,  cas_list, noi, inj_list, fLoss,plane_list)
   print(list)
   format_float = "{:.2f}".format(list.imp)
   print("  Impact factor: ", format_float)

#call fire accident subclass
elif acc_type == 3:
  fire_src=str(input('Enter source of fire: '))
  list=fire_acc(bT, eT, loc, noc,  cas_list, noi, inj_list, fLoss,fire_src)
  print(list)
  format_float = "{:.2f}".format(list.imp)
  print("  Impact factor: ", format_float)

#call marine accident subclass
elif acc_type == 4:
  launchtrack_num=float(input('Enter launch tracking num: '))
  list=mar_acc(bT, eT, loc, noc,  cas_list, noi, inj_list, fLoss,launchtrack_num)
  print(list)
  format_float = "{:.2f}".format(list.imp)
  print("  Impact factor: ", format_float)

#if no subclass called
else:
 list=Accident(bT, eT, loc, noc, cas_list, noi, inj_list, fLoss)
 print(list)
 format_float = "{:.2f}".format(list.imp)
 print("  Impact factor: ", format_float)


# input to update casualties and injuries
c = input('Update casualties? (Y/N): ')
if c in ('y','Y'):
  list.upd_cas()
elif c in ('n','N'):
  d = input('Update injuries? (Y/N): ')
  if d in ('y','Y'):
    list.upd_inj()

print('New number of casualties: ',list.noc)
print('Updated casualty list :\n',list.cas_list)
print('New number of injured: ',list.noi)
print('Updated injury list :\n',list.inj_list)



