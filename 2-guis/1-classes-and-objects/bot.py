class Bot:
  def __init__(self, name, energy, shield):
    self.name = name
    self.age = 0
    self.energy = energy 
    self.shield = shield
    
  def display_name(self):
    print(self.name)
  def display_age(self):
    print(self.age)
  def display_energy(self):
    print(self.energy)
  def display_shield(self):
    print(self.shield)
 # object
beep = Bot("Beep", 100, 100)
beep.display_name()
beep.display_age()
beep.display_energy()
beep.display_shield()
