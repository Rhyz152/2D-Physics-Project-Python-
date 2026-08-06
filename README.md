# 2D Physics Project
This a project programmed in Python, of course, programmed by me.
This project was made when I was basically a beginner in Python.
However, I do have 1.5 years of Luau experience and since Luau is similar to Python, it was fairly easy.
This project uses: **PyQt5**.

# Physics.py
This is what handles all of the physics involved of course.
### update_all(...)
The function applies gravity to every shape.
This applies gravity to all of the shapes.
### Shape collision functions
They are all the same, just different functions since they are different shapes located in different places.
Essentially, for every shape in their shapes, we make them go to the right and down (then it goes back up due to collisions).
### update_engine(...)
This is the **main function** of the physics file.
All it does is call all the functions.
This is called every frame (inside of Ui.py)

# Render.py
This handles all the rendering per-frame.
Using PyQt5's painter, we can just draw new shapes to their new position after the physics update.

# Ui.py
This is actually the main component of the entire project.
This handles Ui, obviously, physics update, and render updates.
### Buttons
Since this is basically a physics engine, I've made buttons that, when interacted, construct a new shape (from shapes.py) and that shape would be whatever button was assigned to it ("Square button" would spawn a square obviously).
Using PyQt5's timer, every frame/tick the tick(...) function is called.
### tick(...)
This will handle all of the frame updates.
It calls the physics.py's update_engine(...).
After that, it calls the canvas' update(...) function.
This handles rendering inside of a canvas.
To make sure that there isn't too much shapes, the function checks whether the amount of shapes inside of the workspace (for each shape) is more than 1000.
If there is, it removes one of them.
