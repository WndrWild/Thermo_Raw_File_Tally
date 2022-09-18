### Python script for generation of Xcaliber run list - ver 1.0
import os
import pandas as pd
from datetime import date
import datetime

# Create empty dataframe
rawTally = pd.DataFrame(columns = ["File Name", "Path", "Date", "Size"])

# Request location
path = input("Enter location to search for '.raw' files: ")

instrument = input("Enter Instrument Name: ")

# Get current date, ISO format
today = date.today()
stamp = today.strftime("%Y%m%d")


# raw_count = 0


# Walk through folders to find files
for (root, dirs, files) in os.walk(path):
	for file in files:
		if file.endswith(".raw"):
			
			# get entire path
			location1 = os.path.join(root,file)
			
			# get location of file
			location2 = os.path.join(root)
			
			# get raw file name
			file_name = file
			print(file_name)
			# raw_count = raw_count + 1
			
			# get creation date of raw file
			creation = os.path.getctime(location1)
			date_created = datetime.datetime.fromtimestamp(int(creation)).strftime("%Y-%m-%d %H:%M:%S")
			
			# get size of raw file (in bytes)
			file_size = os.path.getsize(location1)
			rawTally = rawTally.append({"File Name": file_name, "Path": location2, "Date": date_created, "Size (bytes)": file_size}, ignore_index = True)



# # summarize number of raw files found
# print("\nNumber of raw files found: " + str(raw_count))
# time.sleep(5)


# Export runlist to csv file for instrument & formated for Xcaliber
with open(instrument + "_RawFileTally_" + stamp + ".csv", "w") as fp:
	rawTally.to_csv(fp, index = False, line_terminator = "\n")