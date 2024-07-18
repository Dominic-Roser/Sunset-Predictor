# Download Python
[Python 3.11.9](https://www.python.org/downloads/release/python-3119/)

# **Download TensorFlow**

[TensorFlow 2.16.1 full instructions](https://www.tensorflow.org/install/pip#linux)

## MacOS

`python3 -m pip install tensorflow`

Verify the installation:

`python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"`


## Windows

`python3 -m pip istall tensorflow[and-cuda]`

Verify the installation:

`python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`


## Linux

`python3 -m pip install tensorflow[and-cuda]`

Verify the installation:

`python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

# Download Django 5.0.7

## Windows 

`py -m pip install Django==5.0.7`

## Linux/MacOS

`python -m pip install Django==5.0.7`

