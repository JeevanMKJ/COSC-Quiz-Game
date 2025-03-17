class GameState:
  def __init__(self):
    self.running = True
    self.score = 0
    self.curent_mode = None

  def quit_game(self):
    self.running = False
    print("\nThanks for playing!")
    exit()