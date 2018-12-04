#!/usr/bin/env python3
message = 'Your connection speed\'s rating is '
print('What is your connection speed in Mbps?')
connection = int(input())
if connection >= 150:
	message = message + 'A+.'
elif connection >= 100:
	message = message + 'A.'
elif connection >= 75:
	message = message + 'B.'
elif connection >= 50:
	message = message + 'C.'
else:
	message = message + 'Terribad!! Get better internets n00b!'
print(message)
