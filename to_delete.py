import pypx

pacs_settings = {
  'executable': '/usr/local/bin/echoscu',
  'aec': 'ORTHANC',
  'aet': 'CHIPS',
  'server_ip': '127.0.0.1',
  'server_port': '4242',
}

output = pypx.echo(pacs_settings)
print(output)

# output:
# {
#   'command': '/bin/echoscu --timeout 5  -aec MY-AEC -aet MY-AET 192.168.1.110 4242',
#   'data': '',
#   'status': 'success'
# }