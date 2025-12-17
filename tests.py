from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


def main():
    working_dir = "calculator"

    # root_contents = get_files_info(working_dir)
    # print(root_contents)
    #
    # pkg_contents = get_files_info(working_dir, "pkg")
    # print(pkg_contents)
    #
    # bin_contents = get_files_info(working_dir, "/bin")
    # print(bin_contents)
    #
    # other_contents = get_files_info(working_dir, "../")
    # print(other_contents)
    #
    # print(get_file_content(working_dir, "main.py"))
    # print(get_file_content(working_dir, "pkg/calculator.py"))
    # print(get_file_content(working_dir, "/bin/cat"))

    # print(write_file(working_dir, "lorem_fake.txt", "Lorem ipsum dolor sit amet, consectetur adipiscing elit."))
    # print(write_file(working_dir, "pkg/more_lorem.txt", "Lorem ipsum dolor sit amet, consectetur adipiscing elit."))
    # print(write_file(working_dir, "/tmp/temp.txt", "This should not be allowed."))

    print(run_python_file(working_dir, "tests.py"))
    print(run_python_file(working_dir, "../main.py"))
    print(run_python_file(working_dir, "nonexistent.py"))
    print(run_python_file(working_dir, "main.py", ["3 + 5"]))


if __name__ == "__main__":
    main()
