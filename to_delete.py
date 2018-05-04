import pypx

pacs_settings = {
  'executable': '/usr/local/bin/px-find',
  'aec': 'CHIPS',
  'aet': 'CHIPS',
  'server_ip': '192.168.0.1',
  'server_port': '4242',
}

output = pypx.find(pacs_settings)
print(output)

# output:
# {
#   'command': '/bin/echoscu --timeout 5  -aec MY-AEC -aet MY-AET 192.168.1.110 4242',
#   'data': '',
#   'status': 'success'
# }
