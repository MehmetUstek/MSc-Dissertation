def print_severity(logger, severity, vulnerability):
    if severity == 10:
        logger.critical(vulnerability)
    elif severity >= 7:
        logger.error(vulnerability)
    elif severity < 7:
        logger.warning(vulnerability)