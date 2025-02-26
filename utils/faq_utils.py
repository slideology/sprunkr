"""
FAQ工具模块 - 处理FAQ数据的加载和管理
"""
import json
import os
import logging

logger = logging.getLogger(__name__)

def load_faqs():
    """
    从JSON文件加载FAQ数据
    
    Returns:
        dict: FAQ数据字典
    """
    try:
        # 获取当前文件所在目录的上两级目录，即项目根目录
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        faqs_path = os.path.join(base_dir, 'static', 'data', 'faqs', 'faqs.json')
        
        with open(faqs_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading FAQs: {e}")
        # 返回空字典作为默认值
        return {}

def get_faqs_for_page(page_name):
    """
    获取特定页面的FAQ数据
    
    Args:
        page_name (str): 页面名称
        
    Returns:
        dict: 包含FAQ问答和结论的字典
    """
    faqs_data = load_faqs()
    
    # 如果找不到对应页面的FAQ，返回默认值
    if page_name not in faqs_data:
        return {
            'faqs': [],
            'conclusion': ''
        }
    
    return faqs_data[page_name]
