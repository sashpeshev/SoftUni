mackerel_per_kg = float(input())
sprat_per_kg = float(input())
kg_of_bonito = float(input())
kg_of_horse_mackerel = float(input())
kg_of_mussels = int(input())

mussels_per_kg = 7.50
bonito_per_kg = mackerel_per_kg + mackerel_per_kg * 0.6
horse_mackerel_per_kg = sprat_per_kg + sprat_per_kg * 0.8

bonito_price = kg_of_bonito * bonito_per_kg
horse_mackerel_price = kg_of_horse_mackerel * horse_mackerel_per_kg
mussels_price = kg_of_mussels * mussels_per_kg

total = bonito_price + horse_mackerel_price + mussels_price
print(f"{total:.2f}")
