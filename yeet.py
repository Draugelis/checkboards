from PIL import Image, ImageDraw
import sys


default_args = (5, 5, 32, "output.png", "white", "gray")

def draw_placeholder(w = 5, h = 5, sq_size = 32, name = "output.png", bg_color = "white", sq_color = "black"):
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
            x0 = i * (sq_size)
            y0 = j * (sq_size)
            x1 = (i + 1) * (sq_size) - 1
            y1 = (j + 1) * (sq_size) - 1

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


if sys.argv[1] == "-a" and len(sys.argv) == 8:
    """
        flag -a - argument mode

        Input variables for draw_placeholder are passed via command line
    """


    """
        Saving passed argument to a list 
        Skipping sys.argv[0] as it is file name
        Skipping sys.argv[1] as it is flag
    """
    arguments = sys.argv[2:]

    """
        Changing some argument types
        This is because when I just pass args as "python3 yeet.py 16 9 32 yeet.png "white" "black"  "
        it reads every single thing as strings
    """
    arguments[0] = int(arguments[0])
    arguments[1] = int(arguments[1])
    arguments[2] = int(arguments[2])

elif sys.argv[1] == "-i" and len(sys.argv) == 2:
    """
        flag -i - interactive mode

        Input variables are entered via prompt on command line
    """


    """
        This part is ugly as hell in terms of input() usage
        However, I had to write a description for each input
        So whatever, let it be 
    """
    arguments = []
    print("Enter width in squares (w): ")
    arguments.append(int(input()))
    print("Enter heigth in squares (h): ")
    arguments.append(int(input()))
    print("Enter square side size in pixels (sq_size): ")
    arguments.append(int(input()))
    print("Enter output file name with file extention (name): ")
    arguments.append(input())
    print("Enter base RGB color (bg_color)")
    arguments.append(input())
    print("Enter square RGB color (sq_color)")
    arguments.append(input())




print(*arguments)
print(*sys.argv)
draw_placeholder(*arguments)

print("Done")
    