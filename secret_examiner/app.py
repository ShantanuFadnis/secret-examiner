"""
Secret Examiner App
"""
from ops.file import File
from processor.encryptor import Encryptor
import logging
import sys

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level=logging.INFO)
LOGGER = logging.getLogger("Secret Examiner")
LOGGER.info("Hello from Secret Examiner App.")

if __name__ == "__main__":
    file = File("input")
    metadata = file.parse_path()
    enc = Encryptor()
    transformed_metadata = enc.transform(metadata)
    file.rename_folders(metadata, transformed_metadata)
    file.write_output(transformed_metadata["transformed_dict"])
    sys.exit(0)
