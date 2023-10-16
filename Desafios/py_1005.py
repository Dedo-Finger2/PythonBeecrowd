# Média 1
# LINK: https://www.beecrowd.com.br/judge/pt/problems/view/1005

from decimal import Decimal

a: Decimal = Decimal(input())
b: Decimal = Decimal(input())

PESO_A: float = 3.5
PESO_B: float = 7.5

media: Decimal = ((a * Decimal(PESO_A)) + (b * Decimal(PESO_B))) / (Decimal(PESO_A) + Decimal(PESO_B))

print(f"MEDIA = {round(media, 5)}")
