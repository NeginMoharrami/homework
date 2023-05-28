from time import perf_counter

class Stopwatch:
    def __init__(self): 
        self.reset()
    
    def start(self): 
        if not self._running:
             self._start_time = perf_counter() - self._elapsed 
             self._running = True
    
    def stop(self):
        if self._running:
            self._elapsed = perf_counter() - self._start_time 
            self._running = False
    
    def reset(self):
        self._start_time = self._elapsed = 0 
        self._running = False
    
    def elapsed(self):
        if not self._running: 
            return self._elapsed 
        else: 
            return perf_counter() - self._start_time

