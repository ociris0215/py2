import matplotlib.pyplot as plt


def draw(x,y,title,xtext,ytext):
# Create a figure and an axis
    fig, ax = plt.subplots()

# Plot the data
    ax.plot(x, y)

# Add a title and labels
    ax.set_title(title)
    ax.set_xlabel(xtext)
    ax.set_ylabel(ytext)

# Show the plot
    plt.show()
