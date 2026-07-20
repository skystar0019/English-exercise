"""
英语复习器 - 帮助记忆英语单词、短语和语法时态
功能：
1. 单词/短语默写练习（带提示功能）
2. 语法时态填空练习

数据存储在 data.py 文件中，可单独编辑扩充词库
"""

import random
import math

# 从独立数据文件导入词库
from data import PHRASES, WORDS, TENSE_QUESTIONS


# ==================== 工具函数 ====================
def get_hint(answer, attempt):
    """
    根据尝试次数生成提示
    attempt: 0,1,2 对应三次提示机会，提示越来越多
    """
    hint_length = math.ceil(len(answer) / (3 - attempt))
    return answer[:hint_length]


def practice_with_hints(question, correct_answer, prompt_text):
    """
    带提示的练习模式（用于单词/短语默写）
    答对直接返回True，答错给3次提示机会，最后返回False
    """
    answer = input(f"{prompt_text}{question}: ")
    if answer.strip().lower() == correct_answer.lower():
        print("回答正确！")
        return True
    
    # 三次提示机会
    for i in range(3):
        hint = get_hint(correct_answer, i)
        answer = input(f"提示：{hint}... 请重新输入: ")
        if answer.strip().lower() == correct_answer.lower():
            print("回答正确！")
            return True
    
    # 三次都错了
    print(f"回答错误，正确答案是: {correct_answer}")
    return False


def practice_tense(question_bank, count=5):
    """
    时态填空练习（不带提示，直接判对错）
    """
    questions = list(question_bank.items())
    for _ in range(min(count, len(questions))):
        question, correct_answer = random.choice(questions)
        answer = input(f"{question}: ")
        if answer.strip().lower() == correct_answer.lower():
            print("回答正确！")
        else:
            print(f"回答错误，正确答案是: {correct_answer}")


def get_valid_int_input(prompt, min_val=1, max_val=100):
    """
    获取有效的整数输入，带范围验证
    """
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"请输入{min_val}到{max_val}之间的数字！")
        except ValueError:
            print("输入无效，请输入数字！")


# ==================== 主要功能模块 ====================
def grammar_practice():
    """语法复习模块"""
    tenses = list(TENSE_QUESTIONS.keys())
    print("可选时态：" + "、".join(tenses))
    
    while True:
        choice = input("请输入你想复习的时态：")
        if choice in TENSE_QUESTIONS:
            break
        print(f"输入有误，请从以下选项中选择：{'、'.join(tenses)}")
    
    print(f"\n你选择复习的时态是: {choice}")
    print("请根据提示完成下列句子：\n")
    practice_tense(TENSE_QUESTIONS[choice], count=5)


def vocabulary_practice():
    """单词/短语复习模块"""
    while True:
        word_type = input("请输入你想复习的类型（短语/单词）：")
        if word_type in ['短语', '单词']:
            break
        print("请输入「短语」或「单词」！")
    
    if word_type == '短语':
        bank = PHRASES
        max_count = 20
        count_prompt = f"请输入你想复习的短语数量（1-{max_count}）："
        question_prefix = "请默写以下短语: "
    else:
        bank = WORDS
        max_count = 10
        count_prompt = f"请输入你想复习的单词数量（1-{max_count}）："
        question_prefix = "请默写以下单词: "
    
    count = get_valid_int_input(count_prompt, 1, max_count)
    items = list(bank.items())
    
    for _ in range(count):
        english, chinese = random.choice(items)
        practice_with_hints(chinese, english, question_prefix)


def show_stats():
    """显示词库统计信息"""
    print("\n" + "=" * 30)
    print("📚 词库统计")
    print("=" * 30)
    print(f"短语数量：{len(PHRASES)} 个")
    print(f"单词数量：{len(WORDS)} 个")
    print(f"语法时态：{len(TENSE_QUESTIONS)} 种")
    for tense, questions in TENSE_QUESTIONS.items():
        print(f"  - {tense}：{len(questions)} 道题")
    total_grammar = sum(len(q) for q in TENSE_QUESTIONS.values())
    print(f"语法题目总计：{total_grammar} 道")
    print("=" * 30 + "\n")

def yichuanfenxi():
    """遗传算法分析薄弱点模块"""
    pass #交给你了


def main():
    """主函数"""
    print("=" * 30)
    print("欢迎使用英语复习器！")
    print("=" * 30)
    
    while True:
        print("\n【主菜单】")
        print("1. 单词/短语复习")
        print("2. 语法时态复习")
        print("3. 查看词库统计")
        print("4. 分析薄弱点")
        print("5. 退出程序")

        choice = input("\n请选择功能（输入数字或文字）：")
        
        if choice in ['1', '单词', '短语']:
            vocabulary_practice()
        elif choice in ['2', '语法']:
            grammar_practice()
        elif choice in ['3', '统计', '词库']:
            show_stats()
        elif choice in ['4', '退出', 'exit', 'quit']:
            print("感谢使用，再见！")
            break
        else:
            print("输入有误，请重新选择！")


if __name__ == '__main__':
    main()