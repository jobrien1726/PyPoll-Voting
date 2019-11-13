import os
import csv

election_data = os.path.join("election_data.csv")

candidates = []
total_vote_count = 0

votes_khan = 0
votes_correy = 0
votes_li = 0
votes_otooley = 0

with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader:
        total_vote_count += 1

        #append candidate to candidates list only when new candidate found
        if row[2] not in candidates:
            candidates.append(row[2])

        if row[2] == "Khan":
            votes_khan += 1
        elif row[2] == "Correy":
            votes_correy += 1
        elif row[2] == "Li":
            votes_li += 1
        elif row[2] == "O'Tooley":
            votes_otooley += 1

percent_vote_khan = votes_khan / total_vote_count * 100
percent_vote_correy = votes_correy / total_vote_count * 100
percent_vote_li = votes_li / total_vote_count * 100
percent_vote_otooley = votes_otooley / total_vote_count * 100

vote_results_list = [votes_khan, votes_correy, votes_li, votes_otooley]

if vote_results_list[0] == max(vote_results_list):
    winner = candidates[0]
elif vote_results_list[1] == max(vote_results_list):
    winner = candidates[1]
elif vote_results_list[2] == max(vote_results_list):
    winner = candidates[2]
elif vote_results_list[3] == max(vote_results_list):
    winner = candidates[3]
    
print("Candidates Running for Election: " + str(candidates))
print("------------------------------------------")
print("Election Results")
print("------------------------------------------")
print("Total Votes: " + str(total_vote_count))
print("------------------------------------------")
print(candidates[0] + ":" + str(format(percent_vote_khan, '.3f')) + " % " + "(" + str(votes_khan) + ")")
print(candidates[1] + ":" + str(format(percent_vote_correy, '.3f')) + " % " + "(" + str(votes_correy) + ")")
print(candidates[2] + ":" + str(format(percent_vote_li, '.3f')) + " % " + "(" + str(votes_li) + ")")
print(candidates[3] + ":" + str(format(percent_vote_otooley, '.3f')) + " % " + "(" + str(votes_otooley) + ")")
print("------------------------------------------")
print("Winner: " + winner) 

#Export txt file with Election results
txt_file_path = os.path.join("pypoll.txt")

with open(txt_file_path, 'w') as pypoll:

    pypoll.write('Candidates Running for Election: ' + str(candidates) + '\n')
    pypoll.write('------------------------------------------------\n')
    pypoll.write('Election Results\n')
    pypoll.write('------------------------------------------------\n')
    pypoll.write('Total Votes: ' + str(total_vote_count) + '\n')
    pypoll.write('------------------------------------------------\n')
    pypoll.write(candidates[0] + ':' + str(format(percent_vote_khan, '.3f')) + ' % ' + '(' + str(votes_khan) + ')' + '\n')
    pypoll.write(candidates[1] + ':' + str(format(percent_vote_correy, '.3f')) + ' % ' + '(' + str(votes_correy) + ')' + '\n')
    pypoll.write(candidates[2] + ':' + str(format(percent_vote_li, '.3f')) + ' % ' + '(' + str(votes_li) + ')' + '\n')
    pypoll.write(candidates[3] + ':' + str(format(percent_vote_otooley, '.3f')) + ' % ' + '(' + str(votes_otooley) + ')' + '\n')
    pypoll.write('------------------------------------------------\n')
    pypoll.write('Winner: ' + winner + '\n')