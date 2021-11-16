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
    return ''' ----------- Accident details: ------------- 
> Begin time: {}
> End time: {}
> Location: {}                                    
> Num of casualties: {}
> Casualty list: 
  {}
> Num of injuries: {}
> Injury list: 
  {}
> Financial loss: BDT {}'''.format(self.bT,self.eT,self.loc,self.noc,self.cas_list,self.noi,self.inj_list,self.fLoss)

  # Update casualties:
  # Value of noc incremented by 1 so that updated casualty 
  # and injury list does not replace existing values, 
  # instead starts from one index after last recorded value
  def upd_cas(self):
    x = self.noc + 1
    c = input('Update number (N) or List (L) of casualties? (N/L): ')

    # If number is selected, take input for noc and check
    # if casualty details (name, age, NID) will be added 
    if c in ('n','N'):
      n = int(input('How many new casualties?: '))
      self.noc = self.noc + n
      d = input('Add details? (Y/N): ')
      if d in ('y','Y'):
        for i in range(x,self.noc+1):
          self.cas_list[i] = {}
          print('Casualty ',i)
          self.cas_list[i]['name'] = input('Enter name: ')
          self.cas_list[i]['age'] = input('Enter age: ')
          self.cas_list[i]['NID'] = input('Enter NID num: ')
        return self.noc, self.cas_list
      elif d in ('n','N'):
        for i in range(x,self.noc+1):
          self.cas_list[i] = {}
          self.cas_list[i]['name'] = 'unknown'
          self.cas_list[i]['age'] = 'unknown'
          self.cas_list[i]['NID'] ='unknown'
        return self.noc, self.cas_list


    # If list is selected, record new input list,
    # parse data and convert to dictionary. Update noc.
    elif c in ('l','L'):
      p = input('Enter details seperated by space :')
      # split new casualty list
      new_cas = p.split(" ") 
      # divide length of new list by 3 to get increment amount of noc
      y = int(len(new_cas)/3)
      self.noc = self.noc + y
      # a variable 'j' is set up to traverse new list 
      j = 0 
      # update 'casualty list' dictionary with new data
      for i in range(x,self.noc+1):
         self.cas_list[i] = {}
         self.cas_list[i]['name'] = new_cas[j]
         j += 1
         self.cas_list[i]['age'] = new_cas[j]
         j += 1
         self.cas_list[i]['NID'] = new_cas[j]
         j += 1
      return self.noc, self.cas_list

  # Update injuries method:
  # same as update casualties method
  def upd_inj(self):
    x = self.noi + 1
    c = input('Update number (N) or List (L) of injuries? (N/L): ')

    if c in ('n','N'):
      n = int(input('How many new injuries?: '))
      self.noi = self.noi + n 
      d = input('Add details? (Y/N): ')
      if d in ('y','Y'):
        for i in range(x,self.noi+1):
          self.inj_list[i] = {}
          print('Injured ',i)
          self.inj_list[i]['name'] = input('Enter name: ')
          self.inj_list[i]['age'] = input('Enter age: ')
          self.inj_list[i]['NID'] = input('Enter NID num: ')
        return self.noi, self.inj_list
      elif d in ('n','N'):
        for i in range(x,self.noc):
          self.inj_list[i] = {}
          self.inj_list[i]['name'] = 'unknown'
          self.inj_list[i]['age'] = 'unknown'
          self.inj_list[i]['NID'] ='unknown'
        return self.noi, self.inj_list

    elif c in ('l','L'):
      p = input('Enter details seperated by space :')
      new_inj = p.split(" ") 
      y = int(len(new_inj)/3)
      self.noi = self.noi + y 
      j = 0 
      for i in range(x,self.noi+1):
         self.inj_list[i] = {}
         self.inj_list[i]['name'] = new_inj[j]
         j += 1
         self.inj_list[i]['age'] = new_inj[j]
         j += 1
         self.inj_list[i]['NID'] = new_inj[j]
         j += 1
      return self.noi, self.inj_list


# road accident subclass
class road_acc(Accident):                       
  
  # 'list of cars' (car_list) attribute added
  def __init__(self, car_list):
    super().__init__(bT, eT, loc, noc, cas_list, noi, inj_list, fLoss) # super method to call data from parent class(Accident)
    self.car_list=car_list                       
  
  def __str__(self):                            
    return '> List of cars: {}'.format(self.car_list)


# plane crash subclass
class plane_acc(Accident): 
  def __init__(self, plane_list):
    super().__init__(bT, eT, loc, noc, cas_list, noi, inj_list, fLoss)
    self.plane_list=plane_list # list of planes attribute added
  def __str__(self):
    return '> List of planes: {}'.format(self.plane_list) 

# fire accident subclass
class fire_acc(Accident): 
  def __init__(self, fire_src):
    super().__init__(bT, eT, loc, noc, cas_list, noi, inj_list, fLoss)
    self.fire_src=fire_src # source of fire attribute added
  def __str__(self):
    return '> Source of fire: {}'.format(self.fire_src)

 # marine accident subclass
class mar_acc(Accident): 
  def __init__(self, launchtrack_num):
    super().__init__(bT, eT, loc, noc, cas_list, noi, inj_list, fLoss)
    self.launchtrack_num=launchtrack_num # launch tracking number attribute added
  def __str__(self):
    return '> Launch tracking number: {}'.format(self.launchtrack_num)

###################### DRIVER CODE ###############################

# set up index to seperate incidents and an array to 
# record all subsequent instances of accidents
all_acc = {}
all_acc.clear()
acc_num=int(input('How many record entries?: '))
for i in range(acc_num):
  print('Insert details of Accident: ')

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

  check = input('Is start time recorded? (Y/N): ')
  if check in ('y','Y'):
    start = str(input('Enter start time of accident (hh:mm dd-mm-yyyy): '))
    bT= datetime.strptime(start, "%H:%M %d-%m-%Y")
    check = input('Is end time recorded? (Y/N): ')
    if check in ('y','Y'):
      end = str(input('Enter end time of accident (hh:mm dd-mm-yyyy): '))
      eT= datetime.strptime(end, "%H:%M %d-%m-%Y")
    elif check in ('n','N'):
      eT=bT    
    elif check in ('n','N'):
      bt=0

  check = input('Is end time recorded? (Y/N): ')
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
  noi=int(input('Enter number of injured: '))
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
    all_acc[i]=Accident(bT, eT, loc, noc, cas_list, noi, inj_list, fLoss)
    print(all_acc[i])
    r = road_acc(car_list)
    print(r)
    format_float = "{:.2f}".format(all_acc[i].imp)
    print("  Impact factor: ", format_float)

  #call plane crash subclass
  elif acc_type == 2:
    plane_num=int(input('Enter number of planes: '))
    plane_list = []
    for i in range(0,plane_num):
      name = str(input('Enter name of plane: '))
      plane_list.append(name)
    all_acc[i]=Accident(bT, eT, loc, noc, cas_list, noi, inj_list, fLoss)
    print(all_acc[i])
    p=plane_acc(plane_list)
    print(p)
    format_float = "{:.2f}".format(all_acc[i].imp)
    print("  Impact factor: ", format_float)
    print(' --------------------------------------- ')

  #call fire accident subclass
  elif acc_type == 3:
    fire_src=str(input('Enter source of fire: '))
    all_acc[i]=Accident(bT, eT, loc, noc, cas_list, noi, inj_list, fLoss)
    print(all_acc[i])
    f=fire_acc(fire_src)
    print(f)
    format_float = "{:.2f}".format(all_acc[i].imp)
    print("  Impact factor: ", format_float)
    print(' --------------------------------------- ')

  #call marine accident subclass
  elif acc_type == 4:
    launchtrack_num=float(input('Enter launch tracking num: '))
    all_acc[i]=Accident(bT, eT, loc, noc, cas_list, noi, inj_list, fLoss)
    print(all_acc[i])
    m=mar_acc(launchtrack_num)
    print(m)
    format_float = "{:.2f}".format(all_acc[i].imp)
    print("  Impact factor: ", format_float)
    print(' --------------------------------------- ')

  #if no subclass called
  else:
    all_acc[i]=Accident(bT, eT, loc, noc, cas_list, noi, inj_list, fLoss)
    print(all_acc[i])
    format_float = "{:.2f}".format(all_acc[i].imp)
    print("  Impact factor: ", format_float)
    print(' --------------------------------------- ')

  up = input('Record new data for Accident? (Y/N): ') 
  if up in ('y','Y'):
    # input to update casualties and injuries
    c = input('Update casualties? (Y/N): ')
    if c in ('y','Y'):
      all_acc[i].upd_cas()
    elif c in ('n','N'):
      d = input('Update injuries? (Y/N): ')
      if d in ('y','Y'):
        all_acc[i].upd_inj()

    print(' --------- UPDATES: --------- ')
    print('New number of casualties: ',all_acc[i].noc)
    print('Updated casualty list :\n',all_acc[i].cas_list)
    print('New number of injured: ',all_acc[i].noi)
    print('Updated injury list :\n',all_acc[i].inj_list)

##### UNABLE TO COMPLETE MERGE ########

#mer = input('Merge records (Y/N): ') 
#if mer in ('y','Y'):
#   x1 = int(input('Enter first record to merge :'))
#   x2 = int(input('Enter second record to merge :'))
#   merged = Accident.merge(all_acc[x1],all_acc[x2])
