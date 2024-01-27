import numpy as np

# creating array of size 20
random_vector = np.random.uniform(1, 20, 20)
print("Random Vector : \n", random_vector)

# reshape the array to 4 by 5
random_vector = random_vector.reshape(4,5)
print("after reshaping (4 by 5): \n", random_vector)

# replace the max in each row
random_vector[np.arange(len(random_vector)), random_vector.argmax(1)] = 0
print("Replacing the max in each row : \n", random_vector)