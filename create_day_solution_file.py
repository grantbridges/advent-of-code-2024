# A helper file to create a new day_#_solutions.py file from the stub

# adjust these as needed
YEAR = 2024
DAY = 3

with open('day_solutions_stub.py', 'r') as stub_file:
    stub_contents = stub_file.read()
    stub_contents = stub_contents.replace('9999', str(YEAR))
    stub_contents = stub_contents.replace('-1', str(DAY))
    stub_contents = stub_contents.replace('Stub', str(DAY))

    with open(f'day_{str(DAY)}_solutions.py', 'w+') as solutions_file:
        solutions_file.write(stub_contents)