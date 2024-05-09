def print_severity(logger, severity, vulnerability):
    if severity == 10:
        logger.critical(vulnerability)
    if severity >= 7:
        logger.error(vulnerability)
    if severity < 7:
        logger.warning(vulnerability)