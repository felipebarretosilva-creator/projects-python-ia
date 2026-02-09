# utils/time_utils.py

import time


class TimeCounter:
    """
    Classe para controle de tempo e FPS.
    """

    def __init__(self):

        self.start_time = time.time()
        self.last_time = self.start_time
        self.frame_count = 0
        self.fps = 0


    def timestamp_ms(self):
        """
        Retorna timestamp em milissegundos
        desde o início.
        """

        return int(
            (time.time() - self.start_time) * 1000
        )


    def update_fps(self):
        """
        Atualiza FPS a cada segundo.
        """

        self.frame_count += 1

        now = time.time()
        delta = now - self.last_time

        if delta >= 1.0:

            self.fps = self.frame_count / delta
            self.frame_count = 0
            self.last_time = now

        return self.fps
