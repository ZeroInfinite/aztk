import sys
from install import install

def run():
    if len(sys.argv) < 2:
        print("Error: Expected at least one argument")
        exit(1)

    action = sys.argv[1]

    if action == "setup-node":
        print("Setup node??", sys.argv)
        install.setup_node(sys.argv[2])
    elif action == "setup-spark-container":
        install.setup_spark_container()
    else:
        print("Action not supported")


if __name__ == "__main__":
    run()
