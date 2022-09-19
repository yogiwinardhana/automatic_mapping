# automatic_mapping
Automatic mapping using ArcPy

# How to use <br>

## 1. Change directory location
`my_map` is a variable that will hold the location of the map (.mxd) file. Meanwhile, `out_folder` is the location where we locate the exported map. <br>
`on line (3-4)` <br>
`my_map     = ......` <br>
`out_folder = ......` <br>

## 2. Map Identifier
Map identifier will also get updated as the script run. <br>
`on line (19)` <br>
`list_layout[0].text = 'SECTOR' + " " + y.name`

cheers

