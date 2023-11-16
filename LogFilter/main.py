import json
import os

from Domain.SettingsDomain import Settings
from FilterUtils import (
    getFromFile,
    filterLog,
    collectUniqueFields,
    outputLogProcessing,
    outputDictProcessing,
)
from Domain.LogDomain import Log
from MalwareDetectionIntegration import detectionProcessing


if __name__ == "__main__":
    settings = Settings.fromFile(os.path.join(os.getcwd(), "Settings.json"))

    log = getFromFile(settings.input_path)
    filtered_log = filterLog(log, settings)
    outputLogProcessing(
        filtered_log,
        settings.write_filtered_result.output_path,
        settings.write_options,
        settings.write_filtered_result.enabled,
    )

    unique_event_fields = collectUniqueFields(
        settings.collect_unique_event_fields.fields, filtered_log.event_list.event
    )
    outputDictProcessing(
        unique_event_fields,
        settings.collect_unique_event_fields.output_path,
        settings.write_options,
    )

    unique_process_fields = collectUniqueFields(
        settings.collect_unique_process_fields.fields, filtered_log.process_list.process
    )
    outputDictProcessing(
        unique_process_fields,
        settings.collect_unique_process_fields.output_path,
        settings.write_options,
    )

    detect_result = detectionProcessing(filtered_log.event_list.event, settings)
    if detect_result is not None:
        print(f"Detected nalware with PID {detect_result}")
    else:
        print("There is no malware in events")