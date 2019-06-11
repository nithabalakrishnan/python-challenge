import csv
import os

def readingPolling():
    # file paths
    PyPollcsvPath=os.path.join('Resources','election_data.csv')
    PyPollOutputPath=os.path.join('Resources','Results.txt')
    # read csv file
    with open(PyPollcsvPath, mode='r') as csvfile:
        pyPollReader = csv.reader(csvfile, delimiter=",")
        next(pyPollReader) # Skip header

        #variable declaration
        totalVotes = 0
        candidateVotes = {}

        for row in  pyPollReader:
            candidate = row[2]
            if candidate in candidateVotes:
                candidateVotes[candidate] = int(candidateVotes[candidate]) + 1
            else:
                candidateVotes[candidate] = 1
            totalVotes += 1

        #Output file under resources
        f = open(PyPollOutputPath, "w+")
        f.write("Election Results\n")
        f.write("-------------------------\n")
        f.write("Total Votes: " + str(totalVotes) + "\n")
        f.write("-------------------------\n")

        #Print header details
        print("Election Results")
        print("-------------------------")
        print("Total Votes: " + str(totalVotes))
        print("-------------------------")
        winner = ""
        popularVote = -1

        for vote in candidateVotes.items():
            candidate = vote[0]
            candidateTotalVote = float(vote[1])
            if candidateTotalVote > popularVote:
                popularVote = candidateTotalVote
                winner = candidate
            percent = (candidateTotalVote / totalVotes) * 100
            # Print Candidate vote stats
            print(candidate + ": " + "{0:.3f}%".format(percent) + " (" + "{0:.0f}".format(candidateTotalVote) + ")")
            f.write(candidate + ": " + "{0:.3f}%".format(percent) + " (" + "{0:.0f}".format(candidateTotalVote) + ")" + "\n")

        #Print Winner
        f.write("-------------------------\n")
        f.write("Winner: " + winner + "\n")
        f.write("-------------------------\n")

        print("-------------------------")
        print("Winner: " + winner)
        print("-------------------------")
        f.close() 

readingPolling()