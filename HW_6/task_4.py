def digits_remover(file_path):
    with open(file_path, 'r') as f:
        file_data = f.read()
        with open(file_path, 'w') as f:
            f.write("".join([c for c in file_data if not c.isdigit()]))

digits_remover(file_path="input.txt")
