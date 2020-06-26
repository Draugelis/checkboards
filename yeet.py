from PIL import Image, ImageDraw
import sys

colors = {
    'BLACK'   : (  0,   0,   0),
    'GRAY'    : (128, 128, 128),
    'WHITE'   : (255, 255, 255),
    'DGRAY'   : ( 96,  96,  96),
    'LGRAY'   : (160, 160, 160)
}


default_args = (5, 5, 32, "output.png", WHITE, GRAY)

def draw_placeholder(w = 5, h = 5, sq_size = 32, name = "output.png", bg_color = colors["WHITE"], sq_color = colors["GRAY"]):
    """ 
        Draw a checkerboard pattern rectancle

        w           image width in squares
        h           image heigth in squares
        sq_size     square size
        name        name of the output file
        bg_color    base color in RGB
        sq_color    square color in RGB
    """
    width = w * sq_size
    heigth = h * sq_size
    image_size = (width, heigth)
    square_size = (sq_size, sq_size)

    image = Image.new("RGB", image_size, bg_color)
    image_draw = ImageDraw.Draw(image)

    i_start = 0

    for j in range(h):
        for i in range(i_start, w, 2):    
            """
                Going though the image and drawing squares on it
                i   square position on x axis in squares
                j   square position on y axis in square
            """

            """
                x0, y0  top-left corner of a square
                x1, y1  bottom-right corner of a square
            """
            x0 = i * sq_size
            y0 = j * sq_size
            x1 = (i + 1) * sq_size
            y1 = (j + 1) * sq_size

            cords = [(x0, y0), (x1, y1)]
            del x0, x1, y0, y1

            image_draw.rectangle(cords, sq_color)

        """
            Defining i_start for next row to offset first square by 1 square
        """
        if (j % 2) == 0:
            i_start = 1
        else:
            i_start = 0

    image.save(name)


if len(sys.argv) == 7:
    """
        Saving passed argument to a list 
        Skipping sys.argv[0] as it is file name
    """
    arguments = sys.argv[1:]

    """
        Changing some argument types
        This is because when I just pass args as "python3 yeet.py 16 9 32 yeet.png DGRAY GRAY"
        it reads every single thing as strings
    """
    arguments[0] = int(arguments[0])
    arguments[1] = int(arguments[1])
    arguments[2] = int(arguments[2])

    # I don't want to talk about this part
    arguments[4] = colors[arguments[4]]
    arguments[5] = colors[arguments[5]]

else:
    arguments = default_args




print(*arguments)
print(*sys.argv)
draw_placeholder(*arguments)

print("Done")
    