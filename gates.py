def hadamard(qubits
             ):
    
    script = f"\nH {' '.join(map(str, qubits))}\n"
    return script

def reset_x(qubits, 
            reset_error:None
            ):
    
    script = f"\nRX {' '.join(map(str, qubits))}\n"
    if reset_error:
        script += f"\nZ_ERROR({reset_error}) {' '.join(map(str, qubits))}\n"

    return script


def reset_z(qubits, 
            reset_error:None
            ):
    
    script = f"\nR {' '.join(map(str, qubits))}\n"
    if reset_error:
        script += f"\nX_ERROR({reset_error}) {' '.join(map(str, qubits))}\n"

    return script



def tick():
    return '\nTICK\n'

def depolarize1(qubits, 
                error_rate):

    script = f"\nDEPOLARIZE1({error_rate}) {' '.join(map(str, qubits))}\n"

    return script


def identity(qubits,
             ):
    script = f"\nI {' '.join(map(str, qubits))}\n"
    return script



def cnot(qubits):
    script = '\nCNOT ' 
    for qi,qj in qubits:
        script += f'{qi} {qj} '
    script += '\n' 
    return script


def depolarize2(qubits,
                error_rate:float):
    script = f'\nDEPOLARIZE2({error_rate}) ' 
    for qi,qj in qubits:
        script += f'{qi} {qj} '
    script += '\n'    
    return script


def measure_z(qubits, 
            error_rate, 
            reset: False):

    if reset:
        script = f"\nMR({error_rate}) {' '.join(map(str, qubits))}\n"
        return script
    else:
        script = f"\nM({error_rate}) {' '.join(map(str, qubits))}\n"
        return script

def measure_x(qubits, 
            error_rate, 
            reset: False):

    if reset:
        script = f"\nMXR({error_rate}) {' '.join(map(str, qubits))}\n"
        return script
    else:
        script = f"\nMX({error_rate}) {' '.join(map(str, qubits))}\n"
        return script

