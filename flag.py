# Paires de valeurs (ASCII, y)
data = [
    (101, 5), (107, 6), (96, 7), (102, 8), (51, 9), (49, 10), (122, 11),
    (79, 12), (48, 13), (87, 14), (50, 15), (75, 16), (94, 17), (79, 18),
    (47, 19), (82, 20), (48, 21), (83, 22), (48, 23), (47, 24), (77, 25),
    (124, 26)
]

# Tri des valeurs ASCII en fonction de la coordonnée y
sorted_data = sorted(data, key=lambda x: x[1])

# Extraction des valeurs ASCII triées
sorted_ascii_values = [x[0] for x in sorted_data]

print(sorted_ascii_values)

