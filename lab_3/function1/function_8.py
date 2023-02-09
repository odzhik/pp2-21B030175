#Write a function that takes in a list of integers and returns True if it contains 007 in order

"""def spy_game(nums):
    pass
spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False"""

def find_007(a):
  for i in range(len(a)):
    if a[i] == 0 and a[i+1] == 0 and a[i+2] == 7:
      return True
  return False

a= [int(x) for x in input().split()]
print(find_007(a))