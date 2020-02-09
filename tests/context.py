import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from secret_examiner.ops.file import File
from secret_examiner.processor.encryptor import Encryptor
