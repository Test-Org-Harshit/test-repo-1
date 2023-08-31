import json
import os


ukeys = set()
ll = []
d = {}
dd = {}

directory = os.path.join("c:\\","Users\\harshit.patel\\Desktop\\Comcast\\github-enterprise")
for root,dirs,files in os.walk(directory):
    for file in files:
       if file.endswith(".json"):
            f=open(file, 'r')
            for x in f:
                y = json.loads(x)

                for k, v in y.items():
                    dd[k] = v

                d.setdefault(y["action"], list()).append(str(y))
                
            nd = {}
            for k, v in d.items():
                nd[k] = list(v)


            # for k, v in dd.items():
            #     print(k + ", " + str(v))


            f.close()

for k, v in sorted(d.items()):
	print(k + ", " + str(v[0]))