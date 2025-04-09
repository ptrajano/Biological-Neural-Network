import matplotlib.pyplot as plt
import numpy as np

from Network import Network

if __name__ == "__main__":
    # Parameters
    N = 5  # Number of neurons
    W = np.random.uniform(-1, 1, (N, N))  # Random connection weights
    V = np.random.uniform(0, 0.5, N)  # Random initial potentials
    time_steps = 1000
    dt = 0.1
    external_inputs = np.random.uniform(0, 0.2, N)  # External currents for each neuron

    # Create the network
    network = Network(W=W, V=V, N=N)

    # Simulate the network
    spike_trains = np.zeros((time_steps, N))  # Record spike trains
    membrane_potentials = np.zeros((time_steps, N))

    for t in range(time_steps):
        current_time = t * dt
        network.step(external_inputs=external_inputs, dt=dt, current_time=current_time)
        
        # Record spikes for all neurons
        for i, neuron in enumerate(network.neurons):
            spike_trains[t, i] = 1 if neuron.last_spike_time == current_time else 0
            membrane_potentials[t, i] = neuron.potential  # Record the potential

    # Visualize spike trains
    plt.imshow(spike_trains.T, aspect='auto', cmap='gray_r')
    plt.xlabel("Time")
    plt.ylabel("Neuron")
    plt.title("Spike Trains of the Network")
    plt.show()

    # Plot membrane potential of a selected neuron
    selected_neuron = 0  # Index of the neuron to visualize
    plt.figure(figsize=(10, 6))
    plt.plot(np.arange(time_steps) * dt, membrane_potentials[:, selected_neuron], label=f"Neuron {selected_neuron}")
    plt.xlabel("Time (s)")
    plt.ylabel("Membrane Potential (V)")
    plt.title(f"Membrane Potential of Neuron {selected_neuron}")
    plt.axhline(network.neurons[selected_neuron].threshold, color="r", linestyle="--", label="Threshold")
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 6))
    for i in range(N):
        plt.plot(np.arange(time_steps) * dt, membrane_potentials[:, i], label=f"Neuron {i}")
    plt.xlabel("Time (s)")
    plt.ylabel("Membrane Potential (V)")
    plt.title("Membrane Potentials of All Neurons")
    plt.legend()
    plt.show()  