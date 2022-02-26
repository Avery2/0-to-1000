import os

if __name__ == "__main__":
    with open("index.md", "x") as f:
        for i in range(1001):
            f.write(f"# {i}\n")