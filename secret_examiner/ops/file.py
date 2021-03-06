"""
File Operations Module
"""
from os import listdir, rename, getcwd, mkdir
from os.path import isfile, join, isdir, exists
import logging
import sys
import json

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level=logging.WARN)
LOGGER = logging.getLogger("ops.file.File")
LOGGER.info("Hello from file module!!")


class File:
    """
    Class File
    """

    def __init__(self, path: str):
        """
        Constructor

        :param path: str    Input path where solutions are stored.
        """
        if exists(path):
            self.__path = path
        else:
            LOGGER.error("Path not found: {}".format(path))
            sys.exit(-1)

    def parse_path(self) -> list:
        """
        Parse input path to extract name and file name.
        :return: list   Returns metadata which is a list of tuples, [(name, file_name), ...].
        """
        metadata = []
        for f in listdir(self.__path):
            inner_path = join(self.__path, f)
            if len(listdir(inner_path)) > 1:
                LOGGER.error("Unwanted files found at {}.".format(inner_path))
                sys.exit(-1)
            try:
                inner_file = join(inner_path, listdir(inner_path)[0])
            except IndexError as ie:
                LOGGER.error("{} does not have any solution file.".format(f))
                sys.exit(-1)
            if isdir(inner_path) and isfile(inner_file) and "solution." in inner_file:
                metadata.append((f, inner_file))
            else:
                LOGGER.error("Unwanted files found at {} or {}.".format(f, inner_path))
                sys.exit(-1)
        return metadata

    def rename_folders(self, metadata: list, transformed_metadata: dict) -> None:
        """
        Renames the input folders to encrypted names.
        :param metadata: list               List of lists.
        :param transformed_metadata: dict   Transformed metadata obtained from encryptor module.
        :return: None
        """
        self.__write_mapping(self.__transform_mapping(transformed_metadata["encrypted_metadata"]))
        for i in range(len(metadata)):
            cwd = join(getcwd(), "input")
            LOGGER.debug("Renaming {} to {}."
                         .format(join(cwd, metadata[i][0]),
                                 join(cwd, transformed_metadata["encrypted_metadata"][i][1])))
            rename(join(cwd, metadata[i][0]), join(cwd, transformed_metadata["encrypted_metadata"][i][1]))

    @staticmethod
    def __write_mapping(encrypted_metadata: dict) -> None:
        """
        Writes a secret file.
        :param encrypted_metadata: dict
        :return: None
        """
        with open(".mapping", "w") as file:
            json.dump(encrypted_metadata, file, indent=2)

    @staticmethod
    def __transform_mapping(transformed_metadata: list) -> dict:
        res = {}
        """
        Tranforms the transformed metadata to be written in a mapping file.
        :param transformed_metadata: list   Transformed Metadata
        :return: dict                       Dictionary of name: encrypted file_name
        """
        for item in transformed_metadata:
            res[item[0]] = item[1]
        return res

    @staticmethod
    def write_output(transformed_dict: dict) -> None:
        """
        Writes the output.
        :param transformed_dict: dict
        :return: None
        """
        if not exists("output"):
            mkdir("output")
        with open("output/map.json", "w") as f:
            json.dump(transformed_dict, f, indent=2)


if __name__ == "__main__":
    file = File("input")
    p = file.parse_path()
    print(p)
