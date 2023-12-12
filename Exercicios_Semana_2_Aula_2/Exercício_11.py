pop_pais_A = 80000
pop_pais_B = 200000
cresc_A = 0.03
cresc_B = 0.015
anos = 0

while pop_pais_A < pop_pais_B:
    pop_pais_A *= 1 + cresc_A
    pop_pais_B *=1 + cresc_B
    anos += 1

print(f"Para o País A ultrapassar o País B em população, serão necessários {anos} anos!")