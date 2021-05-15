import math

atk = 1000
cdmg = 1.5
constant = 0.9

def print_dmg(atk, cdmg, constant):
  dmg = atk * cdmg * constant
  print(f"=={atk}==&=={cdmg:1f}==")
  print(f'Attack: {atk}')
  print(f'Crit Damage: {cdmg}')
  print(f'Total Damage: {dmg}')
  print("=====================\n")

atk_cap = 3500
cdmg_cap = 3.0

while atk <= atk_cap:
  print_dmg(atk, cdmg, constant)
  while cdmg <= cdmg_cap:
    print_dmg(atk, cdmg, constant)

    cdmg += 0.1
  atk += 100
