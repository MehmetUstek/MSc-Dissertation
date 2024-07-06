def print_severity(logger, severity, vulnerability_detail):
    if isinstance(severity,int):
        if severity >= 9:
            logger.critical(vulnerability_detail)
        elif severity >= 6:
            logger.error(vulnerability_detail)
        elif severity < 6:
            logger.warning(vulnerability_detail)
    else:
        if severity == "CRITICAL":
            logger.critical(vulnerability_detail)
        elif severity >= "HIGH":
            logger.error(vulnerability_detail)