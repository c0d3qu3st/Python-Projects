def get_binary_digits(num):
  bn_nmbs=[]
  while num!=0:
    quot=num//2
    rem=num%2
    bn_nmbs.append(rem)
    num=quot
  return bn_nmbs

cards=[[] for i in range(6)]

for n in range(1,64):
  bn_dgts= get_binary_digits(n)
  for i in range(len(bn_dgts)):
      if bn_dgts[i]==1:
        cards[i].append(n)

for i in range(6):
  print("cards",cards[i])

def game():
  player_input= input("Think of a number between 1 and 63. Type 'start' when you are ready and hit the 'Enter' key.")
  while player_input != "start":
    player_input= input("Think of a number between 1 and 63. Type 'start' when you are ready and hit the 'Enter' key.")
  num=0
  valid_entries=["yes", "no"]
  if 2**0==1:
    for i in cards:
      print("card",i[0],i,": ")
      answer=input("If the number exists in the displayed set, type 'yes' and press enter otherwise type 'no'!")
      while answer not in valid_entries:
        print("yes or no?")
        answer=input("If the number exists in the displayed set, type 'yes' and press enter otherwise type 'no'!")
      if answer=="yes":
        num+=i[0]
        print("Hmm...Noted!")
      else:
        print("Hmm...Noted!")
  print("THE NUMBER YOU WERE THINKING OF WAS.............")
  print("IT WAS: ",num)
  replay= input("WANNA PLAY AGAIN??")
  while answer not in valid_entries:
        print("yes or no?")  
        replay= input("WANNA PLAY AGAIN OR NO??")
  if replay=="yes":
    game()#recursion
  else:
    print("Have a good day!! Thanks for playing!!")
    
game()