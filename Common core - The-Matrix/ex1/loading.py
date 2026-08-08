import sys
try:
    import pandas
except ImportError:
    print("You need to install (pandas) "
          "you can install it using "
          "pip install pandas "
          "or"
          " poetry add pandas")
    sys.exit(1)
try:
    import matplotlib
except ImportError:
    print("You need to install (matplotlib) "
          "you can install it using "
          "pip install matplotlib "
          "or"
          " poetry add matplotlib")
    sys.exit(1)
try:
    import numpy
except ImportError:
    print("You need to install (numpy) "
          "you can install it using "
          "pip install numpy "
          "or"
          " poetry add numpy")
    sys.exit(1)

print("LOADING STATUS: Loading programs...")
print()
print("Checking dependencies:")
print(f"[OK] pandas {pandas.__version__} - Data manipulation ready")
print(f"[OK] numpy ({numpy.__version__}) - Numerical computation ready")
print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")

data = numpy.random.randint(
    low=0,
    high=100,
    size=1000
)

print()
print("Analyzing Matrix data...")
datafram = pandas.DataFrame({"Signal": data})

print(f"Processing {len(data)} data points...")


print("Generating visualization...")
datafram.plot()
matplotlib.pyplot.savefig("matrix_analysis.png")

print("Analysis complete!")
print("Results saved to: matrix_analysis.png")
