#!/usr/bin/python 
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule  

def main(): 
    module = AnsibleModule( 
        argument_spec=dict( 
        db_name    = dict(required=True, type=’str’), 
        request    = dict(required=True, type=’str’), 
        ) 
    )

db_name_local = module.params.get(’db_name’) 
request_local = module.params.get(’request’)

import MySQLdb

db = MySQLdb.connect(db=db_name_local) 
cur = db.cursor() 
cur.execute(request_local) 
results = cur.fetchall() 
db.close()

module.exit_json(changed=False, resultat=results)  

if __name__ == "__main__": 
    main()
