from interface import QuantumDevice         # the quantum computer you want to use for the random number generation
from simulator import SingleQubitSimulator  # the single qubit simulator from simulator

# create a function that utilizes a quantum device asking for a qubit to collapse.
def qrng(device: QuantumDevice) -> bool:
    with device.using_qubit() as q:
        q.h()
        
        return q.measure()
if __name__ == "__main__":
    qsim = SingleQubitSimulator()
    for idx_sample in range(10):
        random_sample = qrng(qsim)
        print(f"Our QNRG returned {random_sample}.")
