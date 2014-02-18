# -*- encoding: utf-8 -*-
import json;
stri = '{"id":2345, "name":"zhangsong", "grade":{"yuwen":60, "shuxue":70}}';
text = json.loads(stri);
print("id is {0} name is {1} yuwen.grade is {2} shuxue.grade is {3}".format(text["id"], text["name"], text["grade"]["yuwen"], text["grade"]["shuxue"]));
