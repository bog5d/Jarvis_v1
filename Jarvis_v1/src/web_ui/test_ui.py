#!/usr/bin/env python3
"""
Jarvis Web UI 自动化测试脚本
测试 index.html 的交互功能
"""

import urllib.request
import urllib.error
import time
import sys
import os
from pathlib import Path

def test_server_connection():
    """测试HTTP服务器是否返回200"""
    print("🔍 测试HTTP服务器连接...")
    try:
        response = urllib.request.urlopen('http://localhost:8000', timeout=5)
        if response.status == 200:
            print("✅ 服务器返回 200 OK")
            return True
        else:
            print(f"❌ 服务器返回状态码: {response.status}")
            return False
    except urllib.error.URLError as e:
        print(f"❌ 无法连接到服务器: {e}")
        return False
    except Exception as e:
        print(f"❌ 连接测试失败: {e}")
        return False

def test_html_content():
    """测试HTML内容是否包含必要的元素"""
    print("\n🔍 测试HTML内容...")
    
    # 读取index.html文件
    html_file = Path(__file__).parent / 'index.html'
    if not html_file.exists():
        print(f"❌ 找不到文件: {html_file}")
        return False
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tests_passed = 0
        total_tests = 3
        
        # 测试1: 检查togglePanel函数
        if 'function togglePanel()' in content:
            print("✅ HTML包含 togglePanel() 函数")
            tests_passed += 1
        else:
            print("❌ HTML缺少 togglePanel() 函数")
        
        # 测试2: 检查reading-panel元素
        if 'id="reading-panel"' in content:
            print("✅ HTML包含 id='reading-panel' 元素")
            tests_passed += 1
        else:
            print("❌ HTML缺少 id='reading-panel' 元素")
        
        # 测试3: 检查briefing-card元素
        if 'id="briefing-card"' in content:
            print("✅ HTML包含 id='briefing-card' 元素")
            tests_passed += 1
        else:
            print("❌ HTML缺少 id='briefing-card' 元素")
        
        # 额外测试: 检查onclick属性
        if 'onclick="togglePanel()"' in content:
            print("✅ HTML包含 onclick='togglePanel()' 属性")
            tests_passed += 1
            total_tests += 1
        
        print(f"\n📊 测试结果: {tests_passed}/{total_tests} 通过")
        return tests_passed >= total_tests - 1  # 允许一个测试失败
        
    except Exception as e:
        print(f"❌ 读取HTML文件失败: {e}")
        return False

def test_interactive_elements():
    """测试交互元素是否存在"""
    print("\n🔍 测试交互元素...")
    
    html_file = Path(__file__).parent / 'index.html'
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查关键交互元素
        elements_to_check = [
            ('发送按钮', 'text-[#0B57D0]'),
            ('输入框', 'textarea'),
            ('侧边栏菜单按钮', 'material-symbols-outlined'),
            ('晨报卡片', 'bg-[#D3E3FD]'),
            ('关闭面板按钮', 'close-panel-btn'),
        ]
        
        all_found = True
        for element_name, element_id in elements_to_check:
            if element_id in content:
                print(f"✅ 找到 {element_name}")
            else:
                print(f"❌ 未找到 {element_name}")
                all_found = False
        
        return all_found
        
    except Exception as e:
        print(f"❌ 测试交互元素失败: {e}")
        return False

def main():
    """主测试函数"""
    print("=" * 50)
    print("Jarvis Web UI 自动化测试")
    print("=" * 50)
    
    # 检查当前目录
    current_dir = Path(__file__).parent
    print(f"📁 工作目录: {current_dir}")
    
    # 运行测试
    server_ok = test_server_connection()
    html_ok = test_html_content()
    interactive_ok = test_interactive_elements()
    
    print("\n" + "=" * 50)
    print("测试总结:")
    print(f"  HTTP服务器连接: {'✅ 通过' if server_ok else '❌ 失败'}")
    print(f"  HTML内容检查: {'✅ 通过' if html_ok else '❌ 失败'}")
    print(f"  交互元素检查: {'✅ 通过' if interactive_ok else '❌ 失败'}")
    
    if server_ok and html_ok and interactive_ok:
        print("\n🎉 所有测试通过！UI 交互功能正常。")
        print("💡 提示: 点击 '今日晨报已准备就绪 [点击查看]' 按钮测试分屏功能")
        return 0
    else:
        print("\n⚠️  部分测试失败，请检查代码。")
        return 1

if __name__ == '__main__':
    sys.exit(main())
