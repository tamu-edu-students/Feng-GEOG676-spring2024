import arcpy

inputs = r"Lab_7/Inputs/"
outputs = r"Lab_7/Outputs/"

#Composite
band1 = arcpy.sa.Raster(inputs + "Band1.TIF") # blue
band2 = arcpy.sa.Raster(inputs + "Band2.TIF") # green
band3 = arcpy.sa.Raster(inputs + "Band3.TIF") # red
band4 = arcpy.sa.Raster(inputs + "Band4.TIF") # NIR

composite = arcpy.CompositeBands_management([band1, band2, band3, band4], outputs + "combined.tif")

#Hillshade
azimuth = 315
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1

arcpy.ddd.HillShade(inputs + "dem.tif", outputs + "hillshade.tif", azimuth, altitude, shadows, z_factor)

#Slope
output_measurement = "DEGREE"
z_factor = 1
method = "PLANAR"

arcpy.ddd.Slope(inputs + "dem.tif", outputs + "slope.tif",output_measurement, z_factor, method)

