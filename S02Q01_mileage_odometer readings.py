OOD = float(input("Please enter the original odometer reading"))

NOD = float(input("Please enter the new odometer reading")) 

GallonsofGasUsed = float(input("Please enter the gallons og gas used"))

MilesPerGallon = NOD-OOD/GallonsofGasUsed

print( "The car's miles-per-gallon is" + str(MilesPerGallon) + "miles/gallon" )
