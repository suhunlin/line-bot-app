import os
class LineFileSystem:
    def __init__(self,filename):
        self.filename = filename
        self.name = None
        self.phone_number = None
        self.data_input_name = False
        self.data_input_phone_number = False
        self.datas = []

    def read_file(self):
        if os.path.exists(self.filename):
            with open(self.filename,'r', encoding = 'utf-8-sig') as file:
                for line in file:
                    self.datas.append(line.strip().split())
        else:
            print('請檢查檔案及路徑!!!')
        return self.datas

    def write_file(self):
        str = ''
        try:
            with open(self.filename,'w', encoding = 'utf-8-sig') as file:
                for data in self.datas:
                    str = data[0] + '' + data[1] + '\n'
                    file.write(str)
        except Exception as error_message:
            print(error_message)

line_file_system = LineFileSystem(filename = 'line_data.txt')
print('****create line_file_system*****')