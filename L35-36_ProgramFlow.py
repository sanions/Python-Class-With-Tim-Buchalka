
ipAddress = str(input('Please enter an IP Address: '))

character = ''
segment = 1
segment_length = 0


if ipAddress[-1] != '.':
    ipAddress += '.'


for character in ipAddress:
    if character == '.':
        print('Segment {} is {} characters long.'.format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

