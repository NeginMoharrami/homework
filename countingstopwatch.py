from stopwatch import Stopwatch

class CountingStopwatch(Stopwatch):
     def __init__(self):
          super().__init__()
          self._count = 0

     def start(self):
         if not self._running:
            self._count += 1 
         super().start()

     def reset(self): 
         super().reset() 
         self._count = 0
    
     def count(self): 
         return self._count

