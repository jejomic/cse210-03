class TerminalService:
    """
    Presents display
    Prompts user
    """
    
    def _ReadText(self, prompt):
        return input(prompt)
    
    def _DisplayObject(self, list):
        
        for i in list:
            print(i)
            
    def _DisplayText(self, text):
        print(text)
        
    def _ListToText(self, list):
        print(" ".join(list))