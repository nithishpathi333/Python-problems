class car():
    def dooropened(self):
        print("sit inside")
        car()._accelerator()
    def _accelerator(self):
        print("speed increases")
        car().__engine()
    def __engine(self):
        print("engine running")
        
car().dooropened()

Output:  
        sit inside
        speed increases
        engine running
