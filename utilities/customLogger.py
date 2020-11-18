import logging
import os

filename =  os.path.abspath("Logs/automation.log")
print(filename)

class LogGen:
    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
            logging.basicConfig(filename=filename,
                                format='%(asctime)s: %(levelname)s: %(message)s',force=True,
                                )
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            return logger