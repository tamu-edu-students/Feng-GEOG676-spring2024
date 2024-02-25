import arcpy

#set environment workspace
arcpy.env.workspace = r"F:/GEOG676/DevSource/Feng-GEOG676-spring2024/Lab_4/Workspace"
path_gdb = str(arcpy.CreateFileGDB_management(arcpy.env.workspace, "lab_4.gdb"))

#get buffer distance  from user
bufferDis = input("Please enter the intend buffer distance (in meters): ") + " Meters"

#add in data layers

#add garages layer
garages_o = arcpy.MakeXYEventLayer_management("Lab_4/Inputs/garages.csv", "x", "y", "GAR_pt_o")
arcpy.FeatureClassToGeodatabase_conversion(garages_o, path_gdb)
layer_GAR_pt_o = path_gdb + "/GAR_pt_o"

#add buildings layer
layer_BLDG_o = "Lab_4/Inputs/Campus.gdb" + "/Structures"
layer_BLDG = path_gdb + "/BLDG_ply"
arcpy.Copy_management(layer_BLDG_o, layer_BLDG)

#re-project
ref_Spatial = arcpy.Describe(layer_BLDG).spatialReference
layer_GAR = path_gdb + "/GAR_pt"
arcpy.Project_management(layer_GAR_pt_o, layer_GAR, ref_Spatial)

#buffer garages
name_GAR_buffered = "/GAR_buf" + bufferDis.split(" ")[0].replace(".","_")
layer_GAR_buffered = arcpy.Buffer_analysis(layer_GAR, path_gdb + name_GAR_buffered, bufferDis)

#intersect buffered garages with buildings
arcpy.Intersect_analysis([layer_GAR_buffered, layer_BLDG], path_gdb + "/GAR_BLDG_int", "ALL")

#output to table
arcpy.TableToTable_conversion(path_gdb + "/GAR_BLDG_int.dbf", "Lab_4/Outputs", "nearbyBuildings.csv")