def print_severity(logger, severity, vulnerability):
    if severity == 10:
        logger.critical(vulnerability)
    elif severity >= 6:
        logger.error(vulnerability)
    elif severity < 6:
        logger.warning(vulnerability)