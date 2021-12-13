with open('test8.txt') as file_object:
    data = file_object.read()
    data = [i.strip(' |') for i in data.split(sep='\n')]
    input_data = data[0::2]
    output_data = data[1::2]
    print(input_data)
    print(output_data)