
import logging

def get_logger(module_name):
	logger = logging.getLogger(module_name)
	#logger.setLevel(logging.CRITICAL)
	#logger.setLevel(logging.INFO)
	logger.setLevel(logging.DEBUG)

	fh = logging.FileHandler('.'.join((module_name, 'log')))
	fh.setLevel(logging.DEBUG)

	formatter = logging.Formatter('%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s')
	fh.setFormatter(formatter)

	logger.addHandler(fh)
	return logger
