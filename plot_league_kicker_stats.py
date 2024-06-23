import pandas as pd
import matplotlib.pyplot as plt

def plot_total_points(players, total_fg_points):
    """
    Create a scatter plot for total points by kickers.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(players, total_fg_points, color='blue', alpha=0.5)
    plt.xlabel('Player')
    plt.ylabel('Total FG Points')
    plt.title('Scatter Plot of Total FG Points by Player')
    plt.xticks(rotation=90)
      # Calculate the mean of total FG points
    mean_total_fg_points = sum(total_fg_points)/len(total_fg_points)

    # Plot the middle line
    plt.axline((0,mean_total_fg_points),slope=0 , color='red', linestyle='--', label='Mean FG Points')

    plt.grid(True)
    plt.tight_layout()
    plt.show()

      

def main():
    # Player names and their corresponding total FG points
    players = [
        "Jason Myers", "Matt Gay", "Brandon Aubrey", "Cairo Santos", "Greg Zuerlein",
        "Justin Tucker", "Blake Grupe", "Brandon McManus", "Younghoe Koo", "Dustin Hopkins",
        "Harrison Butker", "Wil Lutz", "Anders Carlson", "Cameron Dicker", "Matt Prater",
        "Jake Elliott", "Evan McPherson", "Chase McLaughlin", "Chris Boswell", "Greg Joseph",
        "Daniel Carlson", "Nick Folk", "Tyler Bass", "Eddy Pineiro", "Jason Sanders",
        "Ka'imi Fairbairn", "Jake Moody", "Chad Ryland", "Joey Slye"
    ]

    total_fg_points = [
        105, 99, 108, 105, 105, 96, 90, 90, 96, 99, 99, 90, 81, 93, 84, 90,
        78, 87, 87, 72, 78, 87, 72, 75, 72, 81, 63, 48, 57, 48
    ]

    # Plot total points scatter plot
    plot_total_points(players, total_fg_points)

if __name__ == "__main__":
    main()
