from loguru import logger

logger.add(
    "logs/extraction.log",
    rotation="5 MB",
    level="INFO"
)

logger.info("Resume Extraction Engine Started")