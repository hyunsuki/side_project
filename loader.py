import json

class CsvLoader:
    def __init__(self, sep = ','):
        self.sep = sep

    def load(self, file_path):
        with open(file_path, 'r') as f:
            for line in f:
                value = line.strip()
                if value == '': continue
                yield value.split(self.sep)

class JsonManager:

    def __init__(self, indent = '\t'):
        self.indent = indent

    def saveJsonString(self, topic_name, data_dict):
        with open('conf/sdk/%s_%s.json'%(topic_name, data_dict['eventdate'].split(' ')[0]), 'a') as f:
            f.write('%s\n' %  json.dumps(data_dict))

def main():
    jm = JsonManager()
    jm.loadJson('conf/installInfos_2022-04-08.json')

if __name__ == '__main__':
    main()
