# the CLI that the user experiences

def ask(query: str, inputType = str):
	answer = inputType(input(f'\t{query} '))
	return answer