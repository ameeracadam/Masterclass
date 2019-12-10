import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--text", type = str)
args = parser.parse_args()

text = args.text
processed_text = ""
for i in text:
    processed_text = i + processed_text

print(processed_text)