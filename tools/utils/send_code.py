import ghasedakpack


def send_code(receptor: str, code):
    msg = f'سلام.\r\nکد ورود شما : {code}'

    sms = ghasedakpack.Ghasedak('5216b510de17fd67130c68970b835af4c9356fff42f1f83b05376f9e36d6a3ce')
    sms.send({'message': msg, 'receptor': receptor, 'linenumber': '50001212125380'})
