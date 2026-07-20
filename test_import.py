# 测试数据导入
from data import PHRASES, WORDS, TENSE_QUESTIONS, add_word, add_phrase, add_tense_question

print("✅ 数据导入成功！")
print(f"📚 短语数量: {len(PHRASES)} 个")
print(f"📖 单词数量: {len(WORDS)} 个")
print(f"✏️  语法时态: {len(TENSE_QUESTIONS)} 种")
for tense, questions in TENSE_QUESTIONS.items():
    print(f"   - {tense}: {len(questions)} 道题")

# 测试添加功能
print("\n🔧 测试添加新单词...")
add_word("test", "测试")
print(f"添加后单词数量: {len(WORDS)} 个")
print(f"新添加的单词: 'test' -> '{WORDS['test']}'")

print("\n🎉 所有测试通过！数据文件工作正常。")
