from PIL import Image, ImageDraw
import argparse, uuid 

def parse_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-f' , '--file'  , type = str, nargs = 1)
    arg_parser.add_argument('-x' , '--width' , type = int, nargs = 1)
    arg_parser.add_argument('-y' , '--height', type = int, nargs = 1)
    arg_parser.add_argument('-s' , '--square', type = int, nargs = 1)
    arg_parser.add_argument('-n' , '--name'  , type = str, nargs = 1)
    arg_parser.add_argument('-bg', '--background', type = str, nargs = 1)
    arg_parser.add_argument('-fg', '--foreground', type = str, nargs = 1)
    args = arg_parser.parse_args()

    return args

def get_params(args):
    # default params
    params = {
        'name'      : str(uuid.uuid4()) + '.png',
        'width'     : 8,
        'height'    : 8,
        'square'    : 32,
        'background': 'white',
        'foreground': 'black'
    }

    if args.width:      params['width']      = args.width[0]
    if args.height:     params['height']     = args.height[0]
    if args.square:     params['square']     = args.square[0]
    if args.name:       params['name']       = args.name[0]
    if args.background: params['background'] = args.background[0]
    if args.foreground: params['foreground'] = args.foreground[0]

    return params

def draw(params):
    image_width     = params['width'] * params['square']
    image_height    = params['height'] * params['square']
    image_size      = (image_width, image_height)
    square_size     = params['square']
    image           = Image.new('RGB', image_size, params['background'])
    image_draw      = ImageDraw.Draw(image)

    start_position = 0
    for j in range(image_height):
        for i in range(start_position, image_width, 2):    
            """
                Going though the image and drawing squares on it
                i   square position on x axis in squares
                j   square position on y axis in square
                x0, y0  top-left corner of a square
                x1, y1  bottom-right corner of a square
            """
            x0 = i * (square_size)
            y0 = j * (square_size)
            x1 = (i + 1) * (square_size) - 1
            y1 = (j + 1) * (square_size) - 1

            cords = [(x0, y0), (x1, y1)]
            del x0, x1, y0, y1

            image_draw.rectangle(cords, params['foreground'])
           
        # Defining start_position for next row to offset first square by 1 square
        if (j % 2) == 0: start_position = 1
        else:            start_position = 0

    image.save(params['name'])

def file_handler(args):
    file = open(args.file[0], 'r')
    for row in file:
        param_list = row.split(" ")
        # example param_list: [example.png, 16, 16, 32, white, black]
        params = {
            'name'      : str(param_list[0]),
            'width'     : int(param_list[1]),
            'height'    : int(param_list[2]),
            'square'    : int(param_list[3]),
            'background': str(param_list[4]),
            'foreground': str(param_list[5])
        }
        
        draw(params)

    file.close()

if __name__ == '__main__':
    args = parse_args()

    if args.file:
        file_handler(args)
    else:
        params = get_params(args)
        draw(params)