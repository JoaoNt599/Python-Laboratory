import pickle


def config(property_name: str, serial_number: str, mac_adress: str) -> None:
    file = open('config.dat', 'w+b')
    register = {
        'property_name': property_name,
        'serial_number': serial_number,
        'mac_adress': mac_adress
    }

    pickle.dump(register, file)
    file.close()


if __name__ == "__main__":
    config('John', '1234-5', '19:04:73:8c:4d:a8')