import plotly.graph_objects as go


def _code_mapping(df, src, targ):
    """
    Maps labels / strings in src and target and converts them to integers 0, 1, 2, 3...

    Parameters:
        df : data frame containing artist data that is sorted to put into sankey creation function
        src : string containing name of the source column of the sankey diagram
        targ : string containing name of the target column of the sankey diagram

    Return:
        df : df containing codes sorted in for the original artist values
        labels : list of distinct labels for the data
    """

    # extract distinct labels
    labels = list(set(list(df[src]) + list(df[targ])))

    # define integer codes
    codes = list(range(len(labels)))

    # pair labels with list
    lc_map = dict(zip(labels, codes))

    # in df, substitute codes for labels
    df = df.replace({src: lc_map, targ: lc_map})

    return df, labels


def make_sankey(df, src, targ, vals=None, **kwargs):
    """
    Generate Sankey Diagram

    Parameters:
        df : data frame containing artist data that is sorted to put into sankey creation function
        src : string containing name of the source column of the sankey diagram
        targ : string containing name of the target column of the sankey diagram
        vals : string containing name of the values column of the sankey diagram

    Returns:
        None
    """

    # map labels and strings together
    df, labels = _code_mapping(df, src, targ)

    # checks if values exists and fills with a set of ones if not
    if vals:
        values = df[vals]
    else:
        values = [1] * len(df[src])

    # sets up kwargs for input
    pad = kwargs.get('pad', 50)
    thickness = kwargs.get('thickness', 30)
    line_color = kwargs.get('line_color', 'black')
    line_width = kwargs.get('line_width', 1)

    # creates the links between the source and target columns with the corresponding value and formats nodes
    link = {'source': df[src], 'target': df[targ], 'value': values}
    node = {'label': labels, 'pad': pad, 'thickness': thickness, 'line': {'color': line_color, 'width': line_width}}

    # uses plotly to create sankey diagram using the link and nodes
    sk = go.Sankey(link=link, node=node)
    fig = go.Figure(sk)
    fig.show()
