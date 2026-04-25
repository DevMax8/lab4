import os
LAB_DATA_DIR_NAME = "lab_data"
LOGS_DIR_NAME = "logs"
def main():
    os.mkdir(LAB_DATA_DIR_NAME)
    if not os.path.exists(LAB_DATA_DIR_NAME):
        print(f"directory was not created {LAB_DATA_DIR_NAME}")
        exit(1)
    os.chdir(LAB_DATA_DIR_NAME)
    os.mkdir(LOGS_DIR_NAME)
    if not os.path.exists(LOGS_DIR_NAME):
        print(f"directory was not created {LOGS_DIR_NAME}")
        exit(1)
    os.chdir(LOGS_DIR_NAME)
    os.mkdir(LAB_DATA_DIR_NAME)
if __name__ == '__main__':
    main()
