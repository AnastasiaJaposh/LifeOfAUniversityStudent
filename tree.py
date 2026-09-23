
class Node():
    def __init__(self, id, scene, first_child = None, sec_child = None, thr_child = None):
        self.id = id # this is only for easier navigation, i don't actually use this in code
        self.scene = scene 
        self.first_child = first_child
        self.sec_child = sec_child
        self.thr_child = thr_child

class Tree():
    def __init__(self, start_window):
        self.start_w = start_window