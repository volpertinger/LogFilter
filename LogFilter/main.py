import imp
import json
import os

from Domain.SettingsDomain import Settings
from FilterUtils import getFromFile, filterLog, saveLog
from Domain.LogDomain import Log

# TODO: logs

if __name__ == "__main__":
    settings = Settings.fromFile(os.path.join(os.getcwd(), "Settings.json"))

    log = getFromFile(settings.log_path)
    filtered_log = filterLog(log, settings)
    saveLog(filtered_log, settings.output_path)

    print("END")
