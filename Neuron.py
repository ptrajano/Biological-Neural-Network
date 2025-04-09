import numpy as np

class Neuron:
    def __init__(self,
                 threshold: float = 1.0,
                 reset_value: float = 0.0,
                 tau_m: float=10,
                 refractory_period: float =2.0) -> None:
        """
        Initialize a single neuron with given parameters.
        
        Args:
            threshold (float): Firing threshold for the neuron.
            reset_value (float): Value of the membrane potential after firing.
            tau_m (float): Membrane time constant.
            refractory_period (float): Time after firing during which the neuron cannot fire.
        """
        self.threshold = threshold
        self.reset_value = reset_value
        self.tau_m = tau_m
        self.refractory_period = refractory_period
        
        self.potential = 0.0  # Membrane potential
        self.last_spike_time = -np.inf  # Time of the last spike
        
    def update(self, input_current: float, dt: float, current_time: float) -> bool:
        """
        Update the neuron's state based on input current and time step.
        
        Args:
            input_current (float): External current input to the neuron.
            dt (float): Simulation time step.
            current_time (float): Current time in the simulation.
        
        Returns:
            bool: True if the neuron fired during this time step, False otherwise.
        """
        # Check if the neuron is in its refractory period
        if current_time - self.last_spike_time < self.refractory_period:
            return False
        
        # Update the membrane potential
        dV = (-self.potential / self.tau_m + input_current) * dt
        self.potential += dV
        
        # Check for firing
        if self.potential < self.threshold:
            return False
        
        self.potential = self.reset_value  # Reset potential
        self.last_spike_time = current_time
        return True
        