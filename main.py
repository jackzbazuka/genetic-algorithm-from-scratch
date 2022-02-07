from models import Container


def main() -> None:
    cool_container = Container(0.2, 0.5, 0.6, 1000, 10)
    cool_container.run_evolution()


if __name__ == "__main__":
    main()
