import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

from box import ConfigBox
from pathlib import Path
import yaml
from cnnClassifier import logger
from box.exceptions import BoxValueError

def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty or has invalid content.
        Exception: For any other unexpected errors.

    Returns:
        ConfigBox: The content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file loaded successfully from: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("The YAML file is empty or has invalid structure.")
    except Exception as e:
        logger.error(f"An error occurred while reading the YAML file: {e}")
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: List[str], verbose: bool = True) -> None:
    """
    Creates a list of directories if they do not exist.

    Args:
        path_to_directories (List[str]): A list of directory paths to create.
        verbose (bool, optional): If True, logs the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """
    Saves data to a JSON file.

    Args:
        path (Path): The path where the JSON file will be saved.
        data (dict): The dictionary data to save into the JSON file.
    """
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        logger.info(f"JSON file saved at: {path}")
    except Exception as e:
        logger.error(f"Failed to save JSON file at {path}. Error: {e}")
        raise