# hill_muscle_model\plot_simulation.py
import os
import time
import datetime
import traceback

import pandas as pd
import matplotlib.pyplot as plt

import util

script_name = os.path.splitext(os.path.basename(__file__))[0]
logger = util.setup_logging(script_name)

def plot_simulation():
    try:
        working_directory = util.get_working_directory()

        simulation_results_filepath = os.path.join(working_directory, "data", "muscle.csv")
        df = pd.read_csv(simulation_results_filepath)

        # Plotting the results
        plt.figure(figsize=(12, 8))

        # Muscle length plot
        plt.subplot(3, 1, 1)
        plt.plot(df['Time'], df['Muscle_Length'], label='Muscle Length')
        plt.xlabel('Time (s)')
        plt.ylabel('Length (m)')
        plt.title('Muscle Length Over Time')
        plt.legend()

        # Muscle velocity plot
        plt.subplot(3, 1, 2)
        plt.plot(df['Time'], df['Muscle_Velocity'], label='Muscle Velocity', color='orange')
        plt.xlabel('Time (s)')
        plt.ylabel('Velocity (m/s)')
        plt.title('Muscle Velocity Over Time')
        plt.legend()

        # Muscle force plot
        plt.subplot(3, 1, 3)
        plt.plot(df['Time'], df['Total_Force'], label='Total Muscle Force', color='green')
        plt.xlabel('Time (s)')
        plt.ylabel('Force (N)')
        plt.title('Total Muscle Force Over Time')
        plt.legend()

        plt.tight_layout()
        plt.show()
    except:
        logger.error(f"An error occured:\n{traceback.print_exc()}")

if __name__ == "__main__":
    logger.info("Run directly")
    start_time = time.time()
    plot_simulation()
    end_time = time.time()
    execution_time = end_time - start_time
    execution_time_readable = str(datetime.timedelta(seconds=execution_time))
else:
    logger.info("Imported")