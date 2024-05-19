def read(n):
    with open('legendre.txt', 'r') as file:
        lines = file.readlines()

    data = {}
    current_n = None
    w = []
    x = []

    for line in lines:
        line = line.strip()
        # if not line:
        #     continue
        if line.startswith("n ="):
            if current_n is not None:
                data[current_n] = (w, x)
            current_n = int(line.split('=')[1].strip())
            w = []
            x = []
        else:
            if current_n is not None:
                parts = line.split()
                if len(parts) == 2:
                    weight, coordinate = map(float, parts)
                    w.append(weight)
                    x.append(coordinate)

    if current_n is not None:
        data[current_n] = (w, x)

    return data.get(n, (None, None))


if __name__ == "__main__":
   print(read(2))