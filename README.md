# pyspark_for_dummies_and_experts
Repository for the pyspark course for dummies and experts

How to use it locally
----------------------

To be able to work in your own PC, it is necessary to have an IDE as a development environment as well as to have the environment prepared.

1. Clone the repository using git.
```bash
https://github.com/javiermolinag/pyspark_for_dummies_and_experts.git
```
2. We recommend to have python 3.9. Create a virtual environment called venv with:
```bash
python -m venv venv
```

3. Activate the virtual environment with
```bash
venv\Scripts\activate
```

4. Install dependencies with
```bash
python -m pip install -r requirements.txt
```

5. Using the following command in the terminal you can work with the notebooks: 
```bash
jupyter-notebook
```
6. If you cannot see the spylon kernel (scala) use
```bash
python -m spylon_kernel install
```