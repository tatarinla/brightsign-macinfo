## Description


**macinfo** - a library to get a company name by mac-address(and probably more).


<b>Please, add your api key to environment variables or hardcode it in api_client.py</b>

### Requirements

    python:

       -- version >= 3.8


    packages:

       -- wheel

       -- setuptools

       -- twine


### Installation


All commands should be run from the root directory.


1. Setup venv:


```python3 -m venv macinfo-venv```


```source macinfo/bin/activate```


2. Install required packages:


```python3 -m pip install -r requirements.txt```


3. Install the library:


```python3 setup.py bdist_wheel```

 

```pip install dist/<whl_file>```



### Using as a python library


After installation it's possible to import **macinfo** library to python scripts.


E.g. to use get_vendor() utility:


```from macinfo import get_vendor```


### Using as a cli tool
From the root directory:

```./lookup.sh <your_mac_address> ```

### Using with docker 
WARNING: this is not tested - my Ubuntu machine has died today morning, 
and trying to install docker on my son's old Macbook is too much pain.
1. Navigate to the /docker directory and build the image:

```docker build -t macinfo .```

2. Run the tool in container:
```docker run -e mac=<your_mac_address> -t macinfo```

### Running tests


All tests should be run from the root directory.


1. Run all tests:


```pytest -m tests```


2. Run particular suite:


```pytest -m tests/<suite_name>```


