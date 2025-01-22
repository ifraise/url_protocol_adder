# URL 协议添加器

一个 Python 脚本，用于为 Excel 和 TXT 文件中的 URL 添加 `http://` 协议。该工具非常适合快速将没有协议的 URL（例如 `example.com`）转换为完整的 URL（例如 `http://example.com`），使其在 Excel 或文本文件中可点击访问。

## 功能

- 支持 `.xlsx`（Excel）和 `.txt` 文件。
- 自动为没有协议的 URL 添加 `http://` 协议。
- 可以指定 Excel 文件中需要处理的列。

## 安装
- Python 3.x
安装所需的依赖：
```bash
pip install -r requirements.txt
```
## 使用方法
处理 Excel 文件
要处理 Excel 文件，使用以下命令：
```bash
python add_protocol_to_excel.py -r yourfile.xlsx -c column_name

```
```bash
-r 或 --read：指定需要处理的 Excel 文件（必需）。
-c 或 --column：(可选) 指定包含 URL 的列。可以是列名（例如 urls）或列索引（例如 0 代表第一列）。如果没有指定，默认处理第一列。
```
## 示例
处理名为 data.xlsx 的 Excel 文件，假设 URL 存储在名为 urls 的列中：

```bash
python add_protocol_to_excel.py -r data.xlsx -c urls
```
处理名为 data.txt 的 TXT 文件，脚本将自动为每行 URL 添加 http:// 协议：

```bash
python add_protocol_to_excel.py -r data.txt
```
## 输出
对于 Excel 文件，处理后的文件会以输入文件名为基础，添加 _processed 后缀（例如，data_processed.xlsx）。
对于 TXT 文件，处理后的文件会以 _processed 后缀保存（例如，data_processed.txt）。



