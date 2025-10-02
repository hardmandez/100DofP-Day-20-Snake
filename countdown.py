import time

class CountdownTimer:
    def __init__(self, duration_seconds):
        self.duration = duration_seconds
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def remaining(self):
        if self.start_time is None:
            return self.duration
        elapsed = time.time() - self.start_time
        return max(0, self.duration - elapsed)

    def expired(self):
        return self.remaining() <= 0

    def reset(self, new_duration=None):
        if new_duration is not None:
            self.duration = new_duration
        self.start_time = time.time()
