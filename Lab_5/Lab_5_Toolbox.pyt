# -*- coding: utf-8 -*-

import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [GAR_BLDG_Intersection]


class GAR_BLDG_Intersection(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Lab_5_Toolbox"
        self.description = "determine which buildings on campus intersected with a buffer of the garage's centroid locations"
        self.canRunInBackground = False
        self.category = "Building Tools"

    def getParameterInfo(self):
        """Define parameter definitions"""
        params0 = arcpy.Parameter(
            displayName = "Geodatabase",
            name = "path_gdb",
            datatype = "DEWorkspace",
            parameterType = "Required",
            direction="Input"
        )
        params1 = arcpy.Parameter(
            displayName = "Garage Layer",
            name = "layer_GAR_Name",
            datatype = "DEFeatureClass",
            parameterType = "Required",
            direction="Input"
        )
        params2 = arcpy.Parameter(
            displayName = "Building Layer",
            name = "layer_BLDG_Name",
            datatype = "DEFeatureClass",
            parameterType = "Required",
            direction="Input"
        )
        params3 = arcpy.Parameter(
            displayName = "Buffer Distance (in meters)",
            name = "bufferDis_input",
            datatype = "GPDouble",
            parameterType = "Required",
            direction="Input"
        )
        params4 = arcpy.Parameter(
            displayName = "Output Path",
            name = "path_output",
            datatype = "DEFolder",
            parameterType = "Required",
            direction="Input"
        )
        params = [params0, params1, params2, params3, params4]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        #Setup input variables
        path_gdb = parameters[0].valueAsText
        layer_GAR = parameters[1].valueAsText
        layer_BLDG = parameters[2].valueAsText
        bufferDis = parameters[3].valueAsText + " Meters"
        path_output = parameters[4].valueAsText


        #buffer garages
        name_GAR_buffered = "/GAR_buf" + bufferDis.split(" ")[0].replace(".","_")
        layer_GAR_buffered = arcpy.Buffer_analysis(layer_GAR, path_gdb + name_GAR_buffered, bufferDis)

        #intersect buffered garages with buildings
        arcpy.Intersect_analysis([layer_GAR_buffered, layer_BLDG], path_gdb + "/GAR_BLDG_int", "ALL")

        #output to table
        arcpy.TableToTable_conversion(path_gdb + "/GAR_BLDG_int.dbf", path_output, "nearbyBuildings.csv")

        return None

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
