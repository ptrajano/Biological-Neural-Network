import numpy as np

from Synapse import Synapse
from Neuron import Neuron

class Network:
    def __init__(self, W: np.ndarray,
                 V: np.ndarray,
                 N: int,
                 threshold: float = 1.0,
                 tau_m: float = 10,
                 refractory_period: float = 2.0,
                 reset_value: float = 0.0) -> None:
        """
        Initialize a network of neurons with given connection matrix and initial potentials.
        
        Args:
            W (np.ndarray): NxN matrix representing synaptic weights between neurons.
            V (np.ndarray): N-dimensional vector of initial membrane potentials.
            N (int): Number of neurons in the network.
            threshold (float): Firing threshold for all neurons.
            tau_m (float): Membrane time constant for all neurons.
            refractory_period (float): Refractory period for all neurons.
            reset_value (float): Membrane potential reset value after firing.
        """
        self.N = N
        self.neurons = []
        self.synapses = []
        
        # Create neurons with initial potentials
        for i in range(N):
            neuron = Neuron(
                threshold=threshold, 
                tau_m=tau_m, 
                refractory_period=refractory_period, 
                reset_value=reset_value
            )
            neuron.potential = V[i]
            self.neurons.append(neuron)
        
        # Create synapses based on the weight matrix W
        for i in range(N):
            neuron_synapses = []
            for j in range(N):
                if W[i, j] != 0:  # Only create a synapse if weight is non-zero
                    synapse = Synapse(pre_neuron=self.neurons[j], post_neuron=self.neurons[i], weight=W[i, j])
                    neuron_synapses.append(synapse)
            self.synapses.append(neuron_synapses)
    
    def step(self, external_inputs: np.ndarray, dt: float, current_time: float):
        """
        Simulate one time step of the network.
        
        Args:
            external_inputs (np.ndarray): N-dimensional vector of external currents to each neuron.
            dt (float): Simulation time step.
            current_time (float): Current simulation time.
        """
        # Update each neuron
        for i, neuron in enumerate(self.neurons):
            # Gather synaptic inputs from all connected synapses
            synaptic_current = sum(synapse.propagate(current_time) for synapse in self.synapses[i])
            total_input = synaptic_current + external_inputs[i]
            
            # Update neuron state
            neuron.update(input_current=total_input, dt=dt, current_time=current_time)
