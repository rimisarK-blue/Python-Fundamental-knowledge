
pirating_days = int(input())
plunder_daily = int(input())
expected_plunder = int(input())

total_plunder = 0

for day in range(1, pirating_days + 1):
    if day % 3 == 0 and day % 5 == 0:
        total_plunder += plunder_daily + (plunder_daily * 0.50)
        total_plunder -= (total_plunder * 0.30)
        continue
    if day % 3 == 0:
        total_plunder += plunder_daily + (plunder_daily * 0.50)
        continue
    if day % 5 == 0:
        total_plunder += plunder_daily
        total_plunder -= (total_plunder * 0.30)
        continue
    total_plunder += plunder_daily

per_needed = (total_plunder / expected_plunder) * 100
if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {per_needed:.2f}% of the plunder.")
