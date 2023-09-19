# Define the base class player
class player:
  def play(self):
    print("the player is playing cricket.")

#define the derived class Batsman
class Batman(player):
  def play(self):
    print("The batsman is batting. ")

# define the derived class bowler
class bowler(player):
  def play(self):
    print("The bowler is bowling.")

# create objects of batsman and bowler classes
batman = Batman()
bowler = bowler()

# Call the play() method for each object
batman.play()
batman.play()
