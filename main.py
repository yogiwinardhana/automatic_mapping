import arcpy

my_map = '//directory//to_file//.mxd' # MXD file directory (.mxd)
out_folder = '//directory//to_map//' # Mapping folder output directory (.png)

def get_map():
    # load mxd file
    mxd = arcpy.mapping.MapDocument(my_map) # will return mxd location

    # Save all in variables
    list_layout     = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", 'tittle')
    list_dataframes = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
    list_bookmarks  = arcpy.mapping.ListBookmarks(mxd, data_frame=list_dataframes)

    # Loop through all bookmarks list
    for y in (list_bookmarks):

        # Access text with element name tittle
        list_layout[0].text = [Identifier in MXD File (string)] + " " + y.name

        # Export each layer
        list_dataframes.extent = y.extent
        outFile = out_folder + y.name + ".png"
        arcpy.mapping.ExportToPNG(mxd, outFile, 'PAGE_LAYOUT', 1587, 1123, 600)

        print ("Map for " + y.name + " done.")

if __name__ == '__main__':
    get_map()

