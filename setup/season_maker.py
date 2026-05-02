def seasonMaker():
    return [f"{y}-{str(y + 1)[-2:]}" for y in range(1951, 2026)]