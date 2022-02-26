import os

if __name__ == "__main__":
    with open("0-to-1000-slides.md", "x") as f:
        for i in range(1001):
            f.write(f"# {i}\n")