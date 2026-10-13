import sys
import os


def main() -> None:
    file_name = None
    path = None

    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        start = d_index + 1
        end = len(sys.argv)

        if "-f" in sys.argv:
            f_index = sys.argv.index("-f")
            if f_index > d_index:
                end = f_index

        dirs = sys.argv[start:end]
        path = os.path.join(*dirs)
        os.makedirs(path, exist_ok=True)

    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]

        if path:
            file_name = os.path.join(path, file_name)

    print(file_name)


if __name__ == "__main__":
    main()
