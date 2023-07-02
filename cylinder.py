import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    import numpy as np
    # import matplotlib.pyplot as plt

    # Parameters for the circles
    # radii = [1, 2.5, 5.5, 8, 9.5]  # Radii of circles
    # colors = ['red', 'green', 'blue', 'orange', 'purple']  # Colors of circles

    # Create figure and axis
    # fig, ax = plt.subplots()
    #
    # Plot the circles
    # for radius,color in zip(radii,colors):
    #     circle = plt.Circle((0, 0), radius, color='blue', fill=False)
    #     ax.add_artist(circle)

    # Set plot limits
    # max_radius = max(radii)
    # ax.set_xlim(-max_radius - 1, max_radius + 1)
    # ax.set_ylim(-max_radius - 1, max_radius + 1)

    # Set plot labels and title
    # ax.set_xlabel('X')
    # ax.set_ylabel('Y')
    # ax.set_title('Circles with Different Radii')

    # Show the plot
    # plt.show()
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm

    # Parameters for the circles
    radii = [1.0, 1.5, 2.0, 2.5, 3.0]  # Radii of circles

    # Generate a colormap
    colormap = cm.get_cmap('viridis')
    colors = [colormap(i) for i in np.linspace(0, 1, len(radii))]

    # Create figure and axis
    fig, ax = plt.subplots()

    # Plot the circles
    for radius, color in zip(radii, colors):
        circle = plt.Circle((0, 0), radius, color=color, alpha=0.5)
        ax.add_artist(circle)

    # Set plot limits
    max_radius = max(radii)
    ax.set_xlim(-max_radius - 1, max_radius + 1)
    ax.set_ylim(-max_radius - 1, max_radius + 1)

    # Set plot labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Circles with Different Radii and Colors')

    # Show the plot
    plt.show()




