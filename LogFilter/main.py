import json
import os

from Domain.SettingsDomain import Settings
from FilterUtils import getFromFile, filterLog, saveLog, saveDict, collectUniqueFields
from Domain.LogDomain import Log

# TODO: logs

if __name__ == "__main__":
    settings = Settings.fromFile(os.path.join(os.getcwd(), "Settings.json"))

    log = getFromFile(settings.input_path)
    filtered_log = filterLog(log, settings)
    saveLog(filtered_log, settings.write_filtered_result.output_path)

    unique_fields = collectUniqueFields(filtered_log, settings)
    saveDict(unique_fields, settings.collect_unique_event_fields.output_path)

    print("END")
