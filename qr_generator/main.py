import qrcode

def get_qrcode(url = 'www.vk.com', name = 'default'):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f'QR code was created! Open the {name}.png'

def main():
    print(get_qrcode(url='https://vk.com', name='vk'))

if __name__ == '__main__':
    main()
