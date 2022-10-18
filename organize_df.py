import pandas as pd

# taken from StackOverflow to remove a recurring unnecessary warning
pd.options.mode.chained_assignment = None  # default='warn'


def organize_df(df):
    """
    Organize data frame according to required parameters

    Parameters:
        df : data frame containing artist data to sort into a sankey ready data frame

    Returns:
        df : sorted data frame with nationality, gender, and decade born
    """
    # select only the three columns of note
    df = df[["Nationality", "Gender", "ArtistBio"]]

    # gather a decade born column by getting the year born, converting it to int, and rounding down
    df['Decade_Born'] = df['ArtistBio'].str.extract("[ ](\d+)")
    df = df.dropna().astype({'Decade_Born': 'int'})
    df['Decade_Born'] = df['Decade_Born'].apply(lambda x: x // 10 * 10)

    # drop ArtistBio column
    df = df.drop(['ArtistBio'], axis=1)

    # remove rows where decade is 0
    df = df[df.Decade_Born != 0]

    return df


def aggregate_data(df, src, targ, threshold):
    """
    Aggregate data into df with the source and target combinations and their counts

    Parameters:
        df : data frame containing artist data to sort into a sankey ready data frame
        src : string containing name of the source column of the sankey diagram
        targ : string containing name of the target column of the sankey diagram
        threshold : the filter by which to limit the sankey diagram

    Returns:
        df : data frame containing artist data that is sorted to put into sankey creation function
    """
    # organize the data
    df = organize_df(df)

    # aggregate data
    df = df.groupby([src, targ]).size().reset_index(name='Count')

    # filter out
    df = df[df.Count > threshold]

    return df
