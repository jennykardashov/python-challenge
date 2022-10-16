from ast import Not
import os
import csv

candidates = {}

total_votes = 0

# Define path
csvpath = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read header row 
    csv_header = next(csvfile)

    #Read through rows
    for row in csvreader:
        # The total number of months included in the dataset
        total_votes += 1

        if candidates.get(row[2]) is None:
            #adding new
            candidates[row[2]] = 1
        else:
            #incrementing count
            candidates[row[2]] = candidates.get(row[2]) + 1

# print(candidates)
output = """   Election Results
   -------------------------
   Total Votes: %s
   -------------------------
""" % (total_votes)

mostVotes = 0
votesWinner = ""

for k, v in candidates.items():
    if(v > mostVotes):
        mostVotes = v
        votesWinner = k
    output += "   " + k + ": " + "{0:.3f}%".format((v/total_votes) * 100) + " ({})\n".format(v) 

output = output[:-1]

output += """
   -------------------------
   Winner: %s
   -------------------------
""" % (votesWinner)

print(output)

f = open("Analysis/poll_output.txt", "w")
f.write(output)
f.close()
