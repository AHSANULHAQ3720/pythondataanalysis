# Import both matplotlib.pyplot and seaborn using the aliases plt and sns, respectively.
# Complete the arguments of sns.barplot:
# The first argument should be the list of labels to appear on the x-axis (created in the previous step).
# The second argument should be a list of the variables you wish to plot, as produced in the previous exercise (i.e. a list containing clinton, trump, etc).

# Import packages
import matplotlib.pyplot as plt
import seaborn as sns


# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

word_in_text = [clinton,trump,sanders,cruz]

# Plot the bar chart
ax = sns.barplot(cd, word_in_text)
ax.set(ylabel="count")
plt.show()