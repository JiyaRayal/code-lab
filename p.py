import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#DATA   
x = np.array([-1.0,0.0,1.0,2.0,3.0,4.0], dtype=float)
y = np.array([-1.0,1.0,3.0,5.0,7.0,9.0], dtype=float)

# MODAL
model= tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

#COMPILE
model.compile(optimizer = 'sgd', loss = 'mean_squared_error')

# TRAIN
history = model.fit(x,y, epochs = 500, verbose = False)

print(model.predict(np.array([[10.0]])))

# VISUALIZATION
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.plot(history.history['loss'])
plt.show()