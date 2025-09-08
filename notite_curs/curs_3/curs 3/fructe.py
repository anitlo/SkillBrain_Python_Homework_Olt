import time

fructe: list[str] = ["🍎", "🍌", "🍊", "🍓", "🥝"]

for fruct in fructe:
    print(f"Procesez {fruct}")
    time.sleep(1) # Simulează procesarea

print("Toate fructele au fost procesate! ✅")

