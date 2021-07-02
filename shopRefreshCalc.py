import pandas as pd
from datetime import date

df = pd.read_excel(r'notes/shopRefreshCalc.xlsx', sheet_name='data', index_col=None)
print (df)

# constants
refresh_cost = 3
refreshes = 333
SS_cost = refresh_cost * refreshes
BM_cost = 184000
MM_cost = 280000

action = input("What do you want to do? 'state' or 'count'?")

if action.lower() == 'stat' or action.lower() == 'stats':
	mean = list(df.mean())
	total_cost = mean[1] * BM_cost + mean[2] * MM_cost

	print(f'''
	      per {refreshes} refreshes (999) Skystones, you received on average:
	      Bookmarks	: {mean[1]}
	      Mystics	: {mean[2]}
	      _____________________
	      per {refreshes} refreshes, they cost on average:
	      Skystones cost	: {SS_cost} Skystones
	      Bookmarks cost	: {mean[1] * BM_cost} Gold
	      Mystics cost	: {mean[2] * MM_cost} Gold
	      Total Gold cost : {total_cost} Gold
	      _____________________
	      Thus, the shop refresh rate are:
	      1 Bookmark : {SS_cost / mean[1]} Skystone
	      1 Mystic : {total_cost / mean[2]} Gold
	      ''')

elif action.lower() == 'count':
	while True:
		count = True

		BM = 0
		MM = 0
		SS = int(input("What's the starting SS? "))
		target = SS - 999

		print(f"Starting SS is: {SS}. \nTarget SS is: {target}. Counting now...")

		while count:
			inp = input("What did u get? \n")

			if inp.lower() == "stop":
				count = False
				SS = target
				today = date.today().strftime("%d/%m/%Y")

				# update excel's df
				df = df.append({'Date': today, 'SS': SS, 'BM': BM, 'MM': MM}, ignore_index=True)
				print(f"Finished counting. \nBM = {BM}, MM = {MM}, SS = {SS}. \n{df}")
				df.to_excel(r'notes/shopRefreshCalc.xlsx', sheet_name='data', index=False)

			elif inp.lower() == "b":
				BM += 1
				print(f"BM = {BM}. target: {target}.")

			elif inp.lower() == "m":
				MM += 1
				print(f"MM = {MM}. target: {target}.")

			else:
				print("Unrecognized input. Please enter: 'b', 'm', or 'stop' only.")
				continue

else: print("Unrecognized input. Please enter: 'stats' or count' only.")
