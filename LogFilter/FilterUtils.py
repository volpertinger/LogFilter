import json

from Domain.SettingsDomain import Settings
from Domain.LogDomain import Log


def getFromFile(path: str):
    input_file = open(path)
    input_json = json.load(input_file)
    input_file.close()
    return Log(input_json)


def filterLog(log: Log, settings: Settings):
    result = Log()

    for event in log.event_list.event:
        pass

    return result


def saveLog(log: Log, path: str):
    tmp = log.__dict__()
    json_str = json.dumps(tmp)
    file = open(path, "w+")
    file.write(json_str)
    file.close()