def parse_cycle_file(filepath: str) -> list[str]:
    results = []

    with open(filepath, encoding='utf-8', mode='r') as file:
        for line in file.readlines():
            if line.startswith('#'):
                continue

            results.append(line.strip())

    return results
