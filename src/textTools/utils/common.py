import os
from pathlib import Path
from typing import Any
import yaml
from box import ConfigBox, BoxValueError
from ensure import ensure_annotations
from textTools.logging import configure_logger, get_logger

# Initialize logger
configure_logger()
logger = get_logger("textToolsLogger")


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads YAML file and returns its content as a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox.

    Raises:
        ValueError: If the YAML file is empty.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if not content:
                raise ValueError("YAML file is empty")
            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)
    except (FileNotFoundError, yaml.YAMLError) as e:
        logger.error(f"Error loading YAML file: {e}")
        raise


@ensure_annotations
def create_directories(paths: list, verbose: bool = True):
    """Create directories specified in the list.

    Args:
        paths (list): List of paths for directories to be created.
        verbose (bool, optional): Whether to log creation of each directory. Defaults to True.
    """
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """Get size of a file in kilobytes.

    Args:
        path (Path): Path of the file.

    Returns:
        str: Size of the file in kilobytes.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
