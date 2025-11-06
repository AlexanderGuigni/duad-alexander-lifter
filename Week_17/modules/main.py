from data import Data
from interface import Interface

def main():
    data = Data()
    interface = Interface(data)
    interface.open_main_window()

if __name__ == "__main__":
    main()