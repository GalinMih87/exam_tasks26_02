from math import ceil, floor

sredna_skorost = float(input())
litra_gorivo = float(input())

obsho_do_lunata = 384400 * 2
vreme_za_otivane_i_vrushtane = ceil(obsho_do_lunata / sredna_skorost)
spent_time = vreme_za_otivane_i_vrushtane + 3
fuel = (litra_gorivo * obsho_do_lunata) / 100

print(round(spent_time))
print(round(fuel))

