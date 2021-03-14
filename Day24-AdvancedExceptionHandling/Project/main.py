# ---------------------------------------------------------------------------- #
#*                                DAY 24 PROJECT                                #
# ---------------------------------------------------------------------------- #



# ----------------------- Parser for Dice Roll Program ----------------------- #
import argparse

## Create parser
parser = argparse.ArgumentParser( description="Rolls N dice and returns the number rolled, sum of the values, and the average of the rolls" )


# Number of dice
parser.add_argument(
    "base",
    type=int,
    help="Defines number of dice you want to roll"
)
# Sides on each die
parser.add_argument( 
    "-d",
    "--sides", 
    type=int,
    default=6, 
    help="Defines number of sides for each die. Default=6"
)
# Logging of rolls
parser.add_argument(
    "-l",
    "--log",
    type=str,
    help="Logs history of rolls to file name specified after --log argument"
)
# Consecutive rolling of dice in single terminal command
parser.add_argument(
    "-r",
    "--repeat",
    type=int,
    help="Specifies how many times to roll the dice consecutively"
)

# Parse arguments
args = parser.parse_args()


# Print relevant information
print( f"<< Number of Die = {args.base}, Number of Sides = {args.sides} >>\n" )




# --------------------------- Dice Roll Simulation --------------------------- #
import random


def roll_dice( n_dice, n_sides ):
    rolls = []
    for die in range( n_dice ):
        rolls.append( random.randint( 1, n_sides ) )
    
    # Calculate roll statistics
    total = sum( rolls )
    average = total / n_dice
    
    # Convert rolls list into a readable string 
    rolls = ", ".join( str( roll ) for roll in rolls )

    # Print formatted output to terminal
    output_string = f'''Roll Statistics:
        Rolls: {rolls}
        Total: {total}
        Average: {round( average, 2)}
    '''
    print( output_string )
    
    return output_string # to be logged into roll_log.txt
    
    
    
def create_logfile( filename ):
    with open( f"./{filename}", mode="w" ) as log_file:
        # Don't write anything yet, just create file
        pass


def append_logfile( filename, append_string ):
    with open( f"./{filename}", mode="a" ) as log_file:
        log_file.write( f"{append_string}\n" )



def roll_handler():
    # Retrieve formatted output string from roll_dice()
    
    
    # If user provides a log file name, write to that file. Otherwise, write to roll_log.txt
    if args.repeat:
        if args.log:
            create_logfile( args.log )
            for n in range( args.repeat ):
                roll_log = roll_dice( args.base, args.sides )
                append_logfile( args.log, roll_log)
        else:
            for n in range( args.repeat ):
                roll_log = roll_dice( args.base, args.sides )
                append_logfile( "roll_log.txt", roll_log)
    else:
        if args.log:
            roll_log = roll_dice( args.base, args.sides )
            create_logfile( args.log )
            append_logfile( args.log, roll_log )
        else:
            roll_log = roll_dice( args.base, args.sides )
            append_logfile( "roll_log.txt", roll_log )
        

# ------------------------------- Main Program ------------------------------- #
if __name__ == "__main__":
    roll_handler()
