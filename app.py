from qiskit import QuantumRegister
from qiskit import ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ

#initilising a 16 qubit register 
q = QuantumRegister(16,’q’)


#initialise the 16 bit classical register
c = ClassicalRegister(16,’c’)

#create a quantum circuit using the following code:
circuit = QuantumCircuit(q,c)


#then we apply hadmard gate to put a qubit in to a superposition of 1 and 0 to measure 1 or a 0 with equal probability.
circuit.h(q)

#Measures all qubits 
circuit.measure(q,c)

backend = provider.get_backend('ibmq_qasm_simulator')
job = execute(circuit, backend, shots=1)

result = job.result()
counts = result.get_counts(circuit)

print('RESULT: ',counts,'\n')