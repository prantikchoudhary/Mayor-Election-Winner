from EDL import total_votes
import matplotlib.pyplot as plt

total_votes.plot.bar()
plt.ylabel('Total Votes')
plt.xlabel('Candidate Name')
plt.title('Mayor Election Winner ')

