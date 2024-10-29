#player record programe
class Player:
  def __init__(self, uniqueID, score, minutes, speed, strength, agility):
    self.uniqueID: str = uniqueID
    self.score: int = score
    self.minutes: float = minutes
    self.speed: int = speed
    self.strength: int = strength
    self.agility: int = agility

player_one = Player ("charlotte10", 100, 4.21, 62, 45, 97)

print (player_one.uniqueID, player_one.score, player_one.minutes, player_one.speed, player_one.strength, player_one.agility)
