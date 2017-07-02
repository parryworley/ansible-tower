#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests


def main():


    fields = {
        "pan_api_key": {"required": True, "type": "str"},
        "pan_cmd": {"required": True, "type": "str"},
        "pan_api_url": {"required": True, "type": "str"},
    }
    module = AnsibleModule(argument_spec=fields)
    api_key = module.params['pan_api_key']
    cmd = module.params['pan_cmd']
    url = module.params['pan_api_url']

    payload = {"type": "op", "key": api_key, "cmd": cmd}

    r = requests.get(url, params=payload)
    if r.status_code == requests.codes.ok:
        result = {"response": r.text}
        module.exit_json(changed=False, meta=result)
    else:
        module.exit_json(msg="Something went wrong")


if __name__ == '__main__':
    main()
