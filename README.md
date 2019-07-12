# Equatorial-Coordinates-to-Horizontal-Coordinates
A quick refresher on how to convert astronomical coordinate systems

#Derive equations by writing down the sides of a triangle on a sphere, and the angles.

#Use the cosine rule to relate Elevation/Altitude to the sides

#Then use the cosine rule to relate Azimuthal angle to the sides

#Then use the sine rule to relate Azimuthal angle to the sides

#Divide second and third to get the tangent, i.e. to make Azimuth independent of Elevation.

#Now you have to solve the issue with the domain of the arctangent(Azimuth)

#Use the 2 argument tangent: https://en.wikipedia.org/wiki/Atan2

![Comparison Between numpy.arctan and numpy.arctan2 when converting Equatorial Coordinates to Horizontal Coordinates](https://github.com/ronniyjoseph/Equatorial-Coordinates-to-Horizontal-Coordinates/blob/master/comparing_arctan_arctan2.png)

