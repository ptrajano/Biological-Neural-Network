# Spiking Neural Network Simulation

## Project Overview
This project simulates a biologically-inspired spiking neural network using the integrate-and-fire neuron model. The implementation captures key neural dynamics including membrane potential integration, spike generation, and synaptic transmission between neurons.

## Key Features

### Neuron Model
- **Integrate-and-fire mechanism** with leaky membrane potential
- Configurable **firing threshold** and **reset potential**
- **Absolute refractory period** after spiking
- Membrane time constant controls potential decay rate

### Network Architecture
- Fully configurable **N-neuron network**
- Custom **connection weight matrix** (excitatory/inhibitory)
- **Synaptic transmission** with adjustable delays
- External current inputs to each neuron

### Simulation Capabilities
- Adjustable **time step** for simulation precision
- **Spike timing recording** for all neurons
- **Membrane potential tracking** over time
- Multiple visualization outputs

## How It Works

1. **Initialization**:
   - Creates a network of N neurons with random or specified initial potentials
   - Sets up synaptic connections based on the weight matrix W

2. **Simulation Loop**:
   - At each time step:
     - Neurons integrate inputs (synaptic + external)
     - Check for threshold crossing
     - Generate spikes when threshold is reached
     - Enter refractory period after spiking
   - Synapses propagate spikes with specified delays

3. **Output**:
   - Raster plot of spike times
   - Membrane potential traces
   - Network activity visualization

## Configuration Options

| Parameter | Description | Typical Values |
|-----------|-------------|----------------|
| N | Number of neurons | 5-100 |
| W | Connection weight matrix | Random [-1,1] or custom |
| V | Initial membrane potentials | Random [0,0.5] or specified |
| threshold | Firing threshold | 0.5-2.0 |
| tau_m | Membrane time constant | 5-20 ms |
| refractory | Refractory period | 1-5 ms |
| delay | Synaptic transmission delay | 0-5 ms |
| dt | Simulation time step | 0.01-0.5 ms |

## Dependencies
- Python 3.6+
- NumPy
- Matplotlib

## Usage
1. Install requirements: `pip install numpy matplotlib`
2. Run simulation: `python main.py`
3. View generated plots

## Potential Extensions
- Add synaptic plasticity (STDP)
- Implement different neuron types
- Include more complex network topologies
- Add external stimulus patterns
- Incorporate recording and analysis tools

## Author
[Your Name]  
[Your Contact Information]  
[Date]