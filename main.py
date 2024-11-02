import os
import pandas


def main():
    """ Read data about squirrels from a CSV using pandas library, parse the data
    to identify the number of grey, red and black colored squirells, and write the
    squirrel count to a CSV file.  """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, "Squirrel_Data.csv")
    data = pandas.read_csv(filepath)
    gray_sq_count = len(data[data["Primary Fur Color"] == "Gray"])
    red_sq_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
    black_sq_count = len(data[data["Primary Fur Color"] == "Black"])

    squirrel_colors = {
        "Fur Color": ["grey", "red", "black"],
        "Count": [gray_sq_count, red_sq_count, black_sq_count],
    }

    data_frame = pandas.DataFrame(squirrel_colors)
    filepath = os.path.join(current_dir, "color_count.csv")
    data_frame.to_csv(filepath)


if __name__ == "__main__":
    main()
