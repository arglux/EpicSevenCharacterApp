
class CharacterTemplate:
  def __init__(self, name):
    '''
    Initialize template with attributes
    These attributes are final calculated values to be displayed
    '''
    self.name = name
    self.type = None

    self.attack = None
    self.hp = None
    self.defense = None

    self.critical_chance = None
    self.critical_damage = None
    self.dual_attack_chance = None

    self.effectiveness = None
    self.effect_resistance = None
    self.speed = None

    return self


  def set_type(self, typee):
    self.type = typee
    return self

  def set_base_attack(self, base_attack):
    self.base_attack = base_attack
    return self

  def set_base_hp(self, base_hp):
    self.base_hp = base_hp
    return self

  def set_base_defense(self, base_defense):
    self.base_defense = base_defense
    return self

  def set_base_critical_chance(self, critical_chance):
    self.base_critical_chance = critical_chance
    return self

  def set_base_critical_damage(self, critical_damage):
    self.base_critical_damage = critical_damage
    return self

  def set_base_dual_attack_chance(self, dual_attack_chance):
    self.base_dual_attack_chance = dual_attack_chance
    return self

  def set_base_effectiveness(self, effectiveness):
    self.base_effectiveness = effectiveness
    return self

  def set_base_effect_resistance(self, effect_resistance):
    self.base_effect_resistance = effect_resistance
    return self

  def set_base_speed(self, speed):
    self.base_speed = speed
    return self

if __name__ == "__main__":
  name = input()

