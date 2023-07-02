if __name__=="__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    # Parameters for the circles
    radii = [1.0, 2.0, 3.0,4.0]  # Radii of circles

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(7.16, 8.8))

    # Plot the circles
    for radius in radii:
        circle = plt.Circle((0, 0), radius, fill=False)
        ax.add_artist(circle)

    # Set plot limits
    max_radius = max(radii)
    ax.set_xlim(-max_radius - 1, max_radius + 1)
    ax.set_ylim(-max_radius - 1, max_radius + 1)
    ax.axis('off')



    # Show the plot
    plt.show()
