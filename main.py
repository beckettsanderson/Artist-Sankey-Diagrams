import pandas as pd
import sankey as sk
import organize_df as org


def main():
    # read in the json file
    df = pd.read_json("Artists.json")

    # aggregate data and create sankey based off nationality and decade born
    df1 = org.aggregate_data(df, 'Nationality', 'Decade_Born', 30)
    sk.make_sankey(df1, 'Nationality', 'Decade_Born', 'Count')

    # aggregate data and create sankey based off nationality and gender
    df2 = org.aggregate_data(df, 'Nationality', 'Gender', 50)
    sk.make_sankey(df2, 'Nationality', 'Gender', 'Count')

    # aggregate data and create sankey based off gender and decade born
    df3 = org.aggregate_data(df, 'Gender', 'Decade_Born', 20)
    sk.make_sankey(df3, 'Gender', 'Decade_Born', 'Count')


main()
