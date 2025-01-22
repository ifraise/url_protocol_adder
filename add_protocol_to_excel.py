import pandas as pd
import os
import argparse

def process_urls(input_file, output_file=None, encoding='utf-8', column=None):
    """
    处理 Excel、TXT 文件中的 URL 列或每行 URL，为缺少协议的 URL 添加 http:// 协议。

    :param input_file: 输入的文件路径
    :param output_file: 处理后的文件保存路径
    :param encoding: 文件编码格式（默认 utf-8）
    :param column: 需要处理的列名或列索引
    """
    try:
        # 检查文件是否存在
        if not os.path.isfile(input_file):
            print(f"错误：文件 '{input_file}' 不存在。")
            return

        # 获取文件扩展名
        _, ext = os.path.splitext(input_file)
        ext = ext.lower()

        if ext == '.xlsx':
            # 处理 Excel 文件
            print(f"正在读取 Excel 文件：{input_file}")
            df = pd.read_excel(input_file, engine='openpyxl')

            # 获取需要处理的列
            if column is None:
                column = df.columns[0]  # 默认使用第一列
                print(f"默认使用第一列：'{column}'")
            else:
                # 检查列名是否有效
                if column not in df.columns:
                    print(f"错误：没有找到名为 '{column}' 的列。")
                    return

            def fix_url(url):
                if pd.isna(url):
                    return url
                url = str(url).strip()
                if not (url.startswith('http://') or url.startswith('https://')):
                    return f"http://{url}"
                return url

            df[column] = df[column].apply(fix_url)

            if output_file is None:
                base, _ = os.path.splitext(input_file)
                output_file = f"{base}_processed.xlsx"

            df.to_excel(output_file, index=False, engine='openpyxl')
            print(f"处理完成，结果已保存到 '{output_file}'")

        elif ext == '.txt':
            # 处理 TXT 文件逐行
            print(f"正在读取 TXT 文件：{input_file}")
            with open(input_file, 'r', encoding=encoding) as f:
                lines = f.readlines()

            def fix_url(url):
                url = url.strip()
                if not (url.startswith('http://') or url.startswith('https://')):
                    return f"http://{url}"
                return url

            processed_lines = [fix_url(line) for line in lines]

            if output_file is None:
                base, _ = os.path.splitext(input_file)
                output_file = f"{base}_processed.txt"

            with open(output_file, 'w', encoding=encoding) as f:
                f.writelines(line + '\n' for line in processed_lines)
            print(f"处理完成，结果已保存到 '{output_file}'")

        else:
            print(f"错误：不支持的文件格式 '{ext}'，请提供有效的 Excel 或 TXT 文件。")

    except Exception as e:
        print(f"处理文件时发生错误：{e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="处理 Excel、TXT 文件中的 URL，为缺少协议的 URL 添加 http://。")
    parser.add_argument("-r", "--read", required=True, help="输入文件路径")
    parser.add_argument("-e", "--encoding", default="utf-8", help="指定文件编码，默认 utf-8")
    parser.add_argument("-c", "--column", help="指定需要处理的列名或列索引，默认处理第一列")
    args = parser.parse_args()

    process_urls(args.read, encoding=args.encoding, column=args.column)
