class ParachuteGuy:
    """
    The players parachute and body
    """
    
    def __init__(self):
        self.__parahcute = [ '  ___ ', ' /___\ ' , ' \   / ' , '  \ /  ' ]
        self.__body = ['   o   ','  /|\  ','  / \  ']
        self.__isAlive = True
        
    
    def _GetBody(self):
        return self.__body
    
    #for displaying player gameover
    def _UpdateBody(self, list):
        self.__body = list
    
    #returns player status
    def _CheckHp(self):
        return self.__isAlive
    
    #sets player status
    def _UpdateHp(self, bool):
        self.__isAlive = bool
       
    #returns the parachute
    def _GetParachute(self):
        return self.__parahcute
    
    #makes the game rule damage the parachute
    def _DamageParachute(self):
        self.__parahcute.pop(0)