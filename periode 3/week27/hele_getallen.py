lijst = [1, 'aap', 2, 'apen', 3, 'watermeloen', 15, 27, 15, 'lekker bezig', '6', 7.23, 'makkelijk hoor']

hele_getallen = []
for i in lijst:
    if not isinstance(i, float):
        try:
            hele_getallen.append(int(i))

        except ValueError:
            pass
print(len(hele_getallen))