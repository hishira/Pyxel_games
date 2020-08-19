import pyxel

class Ship:
    def __init__(self):
        self.blocks = [[80,80,4],[84,80,4],[76,80,4],[80,76,4]]
    
    def draw(self):
        for i in self.blocks:
            pyxel.rect(i[0],i[1],i[2],i[2],1)
        
class App:
    def __init__(self):
        self.ship = Ship()
        pyxel.init(150,120,quit_key=pyxel.KEY_Q)
        pyxel.run(self.update,self.draw)
        
    
    def update(self):
        pass
    
    def draw(self):
        pyxel.cls(5)
        self.ship.draw()

App()