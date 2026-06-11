import importlib
import sys

DEPENDENCIES = [
    ("pandas", "Data manipulation ready"),
    ("numpy", "Numerical computation ready"),
    ("matplotlib", "Visualization ready"),
]


def check_package(dependency: tuple[str, str]) -> bool:
    name, message = dependency
    try:
        module = importlib.import_module(name)
    except ImportError:
        print(f"[MISSING] {name} - install required")
        return False

    version = getattr(module, "__version__", "unknown")
    print(f"[OK] {name} ({version}) - {message}")
    return True


def check_dependencies() -> bool:
    print("Checking dependencies:")
    results = [check_package(dependency) for dependency in DEPENDENCIES]
    return all(results)


def print_install_instructions() -> None:
    print()
    print("Missing dependencies detected.")
    print()
    print("Install with pip:")
    print("pip install -r requirements.txt")
    print()
    print("Or install with Poetry:")
    print("poetry install")


def analyze_matrix_data() -> None:
    import matplotlib.pyplot as plt
    import numpy
    import pandas

    print("Analyzing Matrix data...")
    signals = numpy.random.normal(size=1000)
    data = pandas.DataFrame({"signal": signals})

    print("Processing 1000 data points...")
    average = data["signal"].mean()
    maximum = data["signal"].max()
    minimum = data["signal"].min()
    print(f"Average signal: {average:.2f}")
    print(f"Maximum signal: {maximum:.2f}")
    print(f"Minimum signal: {minimum:.2f}")

    print("Generating visualization...")
    plt.figure()
    plt.hist(data["signal"], bins=30)
    plt.title("Matrix Signal Distribution")
    plt.xlabel("Signal")
    plt.ylabel("Frequency")
    plt.savefig("matrix_analysis.png")
    plt.close()

    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    is_installed = check_dependencies()
    if not is_installed:
        print_install_instructions()
        sys.exit(1)
    print()

    analyze_matrix_data()


if __name__ == "__main__":
    main()
