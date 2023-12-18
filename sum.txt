'''
 *0点执行
 *文件以*sum*.txt格式命名,例如sum1.txt，1sum.txt。脚本放在同级目录。
功能：把文件内容重置为0
'''
import os

def modify_js_file(file_path):
    try:
        with open(file_path, 'w') as js_file:
            js_file.write('0')
        print(f'成功修改文件 {file_path}')
    except Exception as e:
        print(f'错误 {file_path}: {e}')

current_directory = os.getcwd()
for filename in os.listdir(current_directory):
    if 'sum' in filename and filename.endswith('.txt'):
        file_path = os.path.join(current_directory, filename)
        modify_js_file(file_path)
