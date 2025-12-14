import marshal
import base64

input_file = "hhh_2.py"      # file gốc của ông
output_file = "hhh_2_enc.py" # file sau khi mã hoá

with open(input_file, "r", encoding="utf-8") as f:
    source = f.read()

code = compile(source, input_file, "exec")
data = marshal.dumps(code)
encoded = base64.b64encode(data)

with open(output_file, "w", encoding="utf-8") as f:
    f.write("import marshal,base64\n")
    f.write(f"exec(marshal.loads(base64.b64decode({encoded!r})))\n")

print("✅ Mã hoá xong ->", output_file)