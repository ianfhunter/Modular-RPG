class Console(UI):

    def clear(self):
        #TODO: Move to UI
        import os
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')