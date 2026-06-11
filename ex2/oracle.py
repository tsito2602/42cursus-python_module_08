import os
from dotenv import load_dotenv


def print_database_status(
    matrix_mode: str | None,
    database_url: str | None,
) -> None:
    if not database_url:
        print("Database: Missing DATABASE_URL")
    elif matrix_mode == "development":
        print("Database: Connected to local instance")
    elif matrix_mode == "production":
        print("Database: Connected to production instance")
    else:
        print("Database: Mode unknown - connection not selected")


def print_zion_status(
    zion_endpoint: str | None,
    api_key: str | None,
) -> None:
    if not zion_endpoint:
        print("Zion Network: Offline - Missing ZION_ENDPOINT")
    elif not api_key:
        print("Zion Network: Offline - Missing API_KEY")
    else:
        print("Zion Network: Online")


def main() -> None:
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    load_dotenv()
    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")

    if matrix_mode:
        print(f"Mode: {matrix_mode}")
    else:
        print("Mode: Missing MATRIX_MODE")
    print_database_status(matrix_mode, database_url)

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API_KEY")

    print(f"Log Level: {log_level}")
    print_zion_status(zion_endpoint, api_key)


if __name__ == "__main__":
    main()
