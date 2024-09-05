import os
import re
import argparse

class Backup:

    def __init__(self, source_path, backup):
        # 备份的文档路径
        self.backup = backup
        # 带日期前缀的博文目录
        self.source_path = source_path

    def process_file(self, file_name):
        # 去掉文件元数据和名称前面的日期

        removing_date_file = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', file_name)

        # 读取文件内容并移除 YAML 前置事项
        with open(f"{self.source_path}/{file_name}", 'r', encoding='utf-8') as file:
            content = file.read()

        # 使用正则表达式找到并去掉第一个以“---”分隔的部分
        content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)

        # 将修改后的内容写入新的文件
        with open(f"{self.backup}/{removing_date_file}", 'w', encoding='utf-8') as new_file:
            new_file.write(content)

    def delete_old_file(self):
        # 获取 backup 目录下的所有 md 文件
        backup_files = {f for f in os.listdir(self.backup) if f.endswith('.md')}

        # 获取 _posts 目录下的所有 md 文件
        source_files = {f for f in os.listdir(self.source_path) if f.endswith('.md')}

        # 获得_posts 目录下去除日期后的文件名的集合
        intermediate_name = {re.sub(r'^\d{4}-\d{2}-\d{2}-', '', f) for f in source_files}

        # 找出在 backup 目录中但不在 source 目录中的文件
        unmatched_files = backup_files - intermediate_name

        # 删除这些不一致的文件
        for file_name in unmatched_files:
            file_path = os.path.join(self.backup, file_name)
            os.remove(file_path)

    def get_post_name(self) -> list[str]:

        post_names = []
        for post_name in os.listdir(self.source_path):
            if post_name.endswith('.md') or post_name.endswith('.txt'):
                post_names.append(post_name)

        return post_names

def main():
    parser = argparse.ArgumentParser(description='Process a file to remove date from filename and YAML front matter.')

    # 添加一个位置参数来接受文件路径
    parser.add_argument('source_path', type=str, help='需要备份的目录')
    parser.add_argument('backup', type=str, help='备份文件存放的目录')

    # 解析命令行参数
    args = parser.parse_args()

    # 创建 Backup 类的实例
    backup = Backup(args.source_path, args.backup)
    post_names = backup.get_post_name()

    for post_name in post_names:
        backup.process_file(post_name)

    backup.delete_old_file()

    print("backup succeed")

if __name__ == '__main__':
    main()