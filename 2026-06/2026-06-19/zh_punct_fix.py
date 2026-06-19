#!/usr/bin/env python3
"""中文标点规范化：把中文语境里误用的半角标点改成全角。
保留：数字千分位/小数点、版本号、纯英文括号、URL、代码。
处理：逗号、句号、冒号、分号、问号、叹号、双引号、含中文的括号。
用法: python3 zh_punct_fix.py <file.md> [file2.md ...]
不传文件则只做自检。
"""
import re
import sys

CJK = r'\u4e00-\u9fff\u3000-\u303f\uff00-\uffef'

def fix_text(t):
    # 1) 双引号：直引号 " → 弯引号，按出现顺序交替 “ ”
    def quotes(s):
        out = []
        open_q = True
        for ch in s:
            if ch == '"':
                out.append('“' if open_q else '”')
                open_q = not open_q
            else:
                out.append(ch)
        return ''.join(out)
    t = quotes(t)

    # 2) 逗号：仅当左或右紧邻 CJK，且不是数字千分位(数字,数字)
    #    先排除数字千分位：数字 , 数字 → 占位
    t = re.sub(r'(?<=\d),(?=\d{3}\b)', '\u0001', t)  # 千分位占位
    t = re.sub(rf'(?<=[{CJK}]),', '，', t)            # 中文后半角逗号
    t = re.sub(rf',(?=[{CJK}])', '，', t)             # 半角逗号后接中文
    t = t.replace('\u0001', ',')                      # 还原千分位

    # 3) 冒号：中文后的半角冒号（排除 时间 1:2 / http: 已无）
    t = re.sub(rf'(?<=[{CJK}]):', '：', t)
    t = re.sub(rf':(?=[{CJK}])', '：', t)

    # 4) 分号：中文后半角分号
    t = re.sub(rf'(?<=[{CJK}]);', '；', t)
    t = re.sub(rf';(?=[{CJK}])', '；', t)

    # 5) 问号/叹号：中文后半角
    t = re.sub(rf'(?<=[{CJK}])\?', '？', t)
    t = re.sub(rf'(?<=[{CJK}])!', '！', t)
    # 紧跟在中文问/叹号边界（如 ?" 收尾在引号内）已由上面覆盖

    # 6) 句号：中文之间的半角句号（保留 5.6 版本号/小数：两侧数字不动）
    t = re.sub(rf'(?<=[{CJK}])\.(?=[{CJK}])', '。', t)
    t = re.sub(rf'(?<=[{CJK}])\.(?=\s|$)', '。', t)

    # 7) 含中文的半角括号 () → 全角 （）；纯英文括号保留
    def paren(m):
        inner = m.group(1)
        if re.search(rf'[{CJK}]', inner):
            return '（' + inner + '）'
        return m.group(0)
    t = re.sub(r'\(([^()]{0,40})\)', paren, t)

    return t

def scan_counts(t):
    return {
        'half_comma_cjk': len(re.findall(rf'(?<=[{CJK}]),|,(?=[{CJK}])', t)),
        'half_colon_cjk': len(re.findall(rf'(?<=[{CJK}]):|:(?=[{CJK}])', t)),
        'half_semi_cjk': len(re.findall(rf'(?<=[{CJK}]);|;(?=[{CJK}])', t)),
        'straight_quote': t.count('"'),
        'half_paren_cjk': len(re.findall(r'\([^()]*[\u4e00-\u9fff][^()]*\)', t)),
    }

def main():
    files = sys.argv[1:]
    if not files:
        print("no files given")
        return
    for fn in files:
        src = open(fn, encoding='utf-8').read()
        before = scan_counts(src)
        out = fix_text(src)
        after = scan_counts(out)
        if out != src:
            open(fn, 'w', encoding='utf-8').write(out)
        print(f"{fn}")
        print(f"  before: {before}")
        print(f"  after : {after}")

if __name__ == '__main__':
    main()
