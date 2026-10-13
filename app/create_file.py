import datetime
import os
import sys


def main() -> None:
    args = sys.argv[1:]
    dirs = []
    file_name = None

    if "-d" in args:
        d_idx = args.index("-d")
        for arg in args[d_idx + 1:]:
            if arg.startswith("-"):
                break
            dirs.append(arg)

    if "-f" in args:
        f_idx = args.index("-f")
        file_name = args[f_idx + 1]

    dir_path = ""
    if dirs:
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)

    if file_name:
        file_path = os.path.join(dir_path, file_name) if dir_path else file_name

        with open(file_path, "a") as f:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{now}\n")
            line_count = 1
            while True:
                line = input("Enter content line: ")
                if line == "stop":
                    break
                f.write(f"{line_count} {line}\n")
                line_count += 1
            f.write("\n")


if __name__ == "__main__":
    main()
