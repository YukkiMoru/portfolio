import segno
qrcode = segno.make('https://yukkimoru.github.io/portfolio/', error='h')
qrcode.save('docs/assets/other/qr.svg', scale=10, dark='black')