### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
  # There is no __init__ defined, to state what the class' attributes are

  def check_for_ace(self, card):
    if card.value = 1: #for comparisons, '==' is required, not '='
      return True
    else #should have a colon at the end of this line
      return False
   

  dif highest_card(self, card1 card2): #typo for word 'def' and missing comma between 'card1' and 'card2'
  if card1.value > card2.value: #this line should be further indented - each line below within this method would also need this change
    return card # typo for 'card1'
  else:
    return card2
  

# This definition is not properly indented in order to use self - whole block should be indented another indentation unit
def cards_total(self, cards):
  total #this line does not properly define the variable. should use 'total = 0'
  for card in cards:
    total += card.value
    return "You have a total of" + total #this line does not properly use string interpolation and is indented incorrectly - should be one less indentation unit
  
```
