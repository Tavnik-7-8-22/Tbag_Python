import time


class Time:
    def __init__(self):
        self.start_time = time.time()
        self.GAME_TIME_MULTIPLIER = 1
        self.timer_time_left = 0
        self.end_time = 0

    def get_game_time(self):
        """
        Returns the current game time in seconds, adjusted based on the GAME_TIME_MULTIPLIER.
        """
        return (time.time() - self.start_time) * self.GAME_TIME_MULTIPLIER

    def set_timer(self, seconds):
        """
        Sets a timer for the specified number of seconds.
        """
        self.end_time = self.get_game_time() + seconds

    def get_time_left(self):
        """
        returns the amount of time left on the timer
        :return:
        """
        if self.end_time < self.get_game_time():
            return 0
        else:
            return self.end_time - self.get_game_time()


if __name__ == '__main__':
    Time = Time()
    game_time = Time.get_game_time()
    print("Current game time: {}".format(round(game_time)))

    seconds = int(input("Length of timer in seconds: "))
    Time.set_timer(seconds)
    print("Timer set for {} seconds...".format(seconds))

    # while Time.get_game_time() < game_time + seconds:
    #     # time.sleep(1)
    #     pass

    time_left = Time.get_time_left()

    while time_left > 0:
        time_left = Time.get_time_left()
        print("Time left: {} ".format(round(time_left)))
        time.sleep(1)

    print("Timer expired!")