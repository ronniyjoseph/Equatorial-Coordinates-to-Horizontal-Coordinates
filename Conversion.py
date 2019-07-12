import numpy
from matplotlib import pyplot

def from_celestial_to_horizontal(HA, dec, L):
    E = numpy.arcsin(numpy.sin(dec)*numpy.sin(L) + numpy.cos(dec)*numpy.cos(HA)*numpy.cos(L))
    A = numpy.arcsin(numpy.cos(dec)*numpy.sin(HA)/numpy.cos(E))
    #A = numpy.arccos((numpy.sin(E)*numpy.sin(L) - numpy.sin(dec)/(numpy.cos(E)*numpy.cos(L))))
    return E, A

latitude = numpy.deg2rad(-26.5)
source_dec = numpy.deg2rad(-80)
hour_angles = numpy.linspace(0, 24, 24)

elevation, azimuth = from_celestial_to_horizontal(hour_angles/24*2*numpy.pi, source_dec, latitude)

print(elevation)
print(numpy.deg2rad(azimuth))

fig = pyplot.figure(figsize=(15,5))
axes1= fig.add_subplot(131, polar = True)
axes2= fig.add_subplot(132)
axes3= fig.add_subplot(133)

axes1.scatter(azimuth, numpy.pi/2 - elevation)
axes1.set_theta_zero_location('S')

axes2.scatter(hour_angles, elevation)
axes3.scatter(hour_angles, azimuth)

pyplot.show()