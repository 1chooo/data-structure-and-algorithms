from qiskit import QuantumCircuit
import math

qc = QuantumCircuit(4,4) 
qc.initialize([1/math.sqrt(2), 1/math.sqrt(2)],0) 
qc.initialize([1/math.sqrt(2), -1/math.sqrt(2)],1) 
qc.h(2)
qc.x(3)
qc.h(3)
qc.draw("mpl")