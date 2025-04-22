import sys

def decide_reply(issue_content):
    # 简单的逻辑判断
    # if "bug" in issue_content.lower():
    #     return "Thanks for reporting the bug! We will investigate it."
    # elif "feature" in issue_content.lower():
    #     return "Thanks for suggesting the feature! We'll consider it for future releases."
    # else:
    #     return "Thanks for your feedback!"
    issue_content = issue_content.lower()
    if "bug" in issue_content:
        return """Thanks for reporting the bug!
The fixed version is almost there!"""
    elif 'request' in issue_content or 'code' in issue_content:
        return """The code is coming soon!
The code is almost there!"""
    else:
        return "What are you talking about?"

# 读取 issue 内容
if len(sys.argv) < 2:
    print("No issue content provided!")
    sys.exit(1)

with open(sys.argv[1], 'r') as file:
    issue_content = file.read()
    
print("-- read --")
print(issue_content)

# 根据 issue 内容决定回复
reply = decide_reply(issue_content)

print("-- reply --")
print(reply)

# 将回复内容写入文件
with open('reply_content.txt', 'w') as file:
    file.write(reply)

print("Reply generated and written to reply_content.txt")
