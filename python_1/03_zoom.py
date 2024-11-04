# Allowed functions : all libs for load, manipulate, display image and table manipulation


"""
Create a program that should load the image "animal.jpeg", print some information
about it and display it after "zooming".
• The size in pixel on both X and Y axis
• The number of channel
• The pixel content of the image.
• Display the scale on the x and y axis on the image
If anything went wrong, the program must not stop abruptly and handle any error
with a clear message.
Expected output:
$> python zoom.py
The shape of image is: (768, 1024, 3)
[[[120 111 132]
[139 130 151]
[155 146 167]
...
[120 156 94]
[119 154 90]
[118 153 89]]]
New shape after slicing: (400, 400, 1) or (400, 400)
[[[167]
[180]
[194]
...
[102]
[104]
[103]]]
$>
"""