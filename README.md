## Utility tool for creating checkerboard pattern images

### Usage
```$ python3 main [options] [params]```

### Options
* ```-f / --file```           reading params from file       [string] (default = None)
* ```-n / --name```           image file name with extension [string] (default = uuid4)
* ```-x / --width```          image width in squares         [int]    (default = 8)
* ```-y / --height```         image height in squares        [int]    (default = 8)
* ```-s / --square```         square side length             [int]    (default = 32)
* ```-bg / --background```    image background color         [string] (default = 'white')
* ```-fg / --foreground```    square color                   [string] (default = 'black')

### Input file (with -f options)
##### {name} {width} {height} {square} {background} {foreground}

```
first.png 16 32 8 yellow blue 
second.jpg 16 32 8 red blue 
third.png 64 64 8 red blue 
```