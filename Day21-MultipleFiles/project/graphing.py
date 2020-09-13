from matplotlib import pyplot


def create_chart( x, y, filename ):
    ## Creates a new figure when called, plots x versus y, and allows user to name output .png file
    
    fig = pyplot.figure()
    pyplot.scatter( x, y, alpha=0.5)
    fig.savefig( f"{filename}.png" )
