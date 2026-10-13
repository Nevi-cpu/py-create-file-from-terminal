import datetime
import os
import sys


def main() -> None:
    dirs = []
    file_name = ""
    args = sys.argv[1:]
    current_flag = None

    for arg in args:
        if arg in ("-d", "-f"):
            current_flag = arg
            continue

        if current_flag == "-d":
            dirs.append(arg)
        elif current_flag == "-f":
            file_name = arg
            current_flag = None

    path = ""
    if dirs:
        path = os.path.join(*dirs)
        os.makedirs(path, exist_ok=True)

    if file_name:
        file_path = os.path.join(path, file_name) if path else file_name
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
