# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
# tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

starttime=(6*60+52)*60
easypace=(8*60+15)*2
tempo=(7*60+12)
breakfasthour = (starttime + easypace + tempo)/(60*60)
breakfastinthour = int(breakfasthour)
breakfastminute  = (breakfasthour - breakfastinthour)*60 #minutes in double format
breakfastintminute = int(breakfastminute) #minutes in int format

print('Breakfast is at {}.{}'.format(breakfastinthour,breakfastintminute))