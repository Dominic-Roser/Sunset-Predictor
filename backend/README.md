# Activate Virtual Environment (maybe) ask first

To activate run the following:

Windows

`sunset-env/bin/activate`

macOS/Linux

`source sunset-env/bin/activate`

When active your terminal will display a prefix

`(sunset-env) <your source filepath>`

# Download Python
[Python 3.11.9](https://www.python.org/downloads/release/python-3119/)

# **Download TensorFlow**

[TensorFlow 2.16.1 full instructions](https://www.tensorflow.org/install/pip#linux)

## MacOS

Ensure that the venv is 

`python3 -m pip install tensorflow`

Verify the installation:

`python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"`


## Windows/Linux

`python3 -m pip istall tensorflow[and-cuda]`

Verify the installation:

`python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`


# Download Django

## Windows 

`py -m pip install Django`

## Linux/MacOS

`python3 -m pip install Django`

# Verify installation 

To check the modules you have downloaded

`pip3 list`

# Running files 

Occasionally due to vscode run configurations, it will run the local python kernel in the venv. :( to fix this just run 

`python3 <filepath>`

instead of the local python filepath

# Download Weather Forecast API

## Install:

`pip install openmeteo-requests`

`pip install requests-cache retry-requests numpy pandas`

For more information go to (https://open-meteo.com/en/docs)

