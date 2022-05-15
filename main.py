from models import Container


def main() -> None:
    """Driver code"""
    cool_container = Container(0.2, 0.9, 0.8, 1000, 300)
    cool_container.run_evolution()


if __name__ == "__main__":
    main()
