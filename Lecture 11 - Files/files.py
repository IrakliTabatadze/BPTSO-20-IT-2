

create_file = open('/var/log/test.txt', 'x')

print(create_file.readable())
print(create_file.writable())



####################################################
# Read
####################################################

readable_file = open('test.txt', 'r')

print(readable_file.readable())
print(readable_file.writable())

print(readable_file.read())
print(readable_file.readline())
print(readable_file.readline())
print(readable_file.readline())
print(readable_file.readlines())

print(readable_file.closed)
readable_file.close()
print(readable_file.closed)


readable_file = open('test1.txt', 'r')
print(readable_file.read())



####################################################
# Write
####################################################

writable_file = open('writable.txt', 'w') # r+ for read and write
print(writable_file.writable())
print(writable_file.readable())

print(writable_file.read())

writable_file.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nNam ac magna condimentum, molestie urna quis, molestie nunc. \nAenean varius interdum justo, et fermentum risus imperdiet sit amet. Aenean ac condimentum nunc, pulvinar malesuada ante. Nunc non urna vitae augue molestie gravida eu sit amet magna. Nunc id consequat enim. Ut id fermentum nisl, id rhoncus velit. Nam gravida dignissim sem vel dictum. Pellentesque eu dolor varius, fringilla lorem ut, fermentum dolor. Donec finibus enim ex.Praesent dapibus ac felis eget tempor. Suspendisse vulputate nibh ac feugiat pretium. Suspendisse rutrum viverra sem, blandit vehicula tellus commodo mattis. Mauris id scelerisque nibh, id interdum sapien. In bibendum, sem id sollicitudin tincidunt, velit purus tristique mauris, id mattis metus metus quis est. Morbi viverra vel odio ut molestie. Ut semper quam et nibh maximus lobortis. Nullam finibus neque vel consequat blandit.Cras sed blandit nisl, a luctus enim. Duis sit amet velit ante. Sed porttitor aliquet scelerisque. Cras eget laoreet orci. Aenean eget convallis velit, vitae elementum massa. Quisque justo nisi, iaculis at facilisis id, viverra eu eros. Donec hendrerit quis dolor ut auctor. Phasellus ac tristique purus. Phasellus in nisi at velit pellentesque volutpat. Morbi vestibulum porta justo ut gravida. Vivamus a porta quam, vitae rhoncus urna. In fringilla ultrices ex a volutpat. In hac habitasse platea dictumst. Suspendisse luctus, erat non laoreet lacinia, risus lacus convallis metus, non tempor ligula sem eu nulla.Nam at dolor est. Donec posuere massa metus. Vestibulum ut pellentesque magna. Sed ut sapien elit. Sed pharetra justo ligula, ut molestie nisl feugiat sed. Sed a posuere nisi. Nulla blandit mauris ac risus ornare, sit amet dignissim turpis dictum. Mauris quis lorem nec diam sodales fringilla at at arcu. Maecenas sed sem sed nulla tempus sodales. Nulla rhoncus id leo eget porttitor. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed ultricies tellus a odio tristique, eget lacinia massa porttitor. Aliquam vel massa quis sem dignissim placerat. Nunc vulputate aliquam pellentesque.Maecenas vitae massa tellus. Praesent a odio et diam pretium finibus non sed nibh. Sed mattis, felis vitae tincidunt lobortis, velit nunc lobortis mi, vel sollicitudin orci dolor a eros. Quisque feugiat sapien vel quam venenatis tempor. Aliquam sed tincidunt diam. Cras venenatis, ipsum sit amet rhoncus ullamcorper, tortor augue eleifend nisl, id viverra dui turpis a mi. Praesent tincidunt pulvinar velit, non lobortis orci. Donec posuere ex velit, egestas placerat tellus viverra et. Integer luctus dolor et nisl luctus vestibulum. Sed semper mauris sit amet elit blandit, vitae placerat leo commodo. Phasellus eu tortor ullamcorper, posuere est eget, faucibus ante.')

txt_lst = ['hello\n', 'world\n', 'Bye\n', 'Lorem\n', 'Ipsum']
writable_file.writelines(txt_lst)

writable_file.close()


####################################################
# Append
####################################################

writable_file = open('writable.txt', 'a')

txt_lst = ['hello\n', 'world\n', 'Bye\n', 'Lorem\n', 'Ipsum\n']
writable_file.writelines(txt_lst)

writable_file.close()


####################################################
# Context Manager
####################################################

with open('test.txt', 'r') as file:
    read_content = file.read()
    with open('new_file.txt', 'w') as new_file:
        read_content += '\nHello From Context Manager'
        new_file.write(read_content)
    print(f'New File: {new_file.closed}')
    print(file.closed)

print(file.closed)


####################################################
# OS
####################################################

import os

print(os.listdir())
os.mkdir('TestDir1')
file = open('TestDir/new_text_file1.txt', 'w')
os.rmdir('TestDir1')
os.remove('TestDir/new_text_file1.txt')