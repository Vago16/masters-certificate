#This function computes the volume of a pyramid with a sqare base.
#Calculate the volume of the Great Pyramid with a heigh of 146 meters base length of 55000 meters.
# @param height a float indicating height of the pyramid
# @param baseLength a float indicating length of one side of the pyramid


def pyramidVolume(height,baselength):
    baseArea = baselength * baselength
    return height * baseArea / 3        #returns volume

#call the function
print ('Volume: {0:,.2f}'.format(pyramidVolume(146, 550000)))