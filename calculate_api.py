import pandas as pd

table = pd.read_excel("/Users/nguyenquangminh/Downloads/Điểm-học-phần.xlsx", index_col=None)
table.columns = ["Semester", "Course ID","Tên tiếng việt", "Tín chỉ", "Score", "Tên tiếng anh"]
table["Score"] = [0]*len(table)
print(table)