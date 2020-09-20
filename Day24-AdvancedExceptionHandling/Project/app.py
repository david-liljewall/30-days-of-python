
#* ----------------------------- Creating a Parser ---------------------------- #
import argparse

parser = argparse.ArgumentParser( description="Returns a number raised to a specified power" )

parser.add_argument( "base", type=float, help="A number to raise to the specified power" )
parser.add_argument( 
    "-e", 
    "--exponent",
    type=float,
    default=2, 
    help="A power to raise the provided base to"
)
    # NOTE: The "-e" is a secondary name for "--exponent" that we can use in the program arguments

args = parser.parse_args()

# Print base ** exponent
print( args.base ** args.exponent )