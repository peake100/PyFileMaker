from PyFileMaker import FMServer
import sys
import json

try:
    params = sys.argv[1]
except IndexError:
    params = ''

fm = FMServer('http://api:3dK3mperInterview@10.1.16.170')
fm.setDb('mh codebook')
fm.setLayout('jobqueue_api')

# print records
resp = fm.doScript('api_find_job', params=params)
resp = fm.toJSON(resp)
print(resp)
resp = json.dumps(fm.toJSON(resp))