boat_side = 'Right'
missionaries_on_right = 3
cannibals_on_right = 3
missionaries_on_left = 0
cannibals_on_left = 0

print('Right Side')
print('M = '+str(missionaries_on_left) +' C = ' + str(cannibals_on_left) + '|-----B|' + 'M = ' + str(missionaries_on_right) + ' C = ' +str(cannibals_on_right))

while True:
   
  ## BOAT ON RIGHT SIDE
  if boat_side == 'Right':
    
    missionaries = int(input('ENTER THE NUMBER OF MISSIONARIES ON BOAT: '))
    cannibals = int(input('ENTER THE NUMBER OF CANNIBALS BOAT: '))
    
    if (missionaries + cannibals)<0 or (missionaries + cannibals)>2:
      print('Invalid Move 1')
      continue
    else:
      if (missionaries_on_right < missionaries) or (cannibals_on_right < cannibals):
        print('Invalid Move 2')
        continue
    
      else:
        cannibals_on_right -= cannibals
        missionaries_on_right -= missionaries
        cannibals_on_left += cannibals
        missionaries_on_left += missionaries

        print('M = '+str(missionaries_on_left) +' C = ' + str(cannibals_on_left) + '|B-----|' + 'M = ' + str(missionaries_on_right) + ' C = ' +str(cannibals_on_right))
        boat_side = 'Left'

  ## BOAT ON LEFT SIDE
  elif boat_side == 'Left':

    missionaries = int(input('ENTER THE NUMBER OF MISSIONARIES ON BOAT: '))
    cannibals = int(input('ENTER THE NUMBER OF CANNIBALS BOAT: '))
    
    if (missionaries + cannibals) < 0 or (missionaries + cannibals) > 2 :
      print('Invalid Move 1')
      continue
    else:
      if (missionaries_on_left < missionaries) or (cannibals_on_left < cannibals):
        print('Invalid Move 2')
        continue
      else:
        cannibals_on_left -= cannibals
        missionaries_on_left -= missionaries
        cannibals_on_right += cannibals
        missionaries_on_right += missionaries

        print('M = '+str(missionaries_on_left) +' C = ' + str(cannibals_on_left) + '|-----B|' + 'M = ' + str(missionaries_on_right) + ' C = ' +str(cannibals_on_right))
        boat_side = 'Right'
  
  ### GAME RESULT
  if ((missionaries_on_right < cannibals_on_right) and (missionaries_on_right > 0)) or ((missionaries_on_left < cannibals_on_left) and (missionaries_on_left > 0)):
    print('YOU LOSE')
    break
    
  elif (missionaries_on_left and cannibals_on_left) == 3:
    print('YOU WIN')  
    break  

print('GAME OVER')