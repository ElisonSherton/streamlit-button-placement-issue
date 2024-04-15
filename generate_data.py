import pandas as pd
import numpy as np
import random

random.seed(10)

num_samples = 21

chemical1_concentration = [random.random() for _ in range(num_samples)]
chemical2_concentration = [random.random() for _ in range(num_samples)]
chemical3_concentration = [random.random() for _ in range(num_samples)]

time_days = np.linspace(0, 1, num_samples).tolist()
dose = np.linspace(0, 2, num_samples).tolist()

df = pd.DataFrame(
    {
        "chemical1": chemical1_concentration,
        "chemical2": chemical2_concentration,
        "chemical3": chemical3_concentration,
        "days": time_days,
        "dose": dose,
    }
)

df.to_csv("data.csv", index = False)