days = 31
def multiply_days(utility):
  return utility * days
total = 0



#print(int (round(total, 1)),  "cents")

light_bulb_type = int(input("Do you have a 75 watt bulb or a 100 watt bulb? "))

light_bulb_amount = int(input("How many lightbulbs in the home? "))

if light_bulb_type == 75:
  lights_on = int(input("How many hours do you leave your lights on for? " ))
  #For a 75 watt bulb it costs 9 cents every hour they are on
  total += multiply_days(lights_on) * 0.09 * light_bulb_amount
elif light_bulb_type == 100:
  lights_on = int(input("How many hours do you leave your lights on for? "))
    #For a 100 watt bulb it costs 12 cents every hour they are on
  total += multiply_days(lights_on) * 0.12 * light_bulb_amount
else:
  0


stove_on = int(input("About how many hours per day do you use your stove for? "))
stove_type = str(input("Is the stove electric or gas? "))
if stove_type == "electric":
  total += multiply_days(stove_on) * 0.36
elif stove_type == "gas":
  total += multiply_days(stove_on) * 0.23
else:
  0
#electric: $0.36/hour; gas: $0.23/hour

fridge = 27.60
#fridge costs 92 cents/day or $27.60/month

#sink_hours = int(input("Around how many hours do you use the sink for per day? "))
#total += multiply_days(sink_hours) * 3.00
#Sinks don't use electricity

kitchen_usage = int(input("How many times a day do you use the microwave? "))
total += (multiply_days(kitchen_usage) * .15) + fridge


#117 dollars is about the average cost of an electric bill
if 110 < total < 140:
  print("You are spending about", round(total,2), "dollars which is around the average amount of money people spend on their electricity bill, to save money you could use use lower wattage or LED lightbulbs, turn off lights when not in use,  etc")
elif total < 110:
  print("You are being very energy efficient and as a reward are only spending", total, "dollars on your bill.")
else:
  print("According to our calculations, you are spending",
  round(total, 2), "dollars, which above the average cost of electricty per month, as well as using around 14,000 kwh of energy per year. If you incorporate methods such as turning the lights off when not using them, switching to a gas stove, not leaving the fridge open for an extended period of time, and switching to 75 watt bulbs, you would reduce annual electric emissions by a large amount, while also saving hundreds on your electricity bill annually.")
""""
Alternatively for the second one we could write that according to our calculations, you are spending both above the average cost of electricty per month, as well as using around 11,200 kwh of energy per year. If you incorporate methods such as turning the lights off when not using them, switching to a gas stove, not leaving the fridge open for an extended period of time you would reduce annual electric emissions by a large amount, while also saving hundreds on your electricity bill annually.
"""
