from pathlib import Path

path = Path(r"d:\Users\21862\PycharmProjects\PythonProject\练习\pi.txt.txt")###调用的时候，一定要加一个r，或者说双斜杠


a = path.read_text(encoding='utf-8')
print(a)