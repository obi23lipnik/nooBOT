from MouseControl import Action as Mouse_Action

mouse = Mouse_Action(x_minimum=62, y_minimum=0, x_maximum=862, y_maximum=600)

print mouse.bow_binary_range(range(3),range(10))
