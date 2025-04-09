from Neuron import Neuron

class Synapse:
    def __init__(self, 
                 pre_neuron: Neuron, 
                 post_neuron: Neuron,
                 weight: float = 1.0,
                 delay: float = 0.0):
        """
        Initialize a synapse connecting two neurons.
        
        Args:
            pre_neuron (Neuron): The pre-synaptic neuron.
            post_neuron (Neuron): The post-synaptic neuron.
            weight (float): Strength of the synaptic connection.
            delay (float): Transmission delay between the pre- and post-synaptic neurons.
        """
        self.pre_neuron = pre_neuron
        self.post_neuron = post_neuron
        self.weight = weight
        self.delay = delay
        self.spike_times = []  # Store the times of spikes from the pre-synaptic neuron
    
    def propagate(self, current_time: float) -> float:
        """
        Propagate spikes from the pre-synaptic neuron to the post-synaptic neuron.
        
        Args:
            current_time (float): Current simulation time.
        
        Returns:
            float: The synaptic current contributed to the post-synaptic neuron.
        """
        # Add the current spike time if the pre-neuron fired
        if self.pre_neuron.last_spike_time == current_time:
            self.spike_times.append(current_time)
        
        # Compute the input current based on delayed spikes
        input_current = 0.0
        for spike_time in self.spike_times[:]:
            if current_time - spike_time >= self.delay:
                input_current += self.weight
                self.spike_times.remove(spike_time)  # Remove processed spike
        
        return input_current
