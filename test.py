from ca2d import CA

ca = CA((6, 7),
        (0, 1, 8),
        'neumann',
        size_x = 4,
        size_y = 8)

ca.step()
print(ca.array)
print(ca.birth_rule)
print(ca.death_rule)
print(ca.neighbourhood)
