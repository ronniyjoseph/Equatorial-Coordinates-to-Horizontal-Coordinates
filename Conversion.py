import numpy
from matplotlib import pyplot

def from_celestial_to_horizontal(HA, dec, L):
    #Derive equations by writing down the sides of a triangle on a sphere, and the angles.
    #Use the cosine rule to relate Elevation/Altitude to the sides
    #Then use the cosine rule to relate Azimuthal angle to the sides
    #Then use the sine rule to relate Azimuthal angle to the sides
    #Divide second and third to get the tangent, i.e. to make Azimuth independent of Elevation.
    #Now you have to solve the issue with the domain of the arctangent(Azimuth)
    #Use the 2 argument tanget: https://en.wikipedia.org/wiki/Atan2


    E = numpy.arcsin(numpy.sin(dec)*numpy.sin(L) + numpy.cos(dec)*numpy.cos(HA)*numpy.cos(L))
    #Use standard arctangent
    A1 = numpy.arctan(numpy.sin(HA)/(numpy.cos(HA)*numpy.sin(L) - numpy.tan(dec)*numpy.cos(L)))
    #use 2 argumented arctangent to account for the quadrants
    A2 = numpy.arctan2(numpy.sin(HA), numpy.cos(HA)*numpy.sin(L) - numpy.tan(dec)*numpy.cos(L))

    return E, A1, A2

latitude = numpy.deg2rad(-26.5)
source_dec = numpy.deg2rad(-10)
hour_angles = numpy.linspace(-12, 12, 24)

elevation, azimuth, azimuth2 = from_celestial_to_horizontal(hour_angles/24*2*numpy.pi, source_dec, latitude)

print(elevation)
print(numpy.deg2rad(azimuth))

fig = pyplot.figure(figsize=(20,5))
axes1= fig.add_subplot(131, polar = True)
axes2= fig.add_subplot(132)
axes3= fig.add_subplot(133)

axes1.scatter(azimuth, numpy.pi/2 - elevation, c='b', label = "arctan(x/y)", alpha = 0.4)
axes1.scatter(azimuth2, numpy.pi/2 - elevation, c= 'r', label = "arctan2(x,y)",  alpha = 0.4)
axes1.set_theta_zero_location('S')

axes2.scatter(hour_angles, elevation, c='k')
axes3.scatter(hour_angles, azimuth, c='b', label = "arctan(x/y)",  alpha = 0.4)
axes3.scatter(hour_angles, azimuth2, c='r', label = "arctan2(x,y)",  alpha = 0.4)

axes2.set_xlabel("Hour Angle", fontsize = 15)
axes3.set_xlabel("Hour Angle", fontsize = 15)

axes2.set_ylabel("Elevation", fontsize = 15)
axes3.set_ylabel("Azimuth", fontsize = 15)


pyplot.legend()
pyplot.savefig("comparing_arctan_arctan2.png")

pyplot.show()