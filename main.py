from SPADE.spade import spade, read_dataset
from datetime import datetime
import time
import matplotlib.pyplot as plt

if __name__ == "__main__":
    input_file = r"BMS1_spmf.txt"
    df = read_dataset(input_file)

    plt.figure()
    sequences_numbers = [500, 1000, 5000]
    min_supports = [10, 100, 300]
    for min_support in min_supports:
        times = []
        for sequences_number in sequences_numbers:
            start_time = time.time()
            support_results = spade(df[:sequences_number], min_support)
            filename = f'results_{datetime.now().strftime("%y-%m-%d-%H:%M")}_sup_{min_support}_len_{sequences_number}.txt'
            support_results.to_csv(filename)
            print(f"Results saved to {filename}")
            elapsed_time = time.time() - start_time
            times.append(elapsed_time)
            print(f"Elapsed time:\t{elapsed_time:.2f} seconds")
        plt.plot(sequences_numbers, times, label=f'min_sup={min_support}')
    plt.xlabel("Number of sequences [-]")
    plt.legend()
    plt.ylabel("Elapsed time [s]")
    plt.title("SPADE: elapsed time as a function of sequences number")
    plt.show()
    plt.savefig(f'SPADE_t_num_{datetime.now().strftime("%y-%m-%d-%H:%M")}.png')
    
    
    
    plt.figure()
    sequences_numbers = [500, 1000, 5000]
    min_supports = [10, 100, 300]
    for min_support in min_supports:
        times = []
        found_sequences = []
        for sequences_number in sequences_numbers:
            start_time = time.time()
            support_results = spade(df[:sequences_number], min_support)
            filename = f'results_{datetime.now().strftime("%y-%m-%d-%H:%M")}_sup_{min_support}_len_{sequences_number}.txt'
            support_results.to_csv(filename)
            print(f"Results saved to {filename}")
            elapsed_time = time.time() - start_time
            times.append(elapsed_time)
            found_sequences.append(support_results.shape[0])
            print(f"Elapsed time:\t{elapsed_time:.2f} seconds")
        plt.plot(sequences_numbers, found_sequences, label=f'min_sup={min_support}')
    plt.xlabel("Number of sequences [-]")
    plt.legend()
    plt.ylabel("Frequent sequences number [-]")
    plt.title("SPADE: Number of frequent sequences")
    plt.show()
    plt.savefig(f'SPADE_frq_num_{datetime.now().strftime("%y-%m-%d-%H:%M")}.png')