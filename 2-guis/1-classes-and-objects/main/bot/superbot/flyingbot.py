# main.py


from superbot import SuperBot

astro_bot = SuperBot("Astro")
astro_bot.display_name()

from flyingbot import Flyingbot
astro_boty = Flyingbot("UFO")
astro_boty.display_name()
# bot.py


class Bot:
  def __init__(self, name, energy=100, shield=100):
    self.name = name
    self.age = 0
    self.energy = energy 
    self.shield = shield
    
  def display_name(self):
    print(self.name)
# superbot.py


from bot import Bot

class SuperBot(Bot):
   def __init__(self, name, power_level=100):
     super().__init__(name)
     self.power_level = power_level
   
   def get_power_level(self):
     return self.power_level


#flyingbot.py
from superbot import SuperBot

class Flyingbot(SuperBot):
  def __init__(self, name, hover_distance=0):
     super().__init__(name)
     self.hover_distance = hover_distance
     
  def get_hover_distance(self):
    return self.hover_distance
