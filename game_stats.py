class GameStats():
    # Track statistics for Alien Invasion

    def __init__(self, ai_settings):
        # Initalize statistics
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start alien invasion in an inactive state
        self.game_active = False

    def reset_stats(self):
        # Initialize the statistics that change during the game
        self.ships_left = self.ai_settings.ship_limit