## Python script that creates checkboard pattern images

***

### Usage in Command Line:
```$ python3 yeet.py -flag [args]```

#### Flags: 
* -a - variables are passed via command line as arguments
* -i - variables are entered via command line prompts

#### Variables

>when using -a flag they are passed in the same sequence.

>bg_color/sq_color type depends on used flag.
>with -a string could be used at this time (gotta fix this).
>with -i flag both types could be used.

Name 	 | Description 				 | Type
---------|---------------------------|-------
w        |   image width in squares  | int
h        |   image heigth in squares | int
sq_size  |   square size 			 | int
name     |   name of the output file | string
bg_color |   base color in RGB		 | string/tuple
sq_color |   square color in RGB	 | string/tuple

