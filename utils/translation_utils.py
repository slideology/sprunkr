"""
翻译工具模块 - 处理多语言翻译数据的加载和管理
"""
import json
import os
import logging

logger = logging.getLogger(__name__)

def get_translations():
    """
    从JSON文件加载翻译数据
    
    Returns:
        dict: 翻译数据字典，默认返回英文翻译
    """
    try:
        # 获取当前文件所在目录的上两级目录，即项目根目录
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        translations_path = os.path.join(base_dir, 'static', 'data', 'translations.json')
        
        with open(translations_path, 'r', encoding='utf-8') as f:
            translations = json.load(f)
            return translations.get('en', {})
    except Exception as e:
        logger.error(f"Error loading translations: {e}")
        # 返回默认翻译数据
        return {
            'nav': {
                'home': 'Home',
                'guide': 'Game Guide',
                'faq': 'FAQ',
                'play': 'Play',
                'about': 'About',
                'contact': 'Contact',
                'games': 'Games'
            },
            "hero": {
                "title_highlight": "Create Music",
                "title_regular": "Like Never Before",
                "description": "Transform your musical ideas into reality with Sprunkr. Mix beats, create melodies, and share your music with the world."
            },
            "game": {
                "title": "Sprunkr",
                "subtitle": "Sprunki Online Horror Music Game",
                "description": "Unleash haunting melodies with our special glitch music system. Stack sounds, witness their digital distortion transformation. Embrace Horror Aesthetics."
            },
            "trending": {
                "title": "Trending Games"
            }
        }
