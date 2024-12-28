from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.problems import ElectronicStructureProblem
from qiskit_nature.second_q.mappers import ParityMapper
from qiskit_nature.second_q.operators import ElectronicEnergy

driver = PySCFDriver(
    atom="H 0 0 0; H 0 0 0.735", 
    basis="sto3g"
)
molecular_data = driver.run()
problem = ElectronicStructureProblem(driver)
second_q_hamiltonian = problem.hamiltonian
mapper = ParityMapper()
qubit_hamiltonian = mapper.map(second_q_hamiltonian.second_q_op())

print("Qubit Hamiltonian:")
print(qubit_hamiltonian)
