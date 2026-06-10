import os
import site
import sys


def main() -> None:
    print()
    is_env = sys.prefix != sys.base_prefix
    if is_env:
        print("MATRIX STATUS: Welcome to the construct")
    else:
        print("MATRIX STATUS: You're still plugged in")

    print()
    print(f"Current Python: {sys.executable}")

    env_path = sys.prefix
    if is_env:
        env_name = os.path.basename(env_path)
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        packages = site.getsitepackages()
        for package in packages:
            print(package)
    else:
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
