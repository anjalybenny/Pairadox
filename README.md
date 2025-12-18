#  Project Setup Guide

Follow these steps to get the Pairadox fuzzy logic environment running on your machine.

## 1. Clone the Repository

Open your terminal (Mac/Linux) or Command Prompt (Windows). Choose one of the options below to download the code:

### Option A: HTTPS (Recommended for most)
Use this if you haven't set up SSH keys.
```bash
git clone [https://github.com/anjalybenny/Pairadox.git](https://github.com/anjalybenny/Pairadox.git)
```

### Option B: SSH (Secure)
Use this only if you have added your SSH public key to GitHub.
```bash
git clone git@github.com:anjalybenny/Pairadox.git
```

Then, move into the project folder:
```bash
cd Pairadox
```

## 2. Create the Virtual Environment

We use a virtual environment to manage our specific libraries (scikit-fuzzy, numpy, etc.) without messing up your system Python.

**Windows:**
```bash
python -m venv venv
```

**Mac / Linux:**
```bash
python3 -m venv venv
```

## 3. Activate the Environment

**Important:** You must do this every time you open a new terminal to work on the project. You know it works when you see `(venv)` appear at the start of your command line.

**Windows:**
```bash
venv\Scripts\activate
```

**Mac / Linux:**
```bash
source venv/bin/activate
```

## 4. Install Dependencies

Once the environment is active (look for the `(venv)` tag), install the required libraries:
```bash
pip install -r requirements.txt
```


##  Managing Dependencies

If you install a new library while working (e.g., `pip install pandas`):

1. **Update the list:**
   ```bash
   pip freeze > requirements.txt
   ```
2. **Commit the change:**
   ```bash
   git add requirements.txt
   git commit -m "Added pandas to requirements"
   ```

If you pull code and it stops working:
* **Re-sync your libraries:**
   ```bash
   pip install -r requirements.txt
   ```