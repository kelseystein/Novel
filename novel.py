import random

# list of books is stored in the list -'books'
books = ['Jersey Mikes', 'Pizza Hut', 'Chipotle']

# An item from the list 'books' is selected
# by random.choice()
print(random.choice(books))

when = ['A few years ago ', 'Yesterday ', 'Last night ', 'A long time ago ', 'Many eaons ago ', 'Long long ago ','In a land far far away ']
who = ['a puppy ', 'an kitten ', 'a mouse ', 'a turtle ']
name = ['Kelsey ', 'Lauren ', 'Dakota ', 'Lux ','Pepper ','Arrow ','Chesnut ','Winston ','Leo ']
residence = ['Fredericksburg ', 'Virginia ', 'Herndon', 'Sterling ','Stafford ','Ohio ']
went = ['cinema ', 'university ', 'school ', 'laundry ','store ','classroom ','library ','festival ']
happened = ['made a lot of friends ', 'found a secret key ', 'solved a mystery ', 'wrote a book ',
'went to China ','took a nap ','followed them home ']
for x in range(5000):
  print( random.choice(when) + random.choice(who) + random.choice(residence) + random.choice(went) + random.choice(happened))
  
  
