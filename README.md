# Equatorial-Coordinates-to-Horizontal-Coordinates
A quick refresher on how to convert Equatorial Coordinates to local Horizontal Coordinates.

Step 1: Derive equations by writing down the sides of a triangle on a sphere, and the angles.
Draw the spheres. No really do it, it won't make sense if you don't get the hang of this bit. 

Remember: The sky rotates from East-West. So Hour Angle Zero is at zenith. Angles toward the East are negatives, Hour angles to the West are positive.

Step 2: Use the cosine rule to relate Elevation/Altitude to the sides (Declination, Latitude)

Step 3: Use the cosine rule to relate Azimuthal angle to the sides (Declination, Latitude)

Step 4: Then use the sine rule to relate Azimuthal angle to the sides
We do this because we need a third equation that gives us an expression for the Azimuthal angle only in terms of the Declination, Latitude and Hour Angle of your source.

Step 5: Divide second and third equation to get the tangent of the Azimuthal angle, i.e. to get rid of our earlier problem.

Step 6: Solve the issue with the domain of the arctangent(Azimuth).
Use the 2 argument tangent: https://en.wikipedia.org/wiki/Atan2

![Comparison Between numpy.arctan and numpy.arctan2 when converting Equatorial Coordinates to Horizontal Coordinates](https://github.com/ronniyjoseph/Equatorial-Coordinates-to-Horizontal-Coordinates/blob/master/comparing_arctan_arctan2.png)

