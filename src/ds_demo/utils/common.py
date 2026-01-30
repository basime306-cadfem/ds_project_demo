import os
from pathlib import Path
import yaml
import json
from src.ds_demo import logger
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from box.exceptions import BoxValueError
import joblib

@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:

    """This function loads yaml file,
    and put in a config box
    """
    try:
        with open(path) as yaml_f:
            content = yaml.safe_load(yaml_f)
            logger.info("yaml file: {path} loaded")

    except BoxValueError:
        raise ValueError("Yaml file is empty")
    
    except Exception as e:
        raise e
@ensure_annotations
def create_directories(list_of_paths: list, verbose=True) -> None:
    """##Create directories 
    Args: List of paths : Path
    Output: None
    """
    for path in list_of_paths:
        os.makedirs(path, exist_ok=True)

        if verbose:
            logger.info('Directory created at {path}')
@ensure_annotations
def load_json(path_to_json: Path) -> ConfigBox:
    """## Load json file -> config box
    Args: Path
    Return: Configbox(content)
    """
    with open(path_to_json) as f:
        data=json.load(f)
    logger.info(f"Json file loaded from {path_to_json}")
    return ConfigBox(data)
@ensure_annotations
def save_json(path: Path, data:dict) -> None:
    """## Saved the given dict data to a json at specified location
    Args: Save path, data
    Return: None
    """

    with open(path, "w") as f:
        json.dump(f, data, indent=4)

    logger.info(f"The json file saved at {path}")

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

    
    



#load_json
#save_json
#load_bin
#save_bin

    


