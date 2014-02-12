
#
# 	[Turing Machine Simulator]
#

# Constants

tape_length = 20

head_initial_pos = 10

limit_iterations = 10

# Turing Machine declaration

machine = {'s1':{'b':['0','1','s2']} , 's2':{'b':['b','1','s3']} , 's3':{'b':['1','1','s4']} , 's4':{'b':['b','1','s1']} , 'ini':'s1'}

# Variables

head = head_initial_pos

stateActual = machine ['ini']

# Tape initialization

tape = [ 'b' for i in range(tape_length) ]	# With blank variables

# Running machine

for i in range (limit_iterations):
	
	symbol = tape [head]

	write_value, move, next_state = machine [stateActual][symbol]

	# Change content

	tape [head] = write_value

	head += int (move)

	stateActual = next_state

	if stateActual == 'END': break

print tape
