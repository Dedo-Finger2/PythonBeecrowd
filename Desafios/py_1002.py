# Área do círculo
# LINK: https://www.beecrowd.com.br/judge/pt/problems/view/1002

from decimal import Decimal

n: float = 3.14159
raio: Decimal = Decimal(input("raio: "))

area: Decimal = pow(raio, 2) * Decimal(n)

print(f"A={round(area, 4)}")
