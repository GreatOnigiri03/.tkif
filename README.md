## Introducing the new image file format - .TKIF!

**Tkinter Image Format** is a vector image format based on *.INI* data structure, and works using *Python* and its library *Tkinter*.

There is also a simple built-in image reader, and you can use it as a template for your own!

## Currently, there is 2 object types
A point:
```
[point_example]
x = 30
y = 20
; The X-Y coordinates is required.
```
A line:
```
[point_A]
x = 10
y = 30

[B]
x = 40
y = 20

[line_example]
a = point_A
b = B
```
Line needs 2 existing points, and it is not required for points' names to begin with "point".

You can also pass the objects, just name it randomly or type "pass" in the end of the object's name.
```
[line_pass]
a = point_foo
b = bar_point
```

### Feel free to modify the .tkif library or the reader!
