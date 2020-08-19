#%%
#The Data we need to retrieve
# 1. the total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. the percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


# %%
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. initalize total votes
total_votes = 0
county_votes_temp = 0
county_votes_total = []

#candidate options
candidate_options = []

#counties lists
counties_options = []
counties_name =[]

#largest county turnout varriable
largestcounty = ""
tempnumberofvotes = 0

# declare empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#county dictionary
votesbycounty = {}



# Open the election results and read the file.
with open(file_to_load) as election_data:

    # to do read and analyze
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
     # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #add to the total vote count
        total_votes += 1

        #print the candidate name from each row
        candidate_name= row[2]

        counties_name= row[1]


        #if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # 2 being tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #if the counties name does not match any existing county
        if counties_name not in counties_options:
            # add the candidate name to the candidate list
            counties_options.append(counties_name)

        if votesbycounty.get(counties_name)==None:
            votesbycounty[counties_name] = 1
        else:
            votesbycounty[counties_name] +=1

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
#determine the largest county
for countyname in votesbycounty:
    if votesbycounty.get(countyname) > tempnumberofvotes:
        tempnumberofvotes = votesbycounty.get(countyname)
        largestcounty = countyname


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #county votes output and writing to txt file
    countyvotes_header = (
        f"\nCounty Votes:\n"
        
    )
    #printing county votes header
    print(countyvotes_header)
    txt_file.write(countyvotes_header)

    for countyname in votesbycounty:
        #calculate county vote percentage
        countyvote_percentage = float(votesbycounty.get(countyname))/float(total_votes) * 100
        countyvotes_results=(
            f"{countyname}: {countyvote_percentage:.1f}% ({votesbycounty.get(countyname):,})\n"
        )
        #printing county votes results
        print(countyvotes_results)
        #writing county votes results to txt file
        txt_file.write(countyvotes_results)
    
    #largest county output/writing
    largestcounty_output = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largestcounty} \n"
        f"-------------------------\n"  
    )

    print(largestcounty_output)
    txt_file.write(largestcounty_output)

    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)




# %%
