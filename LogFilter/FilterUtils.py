import json
from tokenize import String

from Domain.SettingsDomain import EventFilter, ProcessFilter, Settings, NodeSetting
from Domain.LogDomain import Log, Event, Process


def getFromFile(path: str):
    input_file = open(path)
    input_json = json.load(input_file)
    input_file.close()
    return Log(input_json)


def filterLog(log: Log, settings: Settings):
    result = Log()

    if settings.event_filter.enabled:
        for event in log.event_list.event:
            if isEventInFilter(event, settings.event_filter):
                result.addEvent(event)

    if settings.process_filter.enabled:
        for process in log.process_list.process:
            if isProcessInFilter(process, settings.process_filter):
                result.addProcess(process)

    return result


def saveLog(log: Log, path: str):
    tmp = log.__dict__()
    json_str = json.dumps(tmp)
    file = open(path, "w+")
    file.write(json_str)
    file.close()


def isFieldInFilter(field: String, node_setting: NodeSetting):
    if node_setting.enabled:
        if node_setting.include:
            return field in node_setting.data
        return not field in node_setting.data
    return True


def isEventInFilter(event: Event, filter: EventFilter):
    return (
        isFieldInFilter(event.opeartion, filter.operation_filter)
        and isFieldInFilter(event.pid, filter.pid_filter)
        and isFieldInFilter(event.process_index, filter.process_index_filter)
        and isFieldInFilter(event.process_name, filter.process_name_filter)
    )


def isProcessInFilter(process: Process, filter: ProcessFilter):
    return (
        isFieldInFilter(process.command_line, filter.command_line_filter)
        and isFieldInFilter(process.company_name, filter.company_name_filter)
        and isFieldInFilter(process.is_virtualized, filter.is_virtualized_filter)
        and isFieldInFilter(process.process_id, filter.process_id_filter)
        and isFieldInFilter(process.process_name, filter.process_name_filter)
    )