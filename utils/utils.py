def input_nonempty(prompt):
    while True:
        p = input(prompt).strip()
        if p:
            return p
        print("Input cannot be empty.")