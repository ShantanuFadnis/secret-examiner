"""
Encryptor Module
"""
import logging
import hashlib
from random import choice, random

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level=logging.WARN)
LOGGER = logging.getLogger("processor.encryptor.Encryptor")
LOGGER.info("Hello from encryptor module!!")


class Encryptor:
    """
    Class Encryptor
    """

    def __init__(self):
        """Constructor"""
        pass

    def transform(self, metadata: list) -> dict:
        """
        Encrypts the metadata.

        :param metadata: list   List of tuples, [(name, file_name), ...].
        :return: dict           Returns transformed metadata.
        """
        transformed_metadata = {}
        transformed_dict = {}
        encrypted_metadata = [(name, self.__encrypt(file_name)) for name, file_name in metadata]
        for data in encrypted_metadata:
            temp = encrypted_metadata.copy()
            temp.remove(data)
            encrypted_file_names = [data[1] for data in temp]
            transformed_dict[data[0]] = self.__get_random_files(encrypted_file_names)
        transformed_metadata["encrypted_metadata"] = encrypted_metadata
        transformed_metadata["transformed_dict"] = transformed_dict
        return transformed_metadata

    @staticmethod
    def __get_random_files(f: list) -> list:
        """
        Generates a list of random encrypted file names.

        :param f: list  List of file names.
        :return: list   Returns a list of 2 or 3 encrypted file names.
        """
        res = set()
        size = len(f) if len(f) <= 2 else 3
        while len(res) != size:
            res.add(choice(f))
        return list(res)

    @staticmethod
    def __encrypt(file_name: str) -> str:
        """
        MD5 encryption.

        :param file_name: str   File name.
        :return: str            Encrypted file name.
        """
        file_name = file_name + str(random())
        return hashlib.md5(file_name.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    temp_metadata = [('bob', 'input/Bob/solution.txt'),
                     ('alice', 'input/Alice/solution.txt'),
                     ('charlie', 'input/Charlie/solution.txt'),
                     ('david', 'input/David/solution.txt'),
                     ('john', 'input/John/solution.txt')]
    temp_res = Encryptor().transform(temp_metadata)
    import json

    print(json.dumps(temp_res, indent=2))
    temp_metadata = [('bob', 'input/Bob/solution.txt'),
                     ('alice', 'input/Alice/solution.txt'),
                     ('charlie', 'input/Charlie/solution.txt')]
    temp_res = Encryptor().transform(temp_metadata)
    import json

    print(json.dumps(temp_res, indent=2))
    temp_metadata = [('bob', 'input/Bob/solution.txt'),
                     ('alice', 'input/Alice/solution.txt')]
    temp_res = Encryptor().transform(temp_metadata)
    import json

    print(json.dumps(temp_res, indent=2))
