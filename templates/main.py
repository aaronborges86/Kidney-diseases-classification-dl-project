import sys
import os

# Add src directory to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from cnnClassifier import logger

logger.info("Logging initialized successfully!")
