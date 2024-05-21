def print_severity(logger, severity, vulnerability):
    if isinstance(severity,int):
        if severity == 10:
            logger.critical(vulnerability)
        elif severity >= 6:
            logger.error(vulnerability)
        elif severity < 6:
            logger.warning(vulnerability)
    else:
        if severity == "CRITICAL":
            logger.critical(vulnerability)
        elif severity >= "HIGH":
            logger.error(vulnerability)