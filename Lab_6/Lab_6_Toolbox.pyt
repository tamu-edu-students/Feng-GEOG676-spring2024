# -*- coding: utf-8 -*-

import arcpy
import time


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [GraduateColorsRenderer]


class GraduateColorsRenderer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Lab_6_Toolbox"
        self.description = "Generate a graduated color map"
        self.canRunInBackground = False
        self.category = "Map tools"


    def getParameterInfo(self):
        """Define the tool parameters."""
        params0 = arcpy.Parameter(
            displayName= "Input GIS Project Name",
            name= "InputName",
            datatype= "DEFile",
            parameterType="required",
            direction= "Input"
        )
        params1 = arcpy.Parameter(
            displayName = "Target Layer",
            name = "target_layer",
            datatype = "GPLayer",
            parameterType = "Required",
            direction="Input"
        )
        params2 = arcpy.Parameter(
            displayName = "Output Path",
            name = "path_output",
            datatype = "DEFolder",
            parameterType = "Required",
            direction="Input"
        )
        params3 = arcpy.Parameter(
            displayName = "Output Project",
            name = "project_input",
            datatype = "GPString",
            parameterType = "Required",
            direction="Input"
        )
        params = [params0, params1, params2, params3]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        #define progressor variables
        readTime = 1.5
        start = 0
        maximum = 100
        step = 33

        # Setting up the progressor
        arcpy.SetProgressor("step", "Validating project file...", start, maximum, step)
        time.sleep(readTime)
        # Add message to the results pane
        arcpy.AddMessage("Validating project file...")
        
        project = arcpy.mp.ArcGISProject(parameters[0].valueAsText) #GIS project file
        campus = project.listMaps("Map")[0] # Grab the first map in the project

        # Increment the progressor and change the label; add message to the results pane
        arcpy.SetProgressorPosition(start + step)
        arcpy.SetProgressorLabel("Looking for the target layer...")
        time.sleep(readTime)
        arcpy.AddMessage("Looking for the target layer...")

        for layer in campus.listLayers():
            if layer.isFeatureLayer: # Check if layer is a feature layer
                symbology = layer.symbology # Obtain a copy of the layer's symbology
                if hasattr(symbology, "renderer"): # Check if it has a 'renderer' attribute
                    if layer.name == parameters[1].valueAsText: # find the layer match the input name

                        # Increment the progressor and change the label; add message to the results pane #2
                        arcpy.SetProgressorPosition(start + step * 2) #66%
                        arcpy.SetProgressorLabel("Calculating and classifying...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Calculating and classifying...")

                        symbology.updateRenderer("GraduatedColorsRenderer") # Update the copy's renderer to be 'GraduatedColorsRenderer'
                        symbology.renderer.classificationField = "Shape_Area" # set the target field for choropleth off of
                        symbology.renderer.breakCount = 5 # Set the number of classes
                        symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0] # Set the color ramp
                        layer.symbology = symbology # Set the layer's actual symbology equal to the copy's

                        arcpy.AddMessage("Finishing rendering...")
                    else:
                        print("No layer named %s found" %parameters[1].valueAsText)

        # Increment the progressor and change the label; add message to the results pane #3
        arcpy.SetProgressorPosition(start + step * 3) #99%
        arcpy.SetProgressorLabel("Saving the project...")
        time.sleep(readTime)
        arcpy.AddMessage("Saving the project...")

        project.saveACopy(parameters[2].valueAsText + "\\" + parameters[3].valueAsText + ".aprx")

        # Increment the progressor and change the label; add message to the results pane #3
        arcpy.SetProgressorPosition(maximum) #100%
        arcpy.SetProgressorLabel("Finished")
        time.sleep(readTime)
        arcpy.AddMessage("Finished")

        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
