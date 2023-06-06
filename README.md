# An Analysis of Crime in the Seattle Area

## Whether the project can be run directly in the Ed Workspace

Due to the dataset being very large, this project cannot be run directly in Ed Workspace.

## How to install required libraries

We had to install plotly to create the charts and kaleido to save the charts to files.

### plotly

1. Open Anaconda Navigator.
2. Click on Environments, then click on cse163.
3. Search packages for plotly. If the checkbox is not checked, check it and then click Apply.

### kaleido

Run the following commands in the Anaconda Prompt.

```
activate cse163
conda install -c conda-forge python-kaleido
```

## How to run the project's Python code

To run this project's Python code, first download the required dataset for this project by navigating [here](https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5), clicking "Export on the top right, then clicking "CSV."

Next, upload the dataset to the folder in this repository named "data".

At this point, you should be able to execute the code. In VS Code, open main.py, press Ctrl+Shift+P and select "Python: Run Python File in Terminal".
