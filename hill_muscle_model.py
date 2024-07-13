# hill_muscle_model\hill_muscle_model.py
import os
import time
import datetime
import traceback

import util

script_name = os.path.splitext(os.path.basename(__file__))[0]
logger = util.setup_logging(script_name)

class HillMuscle:
    def __init__(self, max_isometric_force, optimal_length, max_velocity, series_elasticity, parallel_elasticity):
        self.F0 = max_isometric_force  # Maximum isometric force
        self.L0 = optimal_length       # Optimal length
        self.V0 = max_velocity         # Maximum contraction velocity
        self.Kse = series_elasticity   # Series elastic stiffness
        self.Kpe = parallel_elasticity # Parallel elastic stiffness

    def total_force(self, length, velocity):
        # Contractile element force
        F_ce = self.F0 * (1 - velocity / self.V0)
        # Series elastic element force
        F_se = self.Kse * (length - self.L0)
        # Parallel elastic element force
        F_pe = self.Kpe * (length - self.L0) if length > self.L0 else 0
        
        # Total muscle force
        return F_ce + F_se + F_pe

def hill_muscle_model():
    try:
        max_isometric_force = 1500  # N
        optimal_length = 0.3        # m
        max_velocity = 1.2          # m/s
        series_elasticity = 2000    # N/m
        parallel_elasticity = 1000  # N/m

        muscle = HillMuscle(max_isometric_force, optimal_length, max_velocity, series_elasticity, parallel_elasticity)

        muscle_length = 0.32  # m
        muscle_velocity = 0.5 # m/s

        total_force = muscle.total_force(muscle_length, muscle_velocity)
        logger.info(f"total_force={total_force}")
    except:
        logger.error(f"An error occured:\n{traceback.print_exc()}")

if __name__ == "__main__":
    logger.info("Run directly")
    start_time = time.time()
    hill_muscle_model()
    end_time = time.time()
    execution_time = end_time - start_time
    execution_time_readable = str(datetime.timedelta(seconds=execution_time))
else:
    logger.info("Imported")