import random
randomNumber = random.randint(1,9)
chances = 3
decider = int(input('Pick a number 1 through 9:'))

if(decider == 5):
    print('Congratulations you won!')
else:
    chances=chances-1
    print('Try again!')
    decider = int(input('Pick a number 1 through 9:'))
    chances=chances-1
    print('Try again')
    decider = int(input('Pick a number 1 through 9:'))
    chances=chances-1
  

if(chances==0):
    print('You have LOST!')




 