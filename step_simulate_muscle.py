# hill_muscle_model\step_simulate_muscle.py
import os
import time
import datetime
import traceback
import json

import numpy as np
import pandas as pd

import util
from hill_muscle_model import HillMuscle

script_name = os.path.splitext(os.path.basename(__file__))[0]
logger = util.setup_logging(script_name)

def step_simulate_muscle():
    try:
        working_directory = util.get_working_directory()
        with open(os.path.join(working_directory, "hill_muscle_inputs.json"), "r") as hill_muscle_inputs_file:
            hill_muscle_inputs = json.load(hill_muscle_inputs_file)

        time = np.linspace(0, 10, 500)  # 10 seconds, 500 time points
        muscle_length = hill_muscle_inputs['optimal_length'] + 0.05 * np.sin(2 * np.pi * 0.5 * time)  # Sinusoidal length change
        muscle_velocity = np.gradient(muscle_length, time)  # Velocity is the derivative of length

        logger.info("Generated muscle")
        muscle = HillMuscle(
            hill_muscle_inputs['max_isometric_force'],
            hill_muscle_inputs['optimal_length'],
            hill_muscle_inputs['max_velocity'],
            hill_muscle_inputs['series_elasticity'],
            hill_muscle_inputs['parallel_elasticity']
        )

        # Calculate the total force at each time step
        total_force = np.array([muscle.total_force(l, v) for l, v in zip(muscle_length, muscle_velocity)])
        # logger.info(f"total_force={total_force}")

        df = pd.DataFrame({
            'Time': time,
            'Muscle_Length': muscle_length,
            'Muscle_Velocity': muscle_velocity,
            'Total_Force': total_force
        })
        logger.info(f"df:\n{df.head(1)}")

        simulation_results_filepath = os.path.join(working_directory, "data", "muscle.csv")
        df.to_csv(simulation_results_filepath, index=False)
        logger.info(f"Muscle simulation saved to {simulation_results_filepath}")
    except:
        logger.error(f"An error occured:\n{traceback.print_exc()}")

if __name__ == "__main__":
    logger.info("Run directly")
    start_time = time.time()
    step_simulate_muscle()
    end_time = time.time()
    execution_time = end_time - start_time
    execution_time_readable = str(datetime.timedelta(seconds=execution_time))
else:
    logger.info("Imported")