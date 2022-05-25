btc = int(input())
cny = float(input())
commission = float(input())
btc_to_bgn = 1168
cny_to_usd = 0.15
usd_to_bgn = 1.76
eur_to_bgn = 1.95

all_in_bgn = btc * btc_to_bgn + (cny * cny_to_usd) * usd_to_bgn
all_in_eur = all_in_bgn / eur_to_bgn
without_commission = all_in_eur - all_in_eur / 100 * commission

print(f"{without_commission:.2f}")
